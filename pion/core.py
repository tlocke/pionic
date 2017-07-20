from antlr4 import CommonTokenStream, InputStream
from antlr4.error import Errors, ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl
from pion.antlr.IonTextLexer import IonTextLexer
from pion.antlr.IonTextParser import IonTextParser
import arrow
from decimal import Decimal


class PionException(Exception):
    pass


class ThrowingErrorListener(ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Errors.ParseCancellationException(
            "line " + str(line) + ":" + str(column) + " " + msg)


def load(file_like):
    return loads(file_like.read())


def loads(ion_str):
    lexer = IonTextLexer(InputStream(ion_str))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = IonTextParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    try:
        tree = parser.top_level()
    except Errors.ParseCancellationException as e:
        raise PionException(str(e)) from e

    return parse(tree)


_trans_dec = str.maketrans('dD', 'ee', '_')


def parse(node):
    if isinstance(node, IonTextParser.StructContext):
        val = {}
        children = [
            c for c in node.getChildren() if not
            isinstance(c, TerminalNodeImpl)]
        for child in children:
            parse(child)
    elif isinstance(
            node, (
                IonTextParser.Top_levelContext,
                IonTextParser.Top_level_valueContext,
                IonTextParser.Delimiting_entityContext,
                IonTextParser.ValueContext,
                IonTextParser.EntityContext,
                IonTextParser.Keyword_entityContext,
                IonTextParser.Numeric_entityContext,
                IonTextParser.AnnotationContext,
                IonTextParser.Sexp_valueContext,
                IonTextParser.Sexp_delimiting_entityContext)):

        children = []
        for c in node.getChildren():
            if isinstance(c, TerminalNodeImpl):
                payload = c.getPayload()
                if payload.type == IonTextParser.EOF:
                    continue
            elif isinstance(c, IonTextParser.AnnotationContext):
                continue

            children.append(c)

        if len(children) == 1:
            val = parse(children[0])
        else:
            raise PionException("Thought there would always be one child.")
    elif isinstance(node, IonTextParser.Any_nullContext):
        val = None
    elif isinstance(node, TerminalNodeImpl):
        token = node.getPayload()
        token_type = token.type

        if token_type == IonTextParser.TIMESTAMP:
            try:
                val = arrow.get(token.text).datetime
            except arrow.parser.ParserError as e:
                raise PionException(
                    "Can't parse the timestamp '" + token.text + "'.") from e
        elif token_type == IonTextParser.BOOL:
            val = token.text == 'true'
        elif token_type == IonTextParser.IDENTIFIER_SYMBOL:
            val = token.text
        elif token_type in (
                IonTextParser.BIN_INTEGER, IonTextParser.DEC_INTEGER,
                IonTextParser.HEX_INTEGER):
            val = int(token.text.replace('_', ''), 0)
        elif token_type == IonTextParser.DECIMAL:
            val = Decimal(token.text.translate(_trans_dec))
        elif token_type == IonTextParser.FLOAT:
            val = float(token.text.replace('_', ''))
        elif token_type == IonTextParser.SHORT_QUOTED_STRING:
            val = unescape(token.text[1:-1])
        elif token_type == IonTextParser.LONG_QUOTED_STRING:
            val = unescape(token.text[3:-3])
        else:
            raise PionException(
                "Don't recognize the token type: " + str(token_type) + ".")
    elif isinstance(node, IonTextParser.SexpContext):
        sexp = []
        for child in node.getChildren():
            if isinstance(child, IonTextParser.Sexp_valueContext):
                for c in child.getChildren():
                    sexp.append(parse(child))
        val = tuple(sexp)
    elif isinstance(node, IonTextParser.Quoted_textContext):
        s = []
        for c in node.getChildren():
            if isinstance(c, IonTextParser.WsContext):
                continue
            s.append(parse(c))
        val = ''.join(s)
    else:
        raise PionException(
            "Don't know what to do with type " + str(type(node)) +
            " with value " + str(node) + ".")
    return val


ESCAPES = {
    '0': '\u0000',   # NUL
    'a': '\u0007',   # alert BEL
    'b': '\u0008',   # backspace BS
    't': '\u0009',   # horizontal tab HT
    'n': '\u000A',   # linefeed LF
    'f': '\u000C',   # form feed FF
    'r': '\u000D',   # carriage return CR
    'v': '\u000B',   # vertical tab VT
    '"': '\u0022',   # double quote
    "'": '\u0027',   # single quote
    '?': '\u003F',   # question mark
    '\\': '\u005C',  # backslash
    '/': '\u002F',   # forward slash
    '\u000D\u000A': '',  # empty string
    '\u000D': '',  # empty string
    '\u000A': ''}  # empty string


def unescape(escaped_str):
    i = escaped_str.find('\\')
    if i == -1:
        return escaped_str
    else:
        head_str = escaped_str[:i]
        tail_str = escaped_str[i+1:]
        for k, v in ESCAPES.items():
            if tail_str.startswith(k):
                return head_str + v + unescape(tail_str[len(k):])

        for prefix, digits in (('x', 2), ('u', 4), ('U', 8)):
            if tail_str.startswith(prefix):
                hex_str = tail_str[1:1 + digits]
                v = chr(int(hex_str, 16))
                return head_str + v + unescape(tail_str[1 + digits:])

        raise PionException(
            "Can't find a valid string following the first backslash of '" +
            escaped_str + "'.")


def dumps(obj):
    return _dump(obj)


def _dump(obj):
    return str(obj)

from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl
from pion.antlr.IonTextLexer import IonTextLexer
from pion.antlr.IonTextParser import IonTextParser
import arrow


class PionException(Exception):
    pass


def load(file_like):
    return loads(file_like.read())


def loads(ion_str):
    lexer = IonTextLexer(InputStream(ion_str))
    stream = CommonTokenStream(lexer)
    parser = IonTextParser(stream)
    tree = parser.top_level()
    return parse(tree)


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
                IonTextParser.Numeric_entityContext)):

        children = []
        for c in node.getChildren():
            if isinstance(c, TerminalNodeImpl):
                payload = c.getPayload()
                if payload.type == IonTextParser.EOF:
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
        else:
            raise PionException("Don't recognize the token type.")
    else:
        raise PionException(
            "Don't know what to do with type " + str(type(node)) +
            " with value " + str(node) + ".")

    return val


def dumps(obj):
    return _dump(obj)


def _dump(obj):
    return str(obj)

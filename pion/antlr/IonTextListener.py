# Generated from IonText.g4 by ANTLR 4.7
from antlr4 import ParseTreeListener
if __name__ is not None and "." in __name__:
    from .IonTextParser import IonTextParser
else:
    from IonTextParser import IonTextParser


# This class defines a complete listener for a parse tree produced by
# IonTextParser.
class IonTextListener(ParseTreeListener):

    # Enter a parse tree produced by IonTextParser#top_level.
    def enterTop_level(self, ctx: IonTextParser.Top_levelContext):
        pass

    # Exit a parse tree produced by IonTextParser#top_level.
    def exitTop_level(self, ctx: IonTextParser.Top_levelContext):
        pass

    # Enter a parse tree produced by IonTextParser#top_level_value.
    def enterTop_level_value(self, ctx: IonTextParser.Top_level_valueContext):
        pass

    # Exit a parse tree produced by IonTextParser#top_level_value.
    def exitTop_level_value(self, ctx: IonTextParser.Top_level_valueContext):
        pass

    # Enter a parse tree produced by IonTextParser#value.
    def enterValue(self, ctx: IonTextParser.ValueContext):
        pass

    # Exit a parse tree produced by IonTextParser#value.
    def exitValue(self, ctx: IonTextParser.ValueContext):
        pass

    # Enter a parse tree produced by IonTextParser#entity.
    def enterEntity(self, ctx: IonTextParser.EntityContext):
        pass

    # Exit a parse tree produced by IonTextParser#entity.
    def exitEntity(self, ctx: IonTextParser.EntityContext):
        pass

    # Enter a parse tree produced by IonTextParser#delimiting_entity.
    def enterDelimiting_entity(
            self, ctx: IonTextParser.Delimiting_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#delimiting_entity.
    def exitDelimiting_entity(
            self, ctx: IonTextParser.Delimiting_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#keyword_delimiting_entity.
    def enterKeyword_delimiting_entity(
            self, ctx: IonTextParser.Keyword_delimiting_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#keyword_delimiting_entity.
    def exitKeyword_delimiting_entity(
            self, ctx: IonTextParser.Keyword_delimiting_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#keyword_entity.
    def enterKeyword_entity(self, ctx: IonTextParser.Keyword_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#keyword_entity.
    def exitKeyword_entity(self, ctx: IonTextParser.Keyword_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#numeric_entity.
    def enterNumeric_entity(self, ctx: IonTextParser.Numeric_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#numeric_entity.
    def exitNumeric_entity(self, ctx: IonTextParser.Numeric_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#annotation.
    def enterAnnotation(self, ctx: IonTextParser.AnnotationContext):
        pass

    # Exit a parse tree produced by IonTextParser#annotation.
    def exitAnnotation(self, ctx: IonTextParser.AnnotationContext):
        pass

    # Enter a parse tree produced by IonTextParser#quoted_annotation.
    def enterQuoted_annotation(
            self, ctx: IonTextParser.Quoted_annotationContext):
        pass

    # Exit a parse tree produced by IonTextParser#quoted_annotation.
    def exitQuoted_annotation(
            self, ctx: IonTextParser.Quoted_annotationContext):
        pass

    # Enter a parse tree produced by IonTextParser#list_type.
    def enterList_type(self, ctx: IonTextParser.List_typeContext):
        pass

    # Exit a parse tree produced by IonTextParser#list_type.
    def exitList_type(self, ctx: IonTextParser.List_typeContext):
        pass

    # Enter a parse tree produced by IonTextParser#sexp.
    def enterSexp(self, ctx: IonTextParser.SexpContext):
        pass

    # Exit a parse tree produced by IonTextParser#sexp.
    def exitSexp(self, ctx: IonTextParser.SexpContext):
        pass

    # Enter a parse tree produced by IonTextParser#sexp_value.
    def enterSexp_value(self, ctx: IonTextParser.Sexp_valueContext):
        pass

    # Exit a parse tree produced by IonTextParser#sexp_value.
    def exitSexp_value(self, ctx: IonTextParser.Sexp_valueContext):
        pass

    # Enter a parse tree produced by IonTextParser#sexp_delimiting_entity.
    def enterSexp_delimiting_entity(
            self, ctx: IonTextParser.Sexp_delimiting_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#sexp_delimiting_entity.
    def exitSexp_delimiting_entity(
            self, ctx: IonTextParser.Sexp_delimiting_entityContext):
        pass

    # Enter a parse tree produced by
    # IonTextParser#sexp_keyword_delimiting_entity.
    def enterSexp_keyword_delimiting_entity(
            self, ctx: IonTextParser.Sexp_keyword_delimiting_entityContext):
        pass

    # Exit a parse tree produced by
    # IonTextParser#sexp_keyword_delimiting_entity.
    def exitSexp_keyword_delimiting_entity(
            self, ctx: IonTextParser.Sexp_keyword_delimiting_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#sexp_null_delimiting_entity.
    def enterSexp_null_delimiting_entity(
            self, ctx: IonTextParser.Sexp_null_delimiting_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#sexp_null_delimiting_entity.
    def exitSexp_null_delimiting_entity(
            self, ctx: IonTextParser.Sexp_null_delimiting_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#sexp_keyword_entity.
    def enterSexp_keyword_entity(
            self, ctx: IonTextParser.Sexp_keyword_entityContext):
        pass

    # Exit a parse tree produced by IonTextParser#sexp_keyword_entity.
    def exitSexp_keyword_entity(
            self, ctx: IonTextParser.Sexp_keyword_entityContext):
        pass

    # Enter a parse tree produced by IonTextParser#operator.
    def enterOperator(self, ctx: IonTextParser.OperatorContext):
        pass

    # Exit a parse tree produced by IonTextParser#operator.
    def exitOperator(self, ctx: IonTextParser.OperatorContext):
        pass

    # Enter a parse tree produced by IonTextParser#struct.
    def enterStruct(self, ctx: IonTextParser.StructContext):
        pass

    # Exit a parse tree produced by IonTextParser#struct.
    def exitStruct(self, ctx: IonTextParser.StructContext):
        pass

    # Enter a parse tree produced by IonTextParser#field.
    def enterField(self, ctx: IonTextParser.FieldContext):
        pass

    # Exit a parse tree produced by IonTextParser#field.
    def exitField(self, ctx: IonTextParser.FieldContext):
        pass

    # Enter a parse tree produced by IonTextParser#any_null.
    def enterAny_null(self, ctx: IonTextParser.Any_nullContext):
        pass

    # Exit a parse tree produced by IonTextParser#any_null.
    def exitAny_null(self, ctx: IonTextParser.Any_nullContext):
        pass

    # Enter a parse tree produced by IonTextParser#typed_null.
    def enterTyped_null(self, ctx: IonTextParser.Typed_nullContext):
        pass

    # Exit a parse tree produced by IonTextParser#typed_null.
    def exitTyped_null(self, ctx: IonTextParser.Typed_nullContext):
        pass

    # Enter a parse tree produced by IonTextParser#field_name.
    def enterField_name(self, ctx: IonTextParser.Field_nameContext):
        pass

    # Exit a parse tree produced by IonTextParser#field_name.
    def exitField_name(self, ctx: IonTextParser.Field_nameContext):
        pass

    # Enter a parse tree produced by IonTextParser#quoted_text.
    def enterQuoted_text(self, ctx: IonTextParser.Quoted_textContext):
        pass

    # Exit a parse tree produced by IonTextParser#quoted_text.
    def exitQuoted_text(self, ctx: IonTextParser.Quoted_textContext):
        pass

    # Enter a parse tree produced by IonTextParser#symbol.
    def enterSymbol(self, ctx: IonTextParser.SymbolContext):
        pass

    # Exit a parse tree produced by IonTextParser#symbol.
    def exitSymbol(self, ctx: IonTextParser.SymbolContext):
        pass

    # Enter a parse tree produced by IonTextParser#ws.
    def enterWs(self, ctx: IonTextParser.WsContext):
        pass

    # Exit a parse tree produced by IonTextParser#ws.
    def exitWs(self, ctx: IonTextParser.WsContext):
        pass

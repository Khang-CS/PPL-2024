# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_prime.
    def visitNewline_prime(self, ctx:ZCodeParser.Newline_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_init.
    def visitVar_init(self, ctx:ZCodeParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#scala_param.
    def visitScala_param(self, ctx:ZCodeParser.Scala_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#option.
    def visitOption(self, ctx:ZCodeParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optionprime.
    def visitOptionprime(self, ctx:ZCodeParser.OptionprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#standalone_stmt.
    def visitStandalone_stmt(self, ctx:ZCodeParser.Standalone_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecllist.
    def visitVardecllist(self, ctx:ZCodeParser.VardecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declprime.
    def visitDeclprime(self, ctx:ZCodeParser.DeclprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normaldecl.
    def visitNormaldecl(self, ctx:ZCodeParser.NormaldeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydecl.
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimensions.
    def visitDimensions(self, ctx:ZCodeParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normaltype.
    def visitNormaltype(self, ctx:ZCodeParser.NormaltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicittype.
    def visitImplicittype(self, ctx:ZCodeParser.ImplicittypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexexp.
    def visitIndexexp(self, ctx:ZCodeParser.IndexexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp9.
    def visitExp9(self, ctx:ZCodeParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayvalue.
    def visitArrayvalue(self, ctx:ZCodeParser.ArrayvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value_list.
    def visitArray_value_list(self, ctx:ZCodeParser.Array_value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccall_stmt.
    def visitFunccall_stmt(self, ctx:ZCodeParser.Funccall_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explist.
    def visitExplist(self, ctx:ZCodeParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expprime.
    def visitExpprime(self, ctx:ZCodeParser.ExpprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt_list.
    def visitElif_stmt_list(self, ctx:ZCodeParser.Elif_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt_prime.
    def visitElif_stmt_prime(self, ctx:ZCodeParser.Elif_stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt_prime.
    def visitElse_stmt_prime(self, ctx:ZCodeParser.Else_stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtprime.
    def visitStmtprime(self, ctx:ZCodeParser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#io_func.
    def visitIo_func(self, ctx:ZCodeParser.Io_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readNumber.
    def visitReadNumber(self, ctx:ZCodeParser.ReadNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeNumber.
    def visitWriteNumber(self, ctx:ZCodeParser.WriteNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readBool.
    def visitReadBool(self, ctx:ZCodeParser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write.
    def visitWrite(self, ctx:ZCodeParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readString.
    def visitReadString(self, ctx:ZCodeParser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeString.
    def visitWriteString(self, ctx:ZCodeParser.WriteStringContext):
        return self.visitChildren(ctx)



del ZCodeParser
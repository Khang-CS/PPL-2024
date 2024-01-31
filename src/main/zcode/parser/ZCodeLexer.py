# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01d2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\5\b\u00bb\n\b\3\b\5\b\u00be\n\b\3\t\3\t\3\t\7\t\u00c3")
        buf.write("\n\t\f\t\16\t\u00c6\13\t\5\t\u00c8\n\t\3\n\3\n\7\n\u00cc")
        buf.write("\n\n\f\n\16\n\u00cf\13\n\3\13\3\13\5\13\u00d3\n\13\3\13")
        buf.write("\3\13\7\13\u00d7\n\13\f\13\16\13\u00da\13\13\3\f\3\f\5")
        buf.write("\f\u00de\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00e8")
        buf.write("\n\r\f\r\16\r\u00eb\13\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f2")
        buf.write("\n\r\3\r\5\r\u00f5\n\r\3\r\3\r\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00fd\n\16\f\16\16\16\u0100\13\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u010d\n\17\f")
        buf.write("\17\16\17\u0110\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*")
        buf.write("\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\79\u01b7\n")
        buf.write("9\f9\169\u01ba\139\3:\3:\3:\3:\7:\u01c0\n:\f:\16:\u01c3")
        buf.write("\13:\3:\3:\3;\3;\3<\6<\u01ca\n<\r<\16<\u01cb\3<\3<\3=")
        buf.write("\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25")
        buf.write("\2\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24")
        buf.write("-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64")
        buf.write("m\65o\66q\67s8u9w:y;\3\2\r\3\2\63;\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\7\2\f\f\17\17")
        buf.write("$$))^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13")
        buf.write("\13\17\17\"\"\2\u01e4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{\3\2\2\2\5\u0086")
        buf.write("\3\2\2\2\7\u0092\3\2\2\2\t\u009b\3\2\2\2\13\u00a1\3\2")
        buf.write("\2\2\r\u00ac\3\2\2\2\17\u00b8\3\2\2\2\21\u00c7\3\2\2\2")
        buf.write("\23\u00c9\3\2\2\2\25\u00d0\3\2\2\2\27\u00dd\3\2\2\2\31")
        buf.write("\u00f4\3\2\2\2\33\u00f8\3\2\2\2\35\u0106\3\2\2\2\37\u0113")
        buf.write("\3\2\2\2!\u0118\3\2\2\2#\u011e\3\2\2\2%\u0125\3\2\2\2")
        buf.write("\'\u012a\3\2\2\2)\u0131\3\2\2\2+\u0138\3\2\2\2-\u013c")
        buf.write("\3\2\2\2/\u0144\3\2\2\2\61\u0149\3\2\2\2\63\u014d\3\2")
        buf.write("\2\2\65\u0153\3\2\2\2\67\u0156\3\2\2\29\u015c\3\2\2\2")
        buf.write(";\u0165\3\2\2\2=\u0168\3\2\2\2?\u016d\3\2\2\2A\u0172\3")
        buf.write("\2\2\2C\u0178\3\2\2\2E\u017c\3\2\2\2G\u0180\3\2\2\2I\u0184")
        buf.write("\3\2\2\2K\u0187\3\2\2\2M\u0189\3\2\2\2O\u018b\3\2\2\2")
        buf.write("Q\u018d\3\2\2\2S\u018f\3\2\2\2U\u0191\3\2\2\2W\u0193\3")
        buf.write("\2\2\2Y\u0196\3\2\2\2[\u0199\3\2\2\2]\u019b\3\2\2\2_\u019e")
        buf.write("\3\2\2\2a\u01a0\3\2\2\2c\u01a3\3\2\2\2e\u01a7\3\2\2\2")
        buf.write("g\u01aa\3\2\2\2i\u01ac\3\2\2\2k\u01ae\3\2\2\2m\u01b0\3")
        buf.write("\2\2\2o\u01b2\3\2\2\2q\u01b4\3\2\2\2s\u01bb\3\2\2\2u\u01c6")
        buf.write("\3\2\2\2w\u01c9\3\2\2\2y\u01cf\3\2\2\2{|\7t\2\2|}\7g\2")
        buf.write("\2}~\7c\2\2~\177\7f\2\2\177\u0080\7P\2\2\u0080\u0081\7")
        buf.write("w\2\2\u0081\u0082\7o\2\2\u0082\u0083\7d\2\2\u0083\u0084")
        buf.write("\7g\2\2\u0084\u0085\7t\2\2\u0085\4\3\2\2\2\u0086\u0087")
        buf.write("\7y\2\2\u0087\u0088\7t\2\2\u0088\u0089\7k\2\2\u0089\u008a")
        buf.write("\7v\2\2\u008a\u008b\7g\2\2\u008b\u008c\7P\2\2\u008c\u008d")
        buf.write("\7w\2\2\u008d\u008e\7o\2\2\u008e\u008f\7d\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7t\2\2\u0091\6\3\2\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096")
        buf.write("\7f\2\2\u0096\u0097\7D\2\2\u0097\u0098\7q\2\2\u0098\u0099")
        buf.write("\7q\2\2\u0099\u009a\7n\2\2\u009a\b\3\2\2\2\u009b\u009c")
        buf.write("\7y\2\2\u009c\u009d\7t\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7g\2\2\u00a0\n\3\2\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7f\2\2\u00a5\u00a6\7U\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7i\2\2\u00ab\f\3\2\2\2\u00ac\u00ad\7y\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7U\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7t\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7i\2\2\u00b7\16\3\2\2\2\u00b8\u00ba\5\21\t\2\u00b9\u00bb")
        buf.write("\5\23\n\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00bd\3\2\2\2\u00bc\u00be\5\25\13\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00bd\u00be\3\2\2\2\u00be\20\3\2\2\2\u00bf\u00c8\7")
        buf.write("\62\2\2\u00c0\u00c4\t\2\2\2\u00c1\u00c3\t\3\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c7\u00bf\3\2\2\2\u00c7\u00c0\3\2\2\2\u00c8\22")
        buf.write("\3\2\2\2\u00c9\u00cd\7\60\2\2\u00ca\u00cc\t\3\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00ce\3\2\2\2\u00ce\24\3\2\2\2\u00cf\u00cd\3\2")
        buf.write("\2\2\u00d0\u00d2\t\4\2\2\u00d1\u00d3\t\5\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d8\t\2\2\2\u00d5\u00d7\t\3\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3")
        buf.write("\2\2\2\u00d9\26\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00de")
        buf.write("\5\37\20\2\u00dc\u00de\5!\21\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\30\3\2\2\2\u00df\u00e0\7$\2\2\u00e0")
        buf.write("\u00f5\7$\2\2\u00e1\u00e9\7$\2\2\u00e2\u00e3\7)\2\2\u00e3")
        buf.write("\u00e8\7$\2\2\u00e4\u00e5\7^\2\2\u00e5\u00e8\t\6\2\2\u00e6")
        buf.write("\u00e8\n\7\2\2\u00e7\u00e2\3\2\2\2\u00e7\u00e4\3\2\2\2")
        buf.write("\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00f1\3\2\2\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ed\7)\2\2\u00ed\u00f2\7$\2\2\u00ee\u00ef")
        buf.write("\7^\2\2\u00ef\u00f2\t\6\2\2\u00f0\u00f2\n\b\2\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u00f5\7$\2\2\u00f4\u00df\3")
        buf.write("\2\2\2\u00f4\u00e1\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\b\r\2\2\u00f7\32\3\2\2\2\u00f8\u00fe\7$\2\2\u00f9\u00fa")
        buf.write("\7^\2\2\u00fa\u00fd\t\6\2\2\u00fb\u00fd\n\7\2\2\u00fc")
        buf.write("\u00f9\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7^\2\2\u0102\u0103")
        buf.write("\n\6\2\2\u0103\u0104\3\2\2\2\u0104\u0105\b\16\3\2\u0105")
        buf.write("\34\3\2\2\2\u0106\u010e\7$\2\2\u0107\u0108\7)\2\2\u0108")
        buf.write("\u010d\7$\2\2\u0109\u010a\7^\2\2\u010a\u010d\t\6\2\2\u010b")
        buf.write("\u010d\n\7\2\2\u010c\u0107\3\2\2\2\u010c\u0109\3\2\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0112\b\17\4\2\u0112\36\3\2\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114\u0115\7t\2\2\u0115\u0116\7w\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117 \3\2\2\2\u0118\u0119\7h\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011d\"\3\2\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7o\2\2\u0121\u0122\7d\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123\u0124\7t\2\2\u0124$\3\2\2\2\u0125\u0126")
        buf.write("\7d\2\2\u0126\u0127\7q\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129&\3\2\2\2\u012a\u012b\7u\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\u012d\7t\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\u0130\7i\2\2\u0130(\3\2\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u0137*\3")
        buf.write("\2\2\2\u0138\u0139\7x\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b,\3\2\2\2\u013c\u013d\7f\2\2\u013d\u013e")
        buf.write("\7{\2\2\u013e\u013f\7p\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7o\2\2\u0141\u0142\7k\2\2\u0142\u0143\7e\2\2\u0143.\3")
        buf.write("\2\2\2\u0144\u0145\7h\2\2\u0145\u0146\7w\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7e\2\2\u0148\60\3\2\2\2\u0149\u014a")
        buf.write("\7h\2\2\u014a\u014b\7q\2\2\u014b\u014c\7t\2\2\u014c\62")
        buf.write("\3\2\2\2\u014d\u014e\7w\2\2\u014e\u014f\7p\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7k\2\2\u0151\u0152\7n\2\2\u0152\64")
        buf.write("\3\2\2\2\u0153\u0154\7d\2\2\u0154\u0155\7{\2\2\u0155\66")
        buf.write("\3\2\2\2\u0156\u0157\7d\2\2\u0157\u0158\7t\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159\u015a\7c\2\2\u015a\u015b\7m\2\2\u015b8\3")
        buf.write("\2\2\2\u015c\u015d\7e\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f\u0160\7v\2\2\u0160\u0161\7k\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162\u0163\7w\2\2\u0163\u0164\7g\2\2\u0164:\3")
        buf.write("\2\2\2\u0165\u0166\7k\2\2\u0166\u0167\7h\2\2\u0167<\3")
        buf.write("\2\2\2\u0168\u0169\7g\2\2\u0169\u016a\7n\2\2\u016a\u016b")
        buf.write("\7u\2\2\u016b\u016c\7g\2\2\u016c>\3\2\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7n\2\2\u016f\u0170\7k\2\2\u0170\u0171")
        buf.write("\7h\2\2\u0171@\3\2\2\2\u0172\u0173\7d\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\u0175\7i\2\2\u0175\u0176\7k\2\2\u0176\u0177")
        buf.write("\7p\2\2\u0177B\3\2\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7f\2\2\u017bD\3\2\2\2\u017c\u017d")
        buf.write("\7p\2\2\u017d\u017e\7q\2\2\u017e\u017f\7v\2\2\u017fF\3")
        buf.write("\2\2\2\u0180\u0181\7c\2\2\u0181\u0182\7p\2\2\u0182\u0183")
        buf.write("\7f\2\2\u0183H\3\2\2\2\u0184\u0185\7q\2\2\u0185\u0186")
        buf.write("\7t\2\2\u0186J\3\2\2\2\u0187\u0188\7-\2\2\u0188L\3\2\2")
        buf.write("\2\u0189\u018a\7/\2\2\u018aN\3\2\2\2\u018b\u018c\7,\2")
        buf.write("\2\u018cP\3\2\2\2\u018d\u018e\7\61\2\2\u018eR\3\2\2\2")
        buf.write("\u018f\u0190\7\'\2\2\u0190T\3\2\2\2\u0191\u0192\7?\2\2")
        buf.write("\u0192V\3\2\2\2\u0193\u0194\7>\2\2\u0194\u0195\7/\2\2")
        buf.write("\u0195X\3\2\2\2\u0196\u0197\7#\2\2\u0197\u0198\7?\2\2")
        buf.write("\u0198Z\3\2\2\2\u0199\u019a\7>\2\2\u019a\\\3\2\2\2\u019b")
        buf.write("\u019c\7>\2\2\u019c\u019d\7?\2\2\u019d^\3\2\2\2\u019e")
        buf.write("\u019f\7@\2\2\u019f`\3\2\2\2\u01a0\u01a1\7@\2\2\u01a1")
        buf.write("\u01a2\7?\2\2\u01a2b\3\2\2\2\u01a3\u01a4\7\60\2\2\u01a4")
        buf.write("\u01a5\7\60\2\2\u01a5\u01a6\7\60\2\2\u01a6d\3\2\2\2\u01a7")
        buf.write("\u01a8\7?\2\2\u01a8\u01a9\7?\2\2\u01a9f\3\2\2\2\u01aa")
        buf.write("\u01ab\7*\2\2\u01abh\3\2\2\2\u01ac\u01ad\7+\2\2\u01ad")
        buf.write("j\3\2\2\2\u01ae\u01af\7]\2\2\u01afl\3\2\2\2\u01b0\u01b1")
        buf.write("\7_\2\2\u01b1n\3\2\2\2\u01b2\u01b3\7.\2\2\u01b3p\3\2\2")
        buf.write("\2\u01b4\u01b8\t\t\2\2\u01b5\u01b7\t\n\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9r\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\7%\2\2\u01bc\u01bd\7%\2\2\u01bd\u01c1\3\2\2\2\u01be")
        buf.write("\u01c0\n\13\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2")
        buf.write("\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\b:\5\2\u01c5")
        buf.write("t\3\2\2\2\u01c6\u01c7\7\f\2\2\u01c7v\3\2\2\2\u01c8\u01ca")
        buf.write("\t\f\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2")
        buf.write("\u01cd\u01ce\b<\5\2\u01cex\3\2\2\2\u01cf\u01d0\13\2\2")
        buf.write("\2\u01d0\u01d1\b=\6\2\u01d1z\3\2\2\2\26\2\u00ba\u00bd")
        buf.write("\u00c4\u00c7\u00cd\u00d2\u00d8\u00dd\u00e7\u00e9\u00f1")
        buf.write("\u00f4\u00fc\u00fe\u010c\u010e\u01b8\u01c1\u01cb\7\3\r")
        buf.write("\2\3\16\3\3\17\4\b\2\2\3=\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NUMLIT = 7
    BOOLLIT = 8
    STRINGLIT = 9
    ILLEGAL_ESCAPE = 10
    UNCLOSED_STRING = 11
    TRUE = 12
    FALSE = 13
    NUMBER = 14
    BOOL = 15
    STRING = 16
    RETURN = 17
    VAR = 18
    DYNAMIC = 19
    FUNC = 20
    FOR = 21
    UNTIL = 22
    BY = 23
    BREAK = 24
    CONTINUE = 25
    IF = 26
    ELSE = 27
    ELIF = 28
    BEGIN = 29
    END = 30
    NOT = 31
    AND = 32
    OR = 33
    ADDOP = 34
    SUBOP = 35
    MULOP = 36
    DIVOP = 37
    MODOP = 38
    EQUALOP = 39
    ASSIGNOP = 40
    DIFFOP = 41
    LESS = 42
    LESSEQ = 43
    LARGER = 44
    LARGEREQ = 45
    DOT = 46
    STRCOMPARE = 47
    LB = 48
    RB = 49
    LP = 50
    RP = 51
    COMMA = 52
    IDENTIFIER = 53
    COMMENT = 54
    NEWLINE = 55
    WS = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber'", "'writeNumber'", "'readBool'", "'write'", "'readString'", 
            "'writeString'", "'true'", "'false'", "'number'", "'bool'", 
            "'string'", "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'...'", "'=='", "'('", "')'", "'['", "']'", 
            "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUMLIT", "BOOLLIT", "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", "ASSIGNOP", "DIFFOP", 
            "LESS", "LESSEQ", "LARGER", "LARGEREQ", "DOT", "STRCOMPARE", 
            "LB", "RB", "LP", "RP", "COMMA", "IDENTIFIER", "COMMENT", "NEWLINE", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NUMLIT", 
                  "INTPART", "DECPART", "EXPONENTPART", "BOOLLIT", "STRINGLIT", 
                  "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "TRUE", "FALSE", 
                  "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", "ASSIGNOP", 
                  "DIFFOP", "LESS", "LESSEQ", "LARGER", "LARGEREQ", "DOT", 
                  "STRCOMPARE", "LB", "RB", "LP", "RP", "COMMA", "IDENTIFIER", 
                  "COMMENT", "NEWLINE", "WS", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.STRINGLIT_action 
            actions[12] = self.ILLEGAL_ESCAPE_action 
            actions[13] = self.UNCLOSED_STRING_action 
            actions[59] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise UncloseString(self.text)
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     



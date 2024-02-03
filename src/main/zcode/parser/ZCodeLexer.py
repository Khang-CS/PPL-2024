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
        buf.write("\u01d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\5\b\u00bf\n\b\3\b\5\b\u00c2\n\b\3\t\3")
        buf.write("\t\3\t\7\t\u00c7\n\t\f\t\16\t\u00ca\13\t\5\t\u00cc\n\t")
        buf.write("\3\n\3\n\7\n\u00d0\n\n\f\n\16\n\u00d3\13\n\3\13\3\13\5")
        buf.write("\13\u00d7\n\13\3\13\3\13\7\13\u00db\n\13\f\13\16\13\u00de")
        buf.write("\13\13\3\f\3\f\5\f\u00e2\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\7\r\u00ec\n\r\f\r\16\r\u00ef\13\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00f6\n\r\3\r\5\r\u00f9\n\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u0101\n\16\f\16\16\16\u0104\13\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\7\17\u0111\n\17\f\17\16\17\u0114\13\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\79\u01bb\n9\f9\169\u01be\139\3:\3:\3:\3:\7:\u01c4")
        buf.write("\n:\f:\16:\u01c7\13:\3:\3:\3;\3;\3<\6<\u01ce\n<\r<\16")
        buf.write("<\u01cf\3<\3<\3=\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\2\23\2\25\2\27\n\31\13\33\f\35\r\37\16!\17#\20%")
        buf.write("\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;")
        buf.write("\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60")
        buf.write("e\61g\62i\63k\64m\65o\66q\67s8u9w:y;\3\2\r\3\2\63;\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$")
        buf.write("$^^\7\2\f\f\17\17$$))^^\5\2C\\aac|\6\2\62;C\\aac|\4\2")
        buf.write("\f\f\17\17\5\2\13\13\17\17\"\"\2\u01e8\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3")
        buf.write("{\3\2\2\2\5\u0086\3\2\2\2\7\u0092\3\2\2\2\t\u009b\3\2")
        buf.write("\2\2\13\u00a5\3\2\2\2\r\u00b0\3\2\2\2\17\u00bc\3\2\2\2")
        buf.write("\21\u00cb\3\2\2\2\23\u00cd\3\2\2\2\25\u00d4\3\2\2\2\27")
        buf.write("\u00e1\3\2\2\2\31\u00f8\3\2\2\2\33\u00fc\3\2\2\2\35\u010a")
        buf.write("\3\2\2\2\37\u0117\3\2\2\2!\u011c\3\2\2\2#\u0122\3\2\2")
        buf.write("\2%\u0129\3\2\2\2\'\u012e\3\2\2\2)\u0135\3\2\2\2+\u013c")
        buf.write("\3\2\2\2-\u0140\3\2\2\2/\u0148\3\2\2\2\61\u014d\3\2\2")
        buf.write("\2\63\u0151\3\2\2\2\65\u0157\3\2\2\2\67\u015a\3\2\2\2")
        buf.write("9\u0160\3\2\2\2;\u0169\3\2\2\2=\u016c\3\2\2\2?\u0171\3")
        buf.write("\2\2\2A\u0176\3\2\2\2C\u017c\3\2\2\2E\u0180\3\2\2\2G\u0184")
        buf.write("\3\2\2\2I\u0188\3\2\2\2K\u018b\3\2\2\2M\u018d\3\2\2\2")
        buf.write("O\u018f\3\2\2\2Q\u0191\3\2\2\2S\u0193\3\2\2\2U\u0195\3")
        buf.write("\2\2\2W\u0197\3\2\2\2Y\u019a\3\2\2\2[\u019d\3\2\2\2]\u019f")
        buf.write("\3\2\2\2_\u01a2\3\2\2\2a\u01a4\3\2\2\2c\u01a7\3\2\2\2")
        buf.write("e\u01ab\3\2\2\2g\u01ae\3\2\2\2i\u01b0\3\2\2\2k\u01b2\3")
        buf.write("\2\2\2m\u01b4\3\2\2\2o\u01b6\3\2\2\2q\u01b8\3\2\2\2s\u01bf")
        buf.write("\3\2\2\2u\u01ca\3\2\2\2w\u01cd\3\2\2\2y\u01d3\3\2\2\2")
        buf.write("{|\7t\2\2|}\7g\2\2}~\7c\2\2~\177\7f\2\2\177\u0080\7P\2")
        buf.write("\2\u0080\u0081\7w\2\2\u0081\u0082\7o\2\2\u0082\u0083\7")
        buf.write("d\2\2\u0083\u0084\7g\2\2\u0084\u0085\7t\2\2\u0085\4\3")
        buf.write("\2\2\2\u0086\u0087\7y\2\2\u0087\u0088\7t\2\2\u0088\u0089")
        buf.write("\7k\2\2\u0089\u008a\7v\2\2\u008a\u008b\7g\2\2\u008b\u008c")
        buf.write("\7P\2\2\u008c\u008d\7w\2\2\u008d\u008e\7o\2\2\u008e\u008f")
        buf.write("\7d\2\2\u008f\u0090\7g\2\2\u0090\u0091\7t\2\2\u0091\6")
        buf.write("\3\2\2\2\u0092\u0093\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7f\2\2\u0096\u0097\7D\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7q\2\2\u0099\u009a\7n\2\2\u009a\b")
        buf.write("\3\2\2\2\u009b\u009c\7y\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7D\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4")
        buf.write("\7n\2\2\u00a4\n\3\2\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa")
        buf.write("\7U\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af\f")
        buf.write("\3\2\2\2\u00b0\u00b1\7y\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7U\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\16")
        buf.write("\3\2\2\2\u00bc\u00be\5\21\t\2\u00bd\u00bf\5\23\n\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2")
        buf.write("\u00c0\u00c2\5\25\13\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\20\3\2\2\2\u00c3\u00cc\7\62\2\2\u00c4\u00c8")
        buf.write("\t\2\2\2\u00c5\u00c7\t\3\2\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00c3\3")
        buf.write("\2\2\2\u00cb\u00c4\3\2\2\2\u00cc\22\3\2\2\2\u00cd\u00d1")
        buf.write("\7\60\2\2\u00ce\u00d0\t\3\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\24\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6\t\4")
        buf.write("\2\2\u00d5\u00d7\t\5\2\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00dc\t\2\2\2\u00d9")
        buf.write("\u00db\t\3\2\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\26\3\2")
        buf.write("\2\2\u00de\u00dc\3\2\2\2\u00df\u00e2\5\37\20\2\u00e0\u00e2")
        buf.write("\5!\21\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\30\3\2\2\2\u00e3\u00e4\7$\2\2\u00e4\u00f9\7$\2\2\u00e5")
        buf.write("\u00ed\7$\2\2\u00e6\u00e7\7)\2\2\u00e7\u00ec\7$\2\2\u00e8")
        buf.write("\u00e9\7^\2\2\u00e9\u00ec\t\6\2\2\u00ea\u00ec\n\7\2\2")
        buf.write("\u00eb\u00e6\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00ea\3")
        buf.write("\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\u00f5\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0")
        buf.write("\u00f1\7)\2\2\u00f1\u00f6\7$\2\2\u00f2\u00f3\7^\2\2\u00f3")
        buf.write("\u00f6\t\6\2\2\u00f4\u00f6\n\b\2\2\u00f5\u00f0\3\2\2\2")
        buf.write("\u00f5\u00f2\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7\u00f9\7$\2\2\u00f8\u00e3\3\2\2\2\u00f8\u00e5")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\b\r\2\2\u00fb")
        buf.write("\32\3\2\2\2\u00fc\u0102\7$\2\2\u00fd\u00fe\7^\2\2\u00fe")
        buf.write("\u0101\t\6\2\2\u00ff\u0101\n\7\2\2\u0100\u00fd\3\2\2\2")
        buf.write("\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3")
        buf.write("\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u0102")
        buf.write("\3\2\2\2\u0105\u0106\7^\2\2\u0106\u0107\n\6\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\b\16\3\2\u0109\34\3\2\2\2\u010a")
        buf.write("\u0112\7$\2\2\u010b\u010c\7)\2\2\u010c\u0111\7$\2\2\u010d")
        buf.write("\u010e\7^\2\2\u010e\u0111\t\6\2\2\u010f\u0111\n\7\2\2")
        buf.write("\u0110\u010b\3\2\2\2\u0110\u010d\3\2\2\2\u0110\u010f\3")
        buf.write("\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u0116\b\17\4\2\u0116\36\3\2\2\2\u0117\u0118\7v\2\2\u0118")
        buf.write("\u0119\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write(" \3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7c\2\2\u011e")
        buf.write("\u011f\7n\2\2\u011f\u0120\7u\2\2\u0120\u0121\7g\2\2\u0121")
        buf.write("\"\3\2\2\2\u0122\u0123\7p\2\2\u0123\u0124\7w\2\2\u0124")
        buf.write("\u0125\7o\2\2\u0125\u0126\7d\2\2\u0126\u0127\7g\2\2\u0127")
        buf.write("\u0128\7t\2\2\u0128$\3\2\2\2\u0129\u012a\7d\2\2\u012a")
        buf.write("\u012b\7q\2\2\u012b\u012c\7q\2\2\u012c\u012d\7n\2\2\u012d")
        buf.write("&\3\2\2\2\u012e\u012f\7u\2\2\u012f\u0130\7v\2\2\u0130")
        buf.write("\u0131\7t\2\2\u0131\u0132\7k\2\2\u0132\u0133\7p\2\2\u0133")
        buf.write("\u0134\7i\2\2\u0134(\3\2\2\2\u0135\u0136\7t\2\2\u0136")
        buf.write("\u0137\7g\2\2\u0137\u0138\7v\2\2\u0138\u0139\7w\2\2\u0139")
        buf.write("\u013a\7t\2\2\u013a\u013b\7p\2\2\u013b*\3\2\2\2\u013c")
        buf.write("\u013d\7x\2\2\u013d\u013e\7c\2\2\u013e\u013f\7t\2\2\u013f")
        buf.write(",\3\2\2\2\u0140\u0141\7f\2\2\u0141\u0142\7{\2\2\u0142")
        buf.write("\u0143\7p\2\2\u0143\u0144\7c\2\2\u0144\u0145\7o\2\2\u0145")
        buf.write("\u0146\7k\2\2\u0146\u0147\7e\2\2\u0147.\3\2\2\2\u0148")
        buf.write("\u0149\7h\2\2\u0149\u014a\7w\2\2\u014a\u014b\7p\2\2\u014b")
        buf.write("\u014c\7e\2\2\u014c\60\3\2\2\2\u014d\u014e\7h\2\2\u014e")
        buf.write("\u014f\7q\2\2\u014f\u0150\7t\2\2\u0150\62\3\2\2\2\u0151")
        buf.write("\u0152\7w\2\2\u0152\u0153\7p\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write("\u0155\7k\2\2\u0155\u0156\7n\2\2\u0156\64\3\2\2\2\u0157")
        buf.write("\u0158\7d\2\2\u0158\u0159\7{\2\2\u0159\66\3\2\2\2\u015a")
        buf.write("\u015b\7d\2\2\u015b\u015c\7t\2\2\u015c\u015d\7g\2\2\u015d")
        buf.write("\u015e\7c\2\2\u015e\u015f\7m\2\2\u015f8\3\2\2\2\u0160")
        buf.write("\u0161\7e\2\2\u0161\u0162\7q\2\2\u0162\u0163\7p\2\2\u0163")
        buf.write("\u0164\7v\2\2\u0164\u0165\7k\2\2\u0165\u0166\7p\2\2\u0166")
        buf.write("\u0167\7w\2\2\u0167\u0168\7g\2\2\u0168:\3\2\2\2\u0169")
        buf.write("\u016a\7k\2\2\u016a\u016b\7h\2\2\u016b<\3\2\2\2\u016c")
        buf.write("\u016d\7g\2\2\u016d\u016e\7n\2\2\u016e\u016f\7u\2\2\u016f")
        buf.write("\u0170\7g\2\2\u0170>\3\2\2\2\u0171\u0172\7g\2\2\u0172")
        buf.write("\u0173\7n\2\2\u0173\u0174\7k\2\2\u0174\u0175\7h\2\2\u0175")
        buf.write("@\3\2\2\2\u0176\u0177\7d\2\2\u0177\u0178\7g\2\2\u0178")
        buf.write("\u0179\7i\2\2\u0179\u017a\7k\2\2\u017a\u017b\7p\2\2\u017b")
        buf.write("B\3\2\2\2\u017c\u017d\7g\2\2\u017d\u017e\7p\2\2\u017e")
        buf.write("\u017f\7f\2\2\u017fD\3\2\2\2\u0180\u0181\7p\2\2\u0181")
        buf.write("\u0182\7q\2\2\u0182\u0183\7v\2\2\u0183F\3\2\2\2\u0184")
        buf.write("\u0185\7c\2\2\u0185\u0186\7p\2\2\u0186\u0187\7f\2\2\u0187")
        buf.write("H\3\2\2\2\u0188\u0189\7q\2\2\u0189\u018a\7t\2\2\u018a")
        buf.write("J\3\2\2\2\u018b\u018c\7-\2\2\u018cL\3\2\2\2\u018d\u018e")
        buf.write("\7/\2\2\u018eN\3\2\2\2\u018f\u0190\7,\2\2\u0190P\3\2\2")
        buf.write("\2\u0191\u0192\7\61\2\2\u0192R\3\2\2\2\u0193\u0194\7\'")
        buf.write("\2\2\u0194T\3\2\2\2\u0195\u0196\7?\2\2\u0196V\3\2\2\2")
        buf.write("\u0197\u0198\7>\2\2\u0198\u0199\7/\2\2\u0199X\3\2\2\2")
        buf.write("\u019a\u019b\7#\2\2\u019b\u019c\7?\2\2\u019cZ\3\2\2\2")
        buf.write("\u019d\u019e\7>\2\2\u019e\\\3\2\2\2\u019f\u01a0\7>\2\2")
        buf.write("\u01a0\u01a1\7?\2\2\u01a1^\3\2\2\2\u01a2\u01a3\7@\2\2")
        buf.write("\u01a3`\3\2\2\2\u01a4\u01a5\7@\2\2\u01a5\u01a6\7?\2\2")
        buf.write("\u01a6b\3\2\2\2\u01a7\u01a8\7\60\2\2\u01a8\u01a9\7\60")
        buf.write("\2\2\u01a9\u01aa\7\60\2\2\u01aad\3\2\2\2\u01ab\u01ac\7")
        buf.write("?\2\2\u01ac\u01ad\7?\2\2\u01adf\3\2\2\2\u01ae\u01af\7")
        buf.write("*\2\2\u01afh\3\2\2\2\u01b0\u01b1\7+\2\2\u01b1j\3\2\2\2")
        buf.write("\u01b2\u01b3\7]\2\2\u01b3l\3\2\2\2\u01b4\u01b5\7_\2\2")
        buf.write("\u01b5n\3\2\2\2\u01b6\u01b7\7.\2\2\u01b7p\3\2\2\2\u01b8")
        buf.write("\u01bc\t\t\2\2\u01b9\u01bb\t\n\2\2\u01ba\u01b9\3\2\2\2")
        buf.write("\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3")
        buf.write("\2\2\2\u01bdr\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0")
        buf.write("\7%\2\2\u01c0\u01c1\7%\2\2\u01c1\u01c5\3\2\2\2\u01c2\u01c4")
        buf.write("\n\13\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c8\u01c9\b:\5\2\u01c9t\3\2\2\2")
        buf.write("\u01ca\u01cb\7\f\2\2\u01cbv\3\2\2\2\u01cc\u01ce\t\f\2")
        buf.write("\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d2\b<\5\2\u01d2x\3\2\2\2\u01d3\u01d4\13\2\2\2\u01d4")
        buf.write("\u01d5\b=\6\2\u01d5z\3\2\2\2\26\2\u00be\u00c1\u00c8\u00cb")
        buf.write("\u00d1\u00d6\u00dc\u00e1\u00eb\u00ed\u00f5\u00f8\u0100")
        buf.write("\u0102\u0110\u0112\u01bc\u01c5\u01cf\7\3\r\2\3\16\3\3")
        buf.write("\17\4\b\2\2\3=\5")
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
            "'readNumber'", "'writeNumber'", "'readBool'", "'writeBool'", 
            "'readString'", "'writeString'", "'true'", "'false'", "'number'", 
            "'bool'", "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
            "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
            "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", "'['", 
            "']'", "','", "'\n'" ]

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
     



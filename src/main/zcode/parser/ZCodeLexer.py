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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0189\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\2\5\2u\n\2\3\3\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\5\3\177")
        buf.write("\n\3\3\4\3\4\7\4\u0083\n\4\f\4\16\4\u0086\13\4\3\5\3\5")
        buf.write("\5\5\u008a\n\5\3\5\3\5\7\5\u008e\n\5\f\5\16\5\u0091\13")
        buf.write("\5\3\6\3\6\5\6\u0095\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\7\7\u009f\n\7\f\7\16\7\u00a2\13\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00a9\n\7\3\7\5\7\u00ac\n\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u00b4\n\b\f\b\16\b\u00b7\13\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00c4\n\t\f\t\16\t\u00c7")
        buf.write("\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\7\63\u016e\n\63\f\63")
        buf.write("\16\63\u0171\13\63\3\64\3\64\3\64\3\64\7\64\u0177\n\64")
        buf.write("\f\64\16\64\u017a\13\64\3\64\3\64\3\65\3\65\3\66\6\66")
        buf.write("\u0181\n\66\r\66\16\66\u0182\3\66\3\66\3\67\3\67\3\67")
        buf.write("\2\28\3\3\5\2\7\2\t\2\13\4\r\5\17\6\21\7\23\b\25\t\27")
        buf.write("\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25")
        buf.write("/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G")
        buf.write("\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65")
        buf.write("\3\2\r\3\2\63;\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhppt")
        buf.write("tvv\6\2\f\f\17\17$$^^\7\2\f\f\17\17$$))^^\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2\f\f\17\17\5\2\13\13\17\17\"\"\2\u019b")
        buf.write("\2\3\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\3o\3\2\2\2\5~\3\2\2\2\7\u0080\3\2\2\2\t\u0087\3\2\2")
        buf.write("\2\13\u0094\3\2\2\2\r\u00ab\3\2\2\2\17\u00af\3\2\2\2\21")
        buf.write("\u00bd\3\2\2\2\23\u00ca\3\2\2\2\25\u00cf\3\2\2\2\27\u00d5")
        buf.write("\3\2\2\2\31\u00dc\3\2\2\2\33\u00e1\3\2\2\2\35\u00e8\3")
        buf.write("\2\2\2\37\u00ef\3\2\2\2!\u00f3\3\2\2\2#\u00fb\3\2\2\2")
        buf.write("%\u0100\3\2\2\2\'\u0104\3\2\2\2)\u010a\3\2\2\2+\u010d")
        buf.write("\3\2\2\2-\u0113\3\2\2\2/\u011c\3\2\2\2\61\u011f\3\2\2")
        buf.write("\2\63\u0124\3\2\2\2\65\u0129\3\2\2\2\67\u012f\3\2\2\2")
        buf.write("9\u0133\3\2\2\2;\u0137\3\2\2\2=\u013b\3\2\2\2?\u013e\3")
        buf.write("\2\2\2A\u0140\3\2\2\2C\u0142\3\2\2\2E\u0144\3\2\2\2G\u0146")
        buf.write("\3\2\2\2I\u0148\3\2\2\2K\u014a\3\2\2\2M\u014d\3\2\2\2")
        buf.write("O\u0150\3\2\2\2Q\u0152\3\2\2\2S\u0155\3\2\2\2U\u0157\3")
        buf.write("\2\2\2W\u015a\3\2\2\2Y\u015e\3\2\2\2[\u0161\3\2\2\2]\u0163")
        buf.write("\3\2\2\2_\u0165\3\2\2\2a\u0167\3\2\2\2c\u0169\3\2\2\2")
        buf.write("e\u016b\3\2\2\2g\u0172\3\2\2\2i\u017d\3\2\2\2k\u0180\3")
        buf.write("\2\2\2m\u0186\3\2\2\2oq\5\5\3\2pr\5\7\4\2qp\3\2\2\2qr")
        buf.write("\3\2\2\2rt\3\2\2\2su\5\t\5\2ts\3\2\2\2tu\3\2\2\2u\4\3")
        buf.write("\2\2\2v\177\7\62\2\2w{\t\2\2\2xz\t\3\2\2yx\3\2\2\2z}\3")
        buf.write("\2\2\2{y\3\2\2\2{|\3\2\2\2|\177\3\2\2\2}{\3\2\2\2~v\3")
        buf.write("\2\2\2~w\3\2\2\2\177\6\3\2\2\2\u0080\u0084\7\60\2\2\u0081")
        buf.write("\u0083\t\3\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\b\3\2\2")
        buf.write("\2\u0086\u0084\3\2\2\2\u0087\u0089\t\4\2\2\u0088\u008a")
        buf.write("\t\5\2\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008f\t\2\2\2\u008c\u008e\t\3\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3")
        buf.write("\2\2\2\u008f\u0090\3\2\2\2\u0090\n\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0095\5\23\n\2\u0093\u0095\5\25\13\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\f\3\2\2\2\u0096")
        buf.write("\u0097\7$\2\2\u0097\u00ac\7$\2\2\u0098\u00a0\7$\2\2\u0099")
        buf.write("\u009a\7)\2\2\u009a\u009f\7$\2\2\u009b\u009c\7^\2\2\u009c")
        buf.write("\u009f\t\6\2\2\u009d\u009f\n\7\2\2\u009e\u0099\3\2\2\2")
        buf.write("\u009e\u009b\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a2\3")
        buf.write("\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a8")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7)\2\2\u00a4")
        buf.write("\u00a9\7$\2\2\u00a5\u00a6\7^\2\2\u00a6\u00a9\t\6\2\2\u00a7")
        buf.write("\u00a9\n\b\2\2\u00a8\u00a3\3\2\2\2\u00a8\u00a5\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\7")
        buf.write("$\2\2\u00ab\u0096\3\2\2\2\u00ab\u0098\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00ae\b\7\2\2\u00ae\16\3\2\2\2\u00af\u00b5")
        buf.write("\7$\2\2\u00b0\u00b1\7^\2\2\u00b1\u00b4\t\6\2\2\u00b2\u00b4")
        buf.write("\n\7\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7")
        buf.write("^\2\2\u00b9\u00ba\n\6\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc")
        buf.write("\b\b\3\2\u00bc\20\3\2\2\2\u00bd\u00c5\7$\2\2\u00be\u00bf")
        buf.write("\7)\2\2\u00bf\u00c4\7$\2\2\u00c0\u00c1\7^\2\2\u00c1\u00c4")
        buf.write("\t\6\2\2\u00c2\u00c4\n\7\2\2\u00c3\u00be\3\2\2\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2")
        buf.write("\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3")
        buf.write("\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\b\t\4\2\u00c9\22")
        buf.write("\3\2\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7g\2\2\u00ce\24\3\2\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\26\3\2\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8\7o\2\2\u00d8\u00d9")
        buf.write("\7d\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7t\2\2\u00db\30")
        buf.write("\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7n\2\2\u00e0\32\3\2\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7i\2\2\u00e7\34")
        buf.write("\3\2\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7t\2\2\u00f2 \3\2\2\2\u00f3\u00f4")
        buf.write("\7f\2\2\u00f4\u00f5\7{\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7o\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7e\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd")
        buf.write("\7w\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7e\2\2\u00ff$\3")
        buf.write("\2\2\2\u0100\u0101\7h\2\2\u0101\u0102\7q\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103&\3\2\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109(\3\2\2\2\u010a\u010b\7d\2\2\u010b\u010c")
        buf.write("\7{\2\2\u010c*\3\2\2\2\u010d\u010e\7d\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7m\2\2\u0112,\3\2\2\2\u0113\u0114\7e\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7p\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b.\3\2\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7h\2\2\u011e\60\3\2\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123\62")
        buf.write("\3\2\2\2\u0124\u0125\7g\2\2\u0125\u0126\7n\2\2\u0126\u0127")
        buf.write("\7k\2\2\u0127\u0128\7h\2\2\u0128\64\3\2\2\2\u0129\u012a")
        buf.write("\7d\2\2\u012a\u012b\7g\2\2\u012b\u012c\7i\2\2\u012c\u012d")
        buf.write("\7k\2\2\u012d\u012e\7p\2\2\u012e\66\3\2\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130\u0131\7p\2\2\u0131\u0132\7f\2\2\u01328\3")
        buf.write("\2\2\2\u0133\u0134\7p\2\2\u0134\u0135\7q\2\2\u0135\u0136")
        buf.write("\7v\2\2\u0136:\3\2\2\2\u0137\u0138\7c\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7f\2\2\u013a<\3\2\2\2\u013b\u013c")
        buf.write("\7q\2\2\u013c\u013d\7t\2\2\u013d>\3\2\2\2\u013e\u013f")
        buf.write("\7-\2\2\u013f@\3\2\2\2\u0140\u0141\7/\2\2\u0141B\3\2\2")
        buf.write("\2\u0142\u0143\7,\2\2\u0143D\3\2\2\2\u0144\u0145\7\61")
        buf.write("\2\2\u0145F\3\2\2\2\u0146\u0147\7\'\2\2\u0147H\3\2\2\2")
        buf.write("\u0148\u0149\7?\2\2\u0149J\3\2\2\2\u014a\u014b\7>\2\2")
        buf.write("\u014b\u014c\7/\2\2\u014cL\3\2\2\2\u014d\u014e\7#\2\2")
        buf.write("\u014e\u014f\7?\2\2\u014fN\3\2\2\2\u0150\u0151\7>\2\2")
        buf.write("\u0151P\3\2\2\2\u0152\u0153\7>\2\2\u0153\u0154\7?\2\2")
        buf.write("\u0154R\3\2\2\2\u0155\u0156\7@\2\2\u0156T\3\2\2\2\u0157")
        buf.write("\u0158\7@\2\2\u0158\u0159\7?\2\2\u0159V\3\2\2\2\u015a")
        buf.write("\u015b\7\60\2\2\u015b\u015c\7\60\2\2\u015c\u015d\7\60")
        buf.write("\2\2\u015dX\3\2\2\2\u015e\u015f\7?\2\2\u015f\u0160\7?")
        buf.write("\2\2\u0160Z\3\2\2\2\u0161\u0162\7*\2\2\u0162\\\3\2\2\2")
        buf.write("\u0163\u0164\7+\2\2\u0164^\3\2\2\2\u0165\u0166\7]\2\2")
        buf.write("\u0166`\3\2\2\2\u0167\u0168\7_\2\2\u0168b\3\2\2\2\u0169")
        buf.write("\u016a\7.\2\2\u016ad\3\2\2\2\u016b\u016f\t\t\2\2\u016c")
        buf.write("\u016e\t\n\2\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170f\3\2\2")
        buf.write("\2\u0171\u016f\3\2\2\2\u0172\u0173\7%\2\2\u0173\u0174")
        buf.write("\7%\2\2\u0174\u0178\3\2\2\2\u0175\u0177\n\13\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017b\u017c\b\64\5\2\u017ch\3\2\2\2\u017d\u017e")
        buf.write("\7\f\2\2\u017ej\3\2\2\2\u017f\u0181\t\f\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\b\66\5")
        buf.write("\2\u0185l\3\2\2\2\u0186\u0187\13\2\2\2\u0187\u0188\b\67")
        buf.write("\6\2\u0188n\3\2\2\2\26\2qt{~\u0084\u0089\u008f\u0094\u009e")
        buf.write("\u00a0\u00a8\u00ab\u00b3\u00b5\u00c3\u00c5\u016f\u0178")
        buf.write("\u0182\7\3\7\2\3\b\3\3\t\4\b\2\2\3\67\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMLIT = 1
    BOOLLIT = 2
    STRINGLIT = 3
    ILLEGAL_ESCAPE = 4
    UNCLOSED_STRING = 5
    TRUE = 6
    FALSE = 7
    NUMBER = 8
    BOOL = 9
    STRING = 10
    RETURN = 11
    VAR = 12
    DYNAMIC = 13
    FUNC = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    BREAK = 18
    CONTINUE = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    BEGIN = 23
    END = 24
    NOT = 25
    AND = 26
    OR = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    DIVOP = 31
    MODOP = 32
    EQUALOP = 33
    ASSIGNOP = 34
    DIFFOP = 35
    LESS = 36
    LESSEQ = 37
    LARGER = 38
    LARGEREQ = 39
    DOT = 40
    STRCOMPARE = 41
    LB = 42
    RB = 43
    LP = 44
    RP = 45
    COMMA = 46
    IDENTIFIER = 47
    COMMENT = 48
    NEWLINE = 49
    WS = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUMLIT", "BOOLLIT", "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", "ASSIGNOP", "DIFFOP", 
            "LESS", "LESSEQ", "LARGER", "LARGEREQ", "DOT", "STRCOMPARE", 
            "LB", "RB", "LP", "RP", "COMMA", "IDENTIFIER", "COMMENT", "NEWLINE", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "NUMLIT", "INTPART", "DECPART", "EXPONENTPART", "BOOLLIT", 
                  "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "TRUE", 
                  "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", 
                  "ASSIGNOP", "DIFFOP", "LESS", "LESSEQ", "LARGER", "LARGEREQ", 
                  "DOT", "STRCOMPARE", "LB", "RB", "LP", "RP", "COMMA", 
                  "IDENTIFIER", "COMMENT", "NEWLINE", "WS", "ERROR_CHAR" ]

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
            actions[5] = self.STRINGLIT_action 
            actions[6] = self.ILLEGAL_ESCAPE_action 
            actions[7] = self.UNCLOSED_STRING_action 
            actions[53] = self.ERROR_CHAR_action 
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
     



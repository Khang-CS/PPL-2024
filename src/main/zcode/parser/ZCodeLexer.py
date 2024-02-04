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
        buf.write("\u0186\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\2\5\2u\n\2\3\3\6\3x\n\3\r\3\16\3y\3\4\3\4\7\4~\n\4\f")
        buf.write("\4\16\4\u0081\13\4\3\5\3\5\5\5\u0085\n\5\3\5\3\5\7\5\u0089")
        buf.write("\n\5\f\5\16\5\u008c\13\5\3\6\3\6\5\6\u0090\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u009a\n\7\f\7\16\7\u009d")
        buf.write("\13\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a4\n\7\3\7\5\7\u00a7")
        buf.write("\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b1\n\b\f\b")
        buf.write("\16\b\u00b4\13\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u00c1\n\t\f\t\16\t\u00c4\13\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\7\63\u016b\n\63\f\63\16\63\u016e\13\63\3\64")
        buf.write("\3\64\3\64\3\64\7\64\u0174\n\64\f\64\16\64\u0177\13\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\6\66\u017e\n\66\r\66\16\66\u017f")
        buf.write("\3\66\3\66\3\67\3\67\3\67\2\28\3\3\5\2\7\2\t\2\13\4\r")
        buf.write("\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17")
        buf.write("#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\32")
        buf.write("9\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a")
        buf.write("/c\60e\61g\62i\63k\64m\65\3\2\r\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\7\2\f\f")
        buf.write("\17\17$$))^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5")
        buf.write("\2\13\13\17\17\"\"\2\u0198\2\3\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5w\3\2\2\2\7")
        buf.write("{\3\2\2\2\t\u0082\3\2\2\2\13\u008f\3\2\2\2\r\u00a6\3\2")
        buf.write("\2\2\17\u00aa\3\2\2\2\21\u00ba\3\2\2\2\23\u00c7\3\2\2")
        buf.write("\2\25\u00cc\3\2\2\2\27\u00d2\3\2\2\2\31\u00d9\3\2\2\2")
        buf.write("\33\u00de\3\2\2\2\35\u00e5\3\2\2\2\37\u00ec\3\2\2\2!\u00f0")
        buf.write("\3\2\2\2#\u00f8\3\2\2\2%\u00fd\3\2\2\2\'\u0101\3\2\2\2")
        buf.write(")\u0107\3\2\2\2+\u010a\3\2\2\2-\u0110\3\2\2\2/\u0119\3")
        buf.write("\2\2\2\61\u011c\3\2\2\2\63\u0121\3\2\2\2\65\u0126\3\2")
        buf.write("\2\2\67\u012c\3\2\2\29\u0130\3\2\2\2;\u0134\3\2\2\2=\u0138")
        buf.write("\3\2\2\2?\u013b\3\2\2\2A\u013d\3\2\2\2C\u013f\3\2\2\2")
        buf.write("E\u0141\3\2\2\2G\u0143\3\2\2\2I\u0145\3\2\2\2K\u0147\3")
        buf.write("\2\2\2M\u014a\3\2\2\2O\u014d\3\2\2\2Q\u014f\3\2\2\2S\u0152")
        buf.write("\3\2\2\2U\u0154\3\2\2\2W\u0157\3\2\2\2Y\u015b\3\2\2\2")
        buf.write("[\u015e\3\2\2\2]\u0160\3\2\2\2_\u0162\3\2\2\2a\u0164\3")
        buf.write("\2\2\2c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016f\3\2\2\2i\u017a")
        buf.write("\3\2\2\2k\u017d\3\2\2\2m\u0183\3\2\2\2oq\5\5\3\2pr\5\7")
        buf.write("\4\2qp\3\2\2\2qr\3\2\2\2rt\3\2\2\2su\5\t\5\2ts\3\2\2\2")
        buf.write("tu\3\2\2\2u\4\3\2\2\2vx\t\2\2\2wv\3\2\2\2xy\3\2\2\2yw")
        buf.write("\3\2\2\2yz\3\2\2\2z\6\3\2\2\2{\177\7\60\2\2|~\t\2\2\2")
        buf.write("}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2")
        buf.write("\2\u0080\b\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084\t\3\2")
        buf.write("\2\u0083\u0085\t\4\2\2\u0084\u0083\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008a\t\5\2\2\u0087")
        buf.write("\u0089\t\2\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\n\3\2\2")
        buf.write("\2\u008c\u008a\3\2\2\2\u008d\u0090\5\23\n\2\u008e\u0090")
        buf.write("\5\25\13\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\f\3\2\2\2\u0091\u0092\7$\2\2\u0092\u00a7\7$\2\2\u0093")
        buf.write("\u009b\7$\2\2\u0094\u0095\7)\2\2\u0095\u009a\7$\2\2\u0096")
        buf.write("\u0097\7^\2\2\u0097\u009a\t\6\2\2\u0098\u009a\n\7\2\2")
        buf.write("\u0099\u0094\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0098\3")
        buf.write("\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u00a3\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u009f\7)\2\2\u009f\u00a4\7$\2\2\u00a0\u00a1\7^\2\2\u00a1")
        buf.write("\u00a4\t\6\2\2\u00a2\u00a4\n\b\2\2\u00a3\u009e\3\2\2\2")
        buf.write("\u00a3\u00a0\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00a7\7$\2\2\u00a6\u0091\3\2\2\2\u00a6\u0093")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\b\7\2\2\u00a9")
        buf.write("\16\3\2\2\2\u00aa\u00b2\7$\2\2\u00ab\u00ac\7)\2\2\u00ac")
        buf.write("\u00b1\7$\2\2\u00ad\u00ae\7^\2\2\u00ae\u00b1\t\6\2\2\u00af")
        buf.write("\u00b1\n\7\2\2\u00b0\u00ab\3\2\2\2\u00b0\u00ad\3\2\2\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b6\7^\2\2\u00b6\u00b7\n\6\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\b\b\3\2\u00b9\20\3\2\2\2\u00ba")
        buf.write("\u00c2\7$\2\2\u00bb\u00bc\7)\2\2\u00bc\u00c1\7$\2\2\u00bd")
        buf.write("\u00be\7^\2\2\u00be\u00c1\t\6\2\2\u00bf\u00c1\n\7\2\2")
        buf.write("\u00c0\u00bb\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00bf\3")
        buf.write("\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5")
        buf.write("\u00c6\b\t\4\2\u00c6\22\3\2\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\24\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write("\u00cf\7n\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\26\3\2\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7w\2\2\u00d4")
        buf.write("\u00d5\7o\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7\7g\2\2\u00d7")
        buf.write("\u00d8\7t\2\2\u00d8\30\3\2\2\2\u00d9\u00da\7d\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7n\2\2\u00dd")
        buf.write("\32\3\2\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7i\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7p\2\2\u00eb\36\3\2\2\2\u00ec")
        buf.write("\u00ed\7x\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7t\2\2\u00ef")
        buf.write(" \3\2\2\2\u00f0\u00f1\7f\2\2\u00f1\u00f2\7{\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7o\2\2\u00f5")
        buf.write("\u00f6\7k\2\2\u00f6\u00f7\7e\2\2\u00f7\"\3\2\2\2\u00f8")
        buf.write("\u00f9\7h\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7p\2\2\u00fb")
        buf.write("\u00fc\7e\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7h\2\2\u00fe")
        buf.write("\u00ff\7q\2\2\u00ff\u0100\7t\2\2\u0100&\3\2\2\2\u0101")
        buf.write("\u0102\7w\2\2\u0102\u0103\7p\2\2\u0103\u0104\7v\2\2\u0104")
        buf.write("\u0105\7k\2\2\u0105\u0106\7n\2\2\u0106(\3\2\2\2\u0107")
        buf.write("\u0108\7d\2\2\u0108\u0109\7{\2\2\u0109*\3\2\2\2\u010a")
        buf.write("\u010b\7d\2\2\u010b\u010c\7t\2\2\u010c\u010d\7g\2\2\u010d")
        buf.write("\u010e\7c\2\2\u010e\u010f\7m\2\2\u010f,\3\2\2\2\u0110")
        buf.write("\u0111\7e\2\2\u0111\u0112\7q\2\2\u0112\u0113\7p\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\u0115\7k\2\2\u0115\u0116\7p\2\2\u0116")
        buf.write("\u0117\7w\2\2\u0117\u0118\7g\2\2\u0118.\3\2\2\2\u0119")
        buf.write("\u011a\7k\2\2\u011a\u011b\7h\2\2\u011b\60\3\2\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f")
        buf.write("\u0120\7g\2\2\u0120\62\3\2\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write("\u0123\7n\2\2\u0123\u0124\7k\2\2\u0124\u0125\7h\2\2\u0125")
        buf.write("\64\3\2\2\2\u0126\u0127\7d\2\2\u0127\u0128\7g\2\2\u0128")
        buf.write("\u0129\7i\2\2\u0129\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b")
        buf.write("\66\3\2\2\2\u012c\u012d\7g\2\2\u012d\u012e\7p\2\2\u012e")
        buf.write("\u012f\7f\2\2\u012f8\3\2\2\2\u0130\u0131\7p\2\2\u0131")
        buf.write("\u0132\7q\2\2\u0132\u0133\7v\2\2\u0133:\3\2\2\2\u0134")
        buf.write("\u0135\7c\2\2\u0135\u0136\7p\2\2\u0136\u0137\7f\2\2\u0137")
        buf.write("<\3\2\2\2\u0138\u0139\7q\2\2\u0139\u013a\7t\2\2\u013a")
        buf.write(">\3\2\2\2\u013b\u013c\7-\2\2\u013c@\3\2\2\2\u013d\u013e")
        buf.write("\7/\2\2\u013eB\3\2\2\2\u013f\u0140\7,\2\2\u0140D\3\2\2")
        buf.write("\2\u0141\u0142\7\61\2\2\u0142F\3\2\2\2\u0143\u0144\7\'")
        buf.write("\2\2\u0144H\3\2\2\2\u0145\u0146\7?\2\2\u0146J\3\2\2\2")
        buf.write("\u0147\u0148\7>\2\2\u0148\u0149\7/\2\2\u0149L\3\2\2\2")
        buf.write("\u014a\u014b\7#\2\2\u014b\u014c\7?\2\2\u014cN\3\2\2\2")
        buf.write("\u014d\u014e\7>\2\2\u014eP\3\2\2\2\u014f\u0150\7>\2\2")
        buf.write("\u0150\u0151\7?\2\2\u0151R\3\2\2\2\u0152\u0153\7@\2\2")
        buf.write("\u0153T\3\2\2\2\u0154\u0155\7@\2\2\u0155\u0156\7?\2\2")
        buf.write("\u0156V\3\2\2\2\u0157\u0158\7\60\2\2\u0158\u0159\7\60")
        buf.write("\2\2\u0159\u015a\7\60\2\2\u015aX\3\2\2\2\u015b\u015c\7")
        buf.write("?\2\2\u015c\u015d\7?\2\2\u015dZ\3\2\2\2\u015e\u015f\7")
        buf.write("*\2\2\u015f\\\3\2\2\2\u0160\u0161\7+\2\2\u0161^\3\2\2")
        buf.write("\2\u0162\u0163\7]\2\2\u0163`\3\2\2\2\u0164\u0165\7_\2")
        buf.write("\2\u0165b\3\2\2\2\u0166\u0167\7.\2\2\u0167d\3\2\2\2\u0168")
        buf.write("\u016c\t\t\2\2\u0169\u016b\t\n\2\2\u016a\u0169\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016df\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170")
        buf.write("\7%\2\2\u0170\u0171\7%\2\2\u0171\u0175\3\2\2\2\u0172\u0174")
        buf.write("\n\13\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2")
        buf.write("\u0177\u0175\3\2\2\2\u0178\u0179\b\64\5\2\u0179h\3\2\2")
        buf.write("\2\u017a\u017b\7\f\2\2\u017bj\3\2\2\2\u017c\u017e\t\f")
        buf.write("\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0182\b\66\5\2\u0182l\3\2\2\2\u0183\u0184\13\2\2\2\u0184")
        buf.write("\u0185\b\67\6\2\u0185n\3\2\2\2\25\2qty\177\u0084\u008a")
        buf.write("\u008f\u0099\u009b\u00a3\u00a6\u00b0\u00b2\u00c0\u00c2")
        buf.write("\u016c\u0175\u017f\7\3\7\2\3\b\3\3\t\4\b\2\2\3\67\5")
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
     



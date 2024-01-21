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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\5\b\u00c1\n\b\3\b\5\b\u00c4\n\b\3\t")
        buf.write("\3\t\3\t\7\t\u00c9\n\t\f\t\16\t\u00cc\13\t\5\t\u00ce\n")
        buf.write("\t\3\n\3\n\7\n\u00d2\n\n\f\n\16\n\u00d5\13\n\3\13\3\13")
        buf.write("\5\13\u00d9\n\13\3\13\3\13\7\13\u00dd\n\13\f\13\16\13")
        buf.write("\u00e0\13\13\3\f\3\f\5\f\u00e4\n\f\3\r\3\r\3\r\3\r\7\r")
        buf.write("\u00ea\n\r\f\r\16\r\u00ed\13\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,")
        buf.write("\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u019d\n:\f:\16:\u01a0")
        buf.write("\13:\3;\3;\3;\3;\7;\u01a6\n;\f;\16;\u01a9\13;\3;\5;\u01ac")
        buf.write("\n;\3;\5;\u01af\n;\3;\3;\3<\6<\u01b4\n<\r<\16<\u01b5\3")
        buf.write("=\6=\u01b9\n=\r=\16=\u01ba\3=\3=\3>\3>\3>\3?\3?\3@\3@")
        buf.write("\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27")
        buf.write("\n\31\13\33\2\35\2\37\f!\r#\16%\17\'\20)\21+\22-\23/\24")
        buf.write("\61\25\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G")
        buf.write(" I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64")
        buf.write("q\65s\66u\67w8y9{:};\177<\3\2\r\3\2\63;\3\2\62;\4\2--")
        buf.write("//\3\2$$\5\2\f\f\17\17$$\t\2))^^ddhhppttvv\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\4\2\f\f\17\17\3\3\f\f\5\2\13\13\17\17")
        buf.write("\"\"\2\u01cf\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u008c")
        buf.write("\3\2\2\2\7\u0098\3\2\2\2\t\u00a1\3\2\2\2\13\u00a7\3\2")
        buf.write("\2\2\r\u00b2\3\2\2\2\17\u00be\3\2\2\2\21\u00cd\3\2\2\2")
        buf.write("\23\u00cf\3\2\2\2\25\u00d6\3\2\2\2\27\u00e3\3\2\2\2\31")
        buf.write("\u00e5\3\2\2\2\33\u00f1\3\2\2\2\35\u00f4\3\2\2\2\37\u00f7")
        buf.write("\3\2\2\2!\u00fc\3\2\2\2#\u0102\3\2\2\2%\u0109\3\2\2\2")
        buf.write("\'\u010e\3\2\2\2)\u0115\3\2\2\2+\u011c\3\2\2\2-\u0120")
        buf.write("\3\2\2\2/\u0128\3\2\2\2\61\u012d\3\2\2\2\63\u0131\3\2")
        buf.write("\2\2\65\u0137\3\2\2\2\67\u013a\3\2\2\29\u0140\3\2\2\2")
        buf.write(";\u0149\3\2\2\2=\u014c\3\2\2\2?\u0151\3\2\2\2A\u0156\3")
        buf.write("\2\2\2C\u015c\3\2\2\2E\u0160\3\2\2\2G\u0164\3\2\2\2I\u0168")
        buf.write("\3\2\2\2K\u016b\3\2\2\2M\u016d\3\2\2\2O\u016f\3\2\2\2")
        buf.write("Q\u0171\3\2\2\2S\u0173\3\2\2\2U\u0175\3\2\2\2W\u0177\3")
        buf.write("\2\2\2Y\u017a\3\2\2\2[\u017d\3\2\2\2]\u017f\3\2\2\2_\u0182")
        buf.write("\3\2\2\2a\u0184\3\2\2\2c\u0187\3\2\2\2e\u018b\3\2\2\2")
        buf.write("g\u018e\3\2\2\2i\u0190\3\2\2\2k\u0192\3\2\2\2m\u0194\3")
        buf.write("\2\2\2o\u0196\3\2\2\2q\u0198\3\2\2\2s\u019a\3\2\2\2u\u01a1")
        buf.write("\3\2\2\2w\u01b3\3\2\2\2y\u01b8\3\2\2\2{\u01be\3\2\2\2")
        buf.write("}\u01c1\3\2\2\2\177\u01c3\3\2\2\2\u0081\u0082\7t\2\2\u0082")
        buf.write("\u0083\7g\2\2\u0083\u0084\7c\2\2\u0084\u0085\7f\2\2\u0085")
        buf.write("\u0086\7P\2\2\u0086\u0087\7w\2\2\u0087\u0088\7o\2\2\u0088")
        buf.write("\u0089\7d\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\4\3\2\2\2\u008c\u008d\7y\2\2\u008d\u008e\7t\2\2\u008e")
        buf.write("\u008f\7k\2\2\u008f\u0090\7v\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\u0092\7P\2\2\u0092\u0093\7w\2\2\u0093\u0094\7o\2\2\u0094")
        buf.write("\u0095\7d\2\2\u0095\u0096\7g\2\2\u0096\u0097\7t\2\2\u0097")
        buf.write("\6\3\2\2\2\u0098\u0099\7t\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\u009b\7c\2\2\u009b\u009c\7f\2\2\u009c\u009d\7D\2\2\u009d")
        buf.write("\u009e\7q\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7n\2\2\u00a0")
        buf.write("\b\3\2\2\2\u00a1\u00a2\7y\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7g\2\2\u00a6")
        buf.write("\n\3\2\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7g\2\2\u00a9")
        buf.write("\u00aa\7c\2\2\u00aa\u00ab\7f\2\2\u00ab\u00ac\7U\2\2\u00ac")
        buf.write("\u00ad\7v\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\u00b1\7i\2\2\u00b1\f\3\2\2\2\u00b2")
        buf.write("\u00b3\7y\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7k\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7U\2\2\u00b8")
        buf.write("\u00b9\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7k\2\2\u00bb")
        buf.write("\u00bc\7p\2\2\u00bc\u00bd\7i\2\2\u00bd\16\3\2\2\2\u00be")
        buf.write("\u00c0\5\21\t\2\u00bf\u00c1\5\23\n\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c4")
        buf.write("\5\25\13\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\20\3\2\2\2\u00c5\u00ce\7\62\2\2\u00c6\u00ca\t\2\2\2\u00c7")
        buf.write("\u00c9\t\3\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00ce\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00c5\3\2\2\2\u00cd\u00c6")
        buf.write("\3\2\2\2\u00ce\22\3\2\2\2\u00cf\u00d3\7\60\2\2\u00d0\u00d2")
        buf.write("\t\3\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\24\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d8\7g\2\2\u00d7\u00d9\t\4\2\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00de\t\2\2\2\u00db\u00dd\t\3\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\26\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1")
        buf.write("\u00e4\5\37\20\2\u00e2\u00e4\5!\21\2\u00e3\u00e1\3\2\2")
        buf.write("\2\u00e3\u00e2\3\2\2\2\u00e4\30\3\2\2\2\u00e5\u00eb\t")
        buf.write("\5\2\2\u00e6\u00ea\5\33\16\2\u00e7\u00ea\5\35\17\2\u00e8")
        buf.write("\u00ea\n\6\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ee\u00ef\t\5\2\2\u00ef\u00f0\b\r\2\2\u00f0")
        buf.write("\32\3\2\2\2\u00f1\u00f2\7^\2\2\u00f2\u00f3\t\7\2\2\u00f3")
        buf.write("\34\3\2\2\2\u00f4\u00f5\7)\2\2\u00f5\u00f6\7$\2\2\u00f6")
        buf.write("\36\3\2\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7g\2\2\u00fb \3\2\2\2\u00fc")
        buf.write("\u00fd\7h\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7n\2\2\u00ff")
        buf.write("\u0100\7u\2\2\u0100\u0101\7g\2\2\u0101\"\3\2\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7w\2\2\u0104\u0105\7o\2\2\u0105")
        buf.write("\u0106\7d\2\2\u0106\u0107\7g\2\2\u0107\u0108\7t\2\2\u0108")
        buf.write("$\3\2\2\2\u0109\u010a\7d\2\2\u010a\u010b\7q\2\2\u010b")
        buf.write("\u010c\7q\2\2\u010c\u010d\7n\2\2\u010d&\3\2\2\2\u010e")
        buf.write("\u010f\7u\2\2\u010f\u0110\7v\2\2\u0110\u0111\7t\2\2\u0111")
        buf.write("\u0112\7k\2\2\u0112\u0113\7p\2\2\u0113\u0114\7i\2\2\u0114")
        buf.write("(\3\2\2\2\u0115\u0116\7t\2\2\u0116\u0117\7g\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7w\2\2\u0119\u011a\7t\2\2\u011a")
        buf.write("\u011b\7p\2\2\u011b*\3\2\2\2\u011c\u011d\7x\2\2\u011d")
        buf.write("\u011e\7c\2\2\u011e\u011f\7t\2\2\u011f,\3\2\2\2\u0120")
        buf.write("\u0121\7f\2\2\u0121\u0122\7{\2\2\u0122\u0123\7p\2\2\u0123")
        buf.write("\u0124\7c\2\2\u0124\u0125\7o\2\2\u0125\u0126\7k\2\2\u0126")
        buf.write("\u0127\7e\2\2\u0127.\3\2\2\2\u0128\u0129\7h\2\2\u0129")
        buf.write("\u012a\7w\2\2\u012a\u012b\7p\2\2\u012b\u012c\7e\2\2\u012c")
        buf.write("\60\3\2\2\2\u012d\u012e\7h\2\2\u012e\u012f\7q\2\2\u012f")
        buf.write("\u0130\7t\2\2\u0130\62\3\2\2\2\u0131\u0132\7w\2\2\u0132")
        buf.write("\u0133\7p\2\2\u0133\u0134\7v\2\2\u0134\u0135\7k\2\2\u0135")
        buf.write("\u0136\7n\2\2\u0136\64\3\2\2\2\u0137\u0138\7d\2\2\u0138")
        buf.write("\u0139\7{\2\2\u0139\66\3\2\2\2\u013a\u013b\7d\2\2\u013b")
        buf.write("\u013c\7t\2\2\u013c\u013d\7g\2\2\u013d\u013e\7c\2\2\u013e")
        buf.write("\u013f\7m\2\2\u013f8\3\2\2\2\u0140\u0141\7e\2\2\u0141")
        buf.write("\u0142\7q\2\2\u0142\u0143\7p\2\2\u0143\u0144\7v\2\2\u0144")
        buf.write("\u0145\7k\2\2\u0145\u0146\7p\2\2\u0146\u0147\7w\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148:\3\2\2\2\u0149\u014a\7k\2\2\u014a")
        buf.write("\u014b\7h\2\2\u014b<\3\2\2\2\u014c\u014d\7g\2\2\u014d")
        buf.write("\u014e\7n\2\2\u014e\u014f\7u\2\2\u014f\u0150\7g\2\2\u0150")
        buf.write(">\3\2\2\2\u0151\u0152\7g\2\2\u0152\u0153\7n\2\2\u0153")
        buf.write("\u0154\7k\2\2\u0154\u0155\7h\2\2\u0155@\3\2\2\2\u0156")
        buf.write("\u0157\7d\2\2\u0157\u0158\7g\2\2\u0158\u0159\7i\2\2\u0159")
        buf.write("\u015a\7k\2\2\u015a\u015b\7p\2\2\u015bB\3\2\2\2\u015c")
        buf.write("\u015d\7g\2\2\u015d\u015e\7p\2\2\u015e\u015f\7f\2\2\u015f")
        buf.write("D\3\2\2\2\u0160\u0161\7p\2\2\u0161\u0162\7q\2\2\u0162")
        buf.write("\u0163\7v\2\2\u0163F\3\2\2\2\u0164\u0165\7c\2\2\u0165")
        buf.write("\u0166\7p\2\2\u0166\u0167\7f\2\2\u0167H\3\2\2\2\u0168")
        buf.write("\u0169\7q\2\2\u0169\u016a\7t\2\2\u016aJ\3\2\2\2\u016b")
        buf.write("\u016c\7-\2\2\u016cL\3\2\2\2\u016d\u016e\7/\2\2\u016e")
        buf.write("N\3\2\2\2\u016f\u0170\7,\2\2\u0170P\3\2\2\2\u0171\u0172")
        buf.write("\7\61\2\2\u0172R\3\2\2\2\u0173\u0174\7\'\2\2\u0174T\3")
        buf.write("\2\2\2\u0175\u0176\7?\2\2\u0176V\3\2\2\2\u0177\u0178\7")
        buf.write(">\2\2\u0178\u0179\7/\2\2\u0179X\3\2\2\2\u017a\u017b\7")
        buf.write("#\2\2\u017b\u017c\7?\2\2\u017cZ\3\2\2\2\u017d\u017e\7")
        buf.write(">\2\2\u017e\\\3\2\2\2\u017f\u0180\7>\2\2\u0180\u0181\7")
        buf.write("?\2\2\u0181^\3\2\2\2\u0182\u0183\7@\2\2\u0183`\3\2\2\2")
        buf.write("\u0184\u0185\7@\2\2\u0185\u0186\7?\2\2\u0186b\3\2\2\2")
        buf.write("\u0187\u0188\7\60\2\2\u0188\u0189\7\60\2\2\u0189\u018a")
        buf.write("\7\60\2\2\u018ad\3\2\2\2\u018b\u018c\7?\2\2\u018c\u018d")
        buf.write("\7?\2\2\u018df\3\2\2\2\u018e\u018f\7*\2\2\u018fh\3\2\2")
        buf.write("\2\u0190\u0191\7+\2\2\u0191j\3\2\2\2\u0192\u0193\7]\2")
        buf.write("\2\u0193l\3\2\2\2\u0194\u0195\7_\2\2\u0195n\3\2\2\2\u0196")
        buf.write("\u0197\7.\2\2\u0197p\3\2\2\2\u0198\u0199\7=\2\2\u0199")
        buf.write("r\3\2\2\2\u019a\u019e\t\b\2\2\u019b\u019d\t\t\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019ft\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write("\2\u01a1\u01a2\7%\2\2\u01a2\u01a3\7%\2\2\u01a3\u01a7\3")
        buf.write("\2\2\2\u01a4\u01a6\n\n\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ac\7\17\2")
        buf.write("\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae")
        buf.write("\3\2\2\2\u01ad\u01af\t\13\2\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b1\b;\3\2\u01b1v\3\2\2\2\u01b2")
        buf.write("\u01b4\t\n\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6x\3\2\2")
        buf.write("\2\u01b7\u01b9\t\f\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01bd\b=\3\2\u01bdz\3\2\2\2\u01be")
        buf.write("\u01bf\13\2\2\2\u01bf\u01c0\b>\4\2\u01c0|\3\2\2\2\u01c1")
        buf.write("\u01c2\13\2\2\2\u01c2~\3\2\2\2\u01c3\u01c4\13\2\2\2\u01c4")
        buf.write("\u0080\3\2\2\2\23\2\u00c0\u00c3\u00ca\u00cd\u00d3\u00d8")
        buf.write("\u00de\u00e3\u00e9\u00eb\u019e\u01a7\u01ab\u01ae\u01b5")
        buf.write("\u01ba\5\3\r\2\b\2\2\3>\3")
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
    TRUE = 10
    FALSE = 11
    NUMBER = 12
    BOOL = 13
    STRING = 14
    RETURN = 15
    VAR = 16
    DYNAMIC = 17
    FUNC = 18
    FOR = 19
    UNTIL = 20
    BY = 21
    BREAK = 22
    CONTINUE = 23
    IF = 24
    ELSE = 25
    ELIF = 26
    BEGIN = 27
    END = 28
    NOT = 29
    AND = 30
    OR = 31
    ADDOP = 32
    SUBOP = 33
    MULOP = 34
    DIVOP = 35
    MODOP = 36
    EQUALOP = 37
    ARROW = 38
    DIFFOP = 39
    LESS = 40
    LESSEQ = 41
    LARGER = 42
    LARGEREQ = 43
    DOT = 44
    STRCOMPARE = 45
    LB = 46
    RB = 47
    LP = 48
    RP = 49
    COMMA = 50
    SEMI = 51
    IDENTIFIER = 52
    COMMENT = 53
    NEWLINE = 54
    WS = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

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
            "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "EQUALOP", "ARROW", "DIFFOP", "LESS", "LESSEQ", "LARGER", 
            "LARGEREQ", "DOT", "STRCOMPARE", "LB", "RB", "LP", "RP", "COMMA", 
            "SEMI", "IDENTIFIER", "COMMENT", "NEWLINE", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NUMLIT", 
                  "INTPART", "DECPART", "EXPONENTPART", "BOOLLIT", "STRINGLIT", 
                  "ESCAPE", "DQ", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODOP", "EQUALOP", "ARROW", "DIFFOP", "LESS", "LESSEQ", 
                  "LARGER", "LARGEREQ", "DOT", "STRCOMPARE", "LB", "RB", 
                  "LP", "RP", "COMMA", "SEMI", "IDENTIFIER", "COMMENT", 
                  "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text)-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     



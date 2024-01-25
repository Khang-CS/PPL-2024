# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u018b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5y\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0081")
        buf.write("\n\6\3\7\3\7\5\7\u0085\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u008c")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0097\n\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\5\13\u009e\n\13\3\f\3\f\5\f\u00a2")
        buf.write("\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00b0\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\5\22\u00be\n\22\3\23\3\23\5")
        buf.write("\23\u00c2\n\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00cd\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00d4")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00db\n\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\7\27\u00e3\n\27\f\27\16\27\u00e6")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00ee\n\30\f")
        buf.write("\30\16\30\u00f1\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u00f9\n\31\f\31\16\31\u00fc\13\31\3\32\3\32\3\32\5")
        buf.write("\32\u0101\n\32\3\33\3\33\3\33\5\33\u0106\n\33\3\34\3\34")
        buf.write("\5\34\u010a\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0112")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u011d\n\37\3 \3 \3 \3 \3 \3 \5 \u0125\n \3!\3!\5!\u0129")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0130\n\"\3#\3#\3#\3#\5#\u0136")
        buf.write("\n#\3#\3#\3#\5#\u013b\n#\3$\3$\3$\3$\3$\3$\5$\u0143\n")
        buf.write("$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\5+\u0160\n+\3,\3,\3,\3")
        buf.write(",\5,\u0166\n,\3-\3-\3-\3-\3-\3-\5-\u016e\n-\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\2\5,.\60\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\b\3")
        buf.write("\2\16\20\3\2\22\23\5\2\'\')-//\3\2 !\3\2\"#\3\2$&\2\u0188")
        buf.write("\2f\3\2\2\2\4m\3\2\2\2\6o\3\2\2\2\bx\3\2\2\2\n\u0080\3")
        buf.write("\2\2\2\f\u0084\3\2\2\2\16\u008b\3\2\2\2\20\u0096\3\2\2")
        buf.write("\2\22\u0098\3\2\2\2\24\u009d\3\2\2\2\26\u00a1\3\2\2\2")
        buf.write("\30\u00a5\3\2\2\2\32\u00af\3\2\2\2\34\u00b1\3\2\2\2\36")
        buf.write("\u00b3\3\2\2\2 \u00b5\3\2\2\2\"\u00bd\3\2\2\2$\u00c1\3")
        buf.write("\2\2\2&\u00cc\3\2\2\2(\u00d3\3\2\2\2*\u00da\3\2\2\2,\u00dc")
        buf.write("\3\2\2\2.\u00e7\3\2\2\2\60\u00f2\3\2\2\2\62\u0100\3\2")
        buf.write("\2\2\64\u0105\3\2\2\2\66\u0109\3\2\2\28\u0111\3\2\2\2")
        buf.write(":\u0113\3\2\2\2<\u011c\3\2\2\2>\u0124\3\2\2\2@\u0128\3")
        buf.write("\2\2\2B\u012f\3\2\2\2D\u0131\3\2\2\2F\u0142\3\2\2\2H\u0144")
        buf.write("\3\2\2\2J\u0148\3\2\2\2L\u0151\3\2\2\2N\u0153\3\2\2\2")
        buf.write("P\u0155\3\2\2\2R\u0158\3\2\2\2T\u015f\3\2\2\2V\u0165\3")
        buf.write("\2\2\2X\u016d\3\2\2\2Z\u016f\3\2\2\2\\\u0173\3\2\2\2^")
        buf.write("\u0178\3\2\2\2`\u017c\3\2\2\2b\u0181\3\2\2\2d\u0185\3")
        buf.write("\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2ij\5\6\4\2jk\5\4")
        buf.write("\3\2kn\3\2\2\2ln\5\6\4\2mi\3\2\2\2ml\3\2\2\2n\5\3\2\2")
        buf.write("\2op\7\24\2\2pq\7\66\2\2qr\7\60\2\2rs\5\f\7\2st\7\61\2")
        buf.write("\2tu\5\b\5\2u\7\3\2\2\2vy\5\n\6\2wy\3\2\2\2xv\3\2\2\2")
        buf.write("xw\3\2\2\2y\t\3\2\2\2z{\5P)\2{|\78\2\2|\u0081\3\2\2\2")
        buf.write("}~\5R*\2~\177\78\2\2\177\u0081\3\2\2\2\u0080z\3\2\2\2")
        buf.write("\u0080}\3\2\2\2\u0081\13\3\2\2\2\u0082\u0085\5\16\b\2")
        buf.write("\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3")
        buf.write("\2\2\2\u0085\r\3\2\2\2\u0086\u0087\5\24\13\2\u0087\u0088")
        buf.write("\7\64\2\2\u0088\u0089\5\16\b\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u008c\5\24\13\2\u008b\u0086\3\2\2\2\u008b\u008a\3\2\2")
        buf.write("\2\u008c\17\3\2\2\2\u008d\u0097\5\24\13\2\u008e\u0097")
        buf.write("\5 \21\2\u008f\u0097\5D#\2\u0090\u0097\5J&\2\u0091\u0097")
        buf.write("\5L\'\2\u0092\u0097\5N(\2\u0093\u0097\5P)\2\u0094\u0097")
        buf.write("\5> \2\u0095\u0097\5R*\2\u0096\u008d\3\2\2\2\u0096\u008e")
        buf.write("\3\2\2\2\u0096\u008f\3\2\2\2\u0096\u0090\3\2\2\2\u0096")
        buf.write("\u0091\3\2\2\2\u0096\u0092\3\2\2\2\u0096\u0093\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\21\3\2")
        buf.write("\2\2\u0098\u0099\5\20\t\2\u0099\u009a\78\2\2\u009a\23")
        buf.write("\3\2\2\2\u009b\u009e\5\26\f\2\u009c\u009e\5\30\r\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e\25\3\2\2\2\u009f")
        buf.write("\u00a2\5\34\17\2\u00a0\u00a2\5\36\20\2\u00a1\u009f\3\2")
        buf.write("\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4")
        buf.write("\7\66\2\2\u00a4\27\3\2\2\2\u00a5\u00a6\5\34\17\2\u00a6")
        buf.write("\u00a7\7\66\2\2\u00a7\u00a8\7\62\2\2\u00a8\u00a9\5\32")
        buf.write("\16\2\u00a9\u00aa\7\63\2\2\u00aa\31\3\2\2\2\u00ab\u00ac")
        buf.write("\7\t\2\2\u00ac\u00ad\7\64\2\2\u00ad\u00b0\5\32\16\2\u00ae")
        buf.write("\u00b0\7\t\2\2\u00af\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\33\3\2\2\2\u00b1\u00b2\t\2\2\2\u00b2\35\3\2\2\2")
        buf.write("\u00b3\u00b4\t\3\2\2\u00b4\37\3\2\2\2\u00b5\u00b6\5\"")
        buf.write("\22\2\u00b6\u00b7\7(\2\2\u00b7\u00b8\5(\25\2\u00b8!\3")
        buf.write("\2\2\2\u00b9\u00be\7\66\2\2\u00ba\u00be\5$\23\2\u00bb")
        buf.write("\u00be\5\30\r\2\u00bc\u00be\5\26\f\2\u00bd\u00b9\3\2\2")
        buf.write("\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00be#\3\2\2\2\u00bf\u00c2\7\66\2\2\u00c0\u00c2")
        buf.write("\5> \2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c4\7\62\2\2\u00c4\u00c5\5&\24\2\u00c5")
        buf.write("\u00c6\7\63\2\2\u00c6%\3\2\2\2\u00c7\u00c8\5(\25\2\u00c8")
        buf.write("\u00c9\7\64\2\2\u00c9\u00ca\5&\24\2\u00ca\u00cd\3\2\2")
        buf.write("\2\u00cb\u00cd\5(\25\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cd\'\3\2\2\2\u00ce\u00cf\5*\26\2\u00cf\u00d0")
        buf.write("\7.\2\2\u00d0\u00d1\5*\26\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d4\5*\26\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4)\3\2\2\2\u00d5\u00d6\5,\27\2\u00d6\u00d7\t\4\2")
        buf.write("\2\u00d7\u00d8\5,\27\2\u00d8\u00db\3\2\2\2\u00d9\u00db")
        buf.write("\5,\27\2\u00da\u00d5\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("+\3\2\2\2\u00dc\u00dd\b\27\1\2\u00dd\u00de\5.\30\2\u00de")
        buf.write("\u00e4\3\2\2\2\u00df\u00e0\f\4\2\2\u00e0\u00e1\t\5\2\2")
        buf.write("\u00e1\u00e3\5.\30\2\u00e2\u00df\3\2\2\2\u00e3\u00e6\3")
        buf.write("\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5-")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\b\30\1\2\u00e8")
        buf.write("\u00e9\5\60\31\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f\4\2")
        buf.write("\2\u00eb\u00ec\t\6\2\2\u00ec\u00ee\5\60\31\2\u00ed\u00ea")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0/\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2")
        buf.write("\u00f3\b\31\1\2\u00f3\u00f4\5\62\32\2\u00f4\u00fa\3\2")
        buf.write("\2\2\u00f5\u00f6\f\4\2\2\u00f6\u00f7\t\7\2\2\u00f7\u00f9")
        buf.write("\5\62\32\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\61\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\7\37\2\2\u00fe\u0101\5\64\33")
        buf.write("\2\u00ff\u0101\5\64\33\2\u0100\u00fd\3\2\2\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0101\63\3\2\2\2\u0102\u0103\7#\2\2\u0103\u0106")
        buf.write("\5\66\34\2\u0104\u0106\5\66\34\2\u0105\u0102\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\65\3\2\2\2\u0107\u010a\5$\23\2\u0108")
        buf.write("\u010a\58\35\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2")
        buf.write("\u010a\67\3\2\2\2\u010b\u0112\7\t\2\2\u010c\u0112\7\n")
        buf.write("\2\2\u010d\u0112\7\13\2\2\u010e\u0112\5:\36\2\u010f\u0112")
        buf.write("\7\66\2\2\u0110\u0112\5> \2\u0111\u010b\3\2\2\2\u0111")
        buf.write("\u010c\3\2\2\2\u0111\u010d\3\2\2\2\u0111\u010e\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u01129\3\2\2")
        buf.write("\2\u0113\u0114\7\62\2\2\u0114\u0115\5<\37\2\u0115\u0116")
        buf.write("\7\63\2\2\u0116;\3\2\2\2\u0117\u0118\58\35\2\u0118\u0119")
        buf.write("\7\64\2\2\u0119\u011a\5<\37\2\u011a\u011d\3\2\2\2\u011b")
        buf.write("\u011d\58\35\2\u011c\u0117\3\2\2\2\u011c\u011b\3\2\2\2")
        buf.write("\u011d=\3\2\2\2\u011e\u011f\7\66\2\2\u011f\u0120\7\60")
        buf.write("\2\2\u0120\u0121\5@!\2\u0121\u0122\7\61\2\2\u0122\u0125")
        buf.write("\3\2\2\2\u0123\u0125\5X-\2\u0124\u011e\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125?\3\2\2\2\u0126\u0129\5B\"\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("A\3\2\2\2\u012a\u012b\5(\25\2\u012b\u012c\7\64\2\2\u012c")
        buf.write("\u012d\5B\"\2\u012d\u0130\3\2\2\2\u012e\u0130\5(\25\2")
        buf.write("\u012f\u012a\3\2\2\2\u012f\u012e\3\2\2\2\u0130C\3\2\2")
        buf.write("\2\u0131\u0132\7\32\2\2\u0132\u0133\5(\25\2\u0133\u0135")
        buf.write("\5\20\t\2\u0134\u0136\5F$\2\u0135\u0134\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u013a\3\2\2\2\u0137\u0138\78\2\2")
        buf.write("\u0138\u0139\7\33\2\2\u0139\u013b\5\20\t\2\u013a\u0137")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013bE\3\2\2\2\u013c\u013d")
        buf.write("\78\2\2\u013d\u013e\5H%\2\u013e\u013f\5F$\2\u013f\u0143")
        buf.write("\3\2\2\2\u0140\u0141\78\2\2\u0141\u0143\5H%\2\u0142\u013c")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0143G\3\2\2\2\u0144\u0145")
        buf.write("\7\34\2\2\u0145\u0146\5(\25\2\u0146\u0147\5\20\t\2\u0147")
        buf.write("I\3\2\2\2\u0148\u0149\7\25\2\2\u0149\u014a\7\66\2\2\u014a")
        buf.write("\u014b\7\26\2\2\u014b\u014c\5(\25\2\u014c\u014d\7\27\2")
        buf.write("\2\u014d\u014e\5(\25\2\u014e\u014f\78\2\2\u014f\u0150")
        buf.write("\5\20\t\2\u0150K\3\2\2\2\u0151\u0152\7\30\2\2\u0152M\3")
        buf.write("\2\2\2\u0153\u0154\7\31\2\2\u0154O\3\2\2\2\u0155\u0156")
        buf.write("\7\21\2\2\u0156\u0157\5(\25\2\u0157Q\3\2\2\2\u0158\u0159")
        buf.write("\7\35\2\2\u0159\u015a\78\2\2\u015a\u015b\5T+\2\u015b\u015c")
        buf.write("\7\36\2\2\u015cS\3\2\2\2\u015d\u0160\5V,\2\u015e\u0160")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("U\3\2\2\2\u0161\u0162\5\22\n\2\u0162\u0163\5V,\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0166\5\22\n\2\u0165\u0161\3\2\2")
        buf.write("\2\u0165\u0164\3\2\2\2\u0166W\3\2\2\2\u0167\u016e\5Z.")
        buf.write("\2\u0168\u016e\5\\/\2\u0169\u016e\5^\60\2\u016a\u016e")
        buf.write("\5`\61\2\u016b\u016e\5b\62\2\u016c\u016e\5d\63\2\u016d")
        buf.write("\u0167\3\2\2\2\u016d\u0168\3\2\2\2\u016d\u0169\3\2\2\2")
        buf.write("\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3")
        buf.write("\2\2\2\u016eY\3\2\2\2\u016f\u0170\7\3\2\2\u0170\u0171")
        buf.write("\7\60\2\2\u0171\u0172\7\61\2\2\u0172[\3\2\2\2\u0173\u0174")
        buf.write("\7\4\2\2\u0174\u0175\7\60\2\2\u0175\u0176\5(\25\2\u0176")
        buf.write("\u0177\7\61\2\2\u0177]\3\2\2\2\u0178\u0179\7\5\2\2\u0179")
        buf.write("\u017a\7\60\2\2\u017a\u017b\7\61\2\2\u017b_\3\2\2\2\u017c")
        buf.write("\u017d\7\6\2\2\u017d\u017e\7\60\2\2\u017e\u017f\5(\25")
        buf.write("\2\u017f\u0180\7\61\2\2\u0180a\3\2\2\2\u0181\u0182\7\7")
        buf.write("\2\2\u0182\u0183\7\60\2\2\u0183\u0184\7\61\2\2\u0184c")
        buf.write("\3\2\2\2\u0185\u0186\7\b\2\2\u0186\u0187\7\60\2\2\u0187")
        buf.write("\u0188\5(\25\2\u0188\u0189\7\61\2\2\u0189e\3\2\2\2!mx")
        buf.write("\u0080\u0084\u008b\u0096\u009d\u00a1\u00af\u00bd\u00c1")
        buf.write("\u00cc\u00d3\u00da\u00e4\u00ef\u00fa\u0100\u0105\u0109")
        buf.write("\u0111\u011c\u0124\u0128\u012f\u0135\u013a\u0142\u015f")
        buf.write("\u0165\u016d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'write'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMLIT", "BOOLLIT", 
                      "STRINGLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", 
                      "DIVOP", "MODOP", "EQUALOP", "ARROW", "DIFFOP", "LESS", 
                      "LESSEQ", "LARGER", "LARGEREQ", "DOT", "STRCOMPARE", 
                      "LB", "RB", "LP", "RP", "COMMA", "SEMI", "IDENTIFIER", 
                      "COMMENT", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_funclist = 1
    RULE_func = 2
    RULE_option = 3
    RULE_optionprime = 4
    RULE_decllist = 5
    RULE_declprime = 6
    RULE_stmt = 7
    RULE_standalone_stmt = 8
    RULE_decl = 9
    RULE_normaldecl = 10
    RULE_arraydecl = 11
    RULE_dimensions = 12
    RULE_normaltype = 13
    RULE_implicittype = 14
    RULE_assign_stmt = 15
    RULE_lhs = 16
    RULE_indexexp = 17
    RULE_index_operators = 18
    RULE_exp = 19
    RULE_exp2 = 20
    RULE_exp3 = 21
    RULE_exp4 = 22
    RULE_exp5 = 23
    RULE_exp6 = 24
    RULE_exp7 = 25
    RULE_exp8 = 26
    RULE_exp9 = 27
    RULE_arrayvalue = 28
    RULE_literallist = 29
    RULE_funccall_stmt = 30
    RULE_explist = 31
    RULE_expprime = 32
    RULE_if_stmt = 33
    RULE_elif_list = 34
    RULE_elif_stmt = 35
    RULE_for_stmt = 36
    RULE_break_stmt = 37
    RULE_continue_stmt = 38
    RULE_return_stmt = 39
    RULE_block_stmt = 40
    RULE_stmtlist = 41
    RULE_stmtprime = 42
    RULE_io_func = 43
    RULE_readNumber = 44
    RULE_writeNumber = 45
    RULE_readBool = 46
    RULE_write = 47
    RULE_readString = 48
    RULE_writeString = 49

    ruleNames =  [ "program", "funclist", "func", "option", "optionprime", 
                   "decllist", "declprime", "stmt", "standalone_stmt", "decl", 
                   "normaldecl", "arraydecl", "dimensions", "normaltype", 
                   "implicittype", "assign_stmt", "lhs", "indexexp", "index_operators", 
                   "exp", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "arrayvalue", "literallist", "funccall_stmt", 
                   "explist", "expprime", "if_stmt", "elif_list", "elif_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "block_stmt", "stmtlist", "stmtprime", "io_func", "readNumber", 
                   "writeNumber", "readBool", "write", "readString", "writeString" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMLIT=7
    BOOLLIT=8
    STRINGLIT=9
    TRUE=10
    FALSE=11
    NUMBER=12
    BOOL=13
    STRING=14
    RETURN=15
    VAR=16
    DYNAMIC=17
    FUNC=18
    FOR=19
    UNTIL=20
    BY=21
    BREAK=22
    CONTINUE=23
    IF=24
    ELSE=25
    ELIF=26
    BEGIN=27
    END=28
    NOT=29
    AND=30
    OR=31
    ADDOP=32
    SUBOP=33
    MULOP=34
    DIVOP=35
    MODOP=36
    EQUALOP=37
    ARROW=38
    DIFFOP=39
    LESS=40
    LESSEQ=41
    LARGER=42
    LARGEREQ=43
    DOT=44
    STRCOMPARE=45
    LB=46
    RB=47
    LP=48
    RP=49
    COMMA=50
    SEMI=51
    IDENTIFIER=52
    COMMENT=53
    NEWLINE=54
    WS=55
    ERROR_CHAR=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funclist(self):
            return self.getTypedRuleContext(ZCodeParser.FunclistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.funclist()
            self.state = 101
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(ZCodeParser.FuncContext,0)


        def funclist(self):
            return self.getTypedRuleContext(ZCodeParser.FunclistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funclist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunclist" ):
                return visitor.visitFunclist(self)
            else:
                return visitor.visitChildren(self)




    def funclist(self):

        localctx = ZCodeParser.FunclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funclist)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.func()
                self.state = 104
                self.funclist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def option(self):
            return self.getTypedRuleContext(ZCodeParser.OptionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.FUNC)
            self.state = 110
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 111
            self.match(ZCodeParser.LB)
            self.state = 112
            self.decllist()
            self.state = 113
            self.match(ZCodeParser.RB)
            self.state = 114
            self.option()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionprime(self):
            return self.getTypedRuleContext(ZCodeParser.OptionprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = ZCodeParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_option)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.optionprime()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optionprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionprime" ):
                return visitor.visitOptionprime(self)
            else:
                return visitor.visitChildren(self)




    def optionprime(self):

        localctx = ZCodeParser.OptionprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optionprime)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.return_stmt()
                self.state = 121
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.block_stmt()
                self.state = 124
                self.match(ZCodeParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declprime(self):
            return self.getTypedRuleContext(ZCodeParser.DeclprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decllist)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.declprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def declprime(self):
            return self.getTypedRuleContext(ZCodeParser.DeclprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclprime" ):
                return visitor.visitDeclprime(self)
            else:
                return visitor.visitChildren(self)




    def declprime(self):

        localctx = ZCodeParser.DeclprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declprime)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.decl()
                self.state = 133
                self.match(ZCodeParser.COMMA)
                self.state = 134
                self.declprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def funccall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Funccall_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 147
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Standalone_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_standalone_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandalone_stmt" ):
                return visitor.visitStandalone_stmt(self)
            else:
                return visitor.visitChildren(self)




    def standalone_stmt(self):

        localctx = ZCodeParser.Standalone_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_standalone_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.stmt()
            self.state = 151
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normaldecl(self):
            return self.getTypedRuleContext(ZCodeParser.NormaldeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 153
                self.normaldecl()
                pass

            elif la_ == 2:
                self.state = 154
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormaldeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def normaltype(self):
            return self.getTypedRuleContext(ZCodeParser.NormaltypeContext,0)


        def implicittype(self):
            return self.getTypedRuleContext(ZCodeParser.ImplicittypeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normaldecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaldecl" ):
                return visitor.visitNormaldecl(self)
            else:
                return visitor.visitChildren(self)




    def normaldecl(self):

        localctx = ZCodeParser.NormaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_normaldecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 157
                self.normaltype()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 158
                self.implicittype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normaltype(self):
            return self.getTypedRuleContext(ZCodeParser.NormaltypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.normaltype()
            self.state = 164
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 165
            self.match(ZCodeParser.LP)
            self.state = 166
            self.dimensions()
            self.state = 167
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimensions)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(ZCodeParser.NUMLIT)
                self.state = 170
                self.match(ZCodeParser.COMMA)
                self.state = 171
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormaltypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_normaltype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaltype" ):
                return visitor.visitNormaltype(self)
            else:
                return visitor.visitChildren(self)




    def normaltype(self):

        localctx = ZCodeParser.NormaltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normaltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicittypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicittype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicittype" ):
                return visitor.visitImplicittype(self)
            else:
                return visitor.visitChildren(self)




    def implicittype(self):

        localctx = ZCodeParser.ImplicittypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_implicittype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.lhs()
            self.state = 180
            self.match(ZCodeParser.ARROW)
            self.state = 181
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def indexexp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexpContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def normaldecl(self):
            return self.getTypedRuleContext(ZCodeParser.NormaldeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lhs)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.indexexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.normaldecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Funccall_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexp" ):
                return visitor.visitIndexexp(self)
            else:
                return visitor.visitChildren(self)




    def indexexp(self):

        localctx = ZCodeParser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_indexexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 189
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 190
                self.funccall_stmt()
                pass


            self.state = 193
            self.match(ZCodeParser.LP)
            self.state = 194
            self.index_operators()
            self.state = 195
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_index_operators)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.exp()
                self.state = 198
                self.match(ZCodeParser.COMMA)
                self.state = 199
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def DOT(self):
            return self.getToken(ZCodeParser.DOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.exp2()
                self.state = 205
                self.match(ZCodeParser.DOT)
                self.state = 206
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp3Context,i)


        def EQUALOP(self):
            return self.getToken(ZCodeParser.EQUALOP, 0)

        def STRCOMPARE(self):
            return self.getToken(ZCodeParser.STRCOMPARE, 0)

        def DIFFOP(self):
            return self.getToken(ZCodeParser.DIFFOP, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LARGER(self):
            return self.getToken(ZCodeParser.LARGER, 0)

        def LESSEQ(self):
            return self.getToken(ZCodeParser.LESSEQ, 0)

        def LARGEREQ(self):
            return self.getToken(ZCodeParser.LARGEREQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = ZCodeParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.exp3(0)
                self.state = 212
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUALOP) | (1 << ZCodeParser.DIFFOP) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESSEQ) | (1 << ZCodeParser.LARGER) | (1 << ZCodeParser.LARGEREQ) | (1 << ZCodeParser.STRCOMPARE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.exp3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.exp4(0) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def ADDOP(self):
            return self.getToken(ZCodeParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(ZCodeParser.SUBOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADDOP or _la==ZCodeParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 234
                    self.exp5(0) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def MULOP(self):
            return self.getToken(ZCodeParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(ZCodeParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(ZCodeParser.MODOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULOP) | (1 << ZCodeParser.DIVOP) | (1 << ZCodeParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.exp6() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp6)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(ZCodeParser.NOT)
                self.state = 252
                self.exp7()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUBOP, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(ZCodeParser.SUBOP, 0)

        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp7)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(ZCodeParser.SUBOP)
                self.state = 257
                self.exp8()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.exp8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexexp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexpContext,0)


        def exp9(self):
            return self.getTypedRuleContext(ZCodeParser.Exp9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp8)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.indexexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Funccall_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = ZCodeParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp9)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.arrayvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.funccall_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def literallist(self):
            return self.getTypedRuleContext(ZCodeParser.LiterallistContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvalue" ):
                return visitor.visitArrayvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.LP)
            self.state = 274
            self.literallist()
            self.state = 275
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiterallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(ZCodeParser.Exp9Context,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def literallist(self):
            return self.getTypedRuleContext(ZCodeParser.LiterallistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterallist" ):
                return visitor.visitLiterallist(self)
            else:
                return visitor.visitChildren(self)




    def literallist(self):

        localctx = ZCodeParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_literallist)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.exp9()
                self.state = 278
                self.match(ZCodeParser.COMMA)
                self.state = 279
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def io_func(self):
            return self.getTypedRuleContext(ZCodeParser.Io_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccall_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_stmt" ):
                return visitor.visitFunccall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def funccall_stmt(self):

        localctx = ZCodeParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_funccall_stmt)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 285
                self.match(ZCodeParser.LB)
                self.state = 286
                self.explist()
                self.state = 287
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.io_func()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExpprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_explist)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExpprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpprime" ):
                return visitor.visitExpprime(self)
            else:
                return visitor.visitChildren(self)




    def expprime(self):

        localctx = ZCodeParser.ExpprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expprime)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.exp()
                self.state = 297
                self.match(ZCodeParser.COMMA)
                self.state = 298
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.IF)
            self.state = 304
            self.exp()
            self.state = 305
            self.stmt()
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 306
                self.elif_list()


            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 309
                self.match(ZCodeParser.NEWLINE)
                self.state = 310
                self.match(ZCodeParser.ELSE)
                self.state = 311
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elif_list)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(ZCodeParser.NEWLINE)
                self.state = 315
                self.elif_stmt()
                self.state = 316
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(ZCodeParser.NEWLINE)
                self.state = 319
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ZCodeParser.ELIF)
            self.state = 323
            self.exp()
            self.state = 324
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(ZCodeParser.FOR)
            self.state = 327
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 328
            self.match(ZCodeParser.UNTIL)
            self.state = 329
            self.exp()
            self.state = 330
            self.match(ZCodeParser.BY)
            self.state = 331
            self.exp()
            self.state = 332
            self.match(ZCodeParser.NEWLINE)
            self.state = 333
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ZCodeParser.RETURN)
            self.state = 340
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.BEGIN)
            self.state = 343
            self.match(ZCodeParser.NEWLINE)
            self.state = 344
            self.stmtlist()
            self.state = 345
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmtlist)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.stmtprime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def standalone_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Standalone_stmtContext,0)


        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtprime" ):
                return visitor.visitStmtprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtprime(self):

        localctx = ZCodeParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmtprime)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.standalone_stmt()
                self.state = 352
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.standalone_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readNumber(self):
            return self.getTypedRuleContext(ZCodeParser.ReadNumberContext,0)


        def writeNumber(self):
            return self.getTypedRuleContext(ZCodeParser.WriteNumberContext,0)


        def readBool(self):
            return self.getTypedRuleContext(ZCodeParser.ReadBoolContext,0)


        def write(self):
            return self.getTypedRuleContext(ZCodeParser.WriteContext,0)


        def readString(self):
            return self.getTypedRuleContext(ZCodeParser.ReadStringContext,0)


        def writeString(self):
            return self.getTypedRuleContext(ZCodeParser.WriteStringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_io_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_func" ):
                return visitor.visitIo_func(self)
            else:
                return visitor.visitChildren(self)




    def io_func(self):

        localctx = ZCodeParser.Io_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_io_func)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.readNumber()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.writeNumber()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.readBool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 360
                self.write()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 361
                self.readString()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 362
                self.writeString()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadNumber" ):
                return visitor.visitReadNumber(self)
            else:
                return visitor.visitChildren(self)




    def readNumber(self):

        localctx = ZCodeParser.ReadNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ZCodeParser.T__0)
            self.state = 366
            self.match(ZCodeParser.LB)
            self.state = 367
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteNumber" ):
                return visitor.visitWriteNumber(self)
            else:
                return visitor.visitChildren(self)




    def writeNumber(self):

        localctx = ZCodeParser.WriteNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(ZCodeParser.T__1)
            self.state = 370
            self.match(ZCodeParser.LB)
            self.state = 371
            self.exp()
            self.state = 372
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBool" ):
                return visitor.visitReadBool(self)
            else:
                return visitor.visitChildren(self)




    def readBool(self):

        localctx = ZCodeParser.ReadBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ZCodeParser.T__2)
            self.state = 375
            self.match(ZCodeParser.LB)
            self.state = 376
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ZCodeParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(ZCodeParser.T__3)
            self.state = 379
            self.match(ZCodeParser.LB)
            self.state = 380
            self.exp()
            self.state = 381
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadString" ):
                return visitor.visitReadString(self)
            else:
                return visitor.visitChildren(self)




    def readString(self):

        localctx = ZCodeParser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.T__4)
            self.state = 384
            self.match(ZCodeParser.LB)
            self.state = 385
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteString" ):
                return visitor.visitWriteString(self)
            else:
                return visitor.visitChildren(self)




    def writeString(self):

        localctx = ZCodeParser.WriteStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(ZCodeParser.T__5)
            self.state = 388
            self.match(ZCodeParser.LB)
            self.state = 389
            self.exp()
            self.state = 390
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.exp3_sempred
        self._predicates[22] = self.exp4_sempred
        self._predicates[23] = self.exp5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





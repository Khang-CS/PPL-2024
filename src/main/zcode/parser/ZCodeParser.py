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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u01d7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\5\3\u0082\n\3")
        buf.write("\3\4\3\4\3\4\5\4\u0087\n\4\3\5\3\5\3\5\3\5\5\5\u008d\n")
        buf.write("\5\3\6\3\6\5\6\u0091\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00a2\n\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\5\13\u00a9\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b0")
        buf.write("\n\f\3\r\3\r\5\r\u00b4\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00bc\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c7\n\17\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\5\21\u00cf\n\21\3\22\3\22\5\22\u00d3\n\22\3\22\3\22")
        buf.write("\3\22\5\22\u00d8\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00e1\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00ec\n\25\3\26\3\26\3\26\3\26\5\26\u00f2")
        buf.write("\n\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u00fe\n\32\3\33\3\33\5\33\u0102\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0113\n\36\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u011a\n\37\3 \3 \3 \3 \3 \5 \u0121\n \3!\3!\3!\3!")
        buf.write("\3!\3!\7!\u0129\n!\f!\16!\u012c\13!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u0134\n\"\f\"\16\"\u0137\13\"\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u013f\n#\f#\16#\u0142\13#\3$\3$\3$\5$\u0147\n")
        buf.write("$\3%\3%\3%\5%\u014c\n%\3&\3&\5&\u0150\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u015c\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u0164\n(\3)\3)\5)\u0168\n)\3*\3*\3*\3*\3*\5*\u016f")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\5,\u017c\n,\3-\3")
        buf.write("-\3-\3-\3-\5-\u0183\n-\3.\3.\3.\3.\3.\3/\3/\3/\3/\5/\u018e")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\5\64\u01a3")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\5\66\u01ac\n")
        buf.write("\66\3\67\3\67\3\67\3\67\5\67\u01b2\n\67\38\38\38\38\3")
        buf.write("8\38\58\u01ba\n8\39\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\2\5@BD")
        buf.write("?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\b\3\2\20\22")
        buf.write("\3\2\24\25\5\2))+/\61\61\3\2\"#\3\2$%\3\2&(\2\u01cf\2")
        buf.write("|\3\2\2\2\4\u0081\3\2\2\2\6\u0086\3\2\2\2\b\u008c\3\2")
        buf.write("\2\2\n\u0090\3\2\2\2\f\u0092\3\2\2\2\16\u0096\3\2\2\2")
        buf.write("\20\u00a1\3\2\2\2\22\u00a3\3\2\2\2\24\u00a8\3\2\2\2\26")
        buf.write("\u00af\3\2\2\2\30\u00b3\3\2\2\2\32\u00bb\3\2\2\2\34\u00c6")
        buf.write("\3\2\2\2\36\u00c8\3\2\2\2 \u00ce\3\2\2\2\"\u00d2\3\2\2")
        buf.write("\2$\u00d9\3\2\2\2&\u00e2\3\2\2\2(\u00eb\3\2\2\2*\u00f1")
        buf.write("\3\2\2\2,\u00f3\3\2\2\2.\u00f5\3\2\2\2\60\u00f7\3\2\2")
        buf.write("\2\62\u00fd\3\2\2\2\64\u0101\3\2\2\2\66\u0103\3\2\2\2")
        buf.write("8\u0108\3\2\2\2:\u0112\3\2\2\2<\u0119\3\2\2\2>\u0120\3")
        buf.write("\2\2\2@\u0122\3\2\2\2B\u012d\3\2\2\2D\u0138\3\2\2\2F\u0146")
        buf.write("\3\2\2\2H\u014b\3\2\2\2J\u014f\3\2\2\2L\u015b\3\2\2\2")
        buf.write("N\u0163\3\2\2\2P\u0167\3\2\2\2R\u016e\3\2\2\2T\u0170\3")
        buf.write("\2\2\2V\u017b\3\2\2\2X\u0182\3\2\2\2Z\u0184\3\2\2\2\\")
        buf.write("\u018d\3\2\2\2^\u018f\3\2\2\2`\u0193\3\2\2\2b\u019c\3")
        buf.write("\2\2\2d\u019e\3\2\2\2f\u01a0\3\2\2\2h\u01a4\3\2\2\2j\u01ab")
        buf.write("\3\2\2\2l\u01b1\3\2\2\2n\u01b9\3\2\2\2p\u01bb\3\2\2\2")
        buf.write("r\u01bf\3\2\2\2t\u01c4\3\2\2\2v\u01c8\3\2\2\2x\u01cd\3")
        buf.write("\2\2\2z\u01d1\3\2\2\2|}\5\b\5\2}~\7\2\2\3~\3\3\2\2\2\177")
        buf.write("\u0082\5\6\4\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0080\3\2\2\2\u0082\5\3\2\2\2\u0083\u0084\79\2\2\u0084")
        buf.write("\u0087\5\6\4\2\u0085\u0087\79\2\2\u0086\u0083\3\2\2\2")
        buf.write("\u0086\u0085\3\2\2\2\u0087\7\3\2\2\2\u0088\u0089\5\n\6")
        buf.write("\2\u0089\u008a\5\b\5\2\u008a\u008d\3\2\2\2\u008b\u008d")
        buf.write("\5\n\6\2\u008c\u0088\3\2\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\t\3\2\2\2\u008e\u0091\5\16\b\2\u008f\u0091\5\f\7\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\13\3\2\2\2\u0092")
        buf.write("\u0093\5\4\3\2\u0093\u0094\5 \21\2\u0094\u0095\5\6\4\2")
        buf.write("\u0095\r\3\2\2\2\u0096\u0097\5\4\3\2\u0097\u0098\7\26")
        buf.write("\2\2\u0098\u0099\7\67\2\2\u0099\u009a\7\62\2\2\u009a\u009b")
        buf.write("\5\24\13\2\u009b\u009c\7\63\2\2\u009c\u009d\5\4\3\2\u009d")
        buf.write("\u009e\5\30\r\2\u009e\17\3\2\2\2\u009f\u00a2\5\22\n\2")
        buf.write("\u00a0\u00a2\5$\23\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3")
        buf.write("\2\2\2\u00a2\21\3\2\2\2\u00a3\u00a4\5,\27\2\u00a4\u00a5")
        buf.write("\7\67\2\2\u00a5\23\3\2\2\2\u00a6\u00a9\5\26\f\2\u00a7")
        buf.write("\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\25\3\2\2\2\u00aa\u00ab\5\20\t\2\u00ab\u00ac\7\66")
        buf.write("\2\2\u00ac\u00ad\5\26\f\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0")
        buf.write("\5\20\t\2\u00af\u00aa\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\27\3\2\2\2\u00b1\u00b4\5\32\16\2\u00b2\u00b4\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\31\3\2")
        buf.write("\2\2\u00b5\u00b6\5f\64\2\u00b6\u00b7\5\6\4\2\u00b7\u00bc")
        buf.write("\3\2\2\2\u00b8\u00b9\5h\65\2\u00b9\u00ba\5\6\4\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bb\u00b8\3\2\2\2")
        buf.write("\u00bc\33\3\2\2\2\u00bd\u00c7\5 \21\2\u00be\u00c7\5\60")
        buf.write("\31\2\u00bf\u00c7\5T+\2\u00c0\u00c7\5`\61\2\u00c1\u00c7")
        buf.write("\5b\62\2\u00c2\u00c7\5d\63\2\u00c3\u00c7\5f\64\2\u00c4")
        buf.write("\u00c7\5N(\2\u00c5\u00c7\5h\65\2\u00c6\u00bd\3\2\2\2\u00c6")
        buf.write("\u00be\3\2\2\2\u00c6\u00bf\3\2\2\2\u00c6\u00c0\3\2\2\2")
        buf.write("\u00c6\u00c1\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c3\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\35")
        buf.write("\3\2\2\2\u00c8\u00c9\5\4\3\2\u00c9\u00ca\5\34\17\2\u00ca")
        buf.write("\u00cb\5\6\4\2\u00cb\37\3\2\2\2\u00cc\u00cf\5\"\22\2\u00cd")
        buf.write("\u00cf\5$\23\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2")
        buf.write("\u00cf!\3\2\2\2\u00d0\u00d3\5,\27\2\u00d1\u00d3\5.\30")
        buf.write("\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d7\7\67\2\2\u00d5\u00d6\7*\2\2\u00d6")
        buf.write("\u00d8\5<\37\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8#\3\2\2\2\u00d9\u00da\5,\27\2\u00da\u00db\7\67\2")
        buf.write("\2\u00db\u00dc\7\64\2\2\u00dc\u00dd\5*\26\2\u00dd\u00e0")
        buf.write("\7\65\2\2\u00de\u00df\7*\2\2\u00df\u00e1\5&\24\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1%\3\2\2\2\u00e2")
        buf.write("\u00e3\7\64\2\2\u00e3\u00e4\5(\25\2\u00e4\u00e5\7\65\2")
        buf.write("\2\u00e5\'\3\2\2\2\u00e6\u00e7\5<\37\2\u00e7\u00e8\7\66")
        buf.write("\2\2\u00e8\u00e9\5(\25\2\u00e9\u00ec\3\2\2\2\u00ea\u00ec")
        buf.write("\5<\37\2\u00eb\u00e6\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write(")\3\2\2\2\u00ed\u00ee\7\t\2\2\u00ee\u00ef\7\66\2\2\u00ef")
        buf.write("\u00f2\5*\26\2\u00f0\u00f2\7\t\2\2\u00f1\u00ed\3\2\2\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f2+\3\2\2\2\u00f3\u00f4\t\2\2")
        buf.write("\2\u00f4-\3\2\2\2\u00f5\u00f6\t\3\2\2\u00f6/\3\2\2\2\u00f7")
        buf.write("\u00f8\5\62\32\2\u00f8\u00f9\7*\2\2\u00f9\u00fa\5<\37")
        buf.write("\2\u00fa\61\3\2\2\2\u00fb\u00fe\7\67\2\2\u00fc\u00fe\5")
        buf.write("\66\34\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe")
        buf.write("\63\3\2\2\2\u00ff\u0102\5\66\34\2\u0100\u0102\58\35\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102\65\3\2")
        buf.write("\2\2\u0103\u0104\7\67\2\2\u0104\u0105\7\64\2\2\u0105\u0106")
        buf.write("\5:\36\2\u0106\u0107\7\65\2\2\u0107\67\3\2\2\2\u0108\u0109")
        buf.write("\5N(\2\u0109\u010a\7\64\2\2\u010a\u010b\5:\36\2\u010b")
        buf.write("\u010c\7\65\2\2\u010c9\3\2\2\2\u010d\u010e\5<\37\2\u010e")
        buf.write("\u010f\7\66\2\2\u010f\u0110\5:\36\2\u0110\u0113\3\2\2")
        buf.write("\2\u0111\u0113\5<\37\2\u0112\u010d\3\2\2\2\u0112\u0111")
        buf.write("\3\2\2\2\u0113;\3\2\2\2\u0114\u0115\5> \2\u0115\u0116")
        buf.write("\7\60\2\2\u0116\u0117\5> \2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u011a\5> \2\u0119\u0114\3\2\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("=\3\2\2\2\u011b\u011c\5@!\2\u011c\u011d\t\4\2\2\u011d")
        buf.write("\u011e\5@!\2\u011e\u0121\3\2\2\2\u011f\u0121\5@!\2\u0120")
        buf.write("\u011b\3\2\2\2\u0120\u011f\3\2\2\2\u0121?\3\2\2\2\u0122")
        buf.write("\u0123\b!\1\2\u0123\u0124\5B\"\2\u0124\u012a\3\2\2\2\u0125")
        buf.write("\u0126\f\4\2\2\u0126\u0127\t\5\2\2\u0127\u0129\5B\"\2")
        buf.write("\u0128\u0125\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012bA\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012d\u012e\b\"\1\2\u012e\u012f\5D#\2\u012f\u0135")
        buf.write("\3\2\2\2\u0130\u0131\f\4\2\2\u0131\u0132\t\6\2\2\u0132")
        buf.write("\u0134\5D#\2\u0133\u0130\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136C\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u0139\b#\1\2\u0139\u013a\5F$\2\u013a")
        buf.write("\u0140\3\2\2\2\u013b\u013c\f\4\2\2\u013c\u013d\t\7\2\2")
        buf.write("\u013d\u013f\5F$\2\u013e\u013b\3\2\2\2\u013f\u0142\3\2")
        buf.write("\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141E\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\7!\2\2\u0144\u0147")
        buf.write("\5F$\2\u0145\u0147\5H%\2\u0146\u0143\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147G\3\2\2\2\u0148\u0149\7%\2\2\u0149\u014c")
        buf.write("\5H%\2\u014a\u014c\5J&\2\u014b\u0148\3\2\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014cI\3\2\2\2\u014d\u0150\5\64\33\2\u014e\u0150")
        buf.write("\5L\'\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("K\3\2\2\2\u0151\u015c\7\t\2\2\u0152\u015c\7\n\2\2\u0153")
        buf.write("\u015c\7\13\2\2\u0154\u015c\7\67\2\2\u0155\u015c\5N(\2")
        buf.write("\u0156\u0157\7\62\2\2\u0157\u0158\5<\37\2\u0158\u0159")
        buf.write("\7\63\2\2\u0159\u015c\3\2\2\2\u015a\u015c\5&\24\2\u015b")
        buf.write("\u0151\3\2\2\2\u015b\u0152\3\2\2\2\u015b\u0153\3\2\2\2")
        buf.write("\u015b\u0154\3\2\2\2\u015b\u0155\3\2\2\2\u015b\u0156\3")
        buf.write("\2\2\2\u015b\u015a\3\2\2\2\u015cM\3\2\2\2\u015d\u015e")
        buf.write("\7\67\2\2\u015e\u015f\7\62\2\2\u015f\u0160\5P)\2\u0160")
        buf.write("\u0161\7\63\2\2\u0161\u0164\3\2\2\2\u0162\u0164\5n8\2")
        buf.write("\u0163\u015d\3\2\2\2\u0163\u0162\3\2\2\2\u0164O\3\2\2")
        buf.write("\2\u0165\u0168\5R*\2\u0166\u0168\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0166\3\2\2\2\u0168Q\3\2\2\2\u0169\u016a")
        buf.write("\5<\37\2\u016a\u016b\7\66\2\2\u016b\u016c\5R*\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016f\5<\37\2\u016e\u0169\3\2\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016fS\3\2\2\2\u0170\u0171\7\34\2")
        buf.write("\2\u0171\u0172\5<\37\2\u0172\u0173\5\4\3\2\u0173\u0174")
        buf.write("\5\34\17\2\u0174\u0175\5V,\2\u0175\u0176\5\\/\2\u0176")
        buf.write("U\3\2\2\2\u0177\u0178\5\6\4\2\u0178\u0179\5X-\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u0177\3\2\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017cW\3\2\2\2\u017d\u017e\5Z.\2")
        buf.write("\u017e\u017f\5\6\4\2\u017f\u0180\5X-\2\u0180\u0183\3\2")
        buf.write("\2\2\u0181\u0183\5Z.\2\u0182\u017d\3\2\2\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183Y\3\2\2\2\u0184\u0185\7\36\2\2\u0185\u0186")
        buf.write("\5<\37\2\u0186\u0187\5\4\3\2\u0187\u0188\5\34\17\2\u0188")
        buf.write("[\3\2\2\2\u0189\u018a\5\6\4\2\u018a\u018b\5^\60\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u0189\3\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e]\3\2\2\2\u018f\u0190\7\35\2")
        buf.write("\2\u0190\u0191\5\4\3\2\u0191\u0192\5\34\17\2\u0192_\3")
        buf.write("\2\2\2\u0193\u0194\7\27\2\2\u0194\u0195\7\67\2\2\u0195")
        buf.write("\u0196\7\30\2\2\u0196\u0197\5<\37\2\u0197\u0198\7\31\2")
        buf.write("\2\u0198\u0199\5<\37\2\u0199\u019a\5\4\3\2\u019a\u019b")
        buf.write("\5\34\17\2\u019ba\3\2\2\2\u019c\u019d\7\32\2\2\u019dc")
        buf.write("\3\2\2\2\u019e\u019f\7\33\2\2\u019fe\3\2\2\2\u01a0\u01a2")
        buf.write("\7\23\2\2\u01a1\u01a3\5<\37\2\u01a2\u01a1\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3g\3\2\2\2\u01a4\u01a5\7\37\2\2\u01a5")
        buf.write("\u01a6\5\4\3\2\u01a6\u01a7\5j\66\2\u01a7\u01a8\7 \2\2")
        buf.write("\u01a8i\3\2\2\2\u01a9\u01ac\5l\67\2\u01aa\u01ac\3\2\2")
        buf.write("\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ack\3\2")
        buf.write("\2\2\u01ad\u01ae\5\36\20\2\u01ae\u01af\5l\67\2\u01af\u01b2")
        buf.write("\3\2\2\2\u01b0\u01b2\5\36\20\2\u01b1\u01ad\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2m\3\2\2\2\u01b3\u01ba\5p9\2\u01b4")
        buf.write("\u01ba\5r:\2\u01b5\u01ba\5t;\2\u01b6\u01ba\5v<\2\u01b7")
        buf.write("\u01ba\5x=\2\u01b8\u01ba\5z>\2\u01b9\u01b3\3\2\2\2\u01b9")
        buf.write("\u01b4\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9\u01b6\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01bao\3\2\2")
        buf.write("\2\u01bb\u01bc\7\3\2\2\u01bc\u01bd\7\62\2\2\u01bd\u01be")
        buf.write("\7\63\2\2\u01beq\3\2\2\2\u01bf\u01c0\7\4\2\2\u01c0\u01c1")
        buf.write("\7\62\2\2\u01c1\u01c2\5<\37\2\u01c2\u01c3\7\63\2\2\u01c3")
        buf.write("s\3\2\2\2\u01c4\u01c5\7\5\2\2\u01c5\u01c6\7\62\2\2\u01c6")
        buf.write("\u01c7\7\63\2\2\u01c7u\3\2\2\2\u01c8\u01c9\7\6\2\2\u01c9")
        buf.write("\u01ca\7\62\2\2\u01ca\u01cb\5<\37\2\u01cb\u01cc\7\63\2")
        buf.write("\2\u01ccw\3\2\2\2\u01cd\u01ce\7\7\2\2\u01ce\u01cf\7\62")
        buf.write("\2\2\u01cf\u01d0\7\63\2\2\u01d0y\3\2\2\2\u01d1\u01d2\7")
        buf.write("\b\2\2\u01d2\u01d3\7\62\2\2\u01d3\u01d4\5<\37\2\u01d4")
        buf.write("\u01d5\7\63\2\2\u01d5{\3\2\2\2(\u0081\u0086\u008c\u0090")
        buf.write("\u00a1\u00a8\u00af\u00b3\u00bb\u00c6\u00ce\u00d2\u00d7")
        buf.write("\u00e0\u00eb\u00f1\u00fd\u0101\u0112\u0119\u0120\u012a")
        buf.write("\u0135\u0140\u0146\u014b\u014f\u015b\u0163\u0167\u016e")
        buf.write("\u017b\u0182\u018d\u01a2\u01ab\u01b1\u01b9")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMLIT", "BOOLLIT", 
                      "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
                      "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                      "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                      "MODOP", "EQUALOP", "ASSIGNOP", "DIFFOP", "LESS", 
                      "LESSEQ", "LARGER", "LARGEREQ", "DOT", "STRCOMPARE", 
                      "LB", "RB", "LP", "RP", "COMMA", "IDENTIFIER", "COMMENT", 
                      "NEWLINE", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_newline_list = 1
    RULE_newline_prime = 2
    RULE_decllist = 3
    RULE_decl = 4
    RULE_var_init = 5
    RULE_func = 6
    RULE_param = 7
    RULE_scala_param = 8
    RULE_paramlist = 9
    RULE_paramprime = 10
    RULE_option = 11
    RULE_optionprime = 12
    RULE_stmt = 13
    RULE_standalone_stmt = 14
    RULE_vardecl = 15
    RULE_normaldecl = 16
    RULE_arraydecl = 17
    RULE_arrayvalue = 18
    RULE_array_value_list = 19
    RULE_dimensions = 20
    RULE_normaltype = 21
    RULE_implicittype = 22
    RULE_assign_stmt = 23
    RULE_lhs = 24
    RULE_indexexp = 25
    RULE_scalar_index_exp = 26
    RULE_funccal_index_exp = 27
    RULE_index_operators = 28
    RULE_exp = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_exp7 = 35
    RULE_exp8 = 36
    RULE_exp9 = 37
    RULE_funccall_stmt = 38
    RULE_explist = 39
    RULE_expprime = 40
    RULE_if_stmt = 41
    RULE_elif_stmt_list = 42
    RULE_elif_stmt_prime = 43
    RULE_elif_stmt = 44
    RULE_else_stmt = 45
    RULE_else_stmt_prime = 46
    RULE_for_stmt = 47
    RULE_break_stmt = 48
    RULE_continue_stmt = 49
    RULE_return_stmt = 50
    RULE_block_stmt = 51
    RULE_stmtlist = 52
    RULE_stmtprime = 53
    RULE_io_func = 54
    RULE_readNumber = 55
    RULE_writeNumber = 56
    RULE_readBool = 57
    RULE_writeBool = 58
    RULE_readString = 59
    RULE_writeString = 60

    ruleNames =  [ "program", "newline_list", "newline_prime", "decllist", 
                   "decl", "var_init", "func", "param", "scala_param", "paramlist", 
                   "paramprime", "option", "optionprime", "stmt", "standalone_stmt", 
                   "vardecl", "normaldecl", "arraydecl", "arrayvalue", "array_value_list", 
                   "dimensions", "normaltype", "implicittype", "assign_stmt", 
                   "lhs", "indexexp", "scalar_index_exp", "funccal_index_exp", 
                   "index_operators", "exp", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "funccall_stmt", "explist", 
                   "expprime", "if_stmt", "elif_stmt_list", "elif_stmt_prime", 
                   "elif_stmt", "else_stmt", "else_stmt_prime", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "block_stmt", 
                   "stmtlist", "stmtprime", "io_func", "readNumber", "writeNumber", 
                   "readBool", "writeBool", "readString", "writeString" ]

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
    ILLEGAL_ESCAPE=10
    UNCLOSED_STRING=11
    TRUE=12
    FALSE=13
    NUMBER=14
    BOOL=15
    STRING=16
    RETURN=17
    VAR=18
    DYNAMIC=19
    FUNC=20
    FOR=21
    UNTIL=22
    BY=23
    BREAK=24
    CONTINUE=25
    IF=26
    ELSE=27
    ELIF=28
    BEGIN=29
    END=30
    NOT=31
    AND=32
    OR=33
    ADDOP=34
    SUBOP=35
    MULOP=36
    DIVOP=37
    MODOP=38
    EQUALOP=39
    ASSIGNOP=40
    DIFFOP=41
    LESS=42
    LESSEQ=43
    LARGER=44
    LARGEREQ=45
    DOT=46
    STRCOMPARE=47
    LB=48
    RB=49
    LP=50
    RP=51
    COMMA=52
    IDENTIFIER=53
    COMMENT=54
    NEWLINE=55
    WS=56
    ERROR_CHAR=57

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

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


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
            self.state = 122
            self.decllist()
            self.state = 123
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newline_list)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_prime" ):
                return visitor.visitNewline_prime(self)
            else:
                return visitor.visitChildren(self)




    def newline_prime(self):

        localctx = ZCodeParser.Newline_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newline_prime)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(ZCodeParser.NEWLINE)
                self.state = 130
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(ZCodeParser.NEWLINE)
                pass


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

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decllist)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.decl()
                self.state = 135
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.decl()
                pass


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

        def func(self):
            return self.getTypedRuleContext(ZCodeParser.FuncContext,0)


        def var_init(self):
            return self.getTypedRuleContext(ZCodeParser.Var_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.var_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = ZCodeParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.newline_list()
            self.state = 145
            self.vardecl()
            self.state = 146
            self.newline_prime()
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

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


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
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.newline_list()
            self.state = 149
            self.match(ZCodeParser.FUNC)
            self.state = 150
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 151
            self.match(ZCodeParser.LB)
            self.state = 152
            self.paramlist()
            self.state = 153
            self.match(ZCodeParser.RB)
            self.state = 154
            self.newline_list()
            self.state = 155
            self.option()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scala_param(self):
            return self.getTypedRuleContext(ZCodeParser.Scala_paramContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.scala_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scala_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normaltype(self):
            return self.getTypedRuleContext(ZCodeParser.NormaltypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scala_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScala_param" ):
                return visitor.visitScala_param(self)
            else:
                return visitor.visitChildren(self)




    def scala_param(self):

        localctx = ZCodeParser.Scala_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scala_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.normaltype()
            self.state = 162
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramlist)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.paramprime()
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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramprime)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.param()
                self.state = 169
                self.match(ZCodeParser.COMMA)
                self.state = 170
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.param()
                pass


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
        self.enterRule(localctx, 22, self.RULE_option)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.optionprime()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
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


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


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
        self.enterRule(localctx, 24, self.RULE_optionprime)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.return_stmt()
                self.state = 180
                self.newline_prime()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.block_stmt()
                self.state = 183
                self.newline_prime()
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


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
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 195
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_standalone_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandalone_stmt" ):
                return visitor.visitStandalone_stmt(self)
            else:
                return visitor.visitChildren(self)




    def standalone_stmt(self):

        localctx = ZCodeParser.Standalone_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_standalone_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.newline_list()
            self.state = 199
            self.stmt()
            self.state = 200
            self.newline_prime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normaldecl(self):
            return self.getTypedRuleContext(ZCodeParser.NormaldeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 202
                self.normaldecl()
                pass

            elif la_ == 2:
                self.state = 203
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


        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normaldecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaldecl" ):
                return visitor.visitNormaldecl(self)
            else:
                return visitor.visitChildren(self)




    def normaldecl(self):

        localctx = ZCodeParser.NormaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_normaldecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 206
                self.normaltype()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 207
                self.implicittype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 210
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNOP:
                self.state = 211
                self.match(ZCodeParser.ASSIGNOP)
                self.state = 212
                self.exp()


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

        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.normaltype()
            self.state = 216
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 217
            self.match(ZCodeParser.LP)
            self.state = 218
            self.dimensions()
            self.state = 219
            self.match(ZCodeParser.RP)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNOP:
                self.state = 220
                self.match(ZCodeParser.ASSIGNOP)
                self.state = 221
                self.arrayvalue()


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

        def array_value_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_listContext,0)


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
        self.enterRule(localctx, 36, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ZCodeParser.LP)
            self.state = 225
            self.array_value_list()
            self.state = 226
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_value_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_list" ):
                return visitor.visitArray_value_list(self)
            else:
                return visitor.visitChildren(self)




    def array_value_list(self):

        localctx = ZCodeParser.Array_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_value_list)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.exp()
                self.state = 229
                self.match(ZCodeParser.COMMA)
                self.state = 230
                self.array_value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.exp()
                pass


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
        self.enterRule(localctx, 40, self.RULE_dimensions)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.NUMLIT)
                self.state = 236
                self.match(ZCodeParser.COMMA)
                self.state = 237
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
        self.enterRule(localctx, 42, self.RULE_normaltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
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
        self.enterRule(localctx, 44, self.RULE_implicittype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
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


        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

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
        self.enterRule(localctx, 46, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.lhs()
            self.state = 246
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 247
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

        def scalar_index_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_index_expContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.scalar_index_exp()
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

        def scalar_index_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_index_expContext,0)


        def funccal_index_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Funccal_index_expContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexp" ):
                return visitor.visitIndexexp(self)
            else:
                return visitor.visitChildren(self)




    def indexexp(self):

        localctx = ZCodeParser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_indexexp)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.scalar_index_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.funccal_index_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_index_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scalar_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_index_exp" ):
                return visitor.visitScalar_index_exp(self)
            else:
                return visitor.visitChildren(self)




    def scalar_index_exp(self):

        localctx = ZCodeParser.Scalar_index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_scalar_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 258
            self.match(ZCodeParser.LP)
            self.state = 259
            self.index_operators()
            self.state = 260
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccal_index_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funccall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Funccall_stmtContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funccal_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccal_index_exp" ):
                return visitor.visitFunccal_index_exp(self)
            else:
                return visitor.visitChildren(self)




    def funccal_index_exp(self):

        localctx = ZCodeParser.Funccal_index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funccal_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.funccall_stmt()
            self.state = 263
            self.match(ZCodeParser.LP)
            self.state = 264
            self.index_operators()
            self.state = 265
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
        self.enterRule(localctx, 56, self.RULE_index_operators)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.exp()
                self.state = 268
                self.match(ZCodeParser.COMMA)
                self.state = 269
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 58, self.RULE_exp)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.exp2()
                self.state = 275
                self.match(ZCodeParser.DOT)
                self.state = 276
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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
        self.enterRule(localctx, 60, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.exp3(0)
                self.state = 282
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUALOP) | (1 << ZCodeParser.DIFFOP) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESSEQ) | (1 << ZCodeParser.LARGER) | (1 << ZCodeParser.LARGEREQ) | (1 << ZCodeParser.STRCOMPARE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 293
                    self.exp4(0) 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADDOP or _la==ZCodeParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 304
                    self.exp5(0) 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 314
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULOP) | (1 << ZCodeParser.DIVOP) | (1 << ZCodeParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 315
                    self.exp6() 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


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
        self.enterRule(localctx, 68, self.RULE_exp6)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(ZCodeParser.NOT)
                self.state = 322
                self.exp6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUBOP, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


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
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(ZCodeParser.SUBOP)
                self.state = 327
                self.exp7()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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
        self.enterRule(localctx, 72, self.RULE_exp8)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.indexexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Funccall_stmtContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = ZCodeParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp9)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 338
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 339
                self.funccall_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 340
                self.match(ZCodeParser.LB)
                self.state = 341
                self.exp()
                self.state = 342
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 344
                self.arrayvalue()
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
        self.enterRule(localctx, 76, self.RULE_funccall_stmt)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 348
                self.match(ZCodeParser.LB)
                self.state = 349
                self.explist()
                self.state = 350
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        self.enterRule(localctx, 78, self.RULE_explist)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
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
        self.enterRule(localctx, 80, self.RULE_expprime)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.exp()
                self.state = 360
                self.match(ZCodeParser.COMMA)
                self.state = 361
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmt_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.IF)
            self.state = 367
            self.exp()
            self.state = 368
            self.newline_list()
            self.state = 369
            self.stmt()
            self.state = 370
            self.elif_stmt_list()
            self.state = 371
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def elif_stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt_list" ):
                return visitor.visitElif_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt_list(self):

        localctx = ZCodeParser.Elif_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elif_stmt_list)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.newline_prime()
                self.state = 374
                self.elif_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def elif_stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt_prime" ):
                return visitor.visitElif_stmt_prime(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt_prime(self):

        localctx = ZCodeParser.Elif_stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elif_stmt_prime)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.elif_stmt()
                self.state = 380
                self.newline_prime()
                self.state = 381
                self.elif_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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
        self.enterRule(localctx, 88, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(ZCodeParser.ELIF)
            self.state = 387
            self.exp()
            self.state = 388
            self.newline_list()
            self.state = 389
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def else_stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_stmt)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.newline_prime()
                self.state = 392
                self.else_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt_prime" ):
                return visitor.visitElse_stmt_prime(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt_prime(self):

        localctx = ZCodeParser.Else_stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_else_stmt_prime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.ELSE)
            self.state = 398
            self.newline_list()
            self.state = 399
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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
        self.enterRule(localctx, 94, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(ZCodeParser.FOR)
            self.state = 402
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 403
            self.match(ZCodeParser.UNTIL)
            self.state = 404
            self.exp()
            self.state = 405
            self.match(ZCodeParser.BY)
            self.state = 406
            self.exp()
            self.state = 407
            self.newline_list()
            self.state = 408
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
        self.enterRule(localctx, 96, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        self.enterRule(localctx, 98, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        self.enterRule(localctx, 100, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(ZCodeParser.RETURN)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUBOP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 415
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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
        self.enterRule(localctx, 102, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.BEGIN)
            self.state = 419
            self.newline_list()
            self.state = 420
            self.stmtlist()
            self.state = 421
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
        self.enterRule(localctx, 104, self.RULE_stmtlist)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
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
        self.enterRule(localctx, 106, self.RULE_stmtprime)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.standalone_stmt()
                self.state = 428
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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


        def writeBool(self):
            return self.getTypedRuleContext(ZCodeParser.WriteBoolContext,0)


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
        self.enterRule(localctx, 108, self.RULE_io_func)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.readNumber()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.writeNumber()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.readBool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.writeBool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 437
                self.readString()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 438
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
        self.enterRule(localctx, 110, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.T__0)
            self.state = 442
            self.match(ZCodeParser.LB)
            self.state = 443
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
        self.enterRule(localctx, 112, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(ZCodeParser.T__1)
            self.state = 446
            self.match(ZCodeParser.LB)
            self.state = 447
            self.exp()
            self.state = 448
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
        self.enterRule(localctx, 114, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ZCodeParser.T__2)
            self.state = 451
            self.match(ZCodeParser.LB)
            self.state = 452
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteBoolContext(ParserRuleContext):
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
            return ZCodeParser.RULE_writeBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteBool" ):
                return visitor.visitWriteBool(self)
            else:
                return visitor.visitChildren(self)




    def writeBool(self):

        localctx = ZCodeParser.WriteBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_writeBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(ZCodeParser.T__3)
            self.state = 455
            self.match(ZCodeParser.LB)
            self.state = 456
            self.exp()
            self.state = 457
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
        self.enterRule(localctx, 118, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(ZCodeParser.T__4)
            self.state = 460
            self.match(ZCodeParser.LB)
            self.state = 461
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
        self.enterRule(localctx, 120, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(ZCodeParser.T__5)
            self.state = 464
            self.match(ZCodeParser.LB)
            self.state = 465
            self.exp()
            self.state = 466
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
        self._predicates[31] = self.exp3_sempred
        self._predicates[32] = self.exp4_sempred
        self._predicates[33] = self.exp5_sempred
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
         





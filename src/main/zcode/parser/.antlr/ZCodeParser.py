# Generated from c://Users//khang//OneDrive//Desktop//PPL 2024//Assignment//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,414,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,1,1,3,1,112,8,1,1,2,1,2,1,2,3,2,117,8,2,1,3,1,3,
        1,3,1,3,3,3,123,8,3,1,4,1,4,3,4,127,8,4,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,143,8,6,1,7,1,7,3,7,147,8,7,
        1,8,1,8,1,8,1,9,1,9,3,9,154,8,9,1,10,1,10,1,10,1,10,1,10,3,10,161,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,169,8,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,180,8,12,1,13,1,13,1,13,1,13,
        1,14,1,14,3,14,188,8,14,1,15,1,15,3,15,192,8,15,1,15,1,15,1,15,3,
        15,197,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,206,8,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,217,8,18,1,19,1,19,
        1,19,1,19,3,19,223,8,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,
        1,23,1,23,3,23,235,8,23,1,24,1,24,3,24,239,8,24,1,25,1,25,1,25,1,
        25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,256,
        8,27,1,28,1,28,1,28,1,28,1,28,3,28,263,8,28,1,29,1,29,1,29,1,29,
        1,29,3,29,270,8,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,278,8,30,10,
        30,12,30,281,9,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,289,8,31,10,
        31,12,31,292,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,300,8,32,10,
        32,12,32,303,9,32,1,33,1,33,1,33,3,33,308,8,33,1,34,1,34,1,34,3,
        34,313,8,34,1,35,1,35,3,35,317,8,35,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,3,36,329,8,36,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,3,38,338,8,38,1,39,1,39,1,39,1,39,1,39,3,39,345,8,39,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,3,41,358,8,41,1,
        42,1,42,1,42,1,42,1,42,3,42,365,8,42,1,43,1,43,1,43,1,43,1,43,1,
        44,1,44,1,44,1,44,3,44,376,8,44,1,45,1,45,1,45,1,45,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,3,
        49,397,8,49,1,50,1,50,1,50,1,50,1,50,1,51,1,51,3,51,406,8,51,1,52,
        1,52,1,52,1,52,3,52,412,8,52,1,52,0,3,60,62,64,53,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,0,6,1,0,8,10,1,0,12,13,3,0,33,33,35,39,41,41,1,0,26,27,1,
        0,28,29,1,0,30,32,408,0,106,1,0,0,0,2,111,1,0,0,0,4,116,1,0,0,0,
        6,122,1,0,0,0,8,126,1,0,0,0,10,128,1,0,0,0,12,132,1,0,0,0,14,146,
        1,0,0,0,16,148,1,0,0,0,18,153,1,0,0,0,20,160,1,0,0,0,22,168,1,0,
        0,0,24,179,1,0,0,0,26,181,1,0,0,0,28,187,1,0,0,0,30,191,1,0,0,0,
        32,198,1,0,0,0,34,207,1,0,0,0,36,216,1,0,0,0,38,222,1,0,0,0,40,224,
        1,0,0,0,42,226,1,0,0,0,44,228,1,0,0,0,46,234,1,0,0,0,48,238,1,0,
        0,0,50,240,1,0,0,0,52,245,1,0,0,0,54,255,1,0,0,0,56,262,1,0,0,0,
        58,269,1,0,0,0,60,271,1,0,0,0,62,282,1,0,0,0,64,293,1,0,0,0,66,307,
        1,0,0,0,68,312,1,0,0,0,70,316,1,0,0,0,72,328,1,0,0,0,74,330,1,0,
        0,0,76,337,1,0,0,0,78,344,1,0,0,0,80,346,1,0,0,0,82,357,1,0,0,0,
        84,364,1,0,0,0,86,366,1,0,0,0,88,375,1,0,0,0,90,377,1,0,0,0,92,381,
        1,0,0,0,94,390,1,0,0,0,96,392,1,0,0,0,98,394,1,0,0,0,100,398,1,0,
        0,0,102,405,1,0,0,0,104,411,1,0,0,0,106,107,3,6,3,0,107,108,5,0,
        0,1,108,1,1,0,0,0,109,112,3,4,2,0,110,112,1,0,0,0,111,109,1,0,0,
        0,111,110,1,0,0,0,112,3,1,0,0,0,113,114,5,49,0,0,114,117,3,4,2,0,
        115,117,5,49,0,0,116,113,1,0,0,0,116,115,1,0,0,0,117,5,1,0,0,0,118,
        119,3,8,4,0,119,120,3,6,3,0,120,123,1,0,0,0,121,123,3,8,4,0,122,
        118,1,0,0,0,122,121,1,0,0,0,123,7,1,0,0,0,124,127,3,12,6,0,125,127,
        3,10,5,0,126,124,1,0,0,0,126,125,1,0,0,0,127,9,1,0,0,0,128,129,3,
        2,1,0,129,130,3,28,14,0,130,131,3,4,2,0,131,11,1,0,0,0,132,133,3,
        2,1,0,133,134,5,14,0,0,134,135,5,47,0,0,135,136,5,42,0,0,136,137,
        3,18,9,0,137,142,5,43,0,0,138,139,3,2,1,0,139,140,3,22,11,0,140,
        143,1,0,0,0,141,143,3,4,2,0,142,138,1,0,0,0,142,141,1,0,0,0,143,
        13,1,0,0,0,144,147,3,16,8,0,145,147,3,32,16,0,146,144,1,0,0,0,146,
        145,1,0,0,0,147,15,1,0,0,0,148,149,3,40,20,0,149,150,5,47,0,0,150,
        17,1,0,0,0,151,154,3,20,10,0,152,154,1,0,0,0,153,151,1,0,0,0,153,
        152,1,0,0,0,154,19,1,0,0,0,155,156,3,14,7,0,156,157,5,46,0,0,157,
        158,3,20,10,0,158,161,1,0,0,0,159,161,3,14,7,0,160,155,1,0,0,0,160,
        159,1,0,0,0,161,21,1,0,0,0,162,163,3,98,49,0,163,164,3,4,2,0,164,
        169,1,0,0,0,165,166,3,100,50,0,166,167,3,4,2,0,167,169,1,0,0,0,168,
        162,1,0,0,0,168,165,1,0,0,0,169,23,1,0,0,0,170,180,3,28,14,0,171,
        180,3,44,22,0,172,180,3,80,40,0,173,180,3,92,46,0,174,180,3,94,47,
        0,175,180,3,96,48,0,176,180,3,98,49,0,177,180,3,74,37,0,178,180,
        3,100,50,0,179,170,1,0,0,0,179,171,1,0,0,0,179,172,1,0,0,0,179,173,
        1,0,0,0,179,174,1,0,0,0,179,175,1,0,0,0,179,176,1,0,0,0,179,177,
        1,0,0,0,179,178,1,0,0,0,180,25,1,0,0,0,181,182,3,2,1,0,182,183,3,
        24,12,0,183,184,3,4,2,0,184,27,1,0,0,0,185,188,3,30,15,0,186,188,
        3,32,16,0,187,185,1,0,0,0,187,186,1,0,0,0,188,29,1,0,0,0,189,192,
        3,40,20,0,190,192,3,42,21,0,191,189,1,0,0,0,191,190,1,0,0,0,192,
        193,1,0,0,0,193,196,5,47,0,0,194,195,5,34,0,0,195,197,3,56,28,0,
        196,194,1,0,0,0,196,197,1,0,0,0,197,31,1,0,0,0,198,199,3,40,20,0,
        199,200,5,47,0,0,200,201,5,44,0,0,201,202,3,38,19,0,202,205,5,45,
        0,0,203,204,5,34,0,0,204,206,3,56,28,0,205,203,1,0,0,0,205,206,1,
        0,0,0,206,33,1,0,0,0,207,208,5,44,0,0,208,209,3,36,18,0,209,210,
        5,45,0,0,210,35,1,0,0,0,211,212,3,56,28,0,212,213,5,46,0,0,213,214,
        3,36,18,0,214,217,1,0,0,0,215,217,3,56,28,0,216,211,1,0,0,0,216,
        215,1,0,0,0,217,37,1,0,0,0,218,219,5,1,0,0,219,220,5,46,0,0,220,
        223,3,38,19,0,221,223,5,1,0,0,222,218,1,0,0,0,222,221,1,0,0,0,223,
        39,1,0,0,0,224,225,7,0,0,0,225,41,1,0,0,0,226,227,7,1,0,0,227,43,
        1,0,0,0,228,229,3,46,23,0,229,230,5,34,0,0,230,231,3,56,28,0,231,
        45,1,0,0,0,232,235,5,47,0,0,233,235,3,50,25,0,234,232,1,0,0,0,234,
        233,1,0,0,0,235,47,1,0,0,0,236,239,3,50,25,0,237,239,3,52,26,0,238,
        236,1,0,0,0,238,237,1,0,0,0,239,49,1,0,0,0,240,241,5,47,0,0,241,
        242,5,44,0,0,242,243,3,54,27,0,243,244,5,45,0,0,244,51,1,0,0,0,245,
        246,3,74,37,0,246,247,5,44,0,0,247,248,3,54,27,0,248,249,5,45,0,
        0,249,53,1,0,0,0,250,251,3,56,28,0,251,252,5,46,0,0,252,253,3,54,
        27,0,253,256,1,0,0,0,254,256,3,56,28,0,255,250,1,0,0,0,255,254,1,
        0,0,0,256,55,1,0,0,0,257,258,3,58,29,0,258,259,5,40,0,0,259,260,
        3,58,29,0,260,263,1,0,0,0,261,263,3,58,29,0,262,257,1,0,0,0,262,
        261,1,0,0,0,263,57,1,0,0,0,264,265,3,60,30,0,265,266,7,2,0,0,266,
        267,3,60,30,0,267,270,1,0,0,0,268,270,3,60,30,0,269,264,1,0,0,0,
        269,268,1,0,0,0,270,59,1,0,0,0,271,272,6,30,-1,0,272,273,3,62,31,
        0,273,279,1,0,0,0,274,275,10,2,0,0,275,276,7,3,0,0,276,278,3,62,
        31,0,277,274,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,
        0,0,280,61,1,0,0,0,281,279,1,0,0,0,282,283,6,31,-1,0,283,284,3,64,
        32,0,284,290,1,0,0,0,285,286,10,2,0,0,286,287,7,4,0,0,287,289,3,
        64,32,0,288,285,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,
        1,0,0,0,291,63,1,0,0,0,292,290,1,0,0,0,293,294,6,32,-1,0,294,295,
        3,66,33,0,295,301,1,0,0,0,296,297,10,2,0,0,297,298,7,5,0,0,298,300,
        3,66,33,0,299,296,1,0,0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,
        1,0,0,0,302,65,1,0,0,0,303,301,1,0,0,0,304,305,5,25,0,0,305,308,
        3,66,33,0,306,308,3,68,34,0,307,304,1,0,0,0,307,306,1,0,0,0,308,
        67,1,0,0,0,309,310,5,29,0,0,310,313,3,68,34,0,311,313,3,70,35,0,
        312,309,1,0,0,0,312,311,1,0,0,0,313,69,1,0,0,0,314,317,3,48,24,0,
        315,317,3,72,36,0,316,314,1,0,0,0,316,315,1,0,0,0,317,71,1,0,0,0,
        318,329,5,1,0,0,319,329,5,2,0,0,320,329,5,3,0,0,321,329,5,47,0,0,
        322,329,3,74,37,0,323,324,5,42,0,0,324,325,3,56,28,0,325,326,5,43,
        0,0,326,329,1,0,0,0,327,329,3,34,17,0,328,318,1,0,0,0,328,319,1,
        0,0,0,328,320,1,0,0,0,328,321,1,0,0,0,328,322,1,0,0,0,328,323,1,
        0,0,0,328,327,1,0,0,0,329,73,1,0,0,0,330,331,5,47,0,0,331,332,5,
        42,0,0,332,333,3,76,38,0,333,334,5,43,0,0,334,75,1,0,0,0,335,338,
        3,78,39,0,336,338,1,0,0,0,337,335,1,0,0,0,337,336,1,0,0,0,338,77,
        1,0,0,0,339,340,3,56,28,0,340,341,5,46,0,0,341,342,3,78,39,0,342,
        345,1,0,0,0,343,345,3,56,28,0,344,339,1,0,0,0,344,343,1,0,0,0,345,
        79,1,0,0,0,346,347,5,20,0,0,347,348,3,56,28,0,348,349,3,2,1,0,349,
        350,3,24,12,0,350,351,3,82,41,0,351,352,3,88,44,0,352,81,1,0,0,0,
        353,354,3,4,2,0,354,355,3,84,42,0,355,358,1,0,0,0,356,358,1,0,0,
        0,357,353,1,0,0,0,357,356,1,0,0,0,358,83,1,0,0,0,359,360,3,86,43,
        0,360,361,3,4,2,0,361,362,3,84,42,0,362,365,1,0,0,0,363,365,3,86,
        43,0,364,359,1,0,0,0,364,363,1,0,0,0,365,85,1,0,0,0,366,367,5,22,
        0,0,367,368,3,56,28,0,368,369,3,2,1,0,369,370,3,24,12,0,370,87,1,
        0,0,0,371,372,3,4,2,0,372,373,3,90,45,0,373,376,1,0,0,0,374,376,
        1,0,0,0,375,371,1,0,0,0,375,374,1,0,0,0,376,89,1,0,0,0,377,378,5,
        21,0,0,378,379,3,2,1,0,379,380,3,24,12,0,380,91,1,0,0,0,381,382,
        5,15,0,0,382,383,5,47,0,0,383,384,5,16,0,0,384,385,3,56,28,0,385,
        386,5,17,0,0,386,387,3,56,28,0,387,388,3,2,1,0,388,389,3,24,12,0,
        389,93,1,0,0,0,390,391,5,18,0,0,391,95,1,0,0,0,392,393,5,19,0,0,
        393,97,1,0,0,0,394,396,5,11,0,0,395,397,3,56,28,0,396,395,1,0,0,
        0,396,397,1,0,0,0,397,99,1,0,0,0,398,399,5,23,0,0,399,400,3,4,2,
        0,400,401,3,102,51,0,401,402,5,24,0,0,402,101,1,0,0,0,403,406,3,
        104,52,0,404,406,1,0,0,0,405,403,1,0,0,0,405,404,1,0,0,0,406,103,
        1,0,0,0,407,408,3,26,13,0,408,409,3,104,52,0,409,412,1,0,0,0,410,
        412,3,26,13,0,411,407,1,0,0,0,411,410,1,0,0,0,412,105,1,0,0,0,36,
        111,116,122,126,142,146,153,160,168,179,187,191,196,205,216,222,
        234,238,255,262,269,279,290,301,307,312,316,328,337,344,357,364,
        375,396,405,411
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "NUMLIT", "BOOLLIT", "STRINGLIT", "ILLEGAL_ESCAPE", 
                      "UNCLOSED_STRING", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", 
                      "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", "ASSIGNOP", 
                      "DIFFOP", "LESS", "LESSEQ", "LARGER", "LARGEREQ", 
                      "DOT", "STRCOMPARE", "LB", "RB", "LP", "RP", "COMMA", 
                      "IDENTIFIER", "COMMENT", "NEWLINE", "WS", "ERROR_CHAR" ]

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
    RULE_stmt = 12
    RULE_standalone_stmt = 13
    RULE_vardecl = 14
    RULE_normaldecl = 15
    RULE_arraydecl = 16
    RULE_arrayvalue = 17
    RULE_array_value_list = 18
    RULE_dimensions = 19
    RULE_normaltype = 20
    RULE_implicittype = 21
    RULE_assign_stmt = 22
    RULE_lhs = 23
    RULE_indexexp = 24
    RULE_scalar_index_exp = 25
    RULE_funccal_index_exp = 26
    RULE_index_operators = 27
    RULE_exp = 28
    RULE_exp2 = 29
    RULE_exp3 = 30
    RULE_exp4 = 31
    RULE_exp5 = 32
    RULE_exp6 = 33
    RULE_exp7 = 34
    RULE_exp8 = 35
    RULE_exp9 = 36
    RULE_funccall_stmt = 37
    RULE_explist = 38
    RULE_expprime = 39
    RULE_if_stmt = 40
    RULE_elif_stmt_list = 41
    RULE_elif_stmt_prime = 42
    RULE_elif_stmt = 43
    RULE_else_stmt = 44
    RULE_else_stmt_prime = 45
    RULE_for_stmt = 46
    RULE_break_stmt = 47
    RULE_continue_stmt = 48
    RULE_return_stmt = 49
    RULE_block_stmt = 50
    RULE_stmtlist = 51
    RULE_stmtprime = 52

    ruleNames =  [ "program", "newline_list", "newline_prime", "decllist", 
                   "decl", "var_init", "func", "param", "scala_param", "paramlist", 
                   "paramprime", "option", "stmt", "standalone_stmt", "vardecl", 
                   "normaldecl", "arraydecl", "arrayvalue", "array_value_list", 
                   "dimensions", "normaltype", "implicittype", "assign_stmt", 
                   "lhs", "indexexp", "scalar_index_exp", "funccal_index_exp", 
                   "index_operators", "exp", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "funccall_stmt", "explist", 
                   "expprime", "if_stmt", "elif_stmt_list", "elif_stmt_prime", 
                   "elif_stmt", "else_stmt", "else_stmt_prime", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "block_stmt", 
                   "stmtlist", "stmtprime" ]

    EOF = Token.EOF
    NUMLIT=1
    BOOLLIT=2
    STRINGLIT=3
    ILLEGAL_ESCAPE=4
    UNCLOSED_STRING=5
    TRUE=6
    FALSE=7
    NUMBER=8
    BOOL=9
    STRING=10
    RETURN=11
    VAR=12
    DYNAMIC=13
    FUNC=14
    FOR=15
    UNTIL=16
    BY=17
    BREAK=18
    CONTINUE=19
    IF=20
    ELSE=21
    ELIF=22
    BEGIN=23
    END=24
    NOT=25
    AND=26
    OR=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    DIVOP=31
    MODOP=32
    EQUALOP=33
    ASSIGNOP=34
    DIFFOP=35
    LESS=36
    LESSEQ=37
    LARGER=38
    LARGEREQ=39
    DOT=40
    STRCOMPARE=41
    LB=42
    RB=43
    LP=44
    RP=45
    COMMA=46
    IDENTIFIER=47
    COMMENT=48
    NEWLINE=49
    WS=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.decllist()
            self.state = 107
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




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newline_list)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.newline_prime()
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 23, 47]:
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




    def newline_prime(self):

        localctx = ZCodeParser.Newline_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newline_prime)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(ZCodeParser.NEWLINE)
                self.state = 114
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
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




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decllist)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.decl()
                self.state = 119
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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




    def var_init(self):

        localctx = ZCodeParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.newline_list()
            self.state = 129
            self.vardecl()
            self.state = 130
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


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.newline_list()
            self.state = 133
            self.match(ZCodeParser.FUNC)
            self.state = 134
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 135
            self.match(ZCodeParser.LB)
            self.state = 136
            self.paramlist()
            self.state = 137
            self.match(ZCodeParser.RB)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 138
                self.newline_list()
                self.state = 139
                self.option()
                pass

            elif la_ == 2:
                self.state = 141
                self.newline_prime()
                pass


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




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.scala_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
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




    def scala_param(self):

        localctx = ZCodeParser.Scala_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scala_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.normaltype()
            self.state = 149
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




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramlist)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.paramprime()
                pass
            elif token in [43]:
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




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramprime)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.param()
                self.state = 156
                self.match(ZCodeParser.COMMA)
                self.state = 157
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_option




    def option(self):

        localctx = ZCodeParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_option)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.return_stmt()
                self.state = 163
                self.newline_prime()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.block_stmt()
                self.state = 166
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




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 174
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 175
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 176
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 177
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 178
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




    def standalone_stmt(self):

        localctx = ZCodeParser.Standalone_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_standalone_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.newline_list()
            self.state = 182
            self.stmt()
            self.state = 183
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




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 185
                self.normaldecl()
                pass

            elif la_ == 2:
                self.state = 186
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




    def normaldecl(self):

        localctx = ZCodeParser.NormaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_normaldecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.state = 189
                self.normaltype()
                pass
            elif token in [12, 13]:
                self.state = 190
                self.implicittype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 194
                self.match(ZCodeParser.ASSIGNOP)
                self.state = 195
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

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.normaltype()
            self.state = 199
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 200
            self.match(ZCodeParser.LP)
            self.state = 201
            self.dimensions()
            self.state = 202
            self.match(ZCodeParser.RP)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 203
                self.match(ZCodeParser.ASSIGNOP)
                self.state = 204
                self.exp()


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




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.LP)
            self.state = 208
            self.array_value_list()
            self.state = 209
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




    def array_value_list(self):

        localctx = ZCodeParser.Array_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_value_list)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.exp()
                self.state = 212
                self.match(ZCodeParser.COMMA)
                self.state = 213
                self.array_value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
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




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dimensions)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ZCodeParser.NUMLIT)
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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




    def normaltype(self):

        localctx = ZCodeParser.NormaltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_normaltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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




    def implicittype(self):

        localctx = ZCodeParser.ImplicittypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_implicittype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.lhs()
            self.state = 229
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 230
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




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lhs)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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




    def indexexp(self):

        localctx = ZCodeParser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_indexexp)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.scalar_index_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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




    def scalar_index_exp(self):

        localctx = ZCodeParser.Scalar_index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_scalar_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 241
            self.match(ZCodeParser.LP)
            self.state = 242
            self.index_operators()
            self.state = 243
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




    def funccal_index_exp(self):

        localctx = ZCodeParser.Funccal_index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funccal_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.funccall_stmt()
            self.state = 246
            self.match(ZCodeParser.LP)
            self.state = 247
            self.index_operators()
            self.state = 248
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




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_operators)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.exp()
                self.state = 251
                self.match(ZCodeParser.COMMA)
                self.state = 252
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
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




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.exp2()
                self.state = 258
                self.match(ZCodeParser.DOT)
                self.state = 259
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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




    def exp2(self):

        localctx = ZCodeParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.exp3(0)
                self.state = 265
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3272765079552) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 276
                    self.exp4(0) 
                self.state = 281
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



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 287
                    self.exp5(0) 
                self.state = 292
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



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 298
                    self.exp6() 
                self.state = 303
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




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp6)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(ZCodeParser.NOT)
                self.state = 305
                self.exp6()
                pass
            elif token in [1, 2, 3, 29, 42, 44, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
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




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp7)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(ZCodeParser.SUBOP)
                self.state = 310
                self.exp7()
                pass
            elif token in [1, 2, 3, 42, 44, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
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




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp8)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.indexexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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




    def exp9(self):

        localctx = ZCodeParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp9)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 322
                self.funccall_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 323
                self.match(ZCodeParser.LB)
                self.state = 324
                self.exp()
                self.state = 325
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 327
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_funccall_stmt




    def funccall_stmt(self):

        localctx = ZCodeParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 331
            self.match(ZCodeParser.LB)
            self.state = 332
            self.explist()
            self.state = 333
            self.match(ZCodeParser.RB)
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




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_explist)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 25, 29, 42, 44, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expprime()
                pass
            elif token in [43]:
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




    def expprime(self):

        localctx = ZCodeParser.ExpprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expprime)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.exp()
                self.state = 340
                self.match(ZCodeParser.COMMA)
                self.state = 341
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZCodeParser.IF)
            self.state = 347
            self.exp()
            self.state = 348
            self.newline_list()
            self.state = 349
            self.stmt()
            self.state = 350
            self.elif_stmt_list()
            self.state = 351
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




    def elif_stmt_list(self):

        localctx = ZCodeParser.Elif_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elif_stmt_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.newline_prime()
                self.state = 354
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




    def elif_stmt_prime(self):

        localctx = ZCodeParser.Elif_stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elif_stmt_prime)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.elif_stmt()
                self.state = 360
                self.newline_prime()
                self.state = 361
                self.elif_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.ELIF)
            self.state = 367
            self.exp()
            self.state = 368
            self.newline_list()
            self.state = 369
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




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_else_stmt)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.newline_prime()
                self.state = 372
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




    def else_stmt_prime(self):

        localctx = ZCodeParser.Else_stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_stmt_prime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(ZCodeParser.ELSE)
            self.state = 378
            self.newline_list()
            self.state = 379
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




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.FOR)
            self.state = 382
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 383
            self.match(ZCodeParser.UNTIL)
            self.state = 384
            self.exp()
            self.state = 385
            self.match(ZCodeParser.BY)
            self.state = 386
            self.exp()
            self.state = 387
            self.newline_list()
            self.state = 388
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




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ZCodeParser.RETURN)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 162728291336206) != 0):
                self.state = 395
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

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(ZCodeParser.BEGIN)
            self.state = 399
            self.newline_prime()
            self.state = 400
            self.stmtlist()
            self.state = 401
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




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmtlist)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 23, 47, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.stmtprime()
                pass
            elif token in [24]:
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




    def stmtprime(self):

        localctx = ZCodeParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmtprime)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.standalone_stmt()
                self.state = 408
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.standalone_stmt()
                pass


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
        self._predicates[30] = self.exp3_sempred
        self._predicates[31] = self.exp4_sempred
        self._predicates[32] = self.exp5_sempred
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
         





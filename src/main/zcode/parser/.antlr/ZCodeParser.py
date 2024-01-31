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
        4,1,57,477,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,1,0,1,0,1,0,1,1,1,1,3,1,128,8,1,1,2,1,2,1,2,3,2,133,
        8,2,1,3,1,3,1,3,1,3,3,3,139,8,3,1,4,1,4,3,4,143,8,4,1,5,1,5,1,5,
        1,5,3,5,149,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,3,7,164,8,7,1,8,1,8,1,8,1,9,1,9,3,9,171,8,9,1,10,1,10,1,10,1,
        10,1,10,3,10,178,8,10,1,11,1,11,3,11,182,8,11,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,190,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,201,8,13,1,14,1,14,1,14,1,14,1,15,1,15,3,15,209,8,15,1,
        16,1,16,3,16,213,8,16,1,17,1,17,1,17,1,17,1,17,3,17,220,8,17,1,18,
        1,18,3,18,224,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,3,20,238,8,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,3,24,252,8,24,1,25,1,25,3,25,256,8,25,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,3,26,267,8,26,1,27,1,
        27,1,27,1,27,1,27,3,27,274,8,27,1,28,1,28,1,28,1,28,1,28,3,28,281,
        8,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,289,8,29,10,29,12,29,292,
        9,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,300,8,30,10,30,12,30,303,
        9,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,311,8,31,10,31,12,31,314,
        9,31,1,32,1,32,1,32,3,32,319,8,32,1,33,1,33,1,33,3,33,324,8,33,1,
        34,1,34,3,34,328,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,3,35,340,8,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        37,3,37,351,8,37,1,38,1,38,1,38,1,38,1,38,1,38,3,38,359,8,38,1,39,
        1,39,3,39,363,8,39,1,40,1,40,1,40,1,40,1,40,3,40,370,8,40,1,41,1,
        41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,3,42,385,
        8,42,1,43,1,43,1,43,1,43,1,43,3,43,392,8,43,1,44,1,44,1,44,1,44,
        1,44,1,44,1,44,1,45,1,45,1,45,1,45,3,45,405,8,45,1,46,1,46,1,46,
        1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,49,
        1,49,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,1,52,3,52,434,
        8,52,1,53,1,53,1,53,1,53,3,53,440,8,53,1,54,1,54,1,54,1,54,1,54,
        1,54,3,54,448,8,54,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,56,
        1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,
        1,60,1,60,1,60,1,60,1,60,1,60,0,3,58,60,62,61,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,0,6,1,0,14,16,1,0,18,19,
        3,0,39,39,41,45,47,47,1,0,32,33,1,0,34,35,1,0,36,38,471,0,122,1,
        0,0,0,2,127,1,0,0,0,4,132,1,0,0,0,6,138,1,0,0,0,8,142,1,0,0,0,10,
        144,1,0,0,0,12,152,1,0,0,0,14,163,1,0,0,0,16,165,1,0,0,0,18,170,
        1,0,0,0,20,177,1,0,0,0,22,181,1,0,0,0,24,189,1,0,0,0,26,200,1,0,
        0,0,28,202,1,0,0,0,30,208,1,0,0,0,32,212,1,0,0,0,34,219,1,0,0,0,
        36,223,1,0,0,0,38,227,1,0,0,0,40,237,1,0,0,0,42,239,1,0,0,0,44,241,
        1,0,0,0,46,243,1,0,0,0,48,251,1,0,0,0,50,255,1,0,0,0,52,266,1,0,
        0,0,54,273,1,0,0,0,56,280,1,0,0,0,58,282,1,0,0,0,60,293,1,0,0,0,
        62,304,1,0,0,0,64,318,1,0,0,0,66,323,1,0,0,0,68,327,1,0,0,0,70,339,
        1,0,0,0,72,341,1,0,0,0,74,350,1,0,0,0,76,358,1,0,0,0,78,362,1,0,
        0,0,80,369,1,0,0,0,82,371,1,0,0,0,84,384,1,0,0,0,86,391,1,0,0,0,
        88,393,1,0,0,0,90,404,1,0,0,0,92,406,1,0,0,0,94,410,1,0,0,0,96,419,
        1,0,0,0,98,421,1,0,0,0,100,423,1,0,0,0,102,426,1,0,0,0,104,433,1,
        0,0,0,106,439,1,0,0,0,108,447,1,0,0,0,110,449,1,0,0,0,112,453,1,
        0,0,0,114,458,1,0,0,0,116,462,1,0,0,0,118,467,1,0,0,0,120,471,1,
        0,0,0,122,123,3,6,3,0,123,124,5,0,0,1,124,1,1,0,0,0,125,128,3,4,
        2,0,126,128,1,0,0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,3,1,0,0,
        0,129,130,5,55,0,0,130,133,3,4,2,0,131,133,5,55,0,0,132,129,1,0,
        0,0,132,131,1,0,0,0,133,5,1,0,0,0,134,135,3,8,4,0,135,136,3,6,3,
        0,136,139,1,0,0,0,137,139,3,8,4,0,138,134,1,0,0,0,138,137,1,0,0,
        0,139,7,1,0,0,0,140,143,3,12,6,0,141,143,3,10,5,0,142,140,1,0,0,
        0,142,141,1,0,0,0,143,9,1,0,0,0,144,145,3,2,1,0,145,148,3,30,15,
        0,146,147,5,40,0,0,147,149,3,54,27,0,148,146,1,0,0,0,148,149,1,0,
        0,0,149,150,1,0,0,0,150,151,3,4,2,0,151,11,1,0,0,0,152,153,3,2,1,
        0,153,154,5,20,0,0,154,155,5,53,0,0,155,156,5,48,0,0,156,157,3,18,
        9,0,157,158,5,49,0,0,158,159,3,2,1,0,159,160,3,22,11,0,160,13,1,
        0,0,0,161,164,3,16,8,0,162,164,3,38,19,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,15,1,0,0,0,165,166,3,42,21,0,166,167,5,53,0,0,167,17,
        1,0,0,0,168,171,3,20,10,0,169,171,1,0,0,0,170,168,1,0,0,0,170,169,
        1,0,0,0,171,19,1,0,0,0,172,173,3,14,7,0,173,174,5,52,0,0,174,175,
        3,20,10,0,175,178,1,0,0,0,176,178,3,14,7,0,177,172,1,0,0,0,177,176,
        1,0,0,0,178,21,1,0,0,0,179,182,3,24,12,0,180,182,1,0,0,0,181,179,
        1,0,0,0,181,180,1,0,0,0,182,23,1,0,0,0,183,184,3,100,50,0,184,185,
        3,4,2,0,185,190,1,0,0,0,186,187,3,102,51,0,187,188,3,4,2,0,188,190,
        1,0,0,0,189,183,1,0,0,0,189,186,1,0,0,0,190,25,1,0,0,0,191,201,3,
        30,15,0,192,201,3,46,23,0,193,201,3,82,41,0,194,201,3,94,47,0,195,
        201,3,96,48,0,196,201,3,98,49,0,197,201,3,100,50,0,198,201,3,76,
        38,0,199,201,3,102,51,0,200,191,1,0,0,0,200,192,1,0,0,0,200,193,
        1,0,0,0,200,194,1,0,0,0,200,195,1,0,0,0,200,196,1,0,0,0,200,197,
        1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,27,1,0,0,0,202,203,3,
        2,1,0,203,204,3,26,13,0,204,205,3,4,2,0,205,29,1,0,0,0,206,209,3,
        36,18,0,207,209,3,38,19,0,208,206,1,0,0,0,208,207,1,0,0,0,209,31,
        1,0,0,0,210,213,3,34,17,0,211,213,1,0,0,0,212,210,1,0,0,0,212,211,
        1,0,0,0,213,33,1,0,0,0,214,215,3,30,15,0,215,216,5,52,0,0,216,217,
        3,34,17,0,217,220,1,0,0,0,218,220,3,30,15,0,219,214,1,0,0,0,219,
        218,1,0,0,0,220,35,1,0,0,0,221,224,3,42,21,0,222,224,3,44,22,0,223,
        221,1,0,0,0,223,222,1,0,0,0,224,225,1,0,0,0,225,226,5,53,0,0,226,
        37,1,0,0,0,227,228,3,42,21,0,228,229,5,53,0,0,229,230,5,50,0,0,230,
        231,3,40,20,0,231,232,5,51,0,0,232,39,1,0,0,0,233,234,5,7,0,0,234,
        235,5,52,0,0,235,238,3,40,20,0,236,238,5,7,0,0,237,233,1,0,0,0,237,
        236,1,0,0,0,238,41,1,0,0,0,239,240,7,0,0,0,240,43,1,0,0,0,241,242,
        7,1,0,0,242,45,1,0,0,0,243,244,3,48,24,0,244,245,5,40,0,0,245,246,
        3,54,27,0,246,47,1,0,0,0,247,252,5,53,0,0,248,252,3,50,25,0,249,
        252,3,38,19,0,250,252,3,36,18,0,251,247,1,0,0,0,251,248,1,0,0,0,
        251,249,1,0,0,0,251,250,1,0,0,0,252,49,1,0,0,0,253,256,5,53,0,0,
        254,256,3,76,38,0,255,253,1,0,0,0,255,254,1,0,0,0,256,257,1,0,0,
        0,257,258,5,50,0,0,258,259,3,52,26,0,259,260,5,51,0,0,260,51,1,0,
        0,0,261,262,3,54,27,0,262,263,5,52,0,0,263,264,3,52,26,0,264,267,
        1,0,0,0,265,267,3,54,27,0,266,261,1,0,0,0,266,265,1,0,0,0,267,53,
        1,0,0,0,268,269,3,56,28,0,269,270,5,46,0,0,270,271,3,56,28,0,271,
        274,1,0,0,0,272,274,3,56,28,0,273,268,1,0,0,0,273,272,1,0,0,0,274,
        55,1,0,0,0,275,276,3,58,29,0,276,277,7,2,0,0,277,278,3,58,29,0,278,
        281,1,0,0,0,279,281,3,58,29,0,280,275,1,0,0,0,280,279,1,0,0,0,281,
        57,1,0,0,0,282,283,6,29,-1,0,283,284,3,60,30,0,284,290,1,0,0,0,285,
        286,10,2,0,0,286,287,7,3,0,0,287,289,3,60,30,0,288,285,1,0,0,0,289,
        292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,59,1,0,0,0,292,290,
        1,0,0,0,293,294,6,30,-1,0,294,295,3,62,31,0,295,301,1,0,0,0,296,
        297,10,2,0,0,297,298,7,4,0,0,298,300,3,62,31,0,299,296,1,0,0,0,300,
        303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,61,1,0,0,0,303,301,
        1,0,0,0,304,305,6,31,-1,0,305,306,3,64,32,0,306,312,1,0,0,0,307,
        308,10,2,0,0,308,309,7,5,0,0,309,311,3,64,32,0,310,307,1,0,0,0,311,
        314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,63,1,0,0,0,314,312,
        1,0,0,0,315,316,5,31,0,0,316,319,3,64,32,0,317,319,3,66,33,0,318,
        315,1,0,0,0,318,317,1,0,0,0,319,65,1,0,0,0,320,321,5,35,0,0,321,
        324,3,66,33,0,322,324,3,68,34,0,323,320,1,0,0,0,323,322,1,0,0,0,
        324,67,1,0,0,0,325,328,3,50,25,0,326,328,3,70,35,0,327,325,1,0,0,
        0,327,326,1,0,0,0,328,69,1,0,0,0,329,340,5,7,0,0,330,340,5,8,0,0,
        331,340,5,9,0,0,332,340,3,72,36,0,333,340,5,53,0,0,334,340,3,76,
        38,0,335,336,5,48,0,0,336,337,3,54,27,0,337,338,5,49,0,0,338,340,
        1,0,0,0,339,329,1,0,0,0,339,330,1,0,0,0,339,331,1,0,0,0,339,332,
        1,0,0,0,339,333,1,0,0,0,339,334,1,0,0,0,339,335,1,0,0,0,340,71,1,
        0,0,0,341,342,5,50,0,0,342,343,3,74,37,0,343,344,5,51,0,0,344,73,
        1,0,0,0,345,346,3,54,27,0,346,347,5,52,0,0,347,348,3,74,37,0,348,
        351,1,0,0,0,349,351,3,54,27,0,350,345,1,0,0,0,350,349,1,0,0,0,351,
        75,1,0,0,0,352,353,5,53,0,0,353,354,5,48,0,0,354,355,3,78,39,0,355,
        356,5,49,0,0,356,359,1,0,0,0,357,359,3,108,54,0,358,352,1,0,0,0,
        358,357,1,0,0,0,359,77,1,0,0,0,360,363,3,80,40,0,361,363,1,0,0,0,
        362,360,1,0,0,0,362,361,1,0,0,0,363,79,1,0,0,0,364,365,3,54,27,0,
        365,366,5,52,0,0,366,367,3,80,40,0,367,370,1,0,0,0,368,370,3,54,
        27,0,369,364,1,0,0,0,369,368,1,0,0,0,370,81,1,0,0,0,371,372,5,26,
        0,0,372,373,5,48,0,0,373,374,3,54,27,0,374,375,5,49,0,0,375,376,
        3,2,1,0,376,377,3,26,13,0,377,378,3,84,42,0,378,379,3,90,45,0,379,
        83,1,0,0,0,380,381,3,4,2,0,381,382,3,86,43,0,382,385,1,0,0,0,383,
        385,1,0,0,0,384,380,1,0,0,0,384,383,1,0,0,0,385,85,1,0,0,0,386,387,
        3,88,44,0,387,388,3,4,2,0,388,389,3,86,43,0,389,392,1,0,0,0,390,
        392,3,88,44,0,391,386,1,0,0,0,391,390,1,0,0,0,392,87,1,0,0,0,393,
        394,5,28,0,0,394,395,5,48,0,0,395,396,3,54,27,0,396,397,5,49,0,0,
        397,398,3,2,1,0,398,399,3,26,13,0,399,89,1,0,0,0,400,401,3,4,2,0,
        401,402,3,92,46,0,402,405,1,0,0,0,403,405,1,0,0,0,404,400,1,0,0,
        0,404,403,1,0,0,0,405,91,1,0,0,0,406,407,5,27,0,0,407,408,3,2,1,
        0,408,409,3,26,13,0,409,93,1,0,0,0,410,411,5,21,0,0,411,412,5,53,
        0,0,412,413,5,22,0,0,413,414,3,54,27,0,414,415,5,23,0,0,415,416,
        3,54,27,0,416,417,3,2,1,0,417,418,3,26,13,0,418,95,1,0,0,0,419,420,
        5,24,0,0,420,97,1,0,0,0,421,422,5,25,0,0,422,99,1,0,0,0,423,424,
        5,17,0,0,424,425,3,54,27,0,425,101,1,0,0,0,426,427,5,29,0,0,427,
        428,3,2,1,0,428,429,3,104,52,0,429,430,5,30,0,0,430,103,1,0,0,0,
        431,434,3,106,53,0,432,434,1,0,0,0,433,431,1,0,0,0,433,432,1,0,0,
        0,434,105,1,0,0,0,435,436,3,28,14,0,436,437,3,106,53,0,437,440,1,
        0,0,0,438,440,3,28,14,0,439,435,1,0,0,0,439,438,1,0,0,0,440,107,
        1,0,0,0,441,448,3,110,55,0,442,448,3,112,56,0,443,448,3,114,57,0,
        444,448,3,116,58,0,445,448,3,118,59,0,446,448,3,120,60,0,447,441,
        1,0,0,0,447,442,1,0,0,0,447,443,1,0,0,0,447,444,1,0,0,0,447,445,
        1,0,0,0,447,446,1,0,0,0,448,109,1,0,0,0,449,450,5,1,0,0,450,451,
        5,48,0,0,451,452,5,49,0,0,452,111,1,0,0,0,453,454,5,2,0,0,454,455,
        5,48,0,0,455,456,3,54,27,0,456,457,5,49,0,0,457,113,1,0,0,0,458,
        459,5,3,0,0,459,460,5,48,0,0,460,461,5,49,0,0,461,115,1,0,0,0,462,
        463,5,4,0,0,463,464,5,48,0,0,464,465,3,54,27,0,465,466,5,49,0,0,
        466,117,1,0,0,0,467,468,5,5,0,0,468,469,5,48,0,0,469,470,5,49,0,
        0,470,119,1,0,0,0,471,472,5,6,0,0,472,473,5,48,0,0,473,474,3,54,
        27,0,474,475,5,49,0,0,475,121,1,0,0,0,38,127,132,138,142,148,163,
        170,177,181,189,200,208,212,219,223,237,251,255,266,273,280,290,
        301,312,318,323,327,339,350,358,362,369,384,391,404,433,439,447
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'write'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

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
    RULE_vardecllist = 16
    RULE_declprime = 17
    RULE_normaldecl = 18
    RULE_arraydecl = 19
    RULE_dimensions = 20
    RULE_normaltype = 21
    RULE_implicittype = 22
    RULE_assign_stmt = 23
    RULE_lhs = 24
    RULE_indexexp = 25
    RULE_index_operators = 26
    RULE_exp = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_exp6 = 32
    RULE_exp7 = 33
    RULE_exp8 = 34
    RULE_exp9 = 35
    RULE_arrayvalue = 36
    RULE_array_value_list = 37
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
    RULE_write = 58
    RULE_readString = 59
    RULE_writeString = 60

    ruleNames =  [ "program", "newline_list", "newline_prime", "decllist", 
                   "decl", "var_init", "func", "param", "scala_param", "paramlist", 
                   "paramprime", "option", "optionprime", "stmt", "standalone_stmt", 
                   "vardecl", "vardecllist", "declprime", "normaldecl", 
                   "arraydecl", "dimensions", "normaltype", "implicittype", 
                   "assign_stmt", "lhs", "indexexp", "index_operators", 
                   "exp", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "arrayvalue", "array_value_list", "funccall_stmt", 
                   "explist", "expprime", "if_stmt", "elif_stmt_list", "elif_stmt_prime", 
                   "elif_stmt", "else_stmt", "else_stmt_prime", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "block_stmt", 
                   "stmtlist", "stmtprime", "io_func", "readNumber", "writeNumber", 
                   "readBool", "write", "readString", "writeString" ]

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


        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_init




    def var_init(self):

        localctx = ZCodeParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.newline_list()
            self.state = 145
            self.vardecl()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 146
                self.match(ZCodeParser.ASSIGNOP)
                self.state = 147
                self.exp()


            self.state = 150
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




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.newline_list()
            self.state = 153
            self.match(ZCodeParser.FUNC)
            self.state = 154
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 155
            self.match(ZCodeParser.LB)
            self.state = 156
            self.paramlist()
            self.state = 157
            self.match(ZCodeParser.RB)
            self.state = 158
            self.newline_list()
            self.state = 159
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




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.scala_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
            self.state = 165
            self.normaltype()
            self.state = 166
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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.paramprime()
                pass
            elif token in [49]:
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
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.param()
                self.state = 173
                self.match(ZCodeParser.COMMA)
                self.state = 174
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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




    def option(self):

        localctx = ZCodeParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_option)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.optionprime()
                pass
            elif token in [-1, 14, 15, 16, 18, 19, 20, 55]:
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




    def optionprime(self):

        localctx = ZCodeParser.OptionprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_optionprime)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.return_stmt()
                self.state = 184
                self.newline_prime()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.block_stmt()
                self.state = 187
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
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 198
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 199
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
        self.enterRule(localctx, 28, self.RULE_standalone_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.newline_list()
            self.state = 203
            self.stmt()
            self.state = 204
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
        self.enterRule(localctx, 30, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 206
                self.normaldecl()
                pass

            elif la_ == 2:
                self.state = 207
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declprime(self):
            return self.getTypedRuleContext(ZCodeParser.DeclprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecllist




    def vardecllist(self):

        localctx = ZCodeParser.VardecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vardecllist)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.declprime()
                pass
            elif token in [-1]:
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

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def declprime(self):
            return self.getTypedRuleContext(ZCodeParser.DeclprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declprime




    def declprime(self):

        localctx = ZCodeParser.DeclprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declprime)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.vardecl()
                self.state = 215
                self.match(ZCodeParser.COMMA)
                self.state = 216
                self.declprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.vardecl()
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




    def normaldecl(self):

        localctx = ZCodeParser.NormaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_normaldecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16]:
                self.state = 221
                self.normaltype()
                pass
            elif token in [18, 19]:
                self.state = 222
                self.implicittype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 225
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




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.normaltype()
            self.state = 228
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 229
            self.match(ZCodeParser.LP)
            self.state = 230
            self.dimensions()
            self.state = 231
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




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dimensions)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.NUMLIT)
                self.state = 234
                self.match(ZCodeParser.COMMA)
                self.state = 235
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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
        self.enterRule(localctx, 42, self.RULE_normaltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_implicittype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
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
        self.enterRule(localctx, 46, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.lhs()
            self.state = 244
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 245
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




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.indexexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
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




    def indexexp(self):

        localctx = ZCodeParser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_indexexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 254
                self.funccall_stmt()
                pass


            self.state = 257
            self.match(ZCodeParser.LP)
            self.state = 258
            self.index_operators()
            self.state = 259
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
        self.enterRule(localctx, 52, self.RULE_index_operators)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.exp()
                self.state = 262
                self.match(ZCodeParser.COMMA)
                self.state = 263
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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
        self.enterRule(localctx, 54, self.RULE_exp)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.exp2()
                self.state = 269
                self.match(ZCodeParser.DOT)
                self.state = 270
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
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
        self.enterRule(localctx, 56, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.exp3(0)
                self.state = 276
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 209456965091328) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    _la = self._input.LA(1)
                    if not(_la==32 or _la==33):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 287
                    self.exp4(0) 
                self.state = 292
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    _la = self._input.LA(1)
                    if not(_la==34 or _la==35):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 298
                    self.exp5(0) 
                self.state = 303
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.exp6() 
                self.state = 314
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
        self.enterRule(localctx, 64, self.RULE_exp6)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(ZCodeParser.NOT)
                self.state = 316
                self.exp6()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 35, 48, 50, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
        self.enterRule(localctx, 66, self.RULE_exp7)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(ZCodeParser.SUBOP)
                self.state = 321
                self.exp7()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 48, 50, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
        self.enterRule(localctx, 68, self.RULE_exp8)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.indexexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
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


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp9




    def exp9(self):

        localctx = ZCodeParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp9)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 332
                self.arrayvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 333
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 334
                self.funccall_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 335
                self.match(ZCodeParser.LB)
                self.state = 336
                self.exp()
                self.state = 337
                self.match(ZCodeParser.RB)
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

        def array_value_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.LP)
            self.state = 342
            self.array_value_list()
            self.state = 343
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
        self.enterRule(localctx, 74, self.RULE_array_value_list)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.exp()
                self.state = 346
                self.match(ZCodeParser.COMMA)
                self.state = 347
                self.array_value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.exp()
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




    def funccall_stmt(self):

        localctx = ZCodeParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_funccall_stmt)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 353
                self.match(ZCodeParser.LB)
                self.state = 354
                self.explist()
                self.state = 355
                self.match(ZCodeParser.RB)
                pass
            elif token in [1, 2, 3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_explist)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 31, 35, 48, 50, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.expprime()
                pass
            elif token in [49]:
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
        self.enterRule(localctx, 80, self.RULE_expprime)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.exp()
                self.state = 365
                self.match(ZCodeParser.COMMA)
                self.state = 366
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

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
        self.enterRule(localctx, 82, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(ZCodeParser.IF)
            self.state = 372
            self.match(ZCodeParser.LB)
            self.state = 373
            self.exp()
            self.state = 374
            self.match(ZCodeParser.RB)
            self.state = 375
            self.newline_list()
            self.state = 376
            self.stmt()
            self.state = 377
            self.elif_stmt_list()
            self.state = 378
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
        self.enterRule(localctx, 84, self.RULE_elif_stmt_list)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.newline_prime()
                self.state = 381
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
        self.enterRule(localctx, 86, self.RULE_elif_stmt_prime)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.elif_stmt()
                self.state = 387
                self.newline_prime()
                self.state = 388
                self.elif_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ZCodeParser.ELIF)
            self.state = 394
            self.match(ZCodeParser.LB)
            self.state = 395
            self.exp()
            self.state = 396
            self.match(ZCodeParser.RB)
            self.state = 397
            self.newline_list()
            self.state = 398
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
        self.enterRule(localctx, 90, self.RULE_else_stmt)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.newline_prime()
                self.state = 401
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
        self.enterRule(localctx, 92, self.RULE_else_stmt_prime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(ZCodeParser.ELSE)
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
        self.enterRule(localctx, 94, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(ZCodeParser.FOR)
            self.state = 411
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 412
            self.match(ZCodeParser.UNTIL)
            self.state = 413
            self.exp()
            self.state = 414
            self.match(ZCodeParser.BY)
            self.state = 415
            self.exp()
            self.state = 416
            self.newline_list()
            self.state = 417
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
        self.enterRule(localctx, 96, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
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
        self.enterRule(localctx, 98, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
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
        self.enterRule(localctx, 100, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ZCodeParser.RETURN)
            self.state = 424
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




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(ZCodeParser.BEGIN)
            self.state = 427
            self.newline_list()
            self.state = 428
            self.stmtlist()
            self.state = 429
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
        self.enterRule(localctx, 104, self.RULE_stmtlist)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 18, 19, 21, 24, 25, 26, 29, 53, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.stmtprime()
                pass
            elif token in [30]:
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
        self.enterRule(localctx, 106, self.RULE_stmtprime)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.standalone_stmt()
                self.state = 436
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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




    def io_func(self):

        localctx = ZCodeParser.Io_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_io_func)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.readNumber()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.writeNumber()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.readBool()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.write()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 445
                self.readString()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 446
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




    def readNumber(self):

        localctx = ZCodeParser.ReadNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(ZCodeParser.T__0)
            self.state = 450
            self.match(ZCodeParser.LB)
            self.state = 451
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




    def writeNumber(self):

        localctx = ZCodeParser.WriteNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(ZCodeParser.T__1)
            self.state = 454
            self.match(ZCodeParser.LB)
            self.state = 455
            self.exp()
            self.state = 456
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




    def readBool(self):

        localctx = ZCodeParser.ReadBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(ZCodeParser.T__2)
            self.state = 459
            self.match(ZCodeParser.LB)
            self.state = 460
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




    def write(self):

        localctx = ZCodeParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.T__3)
            self.state = 463
            self.match(ZCodeParser.LB)
            self.state = 464
            self.exp()
            self.state = 465
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




    def readString(self):

        localctx = ZCodeParser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(ZCodeParser.T__4)
            self.state = 468
            self.match(ZCodeParser.LB)
            self.state = 469
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




    def writeString(self):

        localctx = ZCodeParser.WriteStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ZCodeParser.T__5)
            self.state = 472
            self.match(ZCodeParser.LB)
            self.state = 473
            self.exp()
            self.state = 474
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
        self._predicates[29] = self.exp3_sempred
        self._predicates[30] = self.exp4_sempred
        self._predicates[31] = self.exp5_sempred
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
         





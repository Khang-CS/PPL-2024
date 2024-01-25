grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: funclist EOF;
// RECOGNIZER - PARSER //

funclist: func funclist | func;

func: FUNC IDENTIFIER LB decllist RB option;

option: optionprime |;
optionprime: (return_stmt NEWLINE) | (block_stmt NEWLINE);

decllist: declprime |;

declprime: decl COMMA declprime | decl;

//stmt list
stmt:
	decl
	| assign_stmt
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| funccall_stmt
	| block_stmt;
//

standalone_stmt: stmt NEWLINE;

decl: (normaldecl | arraydecl);

normaldecl: (normaltype | implicittype) IDENTIFIER;

arraydecl: normaltype IDENTIFIER LP dimensions RP;

dimensions: NUMLIT COMMA dimensions | NUMLIT;

normaltype: NUMBER | STRING | BOOL;

implicittype: DYNAMIC | VAR;

//assignment statement
assign_stmt: lhs ASSIGNOP exp;
//

lhs: IDENTIFIER | indexexp | arraydecl | normaldecl;

indexexp: (IDENTIFIER | funccall_stmt) LP index_operators RP;

index_operators: exp COMMA index_operators | exp;

exp: exp2 DOT exp2 | exp2;

exp2:
	exp3 (
		EQUALOP
		| STRCOMPARE
		| DIFFOP
		| LESS
		| LARGER
		| LESSEQ
		| LARGEREQ
	) exp3
	| exp3;

exp3: exp3 (AND | OR) exp4 | exp4;

exp4: exp4 (ADDOP | SUBOP) exp5 | exp5;

exp5: exp5 (MULOP | DIVOP | MODOP) exp6 | exp6;

exp6: NOT exp7 | exp7;

exp7: SUBOP exp8 | exp8;

exp8: indexexp | exp9;

exp9:
	NUMLIT
	| BOOLLIT
	| STRINGLIT
	| arrayvalue
	| IDENTIFIER
	| funccall_stmt;

arrayvalue: LP literallist RP;
literallist: exp9 COMMA literallist | exp9;

// function call statement
funccall_stmt: (IDENTIFIER LB explist RB) | io_func;
//

explist: expprime |;

expprime: exp COMMA expprime | exp;
//

// if statement
if_stmt: IF exp stmt (elif_list)? (NEWLINE ELSE stmt)?;

elif_list: NEWLINE elif_stmt elif_list | NEWLINE elif_stmt;

elif_stmt: ELIF exp stmt;
//

//for statement
for_stmt: FOR IDENTIFIER UNTIL exp BY exp NEWLINE stmt;
//

//break statement
break_stmt: BREAK;
// 

//continue statement
continue_stmt: CONTINUE;
// 

//return statement
return_stmt: RETURN exp;
//

//block statement
block_stmt: BEGIN NEWLINE stmtlist END;
stmtlist: stmtprime |;
stmtprime: standalone_stmt stmtprime | standalone_stmt;
//

// IO
io_func:
	readNumber
	| writeNumber
	| readBool
	| write
	| readString
	| writeString;

readNumber: 'readNumber' LB RB;

writeNumber: 'writeNumber' LB exp RB;

readBool: 'readBool' LB RB;

write: 'write' LB exp RB;

readString: 'readString' LB RB;

writeString: 'writeString' LB exp RB;
//

// arraydecl: scalatype IDENTIFIER LP dimensions RP;

// dimensions: NUMLIT COMMA dimensions | NUMLIT;

// arrayvalue: LP literallist RP; literallist: literal COMMA literallist | literal; literal: NUMLIT
// | STRINGLIT | BOOLLIT | arrayvalue;

// assignstmt: lhs ASSIGNOP exp;

// lhs: scaladecl | arraydecl;

// exp: literal;

// LEXICAL ANALYSIS 

// LITERALS

// 1. Number
NUMLIT: INTPART DECPART? EXPONENTPART?;
fragment INTPART: '0' | [1-9] [0-9]*;
fragment DECPART: '.' [0-9]*;
fragment EXPONENTPART: 'e' ('-' | '+')? [1-9] [0-9]*;

// 2. Boolean literal
BOOLLIT: TRUE | FALSE;

// 3. String
STRINGLIT:
	["] (ESCAPE | DQ | ~["\r\n])* ["] {self.text = self.text[1:len(self.text)-1]};
fragment ESCAPE:
	'\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\');

fragment DQ: '\'"';
//

// KEYWORDS
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not'; // OPERATOR not
AND: 'and'; // OPERATOR and
OR: 'or'; // OPERATOR or
//

// OPERATORS
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
EQUALOP: '=';
ASSIGNOP: '<-';
DIFFOP: '!=';
LESS: '<';
LESSEQ: '<=';
LARGER: '>';
LARGEREQ: '>=';
DOT: '...';
STRCOMPARE: '==';
//

// SEPARATORS
LB: '(';
RB: ')';
LP: '[';
RP: ']';
COMMA: ',';
SEMI: ';';
//

// IDENTIFIER
IDENTIFIER: [A-Za-z_] [A-Za-z0-9_]*;

COMMENT: '##' ~[\r\n]* '\r'? ('\n' | EOF) -> skip;

NEWLINE: ('\r'? '\n')+; //NEWLINE

WS: [ \t\r]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
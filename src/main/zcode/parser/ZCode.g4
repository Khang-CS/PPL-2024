grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decllist EOF;
// RECOGNIZER - PARSER //

//new line declaration
newline_list: newline_prime |;

newline_prime: NEWLINE newline_prime | NEWLINE;
//

decllist: decl decllist | decl;

decl: func | var_init;

var_init: newline_list vardecl newline_prime;

func:
	newline_list FUNC IDENTIFIER LB paramlist RB (
		newline_list option
		| newline_prime
	);

param: scala_param | arraydecl;

scala_param: normaltype IDENTIFIER;

paramlist: paramprime |;

paramprime: param COMMA paramprime | param;

option: return_stmt newline_prime | block_stmt newline_prime;

//stmt list
stmt:
	vardecl
	| assign_stmt
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| funccall_stmt
	| block_stmt;
//

standalone_stmt: newline_list stmt newline_prime;

vardecl: (normaldecl | arraydecl);

normaldecl: (normaltype | implicittype) IDENTIFIER (ASSIGNOP exp)?;

arraydecl:
	normaltype IDENTIFIER LP dimensions RP (ASSIGNOP exp)?;

arrayvalue: LP array_value_list RP;
array_value_list: exp COMMA array_value_list | exp;

dimensions: NUMLIT COMMA dimensions | NUMLIT;

normaltype: NUMBER | STRING | BOOL;

implicittype: DYNAMIC | VAR;

//assignment statement
assign_stmt: lhs ASSIGNOP exp;
//

lhs: IDENTIFIER | scalar_index_exp;

indexexp: scalar_index_exp | funccal_index_exp;

scalar_index_exp: IDENTIFIER LP index_operators RP;
funccal_index_exp: funccall_stmt LP index_operators RP;

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

exp6: NOT exp6 | exp7;

exp7: SUBOP exp7 | exp8;

exp8: indexexp | exp9;

exp9:
	NUMLIT
	| BOOLLIT
	| STRINGLIT
	| IDENTIFIER
	| funccall_stmt
	| LB exp RB
	| arrayvalue;

// function call statement
funccall_stmt: (IDENTIFIER LB explist RB);
//

explist: expprime |;

expprime: exp COMMA expprime | exp;
//

// if statement
if_stmt:
	IF LB exp RB newline_list stmt elif_stmt_list else_stmt;

elif_stmt_list: newline_prime elif_stmt_prime |;

elif_stmt_prime:
	elif_stmt newline_prime elif_stmt_prime
	| elif_stmt;

elif_stmt: ELIF LB exp RB newline_list stmt;

else_stmt: newline_prime else_stmt_prime |;

else_stmt_prime: ELSE newline_list stmt;

//

//for statement
for_stmt: FOR IDENTIFIER UNTIL exp BY exp newline_list stmt;
//

//break statement
break_stmt: BREAK;
// 

//continue statement
continue_stmt: CONTINUE;
// 

//return statement
return_stmt: RETURN exp?;
//

//block statement
block_stmt: BEGIN newline_prime stmtlist END;
stmtlist: stmtprime |;
stmtprime: standalone_stmt stmtprime | standalone_stmt;

// LEXICAL ANALYSIS 

// LITERALS

// 1. Number
NUMLIT: INTPART DECPART? EXPONENTPART?;
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPONENTPART: ('e' | 'E') ('-' | '+')? [1-9] [0-9]*;

// 2. Boolean literal
BOOLLIT: TRUE | FALSE;

// 3. String

// STRING ERROR

STRINGLIT: (
		'""' // Case 1: There is no character
		| '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\n\\"])* (
			'\'"'
			| '\\' [btnfr'\\]
			| ~[\r\n\\"']
		) '"'
	) {self.text = self.text[1:-1]};
// Case 2: There is at least 1 character -> The single quote can not stand at the end of string

//

ILLEGAL_ESCAPE: (
		'"' ('\'"' | '\\' [bfrnt\\'] | ~[\n\r\\"])* (
			'\\' (~[bfrnt'\\])
		)
	) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSED_STRING: ('"' ('\'"' | '\\' [btnfr'\\] | ~[\r\n\\"])*) {self.text = self.text[1:]; raise UncloseString(self.text)
		};

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
NOT: 'not';
// OPERATOR not
AND: 'and';
// OPERATOR and
OR: 'or';
// OPERATOR or

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
//

// IDENTIFIER
IDENTIFIER: [A-Za-z_] [A-Za-z0-9_]*;

COMMENT: '##' ~[\r\n]* -> skip;

NEWLINE: '\n';
//NEWLINE

WS: [ \t\r]+ -> skip;
// skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
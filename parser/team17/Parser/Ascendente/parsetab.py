
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS ACOS ACOSD ACOSH ADD ALL ALTER AND ANDBB ANY AS ASC ASIN ASIND ASINH ATAN ATAN2 ATAN2D ATAND ATANH AVG BETWEEN BIGINT BOOLEAN BY CADENA CADENADOBLE CASE CBRT CEIL CEILING CHAR CHARACTER CHECK COLUMN COMA CONSTRAINT CONVERT CORDER CORIZQ COS COSD COSH COT COTD COUNT CREATE DATABASE DATABASES DATE DAY DECIMAL DECODE DEGREES DELETE DESC DISTINCT DISTINTO DIV DIVISION DOBPTS DOSPTS DOUBLE DROP ENCODE END ENTERO ENUM EXCEPT EXISTS EXP FACTORIAL FALSE FIRST FLOAT FLOOR FOREIGN FROM FULL GCD GET_BYTE GREATEST GROUP HAVING HOUR ID IGUAL IGUALQUE ILIKE IN INHERITS INNER INSERT INT INTEGER INTERSECT INTERVAL INTO IS ISNULL JOIN KEY LAST LCM LEAST LEFT LENGTH LIKE LIMIT LN LOG LOG10 MAS MAX MAYORIG MAYORQUE MD5 MENORIG MENORQUE MENOS MIN MINUTE MIN_SCALE MOD MODULO MONEY MULTI NOT NOTBB NOTNULL NULLS NUMERAL NUMERIC OFFSET ON OR ORBB OUTER OWNER PARDER PARIZQ PI POWER PRECISION PRIMARY PT PTCOMA RADIANS RANDOM REAL REFERENCES RENAME REPLACE RIGHT ROUND SCALE SECOND SELECT SET SETSEED SET_BYTE SHA256 SHIFTDER SHIFTIZQ SHOW SIGN SIMILAR SIN SIND SINH SMALLINT SOME SQRT SUBSTR SUBSTRING SUM TABLE TAN TAND TANH THEN TIME TIMESTAMP TKDECIMAL TKEXP TKNOT TO TRIM TRIM_SCALE TRUC TRUE TYPE UNION UNIQUE UNKNOWN UPDATE VALUES VARCHAR VARYING WHEN WHERE WIDTH_BUCKET YEAR textroot : setinstrucciones\n        setinstrucciones    : setinstrucciones setinstrucciones_paso\n                            | setinstrucciones_paso\n    \n        setinstrucciones_paso   : instruccion\n                                | instruccion PTCOMA\n    \n        instruccion     : select\n    \n        select  : SELECT DISTINCT\n                | SELECT\n    '
    
_lr_action_items = {'SELECT':([0,2,3,4,5,6,7,8,9,],[6,6,-3,-4,-6,-8,-2,-5,-7,]),'$end':([1,2,3,4,5,6,7,8,9,],[0,-1,-3,-4,-6,-8,-2,-5,-7,]),'PTCOMA':([4,5,6,9,],[8,-6,-8,-7,]),'DISTINCT':([6,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'setinstrucciones':([0,],[2,]),'setinstrucciones_paso':([0,2,],[3,7,]),'instruccion':([0,2,],[4,4,]),'select':([0,2,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> setinstrucciones','root',1,'p_init','gramatica.py',348),
  ('setinstrucciones -> setinstrucciones setinstrucciones_paso','setinstrucciones',2,'p_setInstrucciones','gramatica.py',353),
  ('setinstrucciones -> setinstrucciones_paso','setinstrucciones',1,'p_setInstrucciones','gramatica.py',354),
  ('setinstrucciones_paso -> instruccion','setinstrucciones_paso',1,'p_setInstrucciones_paso','gramatica.py',364),
  ('setinstrucciones_paso -> instruccion PTCOMA','setinstrucciones_paso',2,'p_setInstrucciones_paso','gramatica.py',365),
  ('instruccion -> select','instruccion',1,'p_instruccion','gramatica.py',372),
  ('select -> SELECT DISTINCT','select',2,'p_select','gramatica.py',383),
  ('select -> SELECT','select',1,'p_select','gramatica.py',384),
]
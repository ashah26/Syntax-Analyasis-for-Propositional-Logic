from pysmt.shortcuts import  Symbol, And, Not, is_sat,Iff
from parser import Parser

parserObj = Parser()

#
# P = Symbol("P") # Default type is Boolean
#
# Q = Symbol("Q")
#
# f = And(P, Not(Q))
# print(f, Not(f))
# print(is_sat(f))

lexerlist = ['LPAR', 'ID', 'AND', 'NOT', 'ID', 'RPAR', 'COMMA', 'LPAR', 'NOT', 'ID', 'IMPLIES', 'NOT', 'ID', 'RPAR']
postFixList = parserObj.convertToPostfix(lexerlist)

parserObj.checkSatisfiability(postFixList)
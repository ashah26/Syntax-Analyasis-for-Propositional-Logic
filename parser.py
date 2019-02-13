from lexer import Location, Lexer
import sys
import re


class VariableType:
    PROPOSITIONS = 0
    PROPOSITION = 1
    ATOMIC = 2
    MOREPROPOSITIONS = 3
    COMPOUND = 4
    CONNECTIVE = 5


class Parser:
    def __init__(self):
        self.loc = Location(0, 0)
        self.parserList = []
        self.indexCounter = 0
        self.tokenlist = []
        self.errorflag = False
        self.lexerlist = []

    def parse(self, tokenList):

        self.tokenlist = tokenList
        self.indexCounter = 0

        for token in tokenList:
            if token.kind == 0:
                self.lexerlist.append("ID")
            elif token.kind == 1:
                self.lexerlist.append("LPAR")
            elif token.kind == 2:
                self.lexerlist.append("RPAR")
            elif token.kind == 3:
                self.lexerlist.append("NOT")
            elif token.kind == 4:
                self.lexerlist.append("AND")
            elif token.kind == 5:
                self.lexerlist.append("OR")
            elif token.kind == 6:
                self.lexerlist.append("IMPLIES")
            elif token.kind == 7:
                self.lexerlist.append("IFF")
            elif token.kind == 8:
                self.lexerlist.append("COMMA")

        print("Lexer: ", self.lexerlist)
        self.propositions()
        if self.indexCounter < len(self.tokenlist):
            self.errorflag = True

        if not self.errorflag:
            print("Parser: ", self.parserList)
        else:
            print("Syntax error at line: ", self.tokenlist[self.indexCounter].loc.line, " and column: ",
                  self.tokenlist[self.indexCounter].loc.col)
        # raise NotImplementedError

    def match(self, token):

        raise NotImplementedError

    def propositions(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("propositions")
        self.proposition()
        self.more_propositions()

        # raise NotImplementedError

    def more_propositions(self):
        # print(sys.getframe().f_code.co_name)
        if not self.errorflag:
            self.parserList.append("more_propositions")
            if self.indexCounter < len(self.tokenlist) and self.tokenlist[self.indexCounter].kind == 8:
                self.indexCounter += 1
                self.parserList.append("comma")
                self.propositions()
            else:
                self.parserList.append("epsilon")

    def proposition(self):

        if not self.errorflag:
            self.parserList.append("proposition")
            if self.isCompound(self.indexCounter):
                self.compound()
            else:
                self.atomic()

    def atomic(self):

        if not self.errorflag:
            if self.isAtomic(self.indexCounter):
                self.indexCounter += 1
                self.parserList.append("atomic")
                self.parserList.append("ID")
            else:
                self.errorflag = True
                # print("Syntax error at line: ", self.tokenlist[self.indexCounter].loc.line, " and column: ", self.tokenlist[self.indexCounter].loc.col)

        # raise NotImplementedError

    def compound(self):
        # print(sys.getframe().f_code.co_name)

        if not self.errorflag:
            self.parserList.append("compound")

            if self.indexCounter < len(self.tokenlist):
                if self.tokenlist[self.indexCounter].kind == 3:
                    self.parserList.append("not")
                    self.indexCounter += 1
                    self.proposition()
                elif self.tokenlist[self.indexCounter].kind == 1:
                    self.parserList.append("LPAR")
                    self.indexCounter += 1
                    self.proposition()
                    self.parserList.append("RPAR")
                    self.indexCounter += 1
                elif self.isAtomic(self.indexCounter) and self.isConnective(self.indexCounter+1) \
                        and self.indexCounter+2 < len(self.tokenlist):
                    self.atomic()
                    self.connective()
                    self.proposition()
                else:
                    self.errorflag = True
                    # print("Syntax error at line: ", self.tokenlist[self.indexCounter].loc.line, " and column: ",
                    #       self.tokenlist[self.indexCounter].loc.col)

    def connective(self):
        # print(sys.getframe().f_code.co_name)

        if not self.errorflag:
            self.parserList.append("connective")

            if self.isConnective(self.indexCounter):
                if self.tokenlist[self.indexCounter].kind == 4:
                    self.indexCounter += 1
                    self.parserList.append("AND")
                elif self.tokenlist[self.indexCounter].kind == 5:
                    self.indexCounter += 1
                    self.parserList.append("OR")
                elif self.tokenlist[self.indexCounter].kind == 6:
                    self.indexCounter += 1
                    self.parserList.append("IMPLIES")
                elif self.tokenlist[self.indexCounter].kind == 7:
                    self.indexCounter += 1
                    self.parserList.append("IFF")
                else:
                    self.errorflag = True
                    # print("Syntax error at line: ", self.tokenlist[self.indexCounter].loc.line, " and column: ",
                    #       self.tokenlist[self.indexCounter].loc.col)

    def isAtomic(self, index):

        if index < len(self.tokenlist) and self.tokenlist[index].kind == 0:
            return True
        return False

    def isConnective(self, index):
        if index < len(self.tokenlist):
            if self.tokenlist[index].kind == 4:
                return True
            elif self.tokenlist[index].kind == 5:
                return True
            elif self.tokenlist[index].kind == 6:
                return True
            elif self.tokenlist[index].kind == 7:
                return True
        return False

    def isCompound(self, index):
        if index < len(self.tokenlist):
            if self.tokenlist[index].kind == 3:
                return True
            if self.tokenlist[index].kind == 1:
                return True
            if self.isAtomic(index):
               if self.isConnective(index+1):
                   if index+2 < len(self.tokenlist):
                       return True
        return False

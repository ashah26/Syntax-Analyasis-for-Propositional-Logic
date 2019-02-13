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
        self.divisor = 0

    def parse(self, tokenList):

        self.tokenlist = tokenList
        self.indexCounter = 0
        self.divisor = len(tokenList)

        for token in tokenList:
            print("While parsing : ", token.kind)

        self.propositions()
        # raise NotImplementedError

    def match(self, token):

        raise NotImplementedError

    def propositions(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("propositions")
        self.proposition()
        self.more_propositions()
        print("Parser List: ", self.parserList)
        raise NotImplementedError

    def more_propositions(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("more_propositions")
        if self.indexCounter < len(self.tokenlist) and self.tokenlist[self.indexCounter].kind == 8:
            self.indexCounter += 1
            self.parserList.append("comma")
            self.propositions()
        else:
            self.parserList.append("epsilon")

        # raise NotImplementedError

    def proposition(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("proposition")
        # if atomic else compound
        self.atomic()

        # raise NotImplementedError

    def atomic(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("atomic")

        if self.isAtomic():
            self.indexCounter += 1
            self.parserList.append("ID")

        # raise NotImplementedError

    def compound(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("compound")

        if self.indexCounter < len(self.tokenlist):
            if self.tokenlist[self.indexCounter].kind == 3:
                self.parserList.append("not")
                self.proposition()
            elif self.tokenlist[self.indexCounter].kind == 1:
                self.parserList.append("LPAR")
                self.proposition()
                self.parserList.append("RPAR")
            elif self.isAtomic() and self.isConnective():
                self.atomic()
                self.connective()
                self.proposition()

        # raise NotImplementedError

    def connective(self):
        # print(sys.getframe().f_code.co_name)

        self.parserList.append("connective")

        if self.isConnective():
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

        # raise NotImplementedError

    # add more methods if needed
    def isAtomic(self):

        if self.indexCounter < len(self.tokenlist) and self.tokenlist[self.indexCounter].kind == 0:
            return True
        return False

    def isConnective(self):
        if self.indexCounter < len(self.tokenlist):
            if self.tokenlist[self.indexCounter].kind == 4:
                return True
            elif self.tokenlist[self.indexCounter].kind == 5:
                return True
            elif self.tokenlist[self.indexCounter].kind == 6:
                return True
            elif self.tokenlist[self.indexCounter].kind == 7:
                return True
        return False
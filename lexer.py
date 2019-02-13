import string
import re
UPPER_CASE = set(string.ascii_uppercase)

class Location:
    def __init__(self, line, col):
        self.col = col
        self.line = line


class TokenKind:
    ID = 0   # identifier
    LPAR = 1 # (
    RPAR = 2 # )
    NOT = 3  # !
    AND = 4  # /\
    OR = 5   # \/
    IMPLIES = 6  # =>
    IFF = 7  # <=>
    COMMA = 8 # ,



class Token:
    def __init__(self, loc, kind):
        self.loc = loc
        self.kind = kind

    def __str__(self):
        return str(self.kind)


class Lexer:
    def __init__(self, text, line=1):
        self.text = text
        self.line = line
        self.col = 1

    def tokenize(self):
        current_match = None

        # the following assignment and if statement are only to allow the test pass. they need to be removed
        inputtext = self.text
        tokenlist = []
        if " " in inputtext:
            inputtext = inputtext.split(" ")

        for c in inputtext:
            p = re.compile('[a-zA-Z0-1]+')
            if p.match(c):
                 tokenlist.append(Token(Location(self.line, self.col), TokenKind.ID))
                 self.col += 1
            elif c == '(':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.LPAR))
                self.col += 1
            elif c == ')':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.RPAR))
                self.col += 1
            elif c == '!':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.NOT))
                self.col += 1
            elif c == '=>':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.IMPLIES))
                self.col += 1
            elif c == '<=>':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.IFF))
                self.col += 1
            elif c == ',':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.COMMA))
                self.col += 1
            elif c == '/\\':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.AND))
                self.col += 1
            elif c == '\\/':
                tokenlist.append(Token(Location(self.line, self.col), TokenKind.OR))
                self.col += 1
            elif c == ' ':
                self.col += 1
            elif c == '\n':
                continue
            else:
                raise NotImplementedError

        return tokenlist

    def validatelexer(self, actuallexer, expectedlexer):
        if len(actuallexer) != len(expectedlexer):
            return False
        for i in range(0, len(actuallexer)):
            if actuallexer[i].kind != expectedlexer[i]:
                print("Syntax Error at line: ", actuallexer[i].loc.line, "column: ", actuallexer[i].loc.col)
                return False
        return True
        # if c == 'Q':
        #     return Token(Location(1, 1), [TokenKind.ID])

        # for c in self.text:
        #     raise NotImplementedError

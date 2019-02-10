import unittest
from lexer import Lexer, TokenKind
from parser import Parser

# f = open("input.txt")
# linecount = 1
# for line in f:
#     l = Lexer(line, linecount).tokenize()
#     linecount = linecount+1
    # print(l.kind)

class Test(unittest.TestCase):
    def test1(self):
        l = Lexer('Q').tokenize()
        print(l, l.kind, l.loc, TokenKind.ID)
        self.assertEqual(l.kind, [TokenKind.ID])

    def test2(self):
        tokelist = Lexer('Q').tokenize()
        #parse_tree = Parser().parse(tokelist)
        # some assertion goes here

    def test3(self):
        l = Lexer('!Q')
        ll = l.tokenize()
        print(l)
        self.assertTrue(l.validatelexer(ll, [TokenKind.NOT, TokenKind.ID]))

    def test4(self):
        l = Lexer(')Q')
        ll = l.tokenize()
        print(l)
        self.assertTrue(l.validatelexer(ll, [TokenKind.RPAR, TokenKind.ID]))

    def test5(self):
        l = Lexer(')Q')
        ll = l.tokenize()
        print(l)
        self.assertTrue(l.validatelexer(ll, [TokenKind.NOT, TokenKind.ID]))

    def test6(self):
        l = Lexer(')Q')
        ll = l.tokenize()
        print(l)
        self.assertTrue(l.validatelexer(ll, [TokenKind.RPAR, TokenKind.ID]))


if __name__ == '__main__':
    unittest.main()
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    """IDENTIFIER TEST"""
    def test_simple_string(self):
        self.assertTrue(TestLexer.test("book foo","book,foo,<EOF>",101))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("_foo1 foo3","_foo1,foo3,<EOF>",102))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("1foo1","Error Token 1",103))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("__","__,<EOF>",103))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("a <- 5 ## This comment is not allowed in ZCode","a,<-,5,<EOF>",103))

    

    """LITERALS TEST"""

    """Number"""
    def test_simple_string(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",104))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("0.1","0.1,<EOF>",105))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("0.1e-999","0.1e-999,<EOF>",106))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("0.1e-999","0.1e-999,<EOF>",107))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("15.","15.,<EOF>",108))

    """String"""
    def test_simple_string(self):
        self.assertTrue(TestLexer.test("""\"This is a string with tab \t\"""","\"This is a string with tab \t\",<EOF>",109))

    def test_simple_string(self):
        self.assertTrue(TestLexer.test("""\"He asked me: \'\"Where is John?\'\"\"""","He asked me: \'\"Where is John?\'\",<EOF>",110))
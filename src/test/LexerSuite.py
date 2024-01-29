import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    

      
    """IDENTIFIER TEST"""
    def test_1(self):
        self.assertTrue(TestLexer.test("book foo","book,foo,<EOF>",101))

    def test_2(self):
        self.assertTrue(TestLexer.test("_foo1 foo3","_foo1,foo3,<EOF>",102))

    def test_3(self):
        self.assertTrue(TestLexer.test("foo1&","foo1,Error Token &",103))

    def test_4(self):
        self.assertTrue(TestLexer.test("__","__,<EOF>",104))

    def test_5(self):
        self.assertTrue(TestLexer.test("a <- 5 ## This comment is not allowed in ZCode","a,<-,5,<EOF>",105))

    

    # """LITERALS TEST"""

    """Number"""
    def test_6(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",106))

    def test_7(self):
        self.assertTrue(TestLexer.test("0.1","0.1,<EOF>",107))

    def test_8(self):
        self.assertTrue(TestLexer.test("0.1e-999","0.1e-999,<EOF>",108))

    def test_9(self):
        self.assertTrue(TestLexer.test("0.1e-999","0.1e-999,<EOF>",109))

    def test_10(self):
        self.assertTrue(TestLexer.test("15.","15.,<EOF>",110))

    """String"""
    def test_11(self):
        self.assertTrue(TestLexer.test("""\"This is a string with tab\t\"""","This is a string with tab\t,<EOF>",111))

    def test_12(self):
        self.assertTrue(TestLexer.test("""\"He asked me: \'\"Where is John?\'\"\"""","He asked me: \'\"Where is John?\'\",<EOF>",112))

    def test_13(self):
        self.assertTrue(TestLexer.test("""\"'\"""","Unclosed String: '\"",113))

    def test_14(self):
        self.assertTrue(TestLexer.test("""\"Hello world ""","Unclosed String: Hello world ",114))

    def test_15(self):
        self.assertTrue(TestLexer.test("""\"Notre dame \c\"""","Illegal Escape In String: Notre dame \c",115))

    def test_16(self):
        self.assertTrue(TestLexer.test("""\"illegal man \k haha\"""","Illegal Escape In String: illegal man \k",116))

    def test_17(self):
        self.assertTrue(TestLexer.test("""\"Here comes the sun\"\"unclosed baby""","Here comes the sun,Unclosed String: unclosed baby",117))

    def test_18(self):
        self.assertTrue(TestLexer.test("""\"Here comes \i\"\"unclosed baby""","Illegal Escape In String: Here comes \i",118))
    
    def test_19(self):
        self.assertTrue(TestLexer.test("""\"I love you baby \t\o\"\"unclosed baby""","Illegal Escape In String: I love you baby \t\o",119))
    
    def test_20(self):
        self.assertTrue(TestLexer.test("""\"baby\\ \"""","Illegal Escape In String: baby\ ",120))

    def test_21(self):
        self.assertTrue(TestLexer.test("""\"baby""","Unclosed String: baby",121))

    def test_22(self):
        self.assertTrue(TestLexer.test("""\"illegal \\a\"""","""Illegal Escape In String: illegal \\a""",122))

    def test_23(self):
        self.assertTrue(TestLexer.test(
            """\"abc - xyz\" \"abc \ xyz\"""","""abc - xyz,Illegal Escape In String: abc \ """,123))
        
    def test_24(self):
        self.assertTrue(TestLexer.test(
            """\"Mua Thang Sau\"""","""Mua Thang Sau,<EOF>""",124))
    
    def test_25(self):
        self.assertTrue(TestLexer.test(
            """\"Khi nao ra truong ?\"""","""Khi nao ra truong ?,<EOF>""",125))
        
    def test_26(self):
        self.assertTrue(TestLexer.test(
            """\"Unclosed and Illegal\i\z""","""Illegal Escape In String: Unclosed and Illegal\i""",126))
        
    def test_27(self):
        self.assertTrue(TestLexer.test(
            """\"Unclosed and Illegal""","""Unclosed String: Unclosed and Illegal""",127))
        
    def test_28(self):
        self.assertTrue(TestLexer.test(
            """\"Unclosed and Illegal""","""Unclosed String: Unclosed and Illegal""",128))
        
    def test_29(self):
        self.assertTrue(TestLexer.test(
            """\" Hi Hi \s\d\\f \"""","""Illegal Escape In String:  Hi Hi \s""",129))
        
    def test_30(self):
        test="""
        func main(number arg) 
        begin
        string str <- "full stack developer\i"
        end
        """
        expect="""\n,func,main,(,number,arg,),\n,begin,\n,string,str,<-,Illegal Escape In String: full stack developer\i"""
        self.assertTrue(TestLexer.test(test,expect,130))

    def test_31(self):
        test="""\"string\" ## comment"""
        expect="""string,<EOF>"""
        self.assertTrue(TestLexer.test(test,expect,131))

    def test_32(self):
        test="""\"12345986qqqq~~!~~]quanque\';;abcdefghijklmnop_ABCDEFGHIJKLMNOPQRSTUVWXYZ#\'"%>\""""
        expect="""12345986qqqq~~!~~]quanque\';;abcdefghijklmnop_ABCDEFGHIJKLMNOPQRSTUVWXYZ#\'"%>,<EOF>"""
        self.assertTrue(TestLexer.test(test,expect,132))

    def test_33(self):
        test="""\"Je de\'teste La Musique de Rap, j\' aime La Musique de Bolero, c\'est inte\'ressant\""""
        expect="""Je de\'teste La Musique de Rap, j\' aime La Musique de Bolero, c\'est inte\'ressant,<EOF>"""
        self.assertTrue(TestLexer.test(test,expect,133))

    def test_34(self):
        test="""\"\'"\'"\""""
        expect="""'"'",<EOF>"""
        self.assertTrue(TestLexer.test(test,expect,134))

    def test_35(self):
        test="""\"\'\"\""""
        expect="""'",<EOF>"""
        self.assertTrue(TestLexer.test(test,expect,135))

    """Multiple Test"""

    # def test_20(self):
    #     self.assertTrue(TestLexer.test("""\"this is unclosed string""","Unclosed String: this is unclosed string",120))

    # def test_21(self):
    #     self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",121))
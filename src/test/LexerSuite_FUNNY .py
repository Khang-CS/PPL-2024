import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lexer_1(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \t\"","This is a string containing tab \t,<EOF>", 101))

    def test_lexer_2(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab\"","This is a string containing tab,<EOF>", 102))
    
    def test_lexer_3(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 103))

    def test_lexer_4(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 104))

    def test_lexer_5(self):
        input = """
        func isPrime(number x)
            return (num1 % num2 = 0 or num2 % num1 = 0)
            
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()

                if areDivisors(num1, num2) printString("Yes")
                else printString("No")
            end
        """
        expect = """\n,func,isPrime,(,number,x,),\n,return,(,num1,%,num2,=,0,or,num2,%,num1,=,0,),\n,\n,func,main,(,),\n,begin,\n,var,num1,<-,readNumber,(,),\n,var,num2,<-,readNumber,(,),\n,\n,if,areDivisors,(,num1,,,num2,),printString,(,Yes,),\n,else,printString,(,No,),\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_lexer_6(self):
        input = """"He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_lexer_7(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
            end
        """
        expect = """\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_lexer_8(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                else
                    not a
            end
        """
        expect = """\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,else,\n,not,a,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_lexer_9(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                elif -a
                    a - (b - c) * ab
                else
                    not a
            end
        """
        expect = """\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,elif,-,a,\n,a,-,(,b,-,c,),*,ab,\n,else,\n,not,a,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_lexer_10(self):
        input = "0 199 12. 12.3 12.3e 12.3e-30 1.0 1e-12 1.0e-12 0.000000001"
        expect = "0,199,12.,12.3,12.3e,12.3e-30,1.0,1e-12,1.0e-12,0.000000001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))

       

    def test_lexer_11(self):
        input = "number a[5] <- [1, 2, 3, 4, 5]"
        expect = "number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_lexer_12(self):
        input = "number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]"
        expect = "number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test_lexer_13(self):
        input = "[[1, 2], [4, 5], [3, 5]]"
        expect = "[,[,1,,,2,],,,[,4,,,5,],,,[,3,,,5,],],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_lexer_14(self):
        input = "a[3 + foo(2)] <- a[b[2, 3]] + 4"
        expect = "a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_lexer_15(self):
        input = """
        func foo(number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1
                begin
                    a[i] <- i * i + 5
                end
            return -1
        end
        """
        expect = "\n,func,foo,(,number,a,[,5,],,,string,b,),\n,begin,\n,var,i,<-,0,\n,for,i,until,i,>=,5,by,1,\n,begin,\n,a,[,i,],<-,i,*,i,+,5,\n,end,\n,return,-,1,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))

    # def test_lexer_16(self):
    #     input = """
    #     func foo(number a[5], string b)
    #     begin
    #         var i <- 0
    #         for i until i >= 5 by 1
    #             begin
    #                 aPI <- 3.14
    #                 value <- x.foo(5)
    #                 l[3] <- value * aPi
    #             end
    #         return -1
    #     end
    #     """
    #     expect = "func,foo,(,number,a,[,5,],,,string,b,),begin,var,i,<-,0,for,i,until,i,>=,5,by,1,begin,aPI,<-,3.14,value,<-,x,.,foo,(,5,),l,[,3,],<-,value,*,aPi,end,return,-,1,end,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 116))
        
    def test_lexer_17(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                elif -a
                    a - (b - c) * ab
                elif -b
                    a - (b - c) * ab
                else
                    not a
            end
        """
        expect = "\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,elif,-,a,\n,a,-,(,b,-,c,),*,ab,\n,elif,-,b,\n,a,-,(,b,-,c,),*,ab,\n,else,\n,not,a,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_lexer_18(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                elif -a
                    a - (b - c) * ab
                elif -b
                    a - (b - c) * ab
            end
        """
        expect = "\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,elif,-,a,\n,a,-,(,b,-,c,),*,ab,\n,elif,-,b,\n,a,-,(,b,-,c,),*,ab,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_lexer_19(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                elif -a
                    a - (b - c) * ab
                    break
                elif -b
                    a - (b - c) * ab
            end
        """
        expect = "\n,func,test,(,number,a,,,number,b,),\n,return,a,+,b,\n,\n,func,main,(,),\n,begin,\n,if,a,==,b,\n,a,<-,b,\n,elif,-,a,\n,a,-,(,b,-,c,),*,ab,\n,break,\n,elif,-,b,\n,a,-,(,b,-,c,),*,ab,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test_lexer_20(self):
        self.assertTrue(TestLexer.test(".e123","Error Token .", 120))

    def test_lexer_21(self):
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_lexer_22(self):
        input = """ "Hello \\ \" """
        expect = """Illegal Escape In String: Hello \ """
        self.assertTrue(TestLexer.test(input, expect, 122))

    def test_lexer_23(self):
        input = """
        ## Illegal escape: Hello 'W
        "Hello 'World"
        """
        expect = """\n,Hello 'World,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_lexer_24(self):
        input = """
        # Illegal escape: Hello 'W
        "Hello 'World"
        """
        expect = """\n,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_lexer_25(self):
        input = """
        ## Illegal escape: Hello 'W
        "Hello 'World"
        ## Illegal escape: Hello 'W \n 123
        """
        expect = """\n,Hello 'World,\n,123,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test_lexer_26(self):
        input = """
        ## Illegal escape: Hello 'W
        "Hello 'World"
        # Illegal escape: Hello 'W \n 123
        """
        expect = """\n,Hello 'World,\n,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test_lexer_27(self):
        input = """"Test string \'String\' " """
        expect = """Test string 'String' ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))

    # def test_lexer_28(self):
    #     input = """
    #     "Test string String'"
    #     """
    #     expect = """Unclo"""
    #     self.assertTrue(TestLexer.test(input, expect, 128))
        
    def test_lexer_29(self):
        input = """
        func main(number x)
            begin
                number a[5] <- [1, 2, 3, 4, 5]
                number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                var i <- 2
                for i until i > x / 2 by 1
                    writeNumber(i)
            end
        """
        expect = "\n,func,main,(,number,x,),\n,begin,\n,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],\n,var,i,<-,2,\n,for,i,until,i,>,x,/,2,by,1,\n,writeNumber,(,i,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_lexer_30(self):
        input = """
        func main(number x)
            begin
                number a[5] <- [1, 2, 3, 4, 5]
                number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            end
        """
        expect = "\n,func,main,(,number,x,),\n,begin,\n,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test_lexer_31(self):
        input = """
        func main(number x)
            begin
                a[3 + foo(2)] <- a[b[2, 3]] + 4
            end
        """
        expect = """\n,func,main,(,number,x,),\n,begin,\n,a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 131))
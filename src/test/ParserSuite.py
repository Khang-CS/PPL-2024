import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_2(self):
        
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_3(self):
        
        input = """func main() begin
        for i until i>3 by 1
        if (a>3) writeNumber(a)
        elif (a>2) writeNumber(a)
        else break
        readBool()




        var x <- 3/2+a[7]
        end
        func foo(number a) return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_4(self):
        
        input = """func main() 
        begin
        number a[7] <- [1,2,3,4,5,6,7]
        number b[3,7] <- [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]

        a[0] <- 325 + 7
        a[1] <- 2*3+7/5-45
        a[foo(3)+7*9] <- "Anh yeu em pac pac"

        end
        func foo(number a) return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))


    def test_5(self):
        
        input = """
func areDivisors(number num1, number num2)
return true
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) printString("Yes")
else printString("No")
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_6(self):
        
        input = """
                func isPrime(number x)
                func main()
                begin
                number x <- readNumber()
                if (isPrime(x)) printString("Yes")
                else printString("No")
                end

                func isPrime(number x)
                begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                if (x % i = 0) return false
                end
                return true
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_7(self):        
        input = """func main(number arg)
        begin
            number b[2,3] <- [[1+2, 3+5, foo(3)], [foo(15*27/32),"j\' aime la france", "comment allez vous"]]

            number array[2,2] <- [[not true, not false, foo(3) or foo(4)], [not balance, you and i]]

            for z until foo(z) == "error" by 1 
                begin
                    printString("Happy New Year")

                    for i until i < 100 by 2
                        begin
                            printString("Bonne anne\'e !")
                            readNumber()
                            writeNumber(32)
                            readBool()
                            writeBool(true)

                            readString()

                            if (a=2) 
                                begin
                                    printString("Bonjour")
                                end
                        end
                end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))


    def test_8(self):
        
        input = """func main()
        begin
        if (a>7) printString("32")

        elif (a>6) printString("haha")

        elif (a=6) readString() ## else return 32

        var z <- (10 >= 20) > 10 + 15 + (not fun) % 12e-37
        begin
        printString("Wingardium Leviosa")
        begin
        begin
        end
        end
        end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_9(self):
        input="""func printString() return \"haha\"
        func checkIfNameExist(number a, string str, number arr[32])
        begin
        if (a = 7) printString()
        else return arr[1/2%7]
        end
        
        func main(number arg[10]) 
        begin
        var a <- (not true) and (not (not false))
        bool b <- bool
        end

        """
        expect="Error on line 11 col 18: bool"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        input="""func printString() return \"haha\"
        func checkIfNameExist(number a, string str, number arr[32])
        begin
        if (a = 7) printString()
        else return arr[1/2%7]
        end
        
        func main(number arg[10]) 
        begin
        var a <- (not true) and (not (not false))
        bool check <- (15>2) and (1<10) or checkLegit(\"Cristiano Ronaldo is the greatest of all time\")

        string str[7] <- [("str1\t"),("str2\t"),("str3\f")]

        if (a == "hello world" ... "Ronaldo") print(3)

        for i until i<100 by 1
        begin
        a <- a... "New string "

        a <- number f
        end
        end
        
        """
        expect="Error on line 21 col 13: number"
        self.assertTrue(TestParser.test(input,expect,210))


    def test_11(self):
        input="""
        func main(var a, var b) return a
        """
        expect="Error on line 2 col 18: var"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        input="""
        func main(string a, string b) return a ... "the world"
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        input="""func main(string a)
        begin
        ## comment
        var a <- "str" ## this is a comment
        ## this is a comment too >>>> <<<<<<<xxxxx
        end
        ## Cristiano Ronaldo is better than Lionel Messi
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        input="""func main(string a)
        begin
        ## comment
        var a <- "str" ## this is a comment
        ## this is a comment too >>>>
        for a until a<3000 by 1
        begin
        printString("I love you")
        end
        printString("I love you 3000")
        end

        func isPrime(number x)
        begin
        if (x<=1) return false
        var i<-2
        for i until i>x/2 by 1 
        begin
        if (x % i = 0) return false
        end

        return true
        end

        func isLove(string str) return \"je tre\'s aime\' tu\"
        func isDead(string str) return \"je vais a\' Paris pour regarder toi\"
        func isLive(number a, string f, number a[100])
        begin
        if (a>500) isLove()
        elif (a>400) isDead()
        elif (a>300) isLive()
        else

        return 3
        end
        
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,214))
    

    def test_15(self):
        input="""func main(string a)
        begin
        ## comment
        var a <- "str" ## this is a comment
        ## this is a comment too >>>> <<<<<<<xxxxx
        number a[5] <- [3+2/7*18%(32),30e-7-15,110.20e+15]

        
        end
        ## Cristiano Ronaldo is better than Lionel Messi

        
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,215))

    


    
    







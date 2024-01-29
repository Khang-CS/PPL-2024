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

        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    

    

    


    
    







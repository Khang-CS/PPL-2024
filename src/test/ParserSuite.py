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

    def test_16(self):
        input="""number a
        number k <- 300
        number p <- 200

        string str <- "Anh cho em mua xuan"


        dynamic dynamite <- "BTS"..."Bangtang Boys"
        bool check <- not not (not true) and not false or true or false or (30 <= 9) and (30>90) >70 and (("con cho" != "con ngua") = ("Beo phi" == "map dit"))

        bool compare <- (30e-7>20e20)

        func main() return true

        func abasalom(string str, number b)
        begin

        var a<- 3+7 

        var b<- 6+9-10-20/30%15
        end


        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_17(self):
        input="""
        dynamic a <- 0
        number b <- 199
        number c <- 12.
        var d <- 12.3
        var e <- 12.3e1500000 - 3015
        number f <- 12e-15 * 15 / 27
        string str <- "Macbook Pro M1 \t\f"
        func main(string a)
        begin
        ## comment
        var a <- "str" ## this is a comment
        ## this is a comment too >>>> <<<<<<<xxxxx
        number a[5] <- [3+2/7*18%(32),30e-7-15,110.20e+15]


        end
        ## Cristiano Ronaldo is better than Lionel Messi

        
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,217))


    def test_18(self):
        input="""
        dynamic a <- 0
        number b <- 199
        number c <- 12.
        var d <- 12.3
        var e <- -12.3e1500000 - 3015
        number f <- 12e-15 * 15 / 27 and (15<32) = 1

        string frank_sinatra <- "fly me to the moon "..."lala\f" ##comment

        bool check <- true and not false and not true or not false or ((32>10)>0) = true

        bool boolean <- boo + bo + b

        func main(string str[30,31,32,33,34,35], string str2[0]) return str[1,2,3,4,5,5]

        string str[a[2]+1]
        
        """
        expect="Error on line 17 col 19: a"
        self.assertTrue(TestParser.test(input,expect,218))
    
    def test_19(self):
        input="""func deck(number controller) begin
        string str[2,2]<-[["con cho","con meo"],["con khi?","con chim"]]
        if (a>7) 
            if (a%2 = 0) printString("Even")
            else printString("Odd")
        elif (a>6) 
            if (a%3 = 0) printString("multiple of 3")
            else printString("Not multiple of 3")
        else printString("haha")

        str[foo+3/2*(30>1)*15, 100%30%35+10] <- "Con rong" ... "Nam My"
        end 

        func main(var arg) return 0       
        """
        expect="Error on line 14 col 18: var"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_20(self):
        input="""
        string str <- "God of war"

        string str = 3232  
        """
        expect="Error on line 4 col 19: ="
        self.assertTrue(TestParser.test(input,expect,220))

    def test_21(self):
        input="""
        string str <- "God of war"

        var x <- a[1+2,15/32*4] + -32 * 45 + not true

        dynamic a[3,2]
        """
        expect="Error on line 6 col 17: ["
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22(self):
        input="""
        string str <- "God of war"

        var x <- a[1+2,15/32*4] + -32 * 45 + not true

        func superman() begin
        var a[3,2] <- [[1,2],[3,4],[5,6]]
        end        
        """
        expect="Error on line 7 col 13: ["
        self.assertTrue(TestParser.test(input,expect,222))

    def test_23(self):
        input="""
        func foo(number a[5], string b)
        begin
        var i <- 0
        for i until i >=5 by 1
        begin
        a[i] <- i*i+5
        end
        return -1
        end        
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24(self):
        input="""
        func isPrime(number x)
        begin
            if (x<=1) return false
            var i <- 2
            for i until i>x/2 by 2
            begin
                if (x%i = 0)
                begin
                    printString("Break")
                    break
                end
            end 
        return true
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_25(self):
        input="""
        func isPrime(number x)
        begin
            if (x<=1) return false
            var i <- 2*5-32+1/17
            a[3+foo(2)] <- a[b[2,3]]+4
            foo(a[3]+7*25, "string")
            for i until i>x/2 by 2
            begin
                if (x%i = 0)
                begin
                    printString("Break")
                    break
                end
            end 
        return true
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_25(self):
        input="""
        func isPrime(number x)
        begin
            if (x<=1) return false
            var i <- 2*5-32+1/17
            a[3+foo(2)] <- a[b[2,3]]+4
            foo(a[3]+7*25, "string")
            for i until i>x/2 by 2
            begin
                if (x%i = 0)
                begin
                    printString("Break")
                    break
                end
            end 
        return true
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_26(self):
        input="""
        func main(string arg)
        begin
        for i until i!=30 by 1 begin
            if (i >10) break
            else printString("Le Festin")
        end
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_27(self):
        input="""
        func main(var arg)
        begin
        for i until i!=30 by 1 begin
            if (i >10) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 18: var"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_28(self):
        input="""
        func main(var arg)
        begin
        for i until i!=30 by 1 begin
            if (i >10) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 18: var"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_29(self):
        input="""
        func static main(var arg)
        begin
        for i until i!=30 by 1 begin
            if (i >10) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 20: main"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_30(self):
        input="""
        func static main(var arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i >10) break
            else printString("Le Festin")
        end

        callfunc()
        end      
        """
        expect="Error on line 2 col 20: main"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_31(self):
        input="""
        func true(var arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i >10) break
            else printString("Le Festin")
        end

        callfunc()
        end      
        """
        expect="Error on line 2 col 13: true"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_32(self):
        input="""
        func main(number arg)
        begin
        for bool until bool!=30 by 1 begin
            if (i = 3) continue
            if (i >10) break
            else printString("Le Festin")
        end

        callfunc()
        end      
        """
        expect="Error on line 4 col 12: bool"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_33(self):
        input="""
        func main(number arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i >) break
            else printString("Le Festin")
        end

        callfunc()
        end      
        """
        expect="Error on line 6 col 19: )"
        self.assertTrue(TestParser.test(input,expect,233))

    
    







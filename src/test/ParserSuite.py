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

    def test_34(self):
        input="""
        func main(number arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end

        a <- b

        for i until i <49 by 2+3+4*15/32 foo(true,false, not false)

        if (a) callfunc(3)
        
        elif (not a) callfunc(2)

        else callfunc(1)
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_35(self):
        input="""
        func string(number arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 13: string"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_36(self):
        input="""
        func not(number arg)
        begin
        for i until i!=30 by 1 begin
            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 13: not"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_37(self):
        input="""
        func f(number arg)
        begin
        for dynamic until dynamic!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 4 col 12: dynamic"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_38(self):
        input="""
        func f(number arg)
        begin
        for i until dynamic!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 4 col 20: dynamic"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_39(self):
        input="""
        func func(number arg)
        begin
        for i until dynamic!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end
        end      
        """
        expect="Error on line 2 col 13: func"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_40(self):
        input="""
        func main(number arg)
        begin
        for i until i!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end

        var false <- a
        end      
        """
        expect="Error on line 11 col 12: false"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_41(self):
        input="""
        func main(number arg)
        begin
        for i until i!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end

        var variable <- true + false + not foo(3)
        end      
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_42(self):
        input="""
        func notMain(number a, string b) break
        func main(number arg)
        begin
        for i until i!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end

        var variable <- true + false + not foo(3)
        end      
        """
        expect="Error on line 2 col 41: break"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_43(self):
        input="""
        func notMain(number a, string b) begin
        begin
        begin
        begin
        end
        end        
        end

        func main(number arg)
        begin
        for i until i!=30 by 1*9/30-15%2 begin

            if (i = 3) continue
            if (i > 1) break
            else printString("Le Festin")
        end

        var variable <- true + false + not foo(3)
        end      
        """
        expect="Error on line 10 col 8: func"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_44(self):
        input="""
        func rose(string str) return "Nao dau ai muon quen"     
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_45(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string str <- "when i look i to your eyes"

        string str <- "i can see the love restrained" 
        end     
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_46(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string str <- "when i look i to your eyes"

        string str <- "i can see the love restrained" 

        number f <- func(35*10+9-323/71%83)
        end     
        """
        expect="Error on line 9 col 20: func"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_47(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string str1<- "when i look i to your eyes"

        string str2 <- "i can see the love restrained" 



        number f <- funcMain(35*10+9-323/71%83)

        if (if>7) return 1
        end     
        """
        expect="Error on line 13 col 12: if"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_48(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- writeString()
        end     
        """
        expect="Error on line 5 col 32: )"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- readNumber(3*7)
        end     
        """
        expect="Error on line 5 col 31: 3"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_50(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- readBool(true)
        end     
        """
        expect="Error on line 5 col 29: true"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_51(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- writeBool()
        end     
        """
        expect="Error on line 5 col 30: )"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_52(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- readString(arg)
        end     
        """
        expect="Error on line 5 col 31: arg"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_53(self):
        input="""
        func axl_Rose(string str) return "guns\' n\' roses"

        func main() begin
        string f <- writeString()
        end     
        """
        expect="Error on line 5 col 32: )"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_54(self):
        input="""
        func main(string str) <- 3*3+3   
        """
        expect="Error on line 2 col 30: <-"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_55(self):
        input="""
        func main(string str) begin
        bool c <- 32>10>8
        end  
        """
        expect="Error on line 3 col 23: >"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_56(self):
        input="""
        func main(string str) begin
        bool c <- (32>10)>8 and true
        for a until a<39 and true or false by 1*39+27-15
        printString("haha")
        end  
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_57(self):
        input="""
        func main(string str) begin
        bool c <- (32>10)>8 and true
        for a until a<39 and true or false or true and ("con"..."cho" == "con cho") or (69%2!=0) by 1*39+27-15
        begin
        printString("haha")
        end
        end  
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_58(self):
        input="""
        func main(string str) begin
        bool c <- (32>10)>8 and true
        for a until a<39 and true or false or true and ("con"..."cho" == "con cho") or (69%2!=0) by 1*39+27-15
        begin
            for b until a == "Ronaldo" by 13
            print(x)
        end
        end  
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_59(self):
        input="""
        func foo2(number x, string str, number a[3000])
        func foo1(number x) return [1,2,3,4,5]
        func main(number x) begin
        a[5] <- foo(3)[16*9+32]-5
        foo(3)[14] <- 32
        fallInLove("Nam nam roi khong gap, tu khi em lay chong")[true, false, true, not false] <- not true and false and not false and 15>32 or (32 = 10)
        end  
        """
        expect="Error on line 6 col 14: ["
        self.assertTrue(TestParser.test(input,expect,259))

    def test_59(self):
        input = """func main(number x)
            begin
                number a <- 15 
                number a <- [1, 2, 3, 4, 5]
                
                var i <- 2
                for i until i > x / 2 by 1
                    writeNumber(i)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """func main(number x)
            begin
                number a <- 15 
                number a <- [1, 2, 3, 4, 5]
                begin
                    number b <- [1,2,3,4,5] * 32 ... "Frenkie De Jong" + 0.10e-32
                end
                
                var i <- 2
                for i until i > x / 2 by 1
                    writeNumber(i)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_61(self):
        input = """number global_x <- 32*19+38 - [1,2,3,4,5,[1,2,3,5]]
        var _number <- 3*9+1
        
        func main(number x)            
            begin
                number a <- 15 
                number a <- [1, 2, 3, 4, 5]
                begin
                    number b <- [1,2,3,4,5] * 32 ... "Frenkie De Jong" + 0.10e-32
                end
                
                var i <- 2
                for i until i > x / 2 by 1
                    writeNumber(i)
                number arrayNumber[19*23,15]
            end
        """
        expect = "Error on line 15 col 37: *"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """number global_x <- 32*19+38 - [1,2,3,4,5,[1,2,3,5]]
        var _number <- 3*9+1
        string Barcelona_squad[11]<-["Robert Lewandowski","Raphinha","Joao Felix","Gavi","Pedri","Frenkie De Jong","Ronald Araujo","Jules Kounde","Alejandro Balde","Sergio Roberto","Ter Stegen"]

        string RealMadrid_squad[11]<-["Joselu","Vinicius Jr","Jude Bellingham","Federico Valverde","Edouardo Carmavinga","Tchouchameni","David Alaba","Antonio Rudiger","Dani Carvajal","Ferland Mendy","Andriy Lunin"]

        string matchResult <- RealMadrid ... "4-1" ...Barcelona

        """
        expect = "Error on line 7 col 51: ..."
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """
        func manUtd(string manUtd_mem[11,3]) begin
        for i until i<11 by 1
        begin
        if (manUtd_mem[0] == "Bruno Fernandes") printString("Captain")
        elif (manUtd_mem[1] == "Andre Onana") printString("chu be ngu")
        elif (manUtd_mem[2] == "Marcus Rashford") printString("Tien Si")
        elif (manUtd_mem[3] == "Alenjandro Garnacho")
            if(manUtd_mem[3,0] == "Goal") printString("Siuuuu 7777")
            elif(manUtd_mem[3,0] == "Miss") printString("Kim Ri Con")
            else
                if(manUtd_mem[3,1] == "Assist" and manUtd[3,1] = 12) manUtd_mem[3] <- manUtd_mem[3] ... "bay hut"
                else printString("haha")
        end
        end

        """
        expect = "Error on line 12 col 63: ="
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """
        func manUtd(string manUtd_mem[11,3]) begin
        for i until i<11 by 1
        begin
        if (manUtd_mem[0] == "Bruno Fernandes") printString("Captain")
        elif (manUtd_mem[1] == "Andre Onana") printString("chu be ngu")
        elif (manUtd_mem[2] == "Marcus Rashford") printString("Tien Si")
        elif (manUtd_mem[3] == "Alenjandro Garnacho")
            if(manUtd_mem[3,0] == "Goal") printString("Siuuuu 7777")
            elif(manUtd_mem[3,0] == "Miss") printString("Kim Ri Con")
            else
                if(manUtd_mem[3,1] == "Assist" and (manUtd = 12))
                    if(x = 12) print(x)
                    elif (x = 12+12)
                        if(x = 32*32+7) print(st) 
                    else print(f)
                else printString("haha")
        end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def test_65(self):
        input = """    
        func a()
            return 
        var a <- []
        """
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """ 
            var Khanh <- a[1] + 1
            var Khanh <- array[1,1+2][1]
            var Khanh <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var Khanh <- a[1] + fun()[1,fun()] 
            var Khanh <- 1[1]
        """
        expect = "Error on line 3 col 37: ["
        self.assertTrue(TestParser.test(input, expect, 266))



    

    

    
    







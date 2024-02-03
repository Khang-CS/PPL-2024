import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_parser_1(self):
        input = """
        func main ()
            return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_parser_2(self):
        input = """
        func test(number a, number b)
            return a + b

        func main()
            begin
                if a == b
                    a <- b
                elif -a
                    a <- a - (b - c) * ab
                    break
                elif -b
                    a <- a - (b - c) * ab
            end
        """
        expect = "Error on line 12 col 16: elif"
        self.assertTrue(TestParser.test(input, expect, 202))

    # def test_parser_3(self):
    #     input = """
    #     func test(number a, number b)
    #         return a + b

    #     func main()
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 a <- a - (b - c) * ab
    #             elif -b
    #                 a <- a - (b - c) * ab
    #         end

    #     func add()
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 test(3, 4)
    #             elif -b
    #                 a <- test(4, 5)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 203))

    # def test_parser_4(self):
    #     input = """
    #     number x <- 0

    #     func test(number a, number b)
    #         return a + b

    #     string y

    #     func main()
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 a <- a - (b - c) * ab
    #             elif -b
    #                 a <- a - (b - c) * ab
    #         end

    #     func add()
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 test(3, 4)
    #             elif -b
    #                 a <- test(4, 5)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 204))

    # def test_parser_5(self):
    #     input = """number x <- 0

    #     func test(number a, number b, string c)
    #         return a + b

    #     string y <- "test Parse"

    #     func main()
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 a <- a - (b - c) * ab
    #             elif -b
    #                 a <- a - (b - c) * ab
    #         end

    #     func add(string parse, string lexer)
    #         begin
    #             if a == b
    #                 a <- b
    #             elif -a
    #                 test(3, 4, "vietnam")
    #             elif -b
    #                 a <- test(4, 5)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 205))

    # def test_parser_6(self):
    #     input = """func isPrime(number x)

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if x <= 1 return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 206))

    # def test_parser_7(self):
    #     input = """func main() begin
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 207))

    # def test_parser_8(self):
    #     input = """func isPrime(number x)

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if (x <= 1) or (x > 5) and x != 6 return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 208))

    # def test_parser_9(self):
    #     input = """func isPrime(number x)
    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if x <= 1 or x > 5 and x != 6 return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "Error on line 11 col 31: >"
    #     self.assertTrue(TestParser.test(input, expect, 209))

    # def test_parser_10(self):
    #     input = """func isPrime(number x)

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if x + 5 > a - 2 and x != 6 return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "Error on line 12 col 39: !="
    #     self.assertTrue(TestParser.test(input, expect, 210))

    # def test_parser_11(self):
    #     input = """number a <- 5

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if (x + 5 > a - 2) and x != 6 return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 211))

    # def test_parser_12(self):
    #     input = """number a <- 5

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if x + 5 > (a - 2 and x != 6) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 212))

    # def test_parser_13(self):
    #     input = """number a <- 5

    #     func main()
    #         begin
    #             number x <- readNumber()
    #             if isPrime(x) printString("Yes")
    #             else printString("No")
    #         end

    #     func isPrime(number x)
    #         begin
    #             if x + 5 > ((a - 2 > 0) and (x != 6)) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 begin
    #                     if x % i = 0 return false
    #                 end
    #             return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 213))

    # def test_parser_14(self):
    #     input = """func main(number x)
    #         begin
    #             if x + 5 > ((a - 2 > 0) and (x != 6)) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 214))
    
    # def test_parser_15(self):
    #     input = """func main(number x)
    #         begin
    #             if x + 5 > ((a - 2 > 0) and (x != 6)) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 215))

    # def test_parser_16(self):
    #     input = """func main(number x)
    #         begin
    #             number a[5] <- [1, 2, 3, 4, 5]
    #             number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 216))

    # def test_parser_17(self):
    #     input = """func main(number x)
    #         begin
    #             number a[5] <- 5
    #             number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "Error on line 3 col 31: 5"
    #     self.assertTrue(TestParser.test(input, expect, 217))
        
    # def test_parser_18(self):
    #     input = """func main(number x)
    #         begin
    #             number a[5] <- [1, 2, 3, 4, 5]
    #             number b[2, 3] <- "abc"
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "Error on line 4 col 34: abc"
    #     self.assertTrue(TestParser.test(input, expect, 218))

    # def test_parser_19(self):
    #     input = """func main(number x)
    #         begin
    #             number a <- [1, 2, 3, 4, 5]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "Error on line 3 col 28: ["
    #     self.assertTrue(TestParser.test(input, expect, 219))

    # def test_parser_20(self):
    #     input = """func main(number x)
    #         begin
    #             string a[5] <- ["1", "2", "3", "4", "5"]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 220))

    # def test_parser_21(self):
    #     input = """func main(number x)
    #         begin
    #             string a[5] <- [true, false, 3 + 1, false, true]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 221))

    # def test_parser_22(self):
    #     input = """func main(number x)
    #         begin
    #             string a[3, 2] <- [[2, 3], [3, 4], [4, 5]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 222))

    # def test_parser_23(self):
    #     input = """func main(number x)
    #         begin
    #             string a[1] <- [[2, 3]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 223))

    # def test_parser_24(self):
    #     input = """func main(number x)
    #         begin
    #             string a[4, 2] <- [[2, 3], [3, 4], [4, 5], [5, 6]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 224))

    # def test_parser_25(self):
    #     input = """func main(number x)
    #         begin
    #             string a[4, 3] <- [[2, 3, 1], [3, 4], [4, 5, 2], [5, 6]]
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #                 writeNumbe(i)
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 225))

    # def test_parser_26(self):
    #     input = """func main() return 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 226))

    # def test_parser_27(self):
    #     input = """func main() begin
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 227))

    # def test_parser_28(self):
    #     input = """func main() begin
    #     for i until i>3 by 1
    #     if (a>3) writeNumber(a)
    #     elif (a>2) writeNumber(a)
    #     else break
    #     readBool()




    #     var x <- 3/2+a[7]
    #     end
    #     func foo(number a) return 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 228))

    # def test_parser_29(self):
    #     input = """func main() 
    #     begin
    #     number a[7] <- [1,2,3,4,5,6,7]
    #     number b[3,7] <- [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]

    #     a[0] <- 325 + 7
    #     a[1] <- 2*3+7/5-45
    #     a[foo(3)+7*9] <- "Anh yeu em pac pac"

    #     end
    #     func foo(number a) return 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 229))

    # def test_parser_30(self):
    #     input = """
    #         func areDivisors(number num1, number num2)
    #         return true
    #         func main()
    #         begin
    #         var num1 <- readNumber()
    #         var num2 <- readNumber()
    #         if (areDivisors(num1, num2)) printString("mbnmb")
    #         else printString("No")
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 230))

    # def test_parser_31(self):
    #     input = """
    #             func isPrime(number x)
    #             func main()
    #             begin
    #             number x <- readNumber()
    #             if (isPrime(x)) printString("dgdfg")
    #             else printString("No")
    #             end

    #             func isPrime(number x)
    #             begin
    #             if (x <= 1) return false
    #             var i <- 2
    #             for i until i > x / 2 by 1
    #             begin
    #             if (x % i = 0) return false
    #             end
    #             return true
    #             end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 231))

    # def test_parser_32(self):
    #     input = """func main(number arg)
    #     begin
    #         number b[2,3] <- [[1+2, 3+5, foo(3)], [foo(15*27/32),"j\' aime la france", "comment allez vous"]]

    #         number array[2,2] <- [[not true, not false, foo(3) or foo(4)], [not balance, you and i]]

    #         for z until foo(z) == "error" by 1 
    #             begin
    #                 printString("OMG")

    #                 for i until i < 100 by 2
    #                     begin
    #                         printString("Bonne anne\'e !")
    #                         readNumber()
    #                         writeNumber(32)
    #                         readBool()
    #                         writeBool(true)

    #                         readString()

    #                         if (a=2) 
    #                             begin
    #                                 printString("Bonjour")
    #                             end
    #                     end
    #             end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 232))

    # def test_parser_33(self):
    #     input = """func main()
    #     begin
    #     if (a>=17) printString("456")

    #     elif (a>12) printString("mbbmbn")

    #     elif (a=6) readString() ## else return 32        

    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 233))

    # def test_parser_34(self):
    #     input = """func main()
    #     begin
    #     if (a>=17) 
    #         printString("456")

    #     elif (a>12) printString("mbbmbn")

    #     elif (a=6) main()      

    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 234))

    # def test_parser_35(self):
    #     input = """func main()
    #     begin
    #     if (a>=17) 
    #         printString("456")

    #     elif (a>12)
    #         printString("mbbmbn")

    #     elif (a=6) main()       

    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 235))

    # def test_parser_36(self):
    #     input = """func main()
    #     begin
    #     if (a>=17) 
    #         printString("456")

    #     elif (a>12)
    #         printString("mbbmbn")

    #     else main()       

    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 236))

    # def test_parser_37(self):
    #     input = """func main()
    #     begin
    #     if (a>=17) 
    #         printString("456")

    #     elif (a>12)
    #         printString("mbbmbn")

    #     else
    #         main()       

    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 237))

    # def test_parser_38(self):
    #     input = """a <- 4
    #     func main()
    #     begin
    #     if (a>=17) 
    #         printString("456")

    #     elif (a>12)
    #         printString("mbbmbn")

    #     else
    #         main()       

    #     end
    #     """
    #     expect = "Error on line 1 col 0: a"
    #     self.assertTrue(TestParser.test(input, expect, 238))

    # def test_parser_39(self):
    #     input = """if (a>=17) 
    #         printString("456")

    #     elif (a>12)
    #         printString("mbbmbn")

    #     else
    #         main()   
    #     func main()
    #     begin

    #     end
    #     """
    #     expect = "Error on line 1 col 0: if"
    #     self.assertTrue(TestParser.test(input, expect, 239))

    # def test_parser_40(self):
    #     input = """
    #     func main()
    #     begin
    #         string a, b, c
    #     end
    #     """
    #     expect = "Error on line 4 col 20: ,"
    #     self.assertTrue(TestParser.test(input, expect, 240))

    # def test_parser_41(self):
    #     input = """
    #     func main()
    #     begin
    #         bool a, b, c
    #     end
    #     """
    #     expect = "Error on line 4 col 18: ,"
    #     self.assertTrue(TestParser.test(input, expect, 241))

    # def test_parser_42(self):
    #     input = """
    #     func main()
    #     begin
    #         var a, b, c
    #     end
    #     """
    #     expect = "Error on line 4 col 17: ,"
    #     self.assertTrue(TestParser.test(input, expect, 242))

    # def test_parser_43(self):
    #     input = """
    #     func main()
    #     begin
    #         var a
    #     end
    #     """
    #     expect = "Error on line 4 col 18: \n"
    #     self.assertTrue(TestParser.test(input, expect, 243))

    # def test_parser_44(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- "string"
    #         var b <-
    #     end
    #     """
    #     expect = "Error on line 5 col 21: \n"
    #     self.assertTrue(TestParser.test(input, expect, 244))

    # def test_parser_45(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             begin
    #                 var test <- 5
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 1
    #                     end
    #             end
    #         elif a > 20
    #             begin
    #                 var test <- 10
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 2
    #                     end
    #             end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 245))

    # def test_parser_46(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             begin
    #                 var test <- 5
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 1
    #                     end
    #             end
    #         elif a > 20
    #             begin
    #                 var test <- 10
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 2
    #                     end
    #             end
    #         else print("end")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 246))

    # def test_parser_47(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             begin
    #                 var test <- 5
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 1
    #                     end
    #             end
    #         elif a > 20
    #             begin
    #                 var test <- 10
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 2
    #                     end
    #             end
    #         else
    #             begin
    #                 var test <- 15
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 3
    #                     end
    #             end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 247))

    # def test_parser_48(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             begin
    #                 var test <- 5
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 1
    #                     end
    #             end
    #         elif a > 20 print(123)
    #         else
    #             begin
    #                 var test <- 15
    #                 for i until i > 0 by -1
    #                     begin
    #                         sum <- sum + 3
    #                     end
    #             end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 248))

    # def test_parser_49(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #         elif a > 20 
    #             if a > 40
    #                 print("2")
    #         else
    #             if a > 5
    #                 print("3")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 249))

    # def test_parser_50(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50 if a > 70
    #             print("1")
    #         elif a > 20 if a > 40
    #             print("2")
    #         else if a > 5
    #             print("3")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 250))

    # def test_parser_51(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #             else
    #                 print("Hi")
    #         elif a > 20 if a > 40
    #             print("2")
    #         else if a > 5
    #             print("3")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 251))

    # def test_parser_52(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #             else
    #                 print("Hi")
    #         elif a > 20
    #             if a > 40
    #                 print("2")
    #             else
    #                 print("Hello")
    #         else
    #             if a > 5
    #                 print("3")
    #             else
    #                 print("Bye")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 252))

    # def test_parser_53(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #             else
    #                 print("Hi")
    #         elif a > 20
    #             if a > 40
    #                 print("2")
    #             elif
    #                 print("4")
    #             else
    #                 print("Hello")
    #         else
    #             if a > 5
    #                 print("3")
    #             else
    #                 print("Bye")
    #     end
    #     """
    #     expect = "Error on line 13 col 21: \n"
    #     self.assertTrue(TestParser.test(input, expect, 253))

    # def test_parser_54(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #             else
    #                 print("Hi")
    #             a <- 32
    #         elif a > 20
    #             if a > 40
    #                 print("2")
    #             elif (a > 30) or (a <= 25)
    #                 print("4")
    #             else
    #                 print("Hello")
    #         else
    #             if a > 5
    #                 print("3")
    #             else
    #                 print("Bye")
    #     end
    #     """
    #     expect = "Error on line 11 col 12: elif"
    #     self.assertTrue(TestParser.test(input, expect, 254))

    # def test_parser_55(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             a <- 32
    #         elif a > 20
    #             return 23
    #             if a > 40
    #                 print("2")
    #             elif (a > 30) or (a <= 25)
    #                 print("4")
    #             else
    #                 print("Hello")
    #         else
    #             if a > 5
    #                 print("3")
    #             else
    #                 print("Bye")
    #     end
    #     """
    #     expect = "Error on line 15 col 12: else"
    #     self.assertTrue(TestParser.test(input, expect, 255))

    # def test_parser_56(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a <- "string"
    #         dynamic b
    #         dynamic c <- 123
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 256))

    # def test_parser_57(self):
    #     input = """dynamic a <- 123
    #     func main()
    #     begin
    #         number sum <- 0
    #         if a > 50
    #             if a > 70
    #                 print("1")
    #             else
    #                 print("Hi")
    #         elif a > 20
    #             if a > 40
    #                 print("2")
    #             elif (a > 30) or (a <= 25)
    #                 print("4")
    #             else
    #                 print("Hello")
    #         else
    #             if a > 5
    #                 print("3")
    #             else
    #                 print("Bye")
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 257))

    # def test_parser_58(self):
    #     input="""func printString() return \"haha\"
    #     func checkIfNameExist(number a, string str, number arr[32])
    #     begin
    #     if (a = 7) printString()
    #     else return arr[1/2%7]
    #     end
        
    #     func main(number arg[10]) 
    #     begin
    #     var a <- (not true) and (not (not false))
    #     bool b <- bool
    #     end

    #     """
    #     expect="Error on line 11 col 18: bool"
    #     self.assertTrue(TestParser.test(input,expect, 258))

    # def test_parser_59(self):
    #     input="""
    #     func greet(string name) 
    #     return "Hello, " ... name
        
    #     var greeting <- greet("John")
 
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 259))

    # def test_parser_60(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         var i <- 7 * 4 - 2009 + 25/4
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 260))

    # def test_parser_61(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         var a[4]
    #         a[0] <- 1
    #         a[foo(2)..."abc"] <- "2"
            
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="Error on line 5 col 17: ["
    #     self.assertTrue(TestParser.test(input,expect, 261))

    # def test_parser_62(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         var a[4] <- [1, 2, 3, 4]
    #         a[0] <- 1
    #         a[foo(2)..."abc"] <- "2"
            
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="Error on line 5 col 17: ["
    #     self.assertTrue(TestParser.test(input,expect, 262))

    # def test_parser_63(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         dynamic a[4] <- [1, 2, 3, 4]
    #         a[0] <- 1
    #         a[foo(2)..."abc"] <- "2"
    #         a[b[2, 3] / 2] <- true
    #         a[b[2, 3] + c[2]] <- true
            
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="Error on line 5 col 21: ["
    #     self.assertTrue(TestParser.test(input,expect, 263))

    # def test_parser_64(self):
    #     input="""
    #     func foo(number a[5], string check)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 2
    #                 begin
    #                     a[i] <- i * i - 5
    #                 end
    #             return -1
    #         end        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 264))

    # def test_parser_65(self):
    #     input="""
    #     func foo(number a[5], string check, var lol)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 2
    #                 begin
    #                     a[i] <- i * i - 5
    #                 end
    #             return -1
    #         end        
    #     """
    #     expect="Error on line 2 col 44: var"
    #     self.assertTrue(TestParser.test(input,expect, 265))

    # def test_parser_66(self):
    #     input="""
    #     func foo(number a, b)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 2
    #                 begin
    #                     a[i] <- i * i - 5
    #                 end
    #             return -1
    #         end        
    #     """
    #     expect="Error on line 2 col 27: b"
    #     self.assertTrue(TestParser.test(input,expect, 266))

    # def test_parser_67(self):
    #     input="""
    #     func foo(string a, b)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 2
    #                 begin
    #                     a[i] <- i * i - 5
    #                 end
    #             return -1
    #         end        
    #     """
    #     expect="Error on line 2 col 27: b"
    #     self.assertTrue(TestParser.test(input,expect, 267))

    # def test_parser_68(self):
    #     input="""
    #     func foo(dynamic a)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 2
    #                 begin
    #                     a[i] <- i * i - 5
    #                 end
    #             return -1
    #         end        
    #     """
    #     expect="Error on line 2 col 17: dynamic"
    #     self.assertTrue(TestParser.test(input,expect, 268))

    # def test_parser_69(self):
    #     input="""
    #     string str <- "LOL"

    #     number x <- a[1+2,15/32*4] + -32 * 45 + not true

    #     func superman() begin
    #     number a[3,2] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 269))

    # def test_parser_70(self):
    #     input="""
    #     number abc <- 123456

    #     string abc = 123

    #     func superman() begin
    #     number a[3,2] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="Error on line 4 col 19: ="
    #     self.assertTrue(TestParser.test(input,expect, 270))

    # def test_parser_71(self):
    #     input="""
    #     number abc[12.9] <- 123456

    #     func superman() begin
    #     number a[3,2] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="Error on line 2 col 28: 123456"
    #     self.assertTrue(TestParser.test(input,expect, 271))

    # def test_parser_72(self):
    #     input="""
    #     number abc[12.9] <- [123456]

    #     func superman() begin
    #     number a[3,2] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 272))

    # def test_parser_73(self):
    #     input="""
    #     dynamic a <- 0
    #     number b <- 199
    #     number c <- 12.
    #     var d <- 12.3
    #     var e <- -12.3e1500000 - 3015
    #     number f <- 12e-15 * 15 / 27 and (15<32) = 1

    #     string frank_sinatra <- "fly me to the moon "..."lala\f" ##comment

    #     bool check <- true and not false and not true or not false or ((32>10)>0) = true

    #     bool boolean <- boo + bo + b

    #     func main(string str[30,31,32,33,34,35], string str2[0]) return str[1,2,3,4,5,5]

    #     string str[1]
        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 273))

    # def test_parser_74(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         number a[4] <- [1, 2, 3, 4]
    #         a[0] <- 1
    #         a[foo(3) + 4] <- "2"
    #         a[b[2, 3] / 2] <- true
    #         a[b[2, 3] + c[2]] <- true
            
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 274))

    # def test_parser_75(self):
    #     input="""
    #     func isPrime1(number x)
    #     begin
    #         if (x<=1) return false
    #         number a[4] <- [1, 2, 3, 4]
    #         a[0] <- 1
    #         a[foo(2)..."abc"] <- "2"
            
    #         for i until i > x/2 by 2
    #         begin
    #             if (x%i = 0)
    #             begin
    #                 printString("Break")
    #                 break
    #             end
    #         end 
    #     return true
    #     end      
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 275))

    # def test_parser_76(self):
    #     input="""
    #     func main(string str) begin
    #     bool c <- 32 > 10 > 8
    #     end  
    #     """
    #     expect="Error on line 3 col 26: >"
    #     self.assertTrue(TestParser.test(input,expect, 276))

    # def test_parser_77(self):
    #     input="""
    #     func axl_Rose(string str) return "guns\' n\' roses"

    #     func main() begin
    #     string f <- writeString()
    #     end     
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 277))

    # def test_parser_78(self):
    #     input="""
    #     func axl_Rose(string str) return "guns\' n\' roses"

    #     func main() begin
    #     string f <- writeString()
    #     end     
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 278))

    # def test_parser_79(self):
    #     input="""
    #     func main() begin
    #         number arr[abc()] <- [1, 2, 3]
    #     end     
    #     """
    #     expect="Error on line 3 col 26: ("
    #     self.assertTrue(TestParser.test(input,expect, 279))

    # def test_parser_80(self):
    #     input="""
    #     func main() begin
    #         number arr["abc"] <- [1, 2, 3]
    #     end     
    #     """
    #     expect="Error on line 3 col 23: abc"
    #     self.assertTrue(TestParser.test(input,expect, 280))

    # def test_parser_81(self):
    #     input="""
    #     string str <- "LOL"

    #     var x <- a[1+2,15/32*4] + -32 * 45 + not true

    #     func superman() begin
    #     var a[3,2] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="Error on line 7 col 13: ["
    #     self.assertTrue(TestParser.test(input,expect, 281))

    # def test_parser_82(self):
    #     input="""
    #     string str <- "LOL"

    #     var x <- a[1+2,15/32*4] + -32 * 45 + not true

    #     func superman() begin
    #     number a[3.5, 2.3e-3] <- [[1,2],[3,4],[5,6]]
    #     end        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 282))

    # def test_parser_83(self):
    #     input="""
    #     dynamic a <- 0
    #     number b <- 479
    #     number c <- 17.
    #     var d <- 12.3
    #     var e <- 12.3e1505600 - 132015
    #     number f <- 12e-15 * 15 / 27
    #     string str <- "Ip20202020 \t\f"
    #     func main(string a)
    #     begin
    #         ## comment
    #         var a <- "str" ## superman 
    #         ## this is a comment too >>>> <<<<<<<xxxxx
    #         number a[5] <- [3+2/7*18%(32),30e-7-15,110.20e+15]


    #     end
    #     ## Ya YA YA Ya yohohohoho

        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 283))
        
    # def test_parser_84(self):
    #     input="""number abvcvc
    #     number k <- 30045454
    #     number p <- 20054545

    #     string str <- "Bao tien mot mo binh yen"


    #     dynamic dynamite <- "BigBang"..."VIP"
    #     bool check <- not not (not false) and not true or false or true or (300 <= 90) and (30 > 90) > 70 and (("con meo" != "con su tu") = ("Om" == "thin"))

    #     bool compare <- (30e-7>20e20)

    #     func main() return true

    #     func ya(string str, number b)
    #     begin

    #     var a<- 3+7 

    #     var b<- 61+92-120-220/320%125
    #     end


    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 284))

    # def test_parser_85(self):
    #     input="""func main(string a)
    #     begin
    #     ## comment
    #     var a <- "str" ## this is a comment
    #     ## this is a comment too >>>> <<<<<<<xxxxx
    #     number a[5] <- [3+2/7*18%(32),30e-7-15,110.20e+15]


    #     end
    #     ## Ya YA YA Ya yohohohoho

        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 285))
        
    # def test_parser_86(self):
    #     input="""func main(string a)
    #     begin
    #     ## comment
    #     var a <- "str" ## this is a comment
    #     ## this is a comment too >>>>
    #     for a until a<3000 by 1
    #     begin
    #     printString("I love you")
    #     end
    #     printString("I love you 3000")
    #     end

    #     func isPrime(number x)
    #     begin
    #     if (x<=1) return false
    #     var i<-2
    #     for i until i>x/2 by 1 
    #     begin
    #     if (x % i = 0) return false
    #     end

    #     return true
    #     end

    #     func isLove(string str) return \"je tre\'s aime\' tu\"
    #     func isDead(string str) return \"je vais a\' Paris pour regarder toi\"
    #     func isLive(number a, string f, number a[100])
    #     begin
    #     if (a>500) isLove()
    #     elif (a>400) isDead()
    #     elif (a>300) isLive()
    #     else

    #     return 3
    #     end
        
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect, 286))
        
    # def test_parser_87(self):
    #     input="""
    #     func foo2(number x, string str, number a[254])
    #     func foo1(number x) return [1,2,3,4,5]
    #     func main(number x) begin

    #     foo(3)[14] <- 32
    #     fallInLove("Em dang buon buon buon, buon hay vui")[true, false, true, not false] <- not false and true and not false and 125>232 or (322 = 110)
        
    #     end  
    #     """
    #     expect="Error on line 6 col 14: ["
    #     self.assertTrue(TestParser.test(input,expect, 287))

    # def test_parser_88(self):
    #     input = """func main()
    #     begin
    #         if (a > 8) printString("32")

    #         elif (a > 6) printString("hehe")

    #         elif (a = 62) readString() ## else return 321

    #         var z <- (120 >= 220) > 102 + 125 + (not fun) % 12e-25
    #         begin
    #             printString("Demcia")
    #             begin
    #                 begin
    #                 end
    #             end
    #         end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect, 288))
import unittest
from TestUtils import TestParser

  
class ParserSuite(unittest.TestCase):
    # 2115186
    # Please note thast some of these tests are not mine but it good enough to put it in here
    def test_declared(self): 
        # var declarations
        input = """ 
            var a <- 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))    
        
        input = """ 
            number a <- [10,10]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))  
        
        input = """ 
            dynamic a <- 20
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))  
        
        input = """ 
            var a[2] <- [20]
        """
        expect = "Error on line 2 col 17: \n"
        
        input = """ 
            string a[2] <- [20,30]
        """
        expect = "successful\n"
        
        input = """ 
            dynamic a[2] <- [20]
        """
        expect = "Error on line 2 col 21: ["
        
        self.assertTrue(TestParser.test(input, expect, 204))  
        
        input = """ 
            var a
        """
        expect = "Error on line 2 col 23: \n"
        
        input = """ 
            bool a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))   
        
        input = """ 
            dynamic a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))  
        
        input = """ 
            number a["string"]
        """
        expect = "Error on line 2 col 21: string"
        self.assertTrue(TestParser.test(input, expect, 208))  
        
        input = """ 
            number a[1,2,]
        """
        expect = "Error on line 2 col 25: ]"
        self.assertTrue(TestParser.test(input, expect, 209)) 
        
        input = """ 
            number a[[1]]
        """
        expect = "Error on line 2 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 210))
        
        input = """ 
            number a[1+2]
        """
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.test(input, expect, 211))
        
        
        input = """ 
            func main(number f1 <- c)
        """
        expect = "Error on line 2 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 212))       
        
        input = """ 
            func main()
            ## cm
            func main() var a ## cm
        """
        expect = "Error on line 4 col 24: var"
        self.assertTrue(TestParser.test(input, expect, 213))  

        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 214))   
        
        input = """ 
            func main(dynamic a)
        """
        expect = "Error on line 2 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 215))  
        
        input = """ 
            func main(number a)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))               

        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 217))   
        
        input = """ 
            func main(string s) 
                begin 
                    break ## 12
                end
            func main(dynamic b) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 218))    
        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 219))    
        
        input = """ 
            ##12
            func main(number a) 
                ##12
                ##12##12
                ###12
                begin 
                    break
                    break 
                    continue
                end
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))                  

        input = """ 
            ## 12
            
            var d <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))   
        
        input = """var d <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 222))  
        
        input = """var e <- 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223)) 

        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 224))  
                                   
    def test_Expression(self):
        """Expression"""
        input = """ var abcd <- "ab" ... "cd" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
        input = """ var www <- "www" ... 1 ... "www" 
        """
        expect = "Error on line 1 col 24: ..."
        self.assertTrue(TestParser.test(input, expect, 226))
        
        input = """ 
            var t <- 1 > "3" 
            var t <- 1 >= 3
            var t <- true = "true"
            var t <- false == "true"
            var t <- true < "true"
            var t <- 1 <= "tuan"
            var t <- tuan >= "ai" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        
        input = """ var a <- true > x >= z 
        """
        expect = "Error on line 1 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 228))
        
        input = """ 
            var b <- true and "true" or 1 
            var b <- 1 / 2 * 7 % 1
            var b <- 1 / 2 / 7 * 3 % 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        
        input = """var ta <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 31: >"
        self.assertTrue(TestParser.test(input, expect, 230)) 
           
        input = """ 
            var bv <- -1 * not 1
            var bv <- not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 
        
        input = """var VoTien <- - not - not true
        """
        expect = "Error on line 1 col 16: not"
        self.assertTrue(TestParser.test(input, expect, 232)) 
        
        input = """ 
            var arr <- array[1,3+2][1][2,3]
        """
        expect = "Error on line 2 col 35: ["
        self.assertTrue(TestParser.test(input, expect, 233))
        
        input = """var arr <- array[]
        """
        expect = "Error on line 1 col 17: ]"
        self.assertTrue(TestParser.test(input, expect, 234)) 
        
        input = """ 
            var a <- a()
            var a <- a(1,2)
            var a <- a(x,array[2])[2]
            var a <- a(x,y[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))    
        
        input = """var double <- a()()
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 236))  
        
        input = """ 
            var e <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))  

        input = """var woopss <- a[1]()
        """
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 238))         
        
    def test_Statements(self): # test 230 -> ...
        """Statements"""
        
        input = """
        ## comment
        func main()
            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240)) 
        
        input = """
        func main()
            begin
            aPI - 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: -"
        self.assertTrue(TestParser.test(input, expect, 241))
        
        input = """
        func main()
            begin
            aPI() <- 3.14
            end
        """
        expect = "Error on line 4 col 18: <-"
        self.assertTrue(TestParser.test(input, expect, 242))
        
        input = """
        func main()
            begin
            aPI[2]<- 3.14
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        input = """
        func main()
            begin   
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))  
        
        input = """
        func main()
            begin   
                if (api == 1)
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 245))  
        
        input = """
        func main()
            begin   
                if (api == 1) 
                else api <- 1
            end
        """
        expect = "Error on line 5 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 246))    
        
        input = """
        func main()
            begin   
                if (api == 1) api <- 2 
                else api <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))     
        
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                begin  
                    ## comment
                    break
                    break
                    continue
                    a <- 1
                end
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))    
        
        input = """
        func main() ## this was stollen from...
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 249))    

        input = """
        func main()
            begin
            for i*1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: *"
        self.assertTrue(TestParser.test(input, expect, 250)) 
        
        input = """
        func main()
        begin 
            continue ## dsa is good
            break
            for i until i >= 32 by 1 + 1 ... 1 / 1
                begin
                    break
                    continue
                end
            ## why am i here
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))  
        

        input = """
        func main()
            return 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

        input = """
        func main()
            begin
            main()
            main()
            mainy()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))  
        
        input = """
        func main()
            return foo()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))      
        
        input = """
        func main()
            return continue
        """
        expect = "Error on line 3 col 19: continue"
        self.assertTrue(TestParser.test(input, expect, 256)) 
        
        
        input = """
        func main()
        begin
            begin
            end
            begin
            end
            begin
            begin
            begin
            end
            end 
            end
        end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
     
    def test_NewLine(self): 
        """new line"""
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 259))        
        
        input = """var aPI <- 3.14 var a <- 1"""
        expect = "Error on line 1 col 16: var"
        self.assertTrue(TestParser.test(input, expect, 260))  
        
        input = """func main()
        begin
            if (1) break else break
        end
        """
        expect = "Error on line 3 col 25: else"
        self.assertTrue(TestParser.test(input, expect, 261))  
        
        input = """func main()
        begin
            begin end
        end
        """
        expect = "Error on line 3 col 18: end"
        self.assertTrue(TestParser.test(input, expect, 262)) 
        input = """func main()
        begin
            func f(number a)
        end
        """
        expect = "Error on line 3 col 12: func"
        self.assertTrue(TestParser.test(input, expect, 263)) 
  
    def test_Source_Code(self): 
        """Source_Code"""
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))   
        
        
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
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))  
        input = """
        func a() return true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))   
        
        nput = """
        func a() begin
            var a <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
        
        nput = """
        func a() 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        
        input = """
            number x <- x var y <- x
        """
        expect = "Error on line 2 col 26: var"
        self.assertTrue(TestParser.test(input, expect, 269)) 
                

        input = """    
        func foo()
        begin
            break break
        end
        """
        expect = "Error on line 4 col 18: break"
        self.assertTrue(TestParser.test(input, expect, 270)) 
        
        input = """    
        func foo()
        begin
            return 1 continue
        end
        """
        expect = "Error on line 4 col 21: continue"
        self.assertTrue(TestParser.test(input, expect, 271))   
        
        # input = """    
        # func a()
        # begin
        #     if (x + 1 > 36/2%3) return false
        #     if (x <= 1 )
        #         return false 
        #     else
        #         printString("\\ffff")
        # end ## comment
        # """
        # expect = "Error on line 7 col 17: \n"
        # self.assertTrue(TestParser.test(input, expect, 272))  
        
        input = """    
        func a()
        begin
            if (x <= 1) return false
            if (x <= 1 )
                return false 
            else return true
        end ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273)) 
        
        input = """    
        func a()
            fun()
        """
        expect = "Error on line 3 col 12: fun"
        self.assertTrue(TestParser.test(input, expect, 274))  
        
        input = """    
        func a()
            func()
        """
        expect = "Error on line 3 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 275))  
        
        input = """    
        var a <- var
        """
        expect = "Error on line 2 col 17: var"
        self.assertTrue(TestParser.test(input, expect, 276)) 
        
        input = """    
        var a <- 1 <- 1
        """
        expect = "Error on line 2 col 19: <-"
        self.assertTrue(TestParser.test(input, expect, 277)) 
        
        input = """    
        var a <- 1 + 1 ** 
        """
        expect = "Error on line 2 col 24: *"
        self.assertTrue(TestParser.test(input, expect, 278)) 
         
        
        input = """    
        func a()
            return return 1
        """
        expect = "Error on line 3 col 19: return"
        self.assertTrue(TestParser.test(input, expect, 279))  
        
        input = """     
        var a <- []
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 280))  
        
        input = """    
        func a(number a[1*1])
        """
        expect = "Error on line 2 col 25: *"
        self.assertTrue(TestParser.test(input, expect, 281))  
        
        input = """    
            var t <- a[1][2]
        """
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 282))  
        
        input = """    
            var t <- 1[2]
        """
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.test(input, expect, 283))  
        
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 284)) 
        
        input = """    
        func a()
            begin
                a["string"] <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285)) 
        
        
        input = """    
            var a <- [1,2,3][4]
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 286)) 
        
        input = """    
        func a()
            begin a <- 1
            end
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 287)) 
         
        
        input = """    
        func a()
            begin
                a()[1] <- 1
            end
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 288))      
          

        
        input = """    
        func a()
            begin
                hehehe[] <- 1
            end
        """
        expect = "Error on line 4 col 23: ]"
        self.assertTrue(TestParser.test(input, expect, 289))     
        
        input = """    
        func a()
            begin
                1 <- 2
            end
        """
        expect = "Error on line 4 col 16: 1"
        self.assertTrue(TestParser.test(input, expect, 290))     
        
        input = """    
            func a(string s["s"])
        """
        expect = "Error on line 2 col 28: s"
        self.assertTrue(TestParser.test(input, expect, 291))
           
        
        input = """    
            number a <- fun()[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))    
        
        
        input = """    
            func a()
            begin
                if 1 return true
            end
        """
        expect = "Error on line 4 col 19: 1"
        self.assertTrue(TestParser.test(input, expect, 293))    
        
        
        input = """    
            func a()
            begin
                if (1) return true
                elif 1 return true
            end
        """
        expect = "Error on line 5 col 21: 1"
        self.assertTrue(TestParser.test(input, expect, 294))  
        
        input = """    
            func a()
            begin
                if (1)  return true
                else a <- 1 return true
            end
        """
        expect = "Error on line 5 col 28: return"
        self.assertTrue(TestParser.test(input, expect, 295))  
        
        
        
        input="""
        func helloworld()
        begin
            writeString()
        end
        func main()
        begin
            helloworld() 
        end
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,296))
    
        
        input="""
        func checkOddEven(number n)
        begin
            if (n % 2 = 0) 
                return "Even"
            else return "Odd"
        end

        func main()
        begin
            number num <- 7
            string result <- checkOddEven(num)
            writeString(result)
        end
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,297))    
        

        input = """
        func compareArrays(number arr1[5], number arr2[5])
        begin
            if (length(arr1) != length(arr2)) 
                return "Arrays are not equal"

            number len <- length(arr1)
            number i <- 0

            for i until i < len by i + 1
                if (arr1[i] != arr2[i]) 
                    return "Arrays are not equal"
            return "Arrays are equal"
        end

        func main()
        begin
            number array1[5] <- [1, 2, 3, 4, 5]
            number array2[5] <- [1, 2, 3, 4, 5]

            string result <- compareArrays(array1, array2)
            writeString(result)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
        
        input="""
        ##aaaaaaaaa
        """
        expect="Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect, 299))
        
        input="""
        var a <- func()
        """
        expect="Error on line 2 col 17: func"
        self.assertTrue(TestParser.test(input,expect, 300))
        
    def test_simple_program57(self):
            input = """ 
            func createArray(number size)
            begin
                var arr[size] <- [1, 2, 3, 4, 5]  
            end
            """
            expect = "Error on line 4 col 23: ["
            self.assertTrue(TestParser.test(input, expect, 400))
                              
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
        if a>3 writeNumber(a)
        elif a>2 writeNumber(a)
        else break
        readBool()


        

        var x <- 3/2+a[7]
        end
        func foo(number a) return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    







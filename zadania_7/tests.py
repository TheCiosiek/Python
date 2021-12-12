from algorytmy import add, subtract, multiply, divide, Employee, calculate_savings,is_negative,is_numeric
import unittest
class Tests(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(1,2), 3, "Liczby dodatnie")
        self.assertEqual(add(-1,.2),-0.8, "Liczby mieszane")
        self.assertEqual(add(-1,-1),-2, "Liczby ujemne")
        self.assertEqual(add(0.4,2),2.4,"Liczby niecałkowite")
        self.assertEqual(add(0,0.3),0.3,"Działanie z zerem")
        self.assertEqual(add("13c",1),ValueError,"Input jako litera")
        self.assertEqual(add(1,"2.7.5"),ValueError,"Input jako litera")
        self.assertEqual(add(1,"--2.7"),ValueError,"Input jako litera")
        
    def testSubstract(self):
        self.assertEqual(subtract("1",2), -1, "Liczby dodatnie")
        self.assertEqual(subtract(-1,.2),-1.2, "Liczby mieszane")
        self.assertEqual(subtract(-1,-1),0, "Liczby ujemne")
        self.assertEqual(subtract(0.4,2),-1.6,"Liczby niecałkowite")
        self.assertEqual(subtract(0,0.3),-0.3,"Działanie z zerem")
        self.assertEqual(subtract("13c",1),ValueError,"Input jako litera")
        self.assertEqual(subtract(1,"2.7.5"),ValueError,"Input jako litera")
        self.assertEqual(subtract(1,"--2.7"),ValueError,"Input jako litera")

    def testMultiply(self):
        self.assertEqual(multiply("1",2), 2, "Liczby dodatnie")
        self.assertEqual(multiply(-1,.2),-0.2, "Liczby mieszane")
        self.assertEqual(multiply(-1,-1),1, "Liczby ujemne")
        self.assertEqual(multiply(0.4,2),0.8,"Liczby niecałkowite")
        self.assertEqual(multiply(0,0.3),0,"Działanie z zerem")
        self.assertEqual(multiply("13c",1),ValueError,"Input jako litera")
        self.assertEqual(multiply(1,"2.7.5"),ValueError,"Input jako litera")
        self.assertEqual(multiply(1,"--2.7"),ValueError,"Input jako litera")
    
    def testDivide(self):
        self.assertEqual(divide("1",2), 0.5, "Liczby dodatnie")
        self.assertEqual(divide(-1,2),-0.5, "Liczby mieszane")
        self.assertEqual(divide(-1,-1),1, "Liczby ujemne")
        self.assertEqual(divide(0.4,2),0.2,"Liczby niecałkowite")
        self.assertEqual(divide(0,0.3),0,"Działanie z zerem")
        self.assertEqual(divide(1,0),ValueError,"Działanie z zerem, odwrócone")
        self.assertEqual(divide("13c",1),ValueError,"Input jako litera")
        self.assertEqual(divide(1,"2.7.5"),ValueError,"Input jako litera")
        self.assertEqual(divide(1,"--2.7"),ValueError,"Input jako litera")

class Test_Employee(unittest.TestCase):
    def test_introduce(self):
        user1=Employee("steve", "wonder", 19,2100)
        self.assertEqual(user1.introduce_self(),'My name is steve wonder and I am 19 years old')
    def test_salary(self):
        user1=Employee("steve", "wonder", 19,2100)
        user1.raise_salary(5)
        self.assertEqual(user1.salary,10500)
    def test_age(self):
        user1=Employee("steve", "wonder", 19,2100)
        self.assertEqual(user1.check_age(),'Adult employee')
        user1.age=17
        self.assertEqual(user1.check_age(), 'Underage employee')
    def test_email(self):
        user1=Employee("steve", "wonder", 19,2100)
        self.assertEqual(user1.get_email(), "stevewonder@company.com")

class Test_Numeric(unittest.TestCase):
    def test_numeric(self):
        self.assertTrue(is_numeric(75))
        self.assertTrue(is_numeric(-75))
        self.assertTrue(is_numeric(-0.73))
        self.assertTrue(is_numeric(0.73))
        self.assertTrue(is_numeric(-.73))
        self.assertTrue(is_numeric(.73))
        self.assertTrue(is_numeric(".73"))
        self.assertTrue(is_numeric("-.73"))
        self.assertFalse(is_numeric("..73"))
        self.assertFalse(is_numeric("--.73"))
        self.assertFalse(is_numeric("0.73."))
        self.assertFalse(is_numeric("13c"))
class Tests_negative(unittest.TestCase):
    def test_negative(self):
        self.assertTrue(is_negative(-7))
        self.assertFalse(is_negative(0))
        self.assertFalse(is_negative(7))
class Tests_savings(unittest.TestCase):
    def test_savings(self):
        self.assertEqual(calculate_savings(1000,700,100), 8200)
        self.assertEqual(calculate_savings("1000",700,100.0), 8200)
        self.assertEqual(calculate_savings(1000,0,.100), 998.8)
        self.assertEqual(calculate_savings(000,0,.100), -1.2)
        self.assertEqual(calculate_savings(1000,700,"0..01"), ValueError)
        self.assertEqual(calculate_savings("13c",700,100), ValueError)
        self.assertEqual(calculate_savings(1000,"13c",100), ValueError)
        self.assertEqual(calculate_savings(100,0.100,-.100), ValueError)
        self.assertEqual(calculate_savings(-100,0.100,.100), ValueError)
        self.assertEqual(calculate_savings(100,-0.100,.100), ValueError)
unittest.main()

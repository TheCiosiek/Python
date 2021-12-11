from algorytmy import add, subtract, multiply, divide
from algorytmy import Employee
import unittest

class Tests(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(1,2), 3, "Liczby dodatnie")
        self.assertEqual(add(-1,2),1, "Liczby mieszane")
        self.assertEqual(add(-1,-1),-2, "Liczby ujemne")
        self.assertEqual(add(0.4,2),2.4,"Liczby niecałkowite")
        self.assertEqual(add(0,0.3),0.3,"Działanie z zerem")
        self.assertEqual(add("e","l"),ValueError,"Input jako litera")
    def testSubstract(self):
        self.assertEqual(subtract(1,2), -1, "Liczby dodatnie")
        self.assertEqual(subtract(-1,2),-3, "Liczby mieszane")
        self.assertEqual(subtract(-1,-1),0, "Liczby ujemne")
        self.assertEqual(subtract(0.4,2),-1.6,"Liczby niecałkowite")
        self.assertEqual(subtract(0,0.3),-0.3,"Działanie z zerem")
        self.assertEqual(add("e",1),ValueError,"Input jako litera")
    def testMultiply(self):
        self.assertEqual(multiply(1,2), 2, "Liczby dodatnie")
        self.assertEqual(multiply(-1,2),-2, "Liczby mieszane")
        self.assertEqual(multiply(-1,-1),1, "Liczby ujemne")
        self.assertEqual(multiply(0.4,2),0.8,"Liczby niecałkowite")
        self.assertEqual(multiply(0,0.3),0,"Działanie z zerem")
        self.assertEqual(add("e",1),ValueError,"Input jako litera")
    def testDivide(self):
        self.assertEqual(divide(1,2), 0.5, "Liczby dodatnie")
        self.assertEqual(divide(-1,2),-0.5, "Liczby mieszane")
        self.assertEqual(divide(-1,-1),1, "Liczby ujemne")
        self.assertEqual(divide(0.4,2),0.2,"Liczby niecałkowite")
        self.assertEqual(divide(0,0.3),0,"Działanie z zerem")
        self.assertEqual(divide(1,0),ValueError,"Działanie z zerem, odwrócone")
        self.assertEqual(add("e","l"),ValueError,"Input jako litera")

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
unittest.main(verbosity=0)
        
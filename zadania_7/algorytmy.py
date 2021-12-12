import math
def is_numeric(x):
    x=str(x)
    i=1
    length=len(x)
    wasDot=0
    if ord(x[0])==45:
        pass
    elif ord(x[0]) in range (48,58):
        pass
    elif ord(x[0])==46:
        wasDot=1
        pass
    else:
        return False
    while i<length:
        if ord(x[i]) in range (48,58):
            pass
        elif ord(x[i])==46 and wasDot==0:
            wasDot=1
        else:
            return False
        i+=1
    return True

def add(x, y):
    if is_numeric(x) and is_numeric(y):
        x=float(x)
        y=float(y)
        return x+y
    else:
        return ValueError

def subtract(x, y):
    if is_numeric(x) and is_numeric(y):
        x=float(x)
        y=float(y)
        return x-y
    else:
        return ValueError

def multiply(x, y):
    if is_numeric(x) and is_numeric(y):
        x=float(x)
        y=float(y)
        return x*y
    else:
        return ValueError

def divide(x, y):
    try:
        if y == 0:
            raise ValueError('Can not divide by zero!')
    except:
        return ValueError
    if is_numeric(x) and is_numeric(y):
        x=float(x)
        y=float(y)
        return x/y
    else:
        return ValueError


class Employee:
    def __init__(self, first, last, age, salary):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.salary = salary
        
    def introduce_self(self):
        return f'My name is {self.first_name} {self.last_name} and I am {self.age} years old'
    
    def raise_salary(self, ratio):
        self.salary = self.salary * ratio
    def check_age(self):
        if self.age < 18:
            return 'Underage employee'
        else:
            return 'Adult employee'
        
    def get_email(self):
        return f'{self.first_name}{self.last_name}@company.com'

def is_negative(num):
    return num<0
def calculate_savings(starting_amount, monthly_payment, monthly_deductions): 
    if not is_numeric(starting_amount) or not is_numeric(monthly_payment) or not is_numeric(monthly_deductions): 
        return ValueError
    starting_amount, monthly_payment, monthly_deductions = float(starting_amount), float(monthly_payment), float(monthly_deductions)
    if is_negative(starting_amount) or is_negative(monthly_payment) or is_negative(monthly_deductions): 
        return ValueError 
    
    return round(starting_amount + 12 * (monthly_payment - monthly_deductions),2)
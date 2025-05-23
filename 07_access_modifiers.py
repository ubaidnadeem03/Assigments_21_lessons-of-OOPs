class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name #public variable
        self._salary = salary #protection variable
        self.__ssn = ssn #private variable

emp = Employee("Ubaid", 50000, "123456789")


print(emp.name) #accessing public variable
print(emp._salary) #accessing protection variable
print(emp.__ssn) #accessing private variable pass the error because attributes is private and its show on terminal undefined.
#for accessing a private variable we can use _Employee__ssn but this is not a right way to do it.
# print(emp._Employee__ssn)   
#  # if you want to accessing the private variable you can uncommit the upper line.
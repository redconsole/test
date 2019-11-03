class Employee:

    applied_ratio = 1.05

    def __init__(self, first_name,last_name , age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.email = f"{str(self.first_name).lower()}.{str(self.last_name).lower()}@tcs.com"

    def apply_ratio(self):
        return self.salary * Employee.applied_ratio

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first, last = str(name).split(' ')
        self.first_name = first
        self.last_name = last

    # @full_name.getter
    # def full_name(self):
    #     return 'Hello'
    #
    @classmethod
    def new_instance(cls, employee):
        first_name, last_name, age, salary = employee.split('-')
        return cls(first_name, last_name, age, salary)


class Developer(Employee):
    pass


class Manager(Employee):
    pass


employee1 = Employee('Narendra', 'Kashyap', 35, 80000);
employee2 = Employee('Vishesh', 'Sharma', 36, 70000);
print(employee1.email)
print(employee1.full_name)

employee1.full_name = 'Naren Kashyap'
print(employee1.email)

name = employee1.full_name
print(name)

print(employee1.apply_ratio())
print(employee2.apply_ratio())

emp1_str = 'Mayank-Singh-32-75000';
emp1 = Employee.new_instance(emp1_str)
print(emp1.full_name)





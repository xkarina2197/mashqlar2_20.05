# 8-misol
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age =new_age


a1 = Animal('Sher', 5)

res = a1.age
print(res)

a1.age = 16
print(a1.age)


# 9-misol
class Game:
    def __init__(self, title, level):
        self.title = title
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level):
        self.__level = new_level

g1 = Game('Minecraft', 10)

res = g1.level
print(res)

g1.level = 14
print(g1.level)

# 10-misol
class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__rooms = rooms

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, new_rooms):
        self.__rooms = new_rooms

h1 = Hospital('Shifo', 50)

res = h1.rooms
print(res)

h1.rooms = 13
print(h1.rooms)


# 11-misol
class Market:
    def __init__(self, name, income):
        self.name = name
        self.__income = income

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, new_income):
        self.__income = new_income

m1 = Market('Korzinka', 100000)

res = m1.income
print(res)

m1.income = 150000
print(m1.income)


# 12-misol
class Employee:
    def __init__(self, fullname, experince):
        self.fullname = fullname
        self.__experince = experince

    @property
    def experince(self):
        return self.__experince

    @experince.setter
    def experince(self, new_experince):
        self.__experince = new_experince

e1 = Employee('Rustam Aliyev', 3)

res = e1.experince
print(res)

e1.experince = 5
print(e1.experince)


# 13-misol
class School:
    def __init__(self, school_name, students):
        self.school_name = school_name
        self.students = students

    @property
    def students(self):
        return self.students

    @students.setter
    def students(self, new_students):
        self.students = new_students

s1 = School('45-maktab', 800)

res = s1.students
print(res)

s1.students = 905
print(s1.students)

# 14-misol
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, new_pages):
        self.__pages = new_pages

b1 = Book('Python asoslari', 250)

res = b1.pages
print(res)

b1.pages = 456
print(b1.pages)

# 15-misol
class Company:
    def __init__(self, company_name, worker):
        self.company_name = company_name
        self.__worker = worker

    @property
    def worker(self):
        return self.__worker

    @worker.setter
    def worker(self, new_worker):
        self.__worker = new_worker

c1 = Company('Google', 150000)

res = c1.worker
print(res)

c1.worker = 34590
print(c1.worker)

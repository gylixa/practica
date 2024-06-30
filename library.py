class Person:
    def __init__(self, fam, name, surname, department, days, salary):
        self.fam = fam
        self.name = name
        self.surname = surname
        self.department = int(department)
        self.days = int(days)
        self.salary = int(salary)

    def getPerson_forTable(self):
        w = []
        print(self.fam+' '+self.name+' '+self.surname)
        x = self.fam+' '+self.name+' '+self.surname
        w.append(x)
        w.append(self.department)
        w.append(self.days)
        w.append(self.salary)
        print(w)
        return w
    
    def equval_Person(self, B):
        return self.fam == B.fam and \
               self.name == B.name and \
               self.surname == B.surname and \
               self.department == B.department and \
               self.days == B.days and \
               self.salary == B.salary
    
class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in range(len(self.A)):  
            if x in self.A: 
                s += f'Person {x+1}:n'
                s += str(self.A[x])
                s += 'n'
        return s

    def appendPerson(self, List):
        new_Person = Person(*List)
        self.A[self.count] = new_Person
        self.count += 1

    def editPerson(self, x, List):
        P = Person(*List)
        self.A[x] = P

    def Str_Person(self, line):
        if line[-1] == 'n' : line = line[:-1] 
        parts = line.strip().split(";")
        return Person(*parts)

    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line[-1] == 'n':
                    line = line[:-1]
                parts = line.strip().split(";")
                self.A[x] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                x += 1
                self.count += 1

    def find_keyPerson(self, List):
        P = Person(*List)
        for x in self.A:
            if self.A[x].equval_Person(P):
                return x
        return -1

    def delPerson(self, List):
        P = Person(*List)
        for x in self.A:
            if self.A[x].equval_Person(P):
                del self.A[x] 
                self.count = self.count - 1
                break




       

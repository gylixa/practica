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
        w.append(self.surname)
        w.append(self.days)
        w.append(self.salary)
        print(w)
        return w
    
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

    def appendPerson(self, str_Person):
        parts = str_Person.strip().split(" ")
        print("!!!", str_Person) 
        self.A[self.count] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])

        self.count += 1

    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line[-1] == 'n':
                    line = line[:-1]
                parts = line.strip().split(" ")

                self.A[x] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])

                x += 1
                self.count += 1



       

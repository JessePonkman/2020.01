class Person:
    def __init__(self, name, age, apellido, telefono):
        self.name = name
        self.age = age
        self.apellido = apellido
        self.telefono = telefono

      #agrego diccionario a person  
    def get_person(self):
        Person = {"name":self.name, "age":self.age, "apellido":self.apellido, "telefono":self.telefono}
        return Person
        #manera optima de hacerlo return self.__dict__
 
class Employee(Person):
    def __init__(self, name, age, salary, apellido, telefono):
        Person.__init__(self, name, age, apellido, telefono)
        self.salary = salary 

    def get_employee(self):
       Employee = {"name":self.name, "age":self.age, "salary":self.salary, "apellido":self.apellido, "telefono":self.telefono}
       return Employee

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"

if __name__ == "__main__":
    p = Person("Milagros", 19, "Tomba", 2615080491)
    personDic = p.get_person()
    print(p.get_person())
    #me tira un atributo del diccionario
    #print(personDic["name"])
    e = Employee("Milagros", 19, 30000, "Tomba", 2615080491)
    employeeDic = e.get_employee()
    print(e.get_employee())
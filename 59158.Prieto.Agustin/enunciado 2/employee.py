# declaramos la clase persona
class Person:
    # declaramos el metodo __init__ 
    def __init__(self, name, surname, age, cellphone):
        self.name = name
        self.age = age
        self.surname = surname
        self.cellphone = cellphone
 
    # Devuelve una lista con el nombre y la edad
    # return ["Claudio", 32]
    def get_person(self):
        return self.__dict__
 
 
# declaramos la clase Employee
# la clase empleado hereda los atributos y metodos de la clase Persona
class Employee(Person):
    # declaramos el metodo __init__ para Employee
    def __init__(self, name, surname, age, cellphone, salary):
        # llamamos al metodo init de la clase padre
        Person.__init__(self, name, surname, age, cellphone)
        # ingresamos salary para employee
        self.salary = salary
    

    # Devuelve una lista con los atributos
    # return ["Claudio", 32, 30000]
    def get_employee(self):
        return self.__dict__

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    # return "Paga impuestos" or "No paga impuestos"
    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"
 
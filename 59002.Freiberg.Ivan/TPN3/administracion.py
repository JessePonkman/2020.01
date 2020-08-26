from employee import Employee, Person

class Administration:
    listEmployee={}
    
    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'name':"Ivan",'surname':"Freiberg",'age':20,'phone':2615410198})
   adm.add_employee({'name':"Nicolas",'surname':"Pico",'age':30,'phone':2615410198})            
   print(adm.listEmployee)  
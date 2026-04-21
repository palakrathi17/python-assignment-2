class person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _introduce(self):
        print("name: ",self._name)
        print("age: ",self._age)
        
class employee(person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self._employee_id=employee_id
        self._salary=salary
    def _get_employee_info(self):
        print("name: ",self._name)
        print("age: ",self._age)
        print("employee id: ",self.employee_id)
        print("salary: ",self.salary)
        
class manager(employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self._department=department
    def _get_manager_info(self):
        print("name: ",self._name)
        print("age: ",self._age)
        print("employee id: ",self._employee_id)
        print("salary: ",self._salary)
        print("department: ",self._department)

x=manager("shivanee",20,1202,500000,"IT")
x._get_manager_info()
        



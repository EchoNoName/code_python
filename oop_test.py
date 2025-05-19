class Employee:
    def __init__(self, first_name, last_name, email, salary): # Base override
        self.first_name = first_name
        self.last_name = last_name
        self.__email = email
        self.__salary = salary
    
    @property
    def email(self): # Getter
        return self.__email
    
    @property
    def salary(self): # Getter
        return self.__salary
    
    def cry(self): # Method
        return f"{self.first_name} cried at worked today."

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Email: {self.email}, Salary: ${self.salary}"
# End of Employee

class Manager(Employee): # Single inheritance
    def __init__(self, first_name, last_name, email, salary, team_name): # Base override
        super().__init__(first_name, last_name, email, salary)
        self.team_name = team_name
        self.__team_list = set()
    
    @property
    def members(self): # Getter
        return self.__team_list
    
    def add(self, sales_person): # Method/Polymorphism
        self.__team_list.add(sales_person)
    
    def remove(self, sales_person): # Methid/Polymorphism
        self.__team_list.remove(sales_person)
    
    def promote(self, sales_person): # Method
        if sales_person in self.members:
            self.remove(sales_person)
        return Manager(sales_person.first_name, sales_person.last_name, sales_person.email, round(sales_person.salary * 1.15, 2), '')
    
    def cry(self): # Override/Polymorphism
        return f"{self.first_name} cried at worked today. So they are going to yell at people."

    def __str__(self): # Override/Polymorphism
        return f"Manager({super().__str__()}, Team: {self.team_name}, Members: {self.members})"   
# end of Manager()     

class Sales(Employee): # Single Inheritance
    def __init__(self, first_name, last_name, email, salary, team_name, client_list): # Override
        super().__init__(first_name, last_name, email, salary)
        self.team_name = team_name
        self.client_list = client_list

    def add(self, client_name): # Polymorphism
        self.client_list.append(client_name)
    
    def shared_clients(self, other_sales): # Method
        result = []
        for client in self.client_list:
            if client in other_sales.client_list:
                result.append(client)
        return result

    def cry(self): # Override/Polymorphism
        return f"{self.first_name} cried at worked today. So they are taking a sick day tomorrow."

    def __str__(self): # Base Override
        return f"Sales({super().__str__()}, Team: {self.team_name}, Clients: {self.client_list})"
    
    def __repr__(self): # Base Override
        return f"Sales({self.first_name} {self.last_name})"
# end of Sales()

boss = Manager("John", "Doe", "john.doe@company.com", 123000, "Sales Team")
s1 = Sales("Jane", "Doe", "jane.doe@company.com", 88000, "Sales Team", ["ClientA", "ClientB", "ClientC"])
s2 = Sales("Bob", "Johnson", "bob.johnson@company.com", 78000, "Sales Team", ["ClientA" , "ClientC", "ClientE"])

print(boss)
boss.add(s1)
boss.add(s2)
print(boss)
print(s1)
print(s2)
print(f"Shared Clients between {s1.first_name} and {s2.first_name}: {s1.shared_clients(s2)}")
s1 = boss.promote(s1)
print(s1)

print(s1.cry())
print(s2.cry())
print(boss.cry())
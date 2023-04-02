#Calculate the premium amount and display the vehicle details
def check_type():
    vechicle_type=['Two Wheeler','Four Wheeler']
    if type not in vechicle_type:
        return 0
    return 1
class vehicle:
    def __init__(self):
        self.vechicle_cost=None
        self.vechicle_id=None
        self.vechicle_type=None
        self.premium_amount=None
    def set_vechicle_id(self,vechicle_id):
        self.__vechicle_id=vechicle_id
    def set_vechicle_type(self,vechicle_type):
        if check_type(vechicle_type):
            self._vechicle_type=vechicle_type
        else:
            return "Invalid Vechicle Details"
    def set_vechicle_cost(self,vechicle_cost):
        self.__vechicle_cost=vechicle_cost
    def set_vechicle_id(self):
        return self.vechicle_id
    def set_vechicle_type(self):
        return self.vechicle_type
    def set_vechicle_cost(self)
    def calculate_premium(self):

#to represent the students seeking Admission in the university

class student:
    def __init__(self,student_id,marks,age):
        self.__student_id=id
        self.__marks=marks
        self.__age=age
    def validate_marks(self):
        if self.__marks >=0 and self.__marks <=100 :
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>=20:
            return True
        else:
            return False
    def validate_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
            else:
                return False
    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    def set_marks(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    def course_fee(self):
        d={1001:3500,1002:15000,1003:30000}
        discount = 0
        if(self._marks>=85):
            discount = 0.25
        return d[self.__student_id]- discount* d[self.__student_id]
a=student(1001,67,25)
a.set_student_id(1002)
a.set_marks(65)
a.set_age(22)
print(a.validate_qualification())'''

#pizza for you is a pizza store .......
types=['small','medium','Small','Medium']
class customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and customer.validate_quantity(self.__customer):
            if self.__pizza_type.title()=="small":
                self.pizza_cost=150 * customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=35 * customer.get_quantity(self.__customer)
            if self.__pizza_type.title()=="medium":
                self.pizza_cost=200 * customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=50 * customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id=self.__pizza_type[0] + str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms = distance_in_kms
        Pizzaservice.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost +=5
                    if distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self._delivery_charge
    def get_distance_in_kms(self):
        return self._distance_in_kms
c =customer("Asha",5)
p1 = Pizzaservice(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1 = Doordelivery(c,"MEDIUM",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())



#A bank has many customers and each customer has a bank account............






    
                    

    

        



    
    
            
       
        
    
        

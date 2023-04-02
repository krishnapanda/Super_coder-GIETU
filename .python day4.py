#nearest_palindrome(),return the nearest palindrome greater than the given number
import sys
def nearest_palindrome(n):
    nstr=str(n)
    for i in range(n+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(nearest_palindrome(99))

#find the medical fecility visited by the maximum.....
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
   
    result = [0,0,0]
    i = 1 
    while(i< len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P':
            result[0] = result[0] + 1
        elif patient_medical_speciality_list[i] == 'O' :
            result[1] = result[1] + 1
        else : result[2] = result[2] + 1
        i = i + 2
    a = max(result)
    a = result.index(a)
    if a == 0:
        speciality = 'Pediatrics'
    elif a == 1:
        speciality ='Orthopedics'
    else :
        speciality = 'ENT'

    return speciality


patient_medical_speciality_list=[301,'O',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

#display all the common characters between two string
def common(msg1,msg2):
    list = []
    for i in msg1:
        if i == " ":
            continue
        else:
            for j in msg2:
                if j == " ":
                    continue
                elif i==j:
                    if i in list:
                        break
                    else:
                        list.append(i)
    output = "".join(list)
    if len(output)==0:
        return -1
    else:
        return output
msg1 = "I like Python"
msg2 = "Java is a very popular language"
print(common(msg1,msg2))

###############
##OOPS Cpncept

class Example:
        def __init__(self,num):
            self.num=num
        def set_num(self, num):
            self.num-num
        def get_num(self):
            return self.num
obj=Example(10)

print(obj.get_num())
obj.set_num(15)
print(obj.get_num())####0/p:-10 15                                

#########
class customer:
    def__init__(self):
        cust_id=100
c1=customer()
print(c1.cust_id)//error(output)bcz wo don't have self here


#####
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
#mobole().purchase()
#mobile().purchase()
m1=mobile()
print(m1)
m2=mobile()
print(m2)
m1=m2
print(m1)
print(m2)

class customer:
    def __init__(self,cid,name,age,bal):
        self.cid=cid
        self.name=name
        self.age=age
        self.__bal=bal#private
    def update(self,amt):
        if(amt<1000):
            self.__bal+=amt
    def display(self):
         return(self.__bal)
c1=customer(100,"Gopal",24,1000)
c1.update(500)
#print(c1.__bal) -->gives error as the private cannot be
                    #accessed from outside the class
print(c1.display())# --->accessing the private attibute
##correcting the error
class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def len_disp(self):
        return self.__length
d1=dam("ABC dam",3.5)
print("the name:",d1.name)
print("the name:",d1.len_disp())

class table:
    def __init__(self):
        print(id(self))
        self.legs=4
        self.glass=None
        self.wooden=None
din_tab=table()
back_tab=table()
front_tab=back_tab
print(din_tab,id(back_tab),id(front_tab))


      
      
      

    
    
    

       

    

        

    
        

    

   

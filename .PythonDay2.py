'''
#list-->ordered--default index
list1=[]
print(list1,type(list1))
list2=[10,10.2,30+3j,true,"python"]
print(list2,type(list2))
list3=[10,20,30]
print(list3)
list3.append(50)
print(list3)
list3.insert(3,40)
print(list3)
list3.remove(10)
print(list3)
list3.pop(2)
print(list3)

#find the no. of letters and digits in the sentence
def function(str1):
    l_count=0
    d_digit=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_digit=d_digit+1
        else:
            continue
    return[l_count,d_digit]
print(function("Infosys 123"))
print(function("abcefg "))


#find pairs of numbers()which accepts a list of positive integers with no repetitions
def find_pair_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find_pair_of_numbers(num_list,n))


#write a python function which accept a string and returns a string mode of the first 2

def function(str):
    if len(str)<2:
        return -1
    else:
        return str[0:2]+str[-2:]
print(function("w3resource"))
print(function("w3"))
print(function("A"))


#write a py prog to add 'ing' at the end of a given srting and return the new string.
def function(str):
    if len(str)<3:
        return str
    elif str[-3::]=="ing":
        return str+"ly"
    else:
        return str+"ing"
print(function("sleep"))
print(function("amazing"))
print(function("is"))


#write a py fun , check_double(number) which accepts a whole number and return true if ...
def check_double(num):
    c=num*2
    num=str(num)
    count=0
    for x in num:#125874
        if x in num:#251748
            count+=1
        else:
            return False
            break
    if count==len(num):
        return True
print(check_double(245))
print(check_double(125874))
print(check_double(123))

#########################################
###########################################
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    global list_of_marks
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x == y:
                count+=1
        freq.append(count)
    return  freq
print(find_more_than_average())
print(generate_frequency()) #[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
print(sort_marks())

#translate christmas wishes from english into swedish
def translate(dict,eng):
    swed=[]
    for i in eng:
        swed.append(dict[i])
    return swed
dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
eng=["merry","christmas"]
print(translate(dict,eng))'''


#find the no. of distrinct subarrays in an array of position integers .......
n1=int(input("enter a value for n1"))
n2=int

   
    

            
            

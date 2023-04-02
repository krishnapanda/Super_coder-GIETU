'''#list comprehension
#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)

#list comprehension version
print([i for i in range(11)])
#for loop version--> oddelement
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    
print(result)
##or
print([i for i in range(11)if i%2!=0])
########################
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
#or
print([i if i%2!=0 else i**2 for i in range(11)])

#mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop---odd--->squre it
#even --->cube it
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    for j in i:
        if j%2!=0:
            result.append(j**2)
        else:
            result.append(j**3)
print(result)
#or
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
result.append([j**2 if j%2!=0 else j**3 for j in i for i in mat])
# list  comprehension in 2d
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    i_data=[]
    for j in i:
        if j%2!=0:
           i_data.append(j**2)
        else:
           i_data.append(j**3)
    result.append(i_data)
print(result)
#list comprehension
print([j**2 if j%2!=0 else j**3 for i in mat for j in i])
print([j**2 if j%2!=0 else j**3 for j in i for i in mat])

#for each number in list_b,get the number and its position(index) in mylist as are turn list of tuples.
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
#or
print([(i,mylist.index(i)for i in list_b)])

#list under dict
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append({i:mylist.index(i)})
print(result)
###
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result={}
for i in list_b:
    result[i]=mylist.index(i)
print(result)
#or
print({i:mylist.index(i)for i in list_b})

#tokenize the sentence into words, excluding the stopwords.
sentences=["a new world record was set","in the only city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
sw=['for','a','of','the','and','was','to','in','on','with']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in sw:
            row_data.append(word)
    result.append(row_data)
print(result)

#add and concatenateing
#num1=3+2+6+9=20
#num2=5148
#0/p=5148+20=5168
array=list(map (int,input().split(","))) #3,2,6,5,1,4,8,9
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in 1:
    number2+=str(i)
print(int(number2)+number1)


##string rotation
s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))'''


#sum of largest prime factor of cosecutive n numbers from n


def check_prime(m):
    c=0
    for i in range(m,0,-1):
        if(m%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
        

def prime(num):
    large=0
    for i in range(2,num+1):
        if(check_prime(i) and num%i==0 and i>=large):
            large=i
    return large      



n=int(input())
sum1=0
for i in range(n,n+9):
    sum1+=prime(i)
print(sum1)



    
    
        
        
        
        
    
    









        

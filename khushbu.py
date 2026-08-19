#basic programm of python printing hello world
print("hello world")
#print basic input like name,age etc etc 
name=input("enter your name")
age=int(input("enter your age"))
# done all mathematical calculation with the help of python basic progremming 
n1=int(input("enter a number"))
n2=int(input("enter a number"))
a=n1+n2
print("addition of two no",a)
s=n1-n2
print("subtraction of two no",s)
d=n1*n2
print("multiplication of two no",d)
e=n1/n2
print("division of two no is",e)
f=n1//n2
print("float division oftwo no is ",f)
p=n1**n2
print("n1 ke power n2 is ",p)
#find area of rectangle with help of python progremming language 
l=int(input("enter a lenght "))
b=int(input("enter a breadth"))
print("area of rectangle is ",l*b)
#find area of circle using python
import math
radius=int(input("enter the radius of circle"))
area=math.pi*radius**2
print("area of circle is",area)
#convert celcius to farenhite
ca=float(input("enter celsius"))
fe=(ca*9/5)+32
print("in degree fahrenheit",fe)
#programm of swipping two number
h=10
k=20
h,k=k,h
print("h",h)
print("k",k)
#for calculating simple interst
p=float(input("enter principle:"))
r=float(input("enter rate"))
t=float(input("enter time"))
si=(p*r*t)/100
print("simple interest=",si)
# LEVEL 2
#NO IS POSITIVE AND NEGETIVE NUMBER
num=float(input("enter a number:"))
if num>0:
    print("no is posetive ")
elif num<0:
    print("no is negetive")
else:
    print("no is zero which is not consider as posetive as well as negetive")
#find weather no is even or odd
num1=float(input("enter a number"))
if num1%2==0:
    print("no is even")
else:
    print("odd number")
#which no is greter among two
mm=float(input("enter a number"))
nn=float(input("enter a number"))
if mm>nn:
    print("number1 is greter then number 2")
else:
    print("number 2 is greater then number 1")
# teen no m bada no konsa h
x=float(input("enter a number"))
y=float(input("enter a number"))
z=float(input("enter a number"))
if y>x and y>z:
    print("y is gretest")
elif x>y and x>z:
    print("x is gretest")
else:
    print("z is gretest")
#to check the voting eligiblity critia according to age
ag=float(input("enter a number"))
if ag>=18:
    print("you are eligibe to drop a vote")
else:
    print("sorry,you are not fit in a critrea to dorop you vote this time ")
#marks vs grade with python
nnn=input("enter your name")
cl=int(input("enter your class"))
rollno=int(input("enter your roll no"))
subject=[]
if cl>=1 and cl<=10:
    subject=["hindi","english","maths","science","social science"]
    print("check your data")
    print("your subject are hindi,english,maths,science,social science ")
elif cl==11 or cl==12:
    strem=input("enter your stream")
    if strem == "science":
        subject=["english","chemistry","physics"]
        print("your compelsery subject is english,physics,chemisty")
        choice1=input("choose maths or biology:").lower()
        if choice1=="maths":
            print("YOU ARE SELECTED AS PCM STUDENT")
            subject.append("maths")
        elif choice1=="biology":
            print("you are selected as PCB student")
            subject.append("biology")
        else:
            print("invilid choice")
            exit()
        choice2=input("enter yous choice as hindi or computer science").lower()
        if choice2=="hindi":
            print("oh you ar the student of hindi ")
            subject.append("hindi")
        elif choice2=="computer science" or choice2=="cs":
            print("you are the student of computer science")
            subject.append("coumputer science")
        else:
            print("invilid choice")
            exit()
    elif strem=="commerce":
        subject=["english","accountancy","business studies","econpmics","hindi"]
    elif strem=="arts":
        subject=["hindi","english","history",'political science',"geography"]
    else:
        print("invild class")
        exit()
#marks entery
print("\n-------------enter marks---------")
total=0
for sub in subject:
    marks=int(input("enter marks in "+ sub + ":"))
    if marks<0 or marks>100:
        print("invilid marks")
        exit()
    total=total+marks
#percentage
percentage=(total/(len(subject)*100))*100         
#grade
grade=[]
if percentage>=90:
    print("you got grade A+")
elif percentage>+80:
    print("you got grade A")
elif percentage>=70:
    print("you got grade B")
elif percentage >=60:
    print("you got grade C")
elif percentage>=50:
    print("you got grade D")
elif percentage >=33:
    print("you got grade E")
else:
    print("you are fail")
#result
print("\n------------------result---------")
print("name",nnn)
print("rollno",rollno)
print("class",cl)
if cl==11 or cl==12:
    print("stream",strem.capitalize())
print("subject:",subject)
print("percentage:",percentage,"%")
if percentage>=33:
    print("you are pass")
else:
    print("you are fail")
print("==================================")    



    








































          

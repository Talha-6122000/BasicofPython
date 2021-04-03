#Python is a programming langague with a clean syntax
#Python programs can be ru on all desktop programs.
#Hello World will always be the first program that you make in any langague.
#here we did the same
#print is a built in function of android we will learn about function more in detail below
print('hello world')
#so what are variables ?
#Python Supports different  type of variable such as whole numbers, floating points,and text.
f=4 #a whole number
c=3.133 #a floating point number
name="Python" # a string
#we can print  them all using print function
print(c)
print(f)
print(name)
#Let's Talk about Python String in details
#A string can be called as collection of charchters or text
x="Hello"
print(x)
#String Indexing
#Indiviual Charachters  can be acccessed using  blockquotes,couting starts from zero
print(x[0])
print(x[2])
#String Slicing
print(x[0:3])
#Comibing String or Adding them
x="Talha"
#Combing Numbers and Text
#There are a lot of methods to do that
s="My lucky number is %d What is yours?"%7
print(s)
#Alternative method of combining
s="My lucky number is "+str(7)+" what is yours?"
print(s)
#String replace method
#Python has a built in support for  String replacement .
d="Hello world"
d.replace("World","Universe",1)
print(d)
#In python and many other programming languages you can get user input
name=input("talha")
print("Hello"+name)
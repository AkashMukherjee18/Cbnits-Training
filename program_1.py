# Collection Module

#import collections
from collections import Counter, namedtuple, deque, ChainMap, OrderedDict, defaultdict
from array import *
from functools import reduce
from genericpath import exists
from importlib.resources import path
from msilib.schema import Class

# a=namedtuple('cources', 'name, technology')
# s=a('data scince', 'python')
# print("Using NamedTuple : ")
# print(s)

# a=namedtuple('book', 'name, type')
# s=a._make(['chader pahar','advanture'])
# print("Using Named Tuple")
# print(s)

# a=['a','k','a','s','h']
# s=deque(a)
# print("using deque : ")
# print(s)

# s.appendleft("hi")
# print("After append")
# print(s)

# print("After remove word from right side :")
# s.pop()
# print(s)
# print("After remove word from Left side :")
# s.popleft()
# print(s)

# a={"name": 'akash', "age": 20}
# b={"hobby": 'play', "working": 'developer'}
# z=ChainMap(a,b)
# print("Using Chainmap : ")
# print(z)

# a=[1,2,4,2,2,1,1,3,5,1]
# c=Counter(a)
# print(c)
# print(list(c.elements()))
# print(c.most_common())
# sub={1:4, 5:1}
# print(c.subtract(sub))
# print(c.most_common())

# d=OrderedDict()
# d[0]='a'
# d[1]='k'
# d[2]='a'
# d[3]='s'
# d[4]='h'
# print(d)
# print(d.keys())
# print(d.items())
# d[3]='xyz'
# print(d)

# d=DefaultDict(int)
# d['akash']=1
# d['rohit']=2
# d["hi"]=10
# print(d['hello'])
# print(d['rohit'])
# print(d['hi'])

# x=DefaultDict(int)
# x[0]="hi"
# x[5]='xyz'
# # print(x[0])
# # print(x[10])

# a=DefaultDict(int)
# a={1:'abc', 2:'mno'}
# print(a[0])

# words = ['data', 'science', 'machine', 'learning']
# x=[len(i) for i in words]
# print(x)

# p={i:len(i) for i in words}
# print(p)

# a = [1,2,3,4]
# b = [5,6,7]
# lab={(i,j) : i*j for i in a for j in b}
# #print(lab)
# for i in a:
#     for j in b:
#         print(i,j,":",(i*j))

# c=0
# while c<5:
#     print("no : ",c)
#     c=c+1
# print("Good")

# import array as x
# Akash = x.array('i', [1, 2, 3])
# for i in range (0, 3):
#     print (Akash[i])


# myarray = array("i", [5, 8, 10, 13])
# myarray.append(6)
# print(myarray)
# for i in myarray:
#     print(i)
# exit(0)

# arr=["x", ['a','b','c']]
# arr.append('i am roy')
# print(arr)
# arr.pop()
#print(arr)


#arr= ["i",10,20,30,40,50,60,70]
#arr.remove(70)
#print(arr)
#arr.pop(3)
#print(arr)

# 0 1 1 2 3 5 8 13 21
# f=0
# s=1
# for i in range(0,5):
#     if i==0:
#         print(f)
#     elif i==1:
#         print(s)
#     else:
#         f,s=s,f+s
#         print(s)

# fibo=0
# f=0
# s=1
# for i in range(0,10):
#     f=s
#     s=fibo
#     print(fibo,end=" ")
#     fibo=f+s


# def fib():
#     f,s=0,1
#     while True:
#         yield f
#         f,s=s,f+s
# for i in fib():
#     if i>25:
#         break
#     print(i,end=" ")


# from collections import Counter
# X = input(" the number of shoes: ")
# print("------: ",X)
# S = Counter(map(int,input().split()))
# print(" no of shoes ",S)
# n = input("the number of customers: ")
# print("the number of customers ",n)
# N = int(n)
# print("price of shoes and no: ",N) 
# earnings = 0
# print("Enter the size of shoes and price: ")
# for customer in range(N):
#     size, x_i = map(int,input().split())
#     print(" size ",size,"x_i ",x_i)
#     if size in S and S[size] > 0:
#         S[size] -= 1
#         earnings += x_i
#         print(" ernig ",earnings)
# print(earnings)


#Pythagorean No:
#a2 + b2 = c2

# from math import sqrt
# #print(" c=== ",int(sqrt(4)))
# n=int(input("Enter a no: "))
# for a in range(1, n+1):
#     #print(" a1 ",a)
#     for b in range(a, n):
#         #print(" b2 ",b)
#         c_sqrt= a**2 + b**2
#         #print(" a**2 + b**2 ",c_sqrt)
#         c= int(sqrt(c_sqrt))
#         #print(" c3 ",c)
#         #print(" c3**c3 ",c**2)
#         x=(c_sqrt- c**2)
#         #print("minus = ",x)
#         if ((c_sqrt - c**2) == 0):
#             print(a, b, c)

# num=int(input("Enter a no: "))
# fact=1
# if num<0 or num==0:
#     print("please enter positive no")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print("The factorial no of",num,"is: ",fact,end="")

#Using for loop inside a while loop:

# traveling=input("yes or not: ")
# while traveling == 'yes':
#     total=[]
#     num=int(input("Enter the no of people traveling: "))
#     for i in range(1,num+1):
#         name=input("Enter the name: ")
#         age=input("Enter the age: ")
#         sex=input("Enter the sex: ")
#         dic={"Name": name, "Age": age, "Sex": sex}
#         total.append(dic)
#     print(total)
#     print("Oops! forgot someone")
# print("Exit Run Again")

import os
import os.path
from pyclbr import Function
from re import A
from tkinter import Y
from traceback import print_tb
file="demo.txt"
cwd = os.getcwd() 
#print("Current Directory Path is: ",cwd)
# if os.path.isfile(file):
#     print("File is exists")

# if os.path.isfile(file):
#     print ("File exist")
#     f = open(file, "w")
#     f.write("Now the file has more content!")
#     f = open(file, "r")
#     print(f.read())
#     f = open(file, "a")
#     f.write("Now the file has more content 500!")
#     f = open(file, "r")
#     print(f.readline(6))
# else:
#     print ("File not exist")

# if file not in cwd:
#     file=open("demo.txt","x")
#     print("file is created")
    

# x=lambda a: a*a
# m=x(4)
# print("Using lamda functions: ",m)

# def new_func(x):
#     return(lambda y: x+y)
# t=new_func(2) 
# k=new_func(3)
# print(" t =",t(300))
# #print(" k =",k(4))
# print(" t =",t(30))

# Filter returns only true
#data=[1,2,3,4,5,6,7,8]
#x_list=list(filter(lambda a:(a/2==2),data))
#x_list=list(filter(lambda a:(a%2==0),data))
#print(x_list)

# print(4/2) # 2.0
# print(4//2) # 2
# print(4%2) # 0

# Map returns true and false both 
# data=[1,2,3,4,5,6,7,8]
# x_list=list(map(lambda a:(a%2==0),data))
# print(x_list)

# from functools import reduce
# x=reduce(lambda a,b: a+b,[10,20,30,5])
# print("Using Reduce functions: ",x)

#linear Equations

# s=lambda a: a*a
# r=s(5)
# print(r)

# s=lambda x,y: 3*x+4*y
# print(s(10,5))

# Quadratic Equations

# s= lambda x,y: (x+y)**2
# print(s(5,5))

# MAP
# def new(a):
#     return  a*a 
# x=map(new,[1,2,3,4,5])
# print(x)
# print("After converting the x from object to tuple",tuple(x))

# lst=[1,2,3,4,5]
# y=list(map(lambda x:x+3, lst))
# print(y)

#FILTER
# lst=[1,2,3,4,5]
# y=list(filter(lambda x:x>=3, lst))
# print(y)

#REDUCE

# lst=[1,2,3,4,5,6]
# y=reduce(lambda q,p: q*p, lst)
# print(y)

# From Json to fetch data and print

# import json
# def jsondata():
#     f=open('collectionsummary_mini.json')
#     txt=json.load(f)
#     f.close()
#     return json.dumps(txt,indent=2)
# print(jsondata())


# import json
# file = open('collectionsummary_mini.json')
# data = json.load(file)
# print(data)
# file.close()

#Generatir Functions:

# def new(dicts):
#     for x,y in dicts.items():
#         yield x,y
# a={1: "Hi", 2: "Welcome", 3: "India"}
# b=new(a)
# print(" 1st time of generator functions ",b)
# print(" 2nd time ",next(b))
# print(" 3rd time ",next(b))
# print(" 4th time ",next(b))
# print(" 5th time ",next(b))

# def new(val):
#     for x in range(val):
#         yield x
# b=new(5)
# print(" 1st time of generator functions ",b)
# print(" 2nd time ",next(b))
# print(" 3rd time ",next(b))
# print(" 4th time ",next(b))
# print(" 5th time ",next(b))
# print(" 6th time ",next(b))
# print(" 7th time ",next(b))

# def val():
#     n=3
#     yield n
#     n= n*n
#     yield n
# b=val()
# print(" 1st time of generator functions ",b)
# print(" 2nd time ",next(b))
# print(" 3rd time ",next(b))
# print(" 4th time ",next(b))

# for i in b:
#     print(i)

# a=range(10)
# b=(x for x in a)
# #print(b)
# for i in b:
#     print(i,end=" ")

# OOPS

# class Car():
#     pass

# honda=Car()
# tata=Car()

# honda.modelname='city'
# honda.price= 20000

# tata.modelname='bolt'
# tata.price= 50000

# print(honda.modelname)
# print(honda.price)
# print(tata.modelname)
# print(tata.price)

# n = int(input("Enter a no: "))

# def fun(n):
#     if(n==0):
#         result =1
#     else:
#         result = n*fun(n-1)
#     print(result)
#     return result
# fun(n)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# print("\n\nRecursion Example Results")
# tri_recursion(3)


# data={
#   "data": {
#     "courseProgress": {
#       "nodes": [
#         {
#           "user": {
#             "id": "1",
#             "email": "a@a.com",
#             "startedOn": "2019-07-26T05:00:50.523Z"
#           },
#           "course": {
#             "id": "22",
#             "title": "Building Machine Learning Models in Python with scikit-learn"
#           },
#           "percentComplete": 34.0248,
#           "lastViewedClipOn": "2019-07-26T05:26:54.404Z"
#         }
#       ]
#     }
#   }
# }

# def func1(data):
#     for key,value in data.items():
#         print (str(key)+':'+str(value))
#         if isinstance(value, dict):
#             func1(value)
#         elif isinstance(value, list):
#             for val in value:
#                 if isinstance(val, str):
#                     pass
#                 elif isinstance(val, list):
#                     pass
#                 else:
#                     func1(val)
# func1(data)


# students_grade=[]
# for _ in range(int(input())):
#     name = input("Enter a name: ")
#     score = float(input("Enter a score: "))
#     students_grade.append([name,score])
#     #print(students_grade)
# sorted_scores=sorted(list(set(x[1] for x in students_grade)))
# #print(sorted_scores)
# second_lowest=sorted_scores[1]
# #print(second_lowest)
# low_final_list=[]
# for student in students_grade:
#     #print("student",student)
#     if second_lowest==student[1]:
#         low_final_list.append(student[0])
#         #print(low_final_list)
# for student in sorted(low_final_list):
#     print(student)

# students_grade=[]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students_grade.append([name,score])
# sorted_scores=sorted(list(set(x[1] for x in students_grade)))
# second_lowest=sorted_scores[1]
# low_final_list=[]
# for student in students_grade:
#     if second_lowest==student[1]:
#         low_final_list.append(student[0])
# for student in sorted(low_final_list):
#     print(student)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# print(ans)
# for i in range(x+1):
#     # print(i)
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i+j+k) !=n:
#                 print([i,j,k])



# n = int(input())
# student_marks = {}
# for _ in range(n):
#     line = input().split()
#     name, scores = line[0], line[1:]
#     scores = map(float, scores)
#     student_marks[name] = scores
# query_name = input()
# marks=0
# for i in student_marks[query_name]:
#     marks=marks+i
# avg=marks/3
# print("%.2f"%avg)

# n = int(input())
# arr = list(map(int, input().split()))
# mx = max(arr)
# print("mx",mx)
# sc = None
# print("sc 0",sc)
# for num in arr:
#     print("num 1",num)
#     if num == mx:
#         print("num 2 ",num)
#         pass
#     elif sc == None:
#         sc = num
#         print("sc1",sc)
#     elif num > sc:
#         print("sc2",sc)
#         sc = num
#         print("sc3",sc)
# print(sc)


# def print_full_name(first, last):
#     print("Hello %s %s! You just delved into python."%(first,last))
#     # Write your code here
# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)

# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         print("string 1",i)
#         for j in range(len(sub_string)):
#             print("substring",j)
#             if string[i+j]==sub_string[j] and j==(len(sub_string)-1):
#                 print("sting 00 ",string[i+j])
#                 count=count+1
#                 print("count ",count)  
#             if string[i+j]!=sub_string[j]:
#                 print("string",string)
#                 break  
#         if i==len(string)-len(sub_string):
#             print("i",i)
#             break            
#     return count

# string = input().strip()
# sub_string = input().strip()

# count = count_substring(string, sub_string)
# print(count)

# string = "abccyz";  
# print(string.replace('c','?'))

# string=input("Enter a string: ")
# temp=string

# print("Duplicate characters in a given string: ")
# #Counts each character present in the string  
# for i in range(0, len(string)):  
#     count = 1  
#     for j in range(i+1, len(string)):  
#         if(string[i] == string[j] and string[i] != ' '):  
#             count = count + 1  
#             #Set string[j] to 0 to avoid printing visited character  
#             string = string[:j] + '0' + string[j+1:]
   
#     #A character is considered as duplicate if count is greater than 1  
#     if(count > 1 and string[i] != '0'):  
#         # print(string[i])
#         x=temp.replace(string[i],'?')
#         print(x)
#         # print("ok")

# st = "hiiii how arrrre youuu"
# def remover(st):
#     output=""
#     t=""
#     for i in st:
#         if t!=i:
#             output = output + i
#         t=i
#     return output

# x = remover(st)
# print(x)

# st.replace()

# x = int(input())
# for i in range(x):
#     try:
#         a, b = input().split()
#         print(int(a)//int(b))
#     except ZeroDivisionError as e:
#         print("Error Code:",e)
#     except ValueError as v:
#         print("Error Code:",v)

# a=[1,2]
# b=[3,4]
# for i in a:
#     for j in b:
#         x=(i,j)
#         # lst.append(x)
#         # tuple(lst)
#         print(x,end=" ") 

#import textwrap


# str="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# length=len(str)
# # print("----len-------",length)
# range=temp=4
# while(range<=length):
#     if range==temp:
#         print(str[:range])
#     elif range>=temp and range<=(temp+1):
#         range2=range+temp
#         print(str[temp:range2])
#     else:
#         range2=range+temp
#         print(str[range:range2],end="\n")
#     range=range+temp


    
    # print("check",range)
# range2=range*2
# print("firsr------",firstThree)
# print("length------",len(str))
# print("second------",second)

# print(firstThree)
# def wrap(string, max_width):
#     first = string[:max_width]
#     print(first,end="")
#     return first

# string, max_width = input(), int(input())
# result = wrap(string, max_width)
# print(result)

# string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# max_length=4
# for i in range(0, len(string), max_length):
    # print("i --------",i)
    # print("length---------------",max_length)
    # result = (string[i : i + max_length])+'\n'
    # print("i ----2----",i)
    # print("length-----2----------",max_length)
    # print(result)

# cube = lambda x: x**3 # complete the lambda function 
# def fibonacci(n):
#     # return a list of fibonacci 
#     count,n1 = 0,0
#     n2 =1
#     ans = []
#     while count < n:
#         ans.append(n1)
#         nth = n1 + n2
#         n1, n2 = n2, nth
#         count += 1
#     return ans

# n = int(input())
# print(list(map(cube, fibonacci(n))))
# print("cube-------",cube)

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# res=fact(5)
# print("res : ",res)

# def backwardsby2(num):
#     if num <= 0:
#         print('Zero!')
#         return
#     else:
#         emojismiles = []
#         for i in range(0, num):
#             emojismiles += '@'
#         print(num, ' '.join(emojismiles))
#         backwardsby2(num - 2)


# backwardsby2(9)

# def countdown(n):
#     print(n)
#     if n == 0:
#         return       # Terminate recursion
#     else:
#         countdown(n - 1)   # Recursive call
# countdown(4)

# def sumnums(n):
#     if n == 1:
#         return 1
#     print("----------1----------",n)
#     print("-----------2---------",sumnums(n - 1))
#     print("------------3--------",n + sumnums(n - 1))
#     return n + sumnums(n - 1)
    


# print(sumnums(3))
# #print(sumnums(6))
# #print(sumnums(9))

# Program to print the fibonacci series upto n_terms

# Recursive function
# def recursive_fibonacci(n):
#     if n <= 1:
#         print("== n ==",n)
#         return n
#     else:
#         print("--------n---------",n)
#         print("--------(n - 1)---------",(n-1))
#         print("--------(n - 2)---------",(n-2))
#         return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))


# n_terms = 5
# # check if the number of terms is valid
# if n_terms <= 0:
#     print("Invalid input ! Please input a positive value")
# else:
#     print("Fibonacci series:")
# for i in range(n_terms):
# 	print("-- check --",recursive_fibonacci(i))

# def tri_recursion(k):
#   if(k>0):
#     print("------k1----",k)
#     print("------(k-1)----",(k-1))
#     result = k+tri_recursion(k-1)
#     print(result)
#     print("------k2----",k)
#     print("------(k-1)----",(k-1))
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# def reverse(array):
#     # Base case1
#     if len(array) == 0: # If we encounter an empty array, simply return an empty array
#         return []
#     # Base case2
#     elif len(array) == 1 : # Inverting an array of size 1 returns the same array
#         return array
    
#     # Recursive case
#     return [array[len(array) - 1]] + reverse(array[:len(array) - 1])
#     # The first part is storing the last element to be appended later
#     # The second part is calling another instance of the same function with the last element removed
# # Driver Code
# array = [1, 2, 3, 4]
# # print(len(array))
# print(reverse(array))

# def Recur_facto(n):
   
#     if (n == 0):
#         return 1
   
#     return n * Recur_facto(n-1)
   
# # print the result
# print(Recur_facto(6))

# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[2])

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[3:6])

# import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = [True, False, False, False]
# newarr = arr[x]
# print(newarr)

# n=int(input("Enter a no: "))
# for i in range(n+1):
#     print(n,"X",i,"=",n*i)

# a=5
# b=7
# a=a+b
# b=a-b
# a=a-b
# print("A =",a)
# print("B =",b)

# a=3
# b=5
# c=a
# a=b
# b=c
# print("A =",a)
# print("B =",b)

# a=10
# b=8
# x=[a if a>b else b]
# print(x)


# import numpy
# n=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x)

# x=numpy.prod([1,2,3])
# print(x)


# import numpy as np

# result = np.prod([
#     [1, 2],
#     [3, 4]], axis=0)
# print(f'result={result}') # result=[3 8]

# result = np.prod([
#     [1, 2],
#     [3, 4]], axis=1)
# print(f'result={result}') # result=[2, 12]

# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


# PANDA AND NUMPY USE SOME FUNCTIONS

# import pandas as pd


# dic={"name": ['sun', 'mon', 'tues'],
# "days": ['7','2','4'],
# "time": ['10.20', '25', '15:23']}


# val=pd.DataFrame(dic)


# val.index = ['first', 'second', 'third']
# print(val)
# print(val.head(1)) #Show one row from upper
# print(val.tail(1)) #Show one row from lower
# print(val.info())
# print(val.shape) #Shape of the dataset
# print(val.size) #Size of the dataset
# print(val.isna().any()) # find if there is any variable/column with missing values in it?
# print(val.isnull()) # this functions shows all the row and column with a boolean for the data present in the cell.True means null value, false means not a null value.
# print(val.isnull().sum()) # this functions find the sum of null value
# print(val.columns) # this functions find the no of columns

# print(val.nsmallest(2,'days')) # this functions find the smallest no
# print(val.size) #Size of the dataset
# print(val.size) #Size of the dataset
# print(val.describe()) #standard mathematical analysis of each column of datdaset 
# print(val.describe().T) #standard mathematical analysis of each column of datdaset and Transposet
# print(val.nunique()) #standard mathematical analysis of each column of datdaset and Transposet
# 
# val=pd.read_csv('data.csv')
# x=val.nsmallest(3,'money')# this functions find the smallest no
# x=val.nlargest(3,'money')# this functions find the largest no
# print(x)
# print(val) 
# print(val['money']) 
# print(val['money'][0]) 
# val['money'][0]=4874
# print(val['money'][0]) 
# val.to_csv('data.csv')
# print(val)
# val.to_csv('show.csv', index=False) # index 0 1 2 3 no will be disabled

# ser=pd.Series(np.random.rand(15))
# print(ser)
# print(type(ser))

# newdf=pd.DataFrame(np.random.rand(10,5), index=np.arange(10))
# print(newdf)
# print(newdf.index)

# NUMPY

# import numpy as np
# a= np.array([1,2,3])
# print(a)

# b=np.array([[1.2, 5.2, 3.6], [7.8, 9.1, 1.0]])
# print(b)
# print(b.ndim) # dimentions
# print(b.shape) # shape of an array
# print(b.dtype) # dtype
# print(a.itemsize) # 4 
# print(b.itemsize)  # 8
# print(b.dtype) # dtype
# x=np.zeros(5)
# x=np.zeros((2,3))
# x=np.zeros((2,3,2,3))
# x=np.full((2,3), 109) #full
# x=np.ones((4,2,2), dtype='int32')
# x=np.random.rand()
# print(x)

# List Comprehensions 

# num=[1,2,3,4,5,6]
# x=[]
# for i in num:
#     x.append(i)
# print(x)
# num=[4,6,7]
# x=[i for i in num]
# print(x)

# nums=[1,2,3,4,5,6,7,8,9,10]
# x=[]
# for i in num:
#     if i%2==0:
#         x.append(i)
# print(x)

# x=[n for n in num if n%2==0]
# print(x)

# value=list(filter(lambda n: n%2==0, nums))
# print(value)

# letter=[]
# word='abcde'
# lenth=len(word)
# print(lenth)
# for i in word:
#     for x in range(lenth):
#         letter.append((i,x))
# print(letter)

# word='abc'
# val=[(l,n) for l in word for n in range(len(word))]
# print(val)

# Dictionary Comprehensions:
# number=[1,2,3]
# names=['aks', 'sum', 'mon']
# # print(list(zip(number, names)))
# dic={}
# for num,nam in zip(number,names):
#     dic[num]= nam
# print(dic)

# Set Comprehensions:
# nums = [4,4,5,5,6,1,6]
# my_set=set()
# for i in nums:
#     my_set.add(i)
# print(my_set)
# val={i for i in nums}
# print(val)

# n=5
# z=lambda x:x*n
# print(z(9)) # 45

# print(round(3.499))


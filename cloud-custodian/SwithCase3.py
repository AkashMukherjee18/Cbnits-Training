import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=int, help="first")
parser.add_argument("--b", type=int, help="second")

args = parser.parse_args()

x1=args.a
y1=args.b

def getInput():
    f_no=x1
    s_no=y1
    return f_no,s_no
def add(): 
    x, y =getInput()
    return x + y
def sub(): 
    x,y=getInput()
    return x - y
def mul(): 
    x,y=getInput()
    return x * y
def div(): 
    x,y=getInput()
    return x // y

print ("1: add,2: sub,3: mul 4:div")
   
choice =int(input("Enter your choice: "))
operation =[add, sub, mul, div]

output =operation[choice-1]() 
print("output",output)
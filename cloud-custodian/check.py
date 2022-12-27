# def fun():
#     return "oooooookkkkkk" 

# print(fun())

# import pprint

# student_dict = {'Name': 'Tusar', 'Class': 'XII', 
#      'Address': {'FLAT ':1308, 'BLOCK ':'A', 'LANE ':2, 'CITY ': 'HYD'}}

# print(student_dict)
# pprint.pprint(student_dict,width=-1)

# def Push(stk,item):
#     stk.append(item)
#     print("Item is added successfully to the stack")
# def Pop(stk):
#     if stk==[]:
#         print("Stack is already Empty")
#     else:
#         stk.pop()
# def Display(stk):
#     a=stk[::-1]
#     print(a)

# stk=[]

# while True:
#     print("1.Push\n2.Pop\n3.Display")
#     ch=int(input("Enter Your Choice:::"))
#     if ch==1:
#         no=int(input("Enter no. to be added:::"))
#         Push(stk,no)
#     if ch==2:
#         Pop(stk)
#     if ch==3:
#         Display(stk)

import subprocess
def run():
    print("Enter Your AWS CLIENT USER NAME")
    client_name = input()
    if client_name == '':
        print("Enter Your Name")
    # print("Enter Your AWS CLIENT PASSWORD")
    if client_name != '':
        print("Enter Your AWS CLIENT PASSWORD")
        client_password = input()
    if client_password == '':
        print("Enter Your Password")
    if client_password!= '':
        print("Enter Your AWS CLIENT ID")
        client_id = input()
    if client_id == '':
        print("Enter Your Id")
    if client_id != '':
        print("Enter Your AWS CLIENT SECRET KEY")
        client_secret_key = input()
    if client_secret_key == '':
        print("Enter Your Secret Key")
    if client_secret_key != '':
        print("ok")
    
    # exit(0)
    # print("Enter Your AWS CLIENT ID")
    # client_id= input()
    # print("Enter Your AWS CLIENT SECRET KEY")
    # client_secret_key= input()
    # # print("------",client_name,"======",client_password,client_secret_key,client_id)
    # if client_password is None:
    #     print("Give value")
    # if client_id is None:
    #     print("Give value")
    # if client_secret_key is None:
    #     print("Give value")

    # print("OK")
    # subprocess.run("python -m venv custodian")
    # subprocess.run("python -m venv custodian")
    # print("ok")

run()



# print(os.system("dir"))
# print(subprocess.run("python abc.py"))
# subprocess.run(["python", "abc.py"])
# print(subprocess.run(["python", "abc.py"]))
# result=subprocess.run("python abc.py", stdout=subprocess.PIPE)

# print("-----------",result)
# print("-----2------",result.stdout)
# print("-----3------",result.stdout.decode())


# program = "mediaplayer.exe"
# process = subprocess.Popen(program)
# code = process.wait()
# print(code)

# args = ["ping", "mediaplayer"]

# process = subprocess.Popen(args, stdout=subprocess.PIPE)

# data = process.communicate()

# print(data)


    

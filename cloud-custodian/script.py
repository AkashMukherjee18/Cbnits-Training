# import subprocess
# import os

# def cloud_custodian_install():
#     try:
#         # result=subprocess.run("python -m venv custodian")
#         # result=subprocess.run("pip install c7n")
#         result=subprocess.run("python abc.py")
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True
# def cloud_custodian_open():
#     try:
#         result=subprocess.run("python abc.py")
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True
# def custodian_command_list():
#     try:
#         result=subprocess.run("python  abc.py")
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True
# def exit(): 
#     print("Exit")
#     return True

# print ("1:install cloud custodian, 2. open cloud custodian, 3.to see a list of available commands 4.Exit")
# choice =int(input("Enter your choice: "))
# # operation =[cloud_custodian, exit]
# # output =operation[choice-1]() 
# # print("output",output)

# while(choice!=4):
#     if(choice>=1):
#         operation =[cloud_custodian_install, cloud_custodian_open, custodian_command_list, exit]
#         output =operation[choice-1]()
#         print("output",output)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
#         print("1:cloud_custodian_install, 2. open cloud custodian, 3.to see a list of available commands 4.Exit")
#         choice =int(input("Enter your choice: ")) 
#     elif(choice==3):
#         exit()


# # if __name__ == '__main__':
# #     cloud_custodian()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

import subprocess
import shlex

# print(subprocess.run('sh test.sh', shell=True))
# print(out)
# subprocess.call('bash test.sh', shell=True)
# print("ok-----done")
# print(subprocess.run(["test.sh"], shell=True))
# out = proc.stdout

# subprocess.call(shlex.split('test.sh num1 num2'))
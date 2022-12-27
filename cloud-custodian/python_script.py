import subprocess
import argparse
import json

def cloud_custodian_open(cmd):
    try:
        result=subprocess.run(cmd)
#         print("Ok")
        with open('./extractions/text.json') as file:
            data = json.load(file)
        print(data)
        return result
    except Exception as e:
        print("Error",e)
        return True

# print("Write --a filename")
parser = argparse.ArgumentParser()
parser.add_argument("cmd")
parser.add_argument("file")
args = parser.parse_args()
arg1=args.cmd
arg2=args.file
# print("---------",arg1)
cmd = '{}'.format(arg1), '{}'.format(arg2)
cloud_custodian_open(cmd)

# import subprocess
# subprocess.run("python abc.py")

# Dyanamic Code
#------------------------

# import subprocess
# import argparse

# def cloud_custodian_open(cmd):
#     try:
#         result=subprocess.run(cmd)
#         # print("----------------",result)
#         print("Run Successfully")
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True

# parser = argparse.ArgumentParser()
# parser.add_argument("cmd")
# parser.add_argument("file")
# args = parser.parse_args()
# # cmd = 'python {}'.format(args.file)
# cmd = args.cmd, args.file
# cloud_custodian_open(cmd)

# 2. Dynamic 

# import subprocess
# import argparse

# def cloud_custodian_open(cmd):
#     try:
#         result=subprocess.run(cmd)
#         # print("----------------",result)
#         print("Run Successfully")
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True

# parser = argparse.ArgumentParser()
# parser.add_argument("cmd")
# parser.add_argument("file")
# args = parser.parse_args()
# cmd = '{}'.format(args.cmd),'{}'.format(args.file)
# # cmd = args.cmd, args.file
# cloud_custodian_open(cmd)


# 3. Dynamic 3.

# import subprocess
# import argparse
# import json

# def cloud_custodian_open(cmd):
#     try:
#         result=subprocess.run(cmd)
#         print("Ok")
#         with open('./extractions/text.json') as file:
#             data = json.load(file)
#         print(data)
#         return result
#     except Exception as e:
#         print("Error",e)
#         return True
# parser = argparse.ArgumentParser()
# parser.add_argument("cmd")
# parser.add_argument("dir")
# parser.add_argument("file")

# args = parser.parse_args()
# arg1=args.cmd
# arg3=args.dir
# arg4=args.file
# cmd='{}'.format(arg1),'{}'.format(arg3),'--output-dir=.','{}'.format(arg4)
# print("---check---",cmd)
# cloud_custodian_open(cmd)









# cmd='python'
# file= 'abc.py'
# result= cmd,file
# print("---------",result)
# subprocess.run(result)










# parser = argparse.ArgumentParser()
# # parser.add_argument("--a", help="first")
# parser.add_argument("--a", type=str, help="first")
# args = parser.parse_args()
# arg1=args.a
# print("---------",arg1)
# cmd = 'python {}'.format(arg1) # if you want to pass any arguments


# import subprocess
# import argparse

# parser = argparse.ArgumentParser()
# # parser.add_argument("--a", help="first")
# parser.add_argument("--a", type=str, help="first")

# args = parser.parse_args()
# arg1=args.a


# command = 'python {}'.format(arg1) # if you want to pass any arguments
# subprocess.run(command)
# print("OK NOW")
# p = subprocess.Popen(
#         [command],
#         shell=True,
#         stdin=None,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         close_fds=True)
# out, err = p.communicate()
# print("----------",out)
# print("----------",err)
# print("----------",er)

# import os
# import subprocess
# from subprocess import Popen, PIPE
# import yaml



# p=subprocess.run("echo This is sample text > ./extractions/ayz.txt", capture_output=True, shell=True)
# print(p)
# lis=[]
# print(lis.append(p))
# f = open("./extractions/MyFile.txt", encoding='utf-8')
# f = open("./extractions/MyFile.txt", encoding='utf-8')
# print(f.read())


# with open(r'./extractions/ayz.yaml') as file:
#     documents = yaml.full_load(file)

#     for item, doc in documents.items():
#         print(item, ":", doc)

# with open(r'./extractions/ayz.yaml') as file:
#     # The FullLoader parameter handles the conversion from YAML
#     # scalar values to Python the dictionary format
#     fruits_list = yaml.load(file, Loader=yaml.FullLoader)
#     print(fruits_list)

# import json
# with open('./extractions/text.json') as file:
#     data = json.load(file)
# print(data)
# import json
# def jsondata():
#     f=open('collectionsummary_mini.json')
#     txt=json.load(f)
#     f.close()
#     return json.dumps(txt)
# x=jsondata()
# print(x)




#a= { "A": { "B": { "C":  [ { "d": 1, "e": 2, "f": 3 }, { "d": 11, "e": 22, "f": 33 }, { "j": 7, "k": 8, "l": 9 } ] } } }

#print(" keys ",a.keys())
#print(" items ",a.items())
#print(" values ",a.values())
# if a.keys() == a.keys():
# 	print("Ok")
# else:
# 	print("false")

# print(a['A']['B']['C'][1]['e'])

#b={"X": 5, "y": 6, "z": 8}
#print(b.keys())
#print(b.items())


import json

x = """
{
	"project": "log4j",
	"count": 78,
	"partial": 15,
	"missed": 56,
	"resolved": 7,
	"collectionreport": [{
		"input": {
			"pkgInfo": {
				"resourceid": "org.apache.logging.log4j:log4j-core:2.14.1",
				"category": "build"
			}
		},
		"output": {
			"srcInfo": {
				"srcurl": "https://github.com/apache/logging-log4j2",
				"type": "github",
				"matchingref": "log4j-2.14.1-rc1"
			},
			"pkgInfo": {
				"resourceid": "org.apache.logging.log4j:log4j-core:2.14.1",
				"pkgurl": "https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core",
				"type": "maven",
				"category": "build",
				"dependencies": [{
					"input": {
						"pkgInfo": {
							"resourceid": "com.fasterxml.jackson.core:jackson-core:2.14.1",
							"isopensource": true,
							"category": "build"
						}
					},
					"status": "missed"
				}, {
					"input": {
						"pkgInfo": {
							"resourceid": "log4j:log4j:1.2.17",
							"isopensource": true,
							"category": "build"
						}
					},
					"output": {
						"srcInfo": {
							"srcurl": "https://github.com/log4j/",
							"type": "github"
						},
						"pkgInfo": {
							"resourceid": "log4j:log4j:1.2.17",
							"pkgurl": "https://repo1.maven.org/maven2/log4j/log4j",
							"type": "maven",
							"category": "build",
							"dependencies": [{
								"input": {
									"pkgInfo": {
										"resourceid": "org.apache.openejb:javaee-api:5.0-2",
										"category": "build"
									}
								},
								"output": {
									"srcInfo": {
										"srcurl": "https://github.com/codehaus/woodstox",
										"type": "github"
									},
									"pkgInfo": {
										"resourceid": "org.apache.openejb:javaee-api:5.0-2",
										"pkgurl": "https://repo1.maven.org/maven2/org/apache/openejb/javaee-api",
										"type": "maven",
										"category": "build"
									}
								},
								"status": "partial"
							}]
						}
					}
				}]
			}
		}
	}]
}
"""
data = json.loads(x)



#print(data.get('missed'))

#print(data)
# print('\n')

class My_Dictionary(dict):
    #__init__ function
    def __init__(self):
       self = dict()
 
    #Function to add key:value
    def add(self, key, value):
        self[key] = value

#my_level=int(input("Enter the level: "))
key_name=str(input("Enter the key name: "))
key_under_key=str(input("Enter the key under key name: "))
key=str(input("Enter the key: "))


dict_obj = My_Dictionary()
for key, value in data.items():
    dict_obj.add(key,value)
    # print(dict_obj)
for i in dict_obj:
    #print(i)
    if i == key_name:
        val = data.get(i)
        #print("----check-----",val)
        # print("=============",val[0])
        # print("=============",val[0]['input'])
        # print("\n")
        # if i == 'collectionreport' and key_under_key == 'input':
        #     print("------input---------",val[0]['input'])
        # if i == 'collectionreport' and key_under_key == 'output':
        #     print("-------output--------",val[0]['output'])
        # if i == 'collectionreport' and key_under_key == 'pkgInfo':
        #     print("-------pkgInfo--------",val[0]['output']['pkgInfo'])
        # if i == 'collectionreport' and key_under_key == 'pkgInfo' and key== 'input':
        #     print("-------pkgInfo input--------",val[1]['output']['pkgInfo']['input'])

# # #     print("-------------------",i)
# if 'project' in dict_obj and my_level==1:
#     print({key:value})
#     break
# if 'collectionreport' in dict_obj and my_level==2:
#     print({key:value})
    



# if my_level == 1 :
#     print("ok")
# else:
#     print("not")


#print(f)
#print(f['project'])
#print(f['collectionreport'])
# print(f['collectionreport'][0]['input'])
#print(f['collectionreport'][0]['input'])
#print('\n')
#print(f['collectionreport'][0]['output']['srcInfo'])
#print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'])
# # print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][0])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][0]['input'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][0]['status'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['input'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['input']['pkgInfo'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['srcInfo'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['pkgInfo'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['pkgInfo']['dependencies'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['pkgInfo']['dependencies'][0]['input'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['pkgInfo']['dependencies'][0]['output'])
# print('\n')
# print(f['collectionreport'][0]['output']['pkgInfo']['dependencies'][1]['output']['pkgInfo']['dependencies'][0]['output']['pkgInfo'])


#print(f['collectionreport'][0]['output']['pkgInfo'])
























from flask import Flask , redirect, url_for, request

app = Flask(__name__)  
 
# @app.route('/')  
# def home():  
#     return "hello, welcome to our website"

# @app.route('/user/<name>')  
# def name(name):  
#     return "hello,"+name


# @app.route('/user/<int:age>')  
# def age(age):  
#     return "Age = %d"%age

# '''
# add_url_rule(<url rule>, <endpoint>, <view function>)  
# This function is mainly used in the case if the view function is not given and 
# we need to connect a view function to an endpoint externally by using this function
# '''

# def about():  
#     return "This is about page in flask"   
# app.add_url_rule("/about","about",about) 


# @app.route('/admin')  
# def admin():  
#     return 'admin'  
  
# @app.route('/librarion')  
# def librarion():  
#     return 'librarion'  
  
# @app.route('/student')  
# def student():  
#     return 'student'  
  
# @app.route('/user/<name>')  
# def user(name):  
#     if name == 'admin':  
#         return redirect(url_for('admin'))  
#     if name == 'librarion':  
#         return redirect(url_for('librarion'))  
#     if name == 'student':  
#         return redirect(url_for('student'))



# @app.route('/login',methods = ['POST'])  
# def login():  
#     uname=request.form['uname']  
#     passwrd=request.form['pass']  
#     if uname=="ayush" and passwrd=="google":
#         return "Welcome %s" %uname
#     else:
#         return "give the correct username and password"


# @app.route('/login',methods = ['GET'])  
# def login():  
#     uname=request.args.get('uname')  
#     passwrd=request.args.get('pass')  
#     if uname=="ayush" and passwrd=="google":  
#         return "Welcome %s" %uname
#     else:
#         return "give the correct username and password"

# @app.route('/msg')  
# def message():  
#       return "<html><body><h1>Hi, welcome to the website</h1></body></html>"




if __name__ =="__main__":  
    app.run(debug = True)
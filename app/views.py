from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Hello World My Name is Akash")

@app.route('/msgcheck')  
def msg():  
    return render_template('message.html')


@app.route('/custo')  
def customer():  
   return render_template('customer.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result)

if __name__ == '__main__':
    app.run()
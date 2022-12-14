from django import forms

class userForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=50)
    lastname = forms.CharField(label='Last Name', max_length=50)
    img = forms.ImageField(label='Please Enter Your Profile Picture',)
    school = forms.CharField(label='School Name', max_length=50)
    college = forms.CharField(label='College Name', max_length=50)
    email = forms.CharField(label='Emain', max_length=50)
    phone = forms.CharField(label='Phone No', max_length=50)
    skill1 =forms.CharField(label='Enter Your Skills', max_length=50) 
    skill2 =forms.CharField(label='Enter Your Skills', max_length=50) 
    skill3 =forms.CharField(label='Enter Your Skills', max_length=50) 
    skill4 =forms.CharField(label='Enter Your Skills', max_length=50) 
    about = forms.CharField(label='About You', max_length=50)
    insta =forms.CharField(label='Do you have any Instagram account? (optional)', max_length=50) 
    git = forms.CharField(label='Do you have any Github account? (optional)', max_length=50)

    # print("--------now name------",name)

class signupForm(forms.Form):
    fullname = forms.CharField(label='Your Name', max_length=50)
    email = forms.CharField(label='Your Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50)
    repeatpassword = forms.CharField(label='Repeat your password', max_length=50)
    
    # print("--------------",fullname)
    # print("--------------",email)

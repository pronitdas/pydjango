from django import forms

class RegistForm(forms.Form):

    #user_id = forms.AutoField(primary_key=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_id = forms.EmailField(required=False, label='Your e-mail address')
    password = forms.CharField(max_length=50)
    age = forms.CharField(max_length=2)
    gender = forms.CharField(max_length=10)
    level = forms.CharField(max_length=10)
    device_type = forms.CharField(max_length=10)
    device_token = forms.CharField(max_length=200)
    image = forms.ImageField()

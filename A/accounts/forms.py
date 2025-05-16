from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'nameContent'}), label='نام کاربری')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'nameContent'}), label='نام')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'nameContent'}), label='نام خانوادگی')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'emailContent'}), label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id': 'nameContent'}), label='رمز عبور')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'nameContent'}), label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'nameContent'}),label='رمز عبور')
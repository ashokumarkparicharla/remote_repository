from django import forms
class registrationform(forms.Form):
    firstname = forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    lastname = forms.CharField(
        label="enter your last name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your last name'
            }
        )
    )
    username = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'
            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )
    mobile = forms.IntegerField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'
            }
        )
    )
    email = forms.EmailField(
        label="enter your email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'
            }
        )
    )
    gender_choices=(
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=gender_choices,
        label="selct your gender"
    )
    y=range(1960,2020)
    date_of_birth=forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="enter your date of birth"
    )
class loginform(forms.Form):
    username = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'
            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )





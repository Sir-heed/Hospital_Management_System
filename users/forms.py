from django import forms
from .models import User, HospitalStaff, Patient

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Included all the
    required fields, plus a repeat password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2  = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    # is_staff = forms.BooleanField(
    #     label="Internal Staff", 
    #     widget=forms.CheckboxInput,
    #     required=False)

    class Meta:
        model = User
        # fields = ('email', 'username', 'is_staff', 'is_account_manager')
        fields = ('email','firstName', 'lastName',  'middleName', 'gender')
        widgets = {
                'email': forms.EmailInput(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Email',
                    'required': True}),
                'firstName': forms.TextInput(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'First Name',
                    'required': True}),
                'middleName': forms.TextInput(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Other Name',
                    'required': True}),
                'lastName': forms.TextInput(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Last Name',
                    'required': True}),
                'gender': forms.Select(
                    attrs={
                    # 'class': 'listing-input hero__form-input  form-control custom-select'
                    'required': True
                    }), 
                }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is taken!")
        if username.lower() == "admin":
            raise forms.ValidationError("Unauthorized username!")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            # user is active defaultly
            # user is a staff
            user.save()
        return user

class HospitalStaffForm(forms.ModelForm):
    class Meta:
        model = HospitalStaff
        # For now the hospital staff contain the same field as the User class
        fields = ()
        widgets = {}

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('dateOfBirth', 'address')
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={
                    # 'class': 'form-control filter-input',
                    'label':'Date Of Birth',
                    'placeholder': 'Date of birth',
                    'required': True}),
                'address': forms.TextInput(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Address',
                    'required': True})
        }

"""Using django login form"""
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password')

#         widgets = {
#                 'email': forms.EmailInput(attrs={
#                     # 'class': 'form-control filter-input',
#                     'placeholder': 'Email',
#                     'required': True}),
#                 'password': forms.PasswordInput(attrs={
#                     # 'class': 'form-control filter-input',
#                     'placeholder': 'password',
#                     'required': True})            
#             }
from django import forms
import re
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        help_texts = {'username':''}
        widgets = {'password': forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']
    

    def pno_clean(self):
        pno = self.cleaned_data['pno']
        if re.match(r"(?: \+91 ?)?[6-9]\d{9}",pno):
            return pno
        return None
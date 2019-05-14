from django import forms
from .models import Blog

# 폼 수정은 이거 보고 다시 하기 : https://docs.djangoproject.com/en/2.2/topics/forms/

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
        #widget = {
            
            
        #}
        

from django import forms
from mdeditor.fields import MDTextFormField
 
class ArticleForm(forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()

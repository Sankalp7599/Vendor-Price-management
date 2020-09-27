from django import forms

class NewProductForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
    price=forms.FloatField(label='Price')
    company=forms.CharField(label='Company')
    distributer=forms.CharField(label='Distributer')

class SearchForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)

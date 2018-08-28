from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_lenght = 50,
    widget = forms.TextInput(
    attrs = {

    }
    ))

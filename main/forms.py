from django import forms


class StringForm(forms.Form):
    input_string = forms.CharField(label='Input string', max_length=500, min_length=0, required=True)

from django import forms

class Film_q_form(forms.Form):
    title = forms.CharField()
    certificate = forms.MultipleChoiceField()
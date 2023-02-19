from django import forms

class CreateNewMotorcycle(forms.Form):
    motorcycle_text = forms.CharField(label="Motorcycle Name", max_length=200)
    description_text = forms.CharField(label="Description", max_length=200)
    pub_date = forms.DateTimeField(label="Date Published")
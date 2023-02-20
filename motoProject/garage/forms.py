from django import forms

class CreateNewMotorcycle(forms.Form):
    motorcycle_text = forms.CharField(label="Motorcycle Name", max_length=200)
    motorcycle_brand = forms.CharField(label="Brand", max_length=20)
    motorcycle_description = forms.CharField(label="Description", max_length=200)
    pub_date = forms.DateTimeField(label="Date Published")

class ModifyMotorcycle(forms.Form):
    motorcycle_text = forms.CharField(label="Motorcycle Name", max_length=200)
    motorcycle_brand = forms.CharField(label="Brand", max_length=20)
    motorcycle_description = forms.CharField(label="Description", max_length=200)
    pub_date = forms.DateTimeField(label="Date Published")
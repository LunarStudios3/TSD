from django import forms


class ContactForm(forms.Form):
    First_Name = forms.CharField(required=True)
    Last_Name = forms.CharField(required=True)
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-form'}), required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


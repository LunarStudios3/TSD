from django import forms


class ContactForm(forms.Form):
    First_Name = forms.CharField(required = True, label= ("First Name"),
            widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    Last_Name = forms.CharField(required = True, label= ("Last Name"),
            widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    from_email = forms.EmailField(required = True, label= ("Email"),
            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required = True, label= ("Subject"),
            widget=forms.TextInput(attrs={'placeholder': 'Subject'}))

    message = forms.CharField(widget=forms.Textarea, required=True)


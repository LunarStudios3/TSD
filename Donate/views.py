from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from Donate.forms import ContactForm
# Create your views here.
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["First_Name"] + " " + form.cleaned_data["Last_Name"]
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] + "\n" +" \n" + "\n" +" \n" +  "This email was sent from "+ name + " at " + from_email
            try:
                send_mail(subject, message, from_email, ['jmukes97@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "donate.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')

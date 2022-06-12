from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_us_forms
from .models import contactUs
# Create your views here.


def contact_page(request):

    if request.method == 'POST':
        contact_form = contact_us_forms(request.POST)

        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact = contactUs(
                full_name = contact_form.cleaned_data.get('full_name'),
                subject = contact_form.cleaned_data.get('subject'),
                mail = contact_form.cleaned_data.get('mail'),
                message = contact_form.cleaned_data.get('message'),
                is_read_by_admin = False
            )

            contact.save()

            return redirect('home')

    else:
        contact_form = contact_us_forms()

    return render(request,'contact/contact.html',{
        'contact_form' : contact_form
    })


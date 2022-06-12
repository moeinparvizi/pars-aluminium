from django import forms
from .models import contactUs

class contact_us_forms(forms.Form):

    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        error_messages={
            'required' : 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max-length' : 'نام و نام خانوادگی نمی تواند بیشتر از 50 کارکتر باشد'
        },
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'نام و نام خانوادگی'
            }
        )
    )

    mail = forms.EmailField(
        label='ایمیل',
        error_messages={
            'required' : 'لطفا ایمیل خود را وارد کنید'
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }
        )
    )

    subject = forms.CharField(
        error_messages={
            'required': 'لطفا موضوع خود را وارد کنید'
        },
        label='موضوع',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'موضوع'
            }
        )
    )

    message = forms.CharField(
        error_messages={
            'required': 'لطفا پیغام خود را وارد کنید'
        },
        label='پبام',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'پیغام'
            }
        )
    )

class contact_us_model_form(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['full_name','mail','subject','message']
        widgets = {

            'full_name' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'mail': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'message': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


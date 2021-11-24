from django import forms

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ["first_name",
                  "last_name",
                  "phone",
                  "country",
                  "city",
                  "street",
                  "house_number",
                  "url",
                  "phone",
                  "profile_pic"
                  ]

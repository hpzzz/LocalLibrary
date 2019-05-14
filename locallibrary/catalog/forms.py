import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



#The easiest way to validate a single field is to 
# override the method clean_<fieldname>() for the field you want to check.
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Check if date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_("Invalid date - renewal in past"))

        #Check if a date is in allowed range (from now to 4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks = 4):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks ahead"))

        #Remember to always return cleaned data
        return data


from django import forms
import datetime
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

MENU_ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,11)]

class OrderAddMenuItemForm(forms.Form):
	quantity = forms.TypedChoiceField(choices = MENU_ITEM_QUANTITY_CHOICES,
										coerce=int)
	date = forms.DateField(initial = datetime.date.today())
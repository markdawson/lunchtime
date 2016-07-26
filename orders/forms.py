from django import forms
import datetime

MENU_ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,11)]

class OrderAddMenuItemForm(forms.Form):
	quantity = forms.TypedChoiceField(choices = MENU_ITEM_QUANTITY_CHOICES,
										coerce=int) 
	date = forms.DateField(initial = datetime.date.today(),
							 widget=forms.TextInput(attrs={'type': 'date'}))

	def clean_date(self):
		cd = self.cleaned_data
		if cd['date'] < datetime.date.today():
			raise forms.ValidationError("The date cannot be in the past.")
		return cd['date']

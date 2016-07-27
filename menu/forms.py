from django import forms
from .models import MenuItemReview
from .models import MenuItemRating

class ReviewForm(forms.ModelForm):
	class Meta:
		model = MenuItemReview
		fields = ('review',)

class RatingForm(forms.Form):
	RATING_CHOICES = [(i, str(i)) for i in range(1,6)]
	rating = forms.TypedChoiceField(choices = RATING_CHOICES, coerce=int) 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


AGE_RANGE_CHOICES = (
	('Under 12 years old', 'Under 12 years old'),
	('12-17 years old', '12-17 years old'),
	('18-24 years old', '18-24 years old'),
	('25-34 years old', '25-34 years old'),
	('35-44 years old', '35-44 years old'),
	('45-54 years old', '45-54 years old'),
	('55-64 years old', '55-64 years old'),
	('65-74 years old', '65-74 years old'),
	('Above 74 years old', 'Above years old'),
)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	age_range = forms.ChoiceField(choices=AGE_RANGE_CHOICES, required=False)

	class Meta:
		model = User
		fields = ("username", "email", "age_range", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
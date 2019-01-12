from django import forms

class StoreForm(forms.Form):

	name = forms.CharField(max_length = 40,
	                       widget=forms.TextInput(
	                                              attrs={'class': 'form-control form-control-lg', 'placeholder': 'Name'}))
	email = forms.EmailField(max_length = 40,
	                       widget=forms.TextInput(
	                                              attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}))

	def clean(self):
		name = self.cleaned_data['name']
		if len(name) < 2:
			return ValidationError('First name must contain only letters')
		return name
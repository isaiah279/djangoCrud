from django import forms
from.models import Book

# DATA I.S.M

class BookCreate(forms.ModelForm):
	class Meta:
		model=Book
		fields='__all__'
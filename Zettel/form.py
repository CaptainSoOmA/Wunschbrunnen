from django import forms
from django.forms import ModelForm
from Zettel.models import Zettel, BibInfo

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class ZettelForm(ModelForm):
	class Meta:
		model = Zettel
		fields = ["headline","text"]

class BibInfoZettel(ModelForm):
	class Meta:
		model = BibInfo
		fields = [	"author","title","journal",
					"page_from","page_to","year"]
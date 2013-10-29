from tracker.list.models import Article, Impact, Training, TrainingType
from django import forms

class ContactForm(forms.Form):
	event_type = forms.ModelChoiceField(queryset=TrainingType.objects.all().order_by('name'), required=False)
	email = forms.EmailField(required=False)
	byline = forms.CharField(required=False)
	headline = forms.CharField(required=False)
	hyperlink = forms.URLField(initial='http://', required=False)
	pub_date = forms.DateField(initial='mm/dd/yyyy', required=False)
	event_date = forms.DateField(initial='mm/dd/yyyy', required=False)
	story_summary = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:500px'}), required=False)

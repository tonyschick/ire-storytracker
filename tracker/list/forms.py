from tracker.list.models import Article, Impact, Training, TrainingType
from django import forms

EVENT_TYPE_CHOICES = (
(1, 'Watchdog Workshop'),
(2, 'Total Newsroom Training'),
(3, 'CAR Boot Camp'),
(4, 'Mapping Boot Camp'),
(5, 'CAR Conference'),
(6, 'IRE Conference'),
(7, 'Custom training'),
(8, 'None'),
)

class ContactForm(forms.Form):
	event_type = forms.ModelChoiceField(choices=EVENT_TYPE_CHOICES, required=False)
	email = forms.EmailField(required=False)
	byline = forms.CharField(required=False)
	headline = forms.CharField(required=False)
	hyperlink = forms.URLField(initial='http://', required=False)
	pub_date = forms.DateField(initial='mm/dd/yyyy', required=False)
	event_date = forms.DateField(initial='mm/dd/yyyy', required=False)
	story_summary = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:500px'}), required=False)

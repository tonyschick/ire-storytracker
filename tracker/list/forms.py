from tracker.list.models import Article, Impact, Training, TrainingType
from django import forms

class ContactForm(forms.Form):
	eventtype = forms.ModelChoiceField(queryset=TrainingType.objects.all().order_by('name'))
	email = forms.EmailField()
	byline = forms.CharField(required=False)
	headline = forms.CharField()
	hyperlink = forms.URLField(initial='http://')
	pub_date = forms.DateField(initial='mm/dd/yyyy',
						   widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
	event_date = forms.DateField(initial='mm/dd/yyyy',
						   widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
	story_summary = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:500px'}), required=False, )

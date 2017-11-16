from django import forms

from .models import Car

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(
                                        attrs={'placeholder':"Tweet",
                                               'class': "textarea"}
                              ))

    class Meta:
        model = Car
        fields = [
            "content"
        ]

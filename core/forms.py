from django import forms

from .models import News


class NewsForm(forms.ModelForm):
    # headline = forms.CharField(max_length=150, required=False)
    # content = forms.Textarea()
    
    class Meta:
        model = News
        fields = ("headline", "content")
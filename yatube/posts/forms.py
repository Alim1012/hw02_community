from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if '' not in data.lower():
            raise forms.ValidationError(
                'Вы обязательно должны заполнить это поле!'
            )
        return data

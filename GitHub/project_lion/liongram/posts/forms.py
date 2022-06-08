from django import forms
from .models import Post


class PostBaseForm(forms.Form):
    CATEGORY_CHOICES=[
        ('1','일반'),
        ('2','계정')
    ]

    image = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea, required=True)
    #category = forms.CharField(choices=CATEGORY_CHOICES)


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm):
        field = ['image','content']

    def clean_content(self):
        data = self.cleaned_data['content']
        if '비속어' == data:
            raise forms.ValidationError('비속어는 사용하실 수 없습니다.')

        return data
        

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm):
        field = ['image','content']

class PostDetailForm(PostBaseForm):
    pass
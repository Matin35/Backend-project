from django import forms
from . models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    secondTitle = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bodySection1 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    bodySection2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    bodySection3 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    bodySection4 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    bodyPoint = forms.CharField(max_length=400 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    mainPoster = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    secondPoster = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    thirdPoster = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    postersTitle = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))



class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'secondTitle',
            'bodySection1',
            'bodySection2',
            'bodySection3',
            'bodySection4',
            'bodyPoint',
            'mainPoster',
            'secondPoster',
            'thirdPoster',
            'postersTitle',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'secondTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'bodySection1': forms.Textarea(attrs={'class': 'form-control'}),
            'bodySection2': forms.Textarea(attrs={'class': 'form-control'}),
            'bodySection3': forms.Textarea(attrs={'class': 'form-control'}),
            'bodySection4': forms.Textarea(attrs={'class': 'form-control'}),
            'bodyPoint': forms.TextInput(attrs={'class': 'form-control'}),
            'postersTitle': forms.TextInput(attrs={'class': 'form-control'}),
        }

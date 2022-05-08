from django import forms 

#from pizza.models import Comment 
'''
class CommentForm(forms.CommentForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
'''


class CommentForm (forms.Form):
    comment = forms.CharField(Label="Comment", Max_Length=200)
    Check = forms.BooleanField

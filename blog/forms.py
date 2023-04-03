from django import forms
from tinymce.widgets import TinyMCE
from . models import BlogPost, Comment
from mptt.forms import TreeNodeChoiceField
class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class AddPost(forms.ModelForm):
    post = forms.CharField(widget=TinyMCE(attrs={'class':'input-group',
        'name':'post',
        'id':'post',
        'type':'text',
        'placeholder':'Post',
        'cols': 90, 'rows': 30})),

    class Meta:
        model = BlogPost
        fields = {'title', 'summary','post', 'image'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'input-group',
        'name':'title',
        'id':'title',
        'type':'text',
        'placeholder':'Title'
        })
        self.fields['summary'].widget.attrs.update({'class':'input-group',
        'name':'summary',
        'id':'summary',
        'type':'text',
        'placeholder':'Summary'
        })
        self.fields['image'].widget.attrs.update({'class':'input-group',
        'name':'image',
        'id':'image',
        'type':'image',
        'placeholder':'Image'
        })

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='',widget= forms.Textarea(attrs={'class':'comment-section',
        'name':'comment',
        'id':'comment',
        'type':'textarea',
        'placeholder':' Add a Comment',
        'cols': 90, 'rows': 4,}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required=False
        self.fields['parent'].label=''
        self.fields['parent'].widget.attrs.update({'class':'parent no-display',
        })
    class Meta:
        model = Comment
        fields = ['body','parent']
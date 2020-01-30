from django import forms
from .models import Tag,Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    """
    Tag form.
    """
    class Meta:
        model = Tag
        fields = ['title','slug']

        widgets = {
        'title': forms.TextInput(attrs = {'class':'form-control'}),
        'slug':forms.TextInput(attrs = {'class':'form-control'}),
        }

    def clean_slug(self):
        """
        Clean method for slug field which creates restrictions on saving.
        """
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug=='create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    """
    Post form.
    """
    class Meta:
        model = Post
        fields = ['title','slug','body','tags']

        widget = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'slug':forms.TextInput(attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs = {'class':'form-control'}),
        }

        def clean_slug(self):
            """
            Clean method for slug field which creates restrictions on saving.
            """
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug may not be "create"')
            return new_slug
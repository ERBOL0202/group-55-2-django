from django import forms
from posts.models import Category, Post, Tag

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=256)
    content = forms.CharField(max_length=556)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Javascript is noy allowed")
        return title
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content should be different")
        return cleaned_data
class SearchForm(form.Form):
    q = forms.CharField(max_length=256, required=False, label="Search")
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags_id = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (("created_at", "по дате создание"), 
                 ("-created_at", "по дате создание(по убыванию)"),
                 ("updated_at", "по дате обновления"),
                 ("-updated_at", "по дате обновления (по убыванию)"),
                 ("title", "по названию"),
                 ("-title", "по названию(по убыванию)")б
                 ("rate", "по рейтингу"),
                 ("-rate", "по рейтингу(по убыванию)"),
                 (None, None)
                 )
    ordering = forms.ChoiceField(choices=orderings, required=False)


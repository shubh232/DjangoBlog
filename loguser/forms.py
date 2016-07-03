from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from loguser.models import Article
class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','Description']
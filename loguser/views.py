from loguser.models import Article
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,DetailView
from loguser.forms import RegForm,ArticleForm
class Regis(CreateView):
    form_class = RegForm
    template_name = 'register.html'
    success_url = '/login/'

class NewArt(CreateView):
    form_class = ArticleForm
    template_name = 'newart.html'
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        form.instance.Author = self.request.user.username
        return super(NewArt, self).form_valid(form)

class Landing(ListView):
    model = User
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super(Landing,self).get_context_data()
        context['l1'] = len(User.objects.all())
        return context


class AllPosts(ListView):
    model = Article
    template_name = 'allposts.html'
    context_object_name = 'article_list'
    paginate_by = 5
    ordering = '-timestamp'



class MyPostsQuery(ListView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(title__icontains=query)
    template_name = 'myposts.html'
    context_object_name = 'article_list'
    paginate_by = 5
    ordering = '-timestamp'

class MyPosts(ListView):
    def get_queryset(self):
        return Article.objects.filter(Author=self.request.user)
    template_name = 'myposts.html'
    context_object_name = 'article_list'
    paginate_by = 5
    ordering = '-timestamp'

class ArticleView(DetailView):
    model = Article
    slug_field = 'title'
    template_name = 'eachpost.html'


    
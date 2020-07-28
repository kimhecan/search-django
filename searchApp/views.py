from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post
from django.db.models import Q
# Create your views here.


class index(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all


class create(generic.CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content', 'author']

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.save()

        return HttpResponseRedirect(self.request.POST.get('next', '/'))


class detail(generic.DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'


def result(request):
    posts = Post.objects.all()
    query = request.GET.get('query', '')
    setting = request.GET.get('set', '')
    settingFormat = ''

    if query:
        if setting == 'all':
            settingFormat = '전체'
            posts = posts.filter(Q(title__icontains=query) | Q(
                content__icontains=query) | Q(author__icontains=query)).order_by('-time')
        elif setting == 'title':
            settingFormat = '제목'
            posts = posts.filter(title__icontains=query).order_by('-time')
        elif setting == 'content':
            settingFormat = '내용'
            posts = posts.filter(content__icontains=query).order_by('-time')
        elif setting == 'author':
            settingFormat = '필자'
            posts = posts.filter(author__icontains=query).order_by('-time')
        else:
            posts = posts

        return render(request, 'result.html', {'posts': posts, 'query': query, "setting": settingFormat})

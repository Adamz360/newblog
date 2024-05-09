from django.shortcuts import render
from .models import posts  
from django.views import generic
from django.views.decorators.http import require_GET

# creating the class based view for post
class postslist(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_home.html'
    paginate_by = 6


class postdetail(generic.DetailView):
    model = posts
    template_name = "blog_post.html"


def about(request):
    return render(request, 'about.html')


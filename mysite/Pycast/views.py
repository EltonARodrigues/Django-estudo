from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponse, request
from django.views.generic.base import TemplateView
from .models import Post
from django.utils import timezone
from django.views import generic


class IndexView(generic.ListView):

    template_name = "pycast/index.html"
    context_object_name= 'posts'

    def get_queryset(self):

        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:20]

        #return render(request, 'blog/post_list.html', {})

        #return render(request, {'posts': posts })

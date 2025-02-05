from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread, Post


class ThreadListView(ListView):
    model = Thread
    template_name = 'forum.html'
    context_object_name = 'threads'

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title']
    template_name = 'thread_form.html'
    success_url = reverse_lazy('forum_home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# def forum(request):
#      template = loader.get_template('forum.html')
#      return HttpResponse(template.render())
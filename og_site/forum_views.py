from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread, Post


class ThreadList(ListView):
    model = Thread
    template_name = 'forum.html'
    context_object_name = 'threads'


class ThreadDetail(DetailView):
    model = Thread
    template_name = 'thread_detail.html'
    context_object_name = 'thread'


class ThreadCreate(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title']
    template_name = 'thread_form.html'

    def form_valid(self, form):
        # set the user as the creator of the thread
        form.instance.created_by = self.request.user
        thread = form.save()

        # create the initial post
        content = self.request.POST.get('content')  # Getting content from the form
        Post.objects.create(
            content=content,
            created_by=self.request.user,
            thread=thread
        )

        return super().form_valid(form)

    def get_success_url(self):
        # redirect to the newly created thread's detail page
        return reverse_lazy('thread_detail', kwargs={'pk': self.object.pk})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.thread_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('thread_detail', kwargs={'pk': self.kwargs['pk']})

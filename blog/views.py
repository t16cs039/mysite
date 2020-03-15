from django.shortcuts import render

from .models import Post, Status

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from authentication.models import Member

# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    model = Post
    template_name = 'blog/index.html'
    
    def get(self, request, post_id, *args, **kwargs):    
        post = Post.objects.get(pk=post_id)
        return render(request, 'blog/index.html', {'post': post})

class BlogList(LoginRequiredMixin, TemplateView):
    model = Member
    template_name = 'blog/list.html'
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        all_post = Post.objects.all()
        return render(request, 'blog/list.html', {'all_post': all_post})
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = Member.objects.get(user=self.request.user)
        context['member'] = member
        
        context['all_posts'] = Post.objects.filter(status=member.status.all())
        '''
        for i, member_status in enumerate(member.status.all()):
            if i == 0:
                context['all_posts'] = Post.objects.get(status=Status.objects.get(name=member_status))
            else:
                context['all_posts'] += Post.objects.get(status=Status.objects.get(name=member_status))    
        '''
        return context
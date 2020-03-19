from django.shortcuts import render, redirect

from .models import Post, Status

from django.views.generic import TemplateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from authentication.models import Member

# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    model = Post
    template_name = 'blog/index.html'
    '''
    def get(self, request, post_id, *args, **kwargs):    
        post = Post.objects.get(pk=post_id)
        return render(request, 'blog/index.html', {'post': post})
    '''
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        context['post'] = Post.objects.get(pk=self.kwargs.get('post_id'))

        flag = 0

        for s in Member.objects.get(user=self.request.user).status.all():
            if(self.kwargs.get('stat') == str(s)):
                flag += 1
        
        if flag != 1:
            return redirect('authentication:home')
        else:
            return render(request, 'blog/index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        context['post'] = Post.objects.get(pk=self.kwargs.get('post_id'))
        return context

class Sample(LoginRequiredMixin, TemplateView):
    model = Post
    #paginate_by = 5
    template_name = 'blog/sample.html'
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Post.objects.get(status=Status.objects.get(name=self.kwargs.get('status')))
        return context
    '''
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        context['object_list'] = Post.objects.filter(status=Status.objects.get(name=self.kwargs.get('stat'))).order_by('id').reverse()
        flag = 0

        for s in Member.objects.get(user=self.request.user).status.all():
            if(self.kwargs.get('stat') == str(s)):
                flag += 1
        
        if flag != 1:
            return redirect('authentication:home')
        else:
            return render(request, 'blog/sample.html', context)
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

    def get_queryset(self, **kwargs):
        return Post.objects.filter(status=Status.objects.get(name=self.kwargs.get('stat'))).order_by('id').reverse()
    '''

class BlogList(LoginRequiredMixin, TemplateView):
    #model = Member
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
        #status_list = Status.objects.values_list('id', flat=True) #ステータスのIDをリストで取得
        status_list = [1, 2]
        #context['all_posts'] = Post.objects.filter(status=status_list)
        print(Post.objects.all().values())
        #status_list = ['Vlog', 'Beginner']
        #context['all_posts'] = Post.objects.filter(status_id=member.status.all())
        #print(print(Post.objects.all().values()))
        context['all_posts'] = Post.objects.filter(status__in=member.status.all())
        '''
        for i, member_status in enumerate(member.status.all()):
            if i == 0:
                context['all_posts'] = Post.objects.get(status=Status.objects.get(name=member_status))
            else:
                context['all_posts'] += Post.objects.get(status=Status.objects.get(name=member_status))    
        '''
        return context
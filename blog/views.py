from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.views import TaggedObjectList

from blog.forms import PostSearchForm
from blog.models import Post


class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        sch_word = '%s' % self.request.POST.get('search_word', '')
        post_list = Post.objects.filter(Q(title__icontains=sch_word) |
                                        Q(description__icontains=sch_word) |
                                        Q(content__icontains=sch_word)).distinct()
        context = dict()
        context['form'] = form
        context['search_term'] = sch_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

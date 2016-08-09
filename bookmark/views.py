from django.template.defaultfilters import register
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from Leopold.views import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark

    def get_context_data(self, **kwargs):
        context = super(BookmarkLV, self).get_context_data()
        context['nav'] = 'bookmark'
        return context


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url', ]
    success_url = reverse_lazy('bookmark:index')

    def form_invalid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkChangeView(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url', ]
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')


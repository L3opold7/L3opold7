from django.shortcuts import render

# json 응답과 404
from django.http import JsonResponse, Http404, HttpResponseRedirect

# 클래스뷰 전용 로그인 데코레이터
from django.contrib.auth.mixins import LoginRequiredMixin

# 일회용 메시지 (세션)
from django.contrib import messages

# 객체 리스트 뷰 (페이지네이션)
from django.views.generic import ListView

# 객체 자세히보기 뷰
from django.views.generic.detail import DetailView

# 객체 생성 뷰, 객체 삭제 뷰
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# post 모델 
from .models import Post, Photo, Comment

# 오브젝트가 없을때 예외
from django.core.exceptions import ObjectDoesNotExist

# 폼
from .forms import NewPostForm, PhotoForm, CommentForm

'''

model = 사용될 모델
template_name = 템플릿 이름 ( 정의를 안해주면 고유 템플릿 사용 )
context_object_name = 템플릿에서 사용될 이름 ( 정의를 안해주면 기본 object나 모델이름이 사용됨 제네릭 뷰에 따라 다름)
paginate_by = 한페이지당 가져올 글 갯수
queryset = 쿼리셋

def form_valid = 폼 검증 완료시

'''


# /post/ 글 리스트
class ListPost(ListView):
    model = Post
    template_name = 'post/list_post.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListPost, self).get_context_data(**kwargs)
        posts = Post.objects.order_by('-id')
        thumbs = Photo.objects.all()
        context['posts'] = posts
        context['thumbs'] = thumbs
        return context


# /post/tag/<tag> 태그 검색 결과 리스트
class TagListPost(ListView):
    model = Post
    template_name = 'post/list_post.html'
    slug_field = 'tag'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(tag=self.kwargs['slug'])


# /post/<id>/ 글 보기
class ViewPost(DetailView):
    model = Post
    template_name = 'post/view_post.html'

    def get_context_data(self, **kwargs):
        context = super(ViewPost, self).get_context_data(**kwargs)
        photos = Photo.objects.filter(post=self.get_object())
        photos_url = []
        for photo in photos:
            photos_url.append(photo.photo.url)
        context["photos"] = photos_url
        return context


# /post/new/ 글 쓰기
class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/new_post.html'
    form_class = NewPostForm
    success_url = '/post/'

    def form_valid(self, form):
        # 글이 등록되기전 author에 현재 로그인유저를 FK로 넣는다
        post = form.save(commit=False)
        post.author = self.request.user
        messages.success(self.request, 'Complete created Post')
        return super(NewPost, self).form_valid(form)


# /post/<id>/delete/ 글 삭제
class DeletePost(DeleteView):
    model = Post
    success_url = '/post/'

    def get_object(self, queryset=None):
        obj = super(DeletePost, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


# /post/<id>/update/ 글 수정
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/update_post.html'
    form_class = NewPostForm
    success_url = '/post/'

    def get_object(self, queryset=None):
        obj = super(UpdatePost, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

    def form_valid(self, form):
        # 글이 등록되기전 author에 현재 로그인유저를 FK로 넣는다
        messages.success(self.request, 'Complete updated Post!')
        return super(UpdatePost, self).form_valid(form)


# /post/<id>/vote/ 글 투표
# AJAX로 요청함
# 다음 커밋때 고칠예정.
def vote_post(request, id):
    what = request.POST.get('what', False)

    if request.method == 'POST' and what == 'up' or what == 'down':
        # http method가 post이고 what이 up, down인 경우
        if not request.user.is_authenticated():
            raise Http404

        else:
            try:
                # 글을 가져온다
                post = Post.objects.get(id=id)

            except ObjectDoesNotExist:
                raise Http404

            else:
                if what =='up':
                    # up인경우 vote를 + 1
                    post.vote += 1
                    post.save()

                else:
                    # down인경우 vote를 -1
                    post.vote -= 1
                    post.save()

                return JsonResponse({
                    'status': 'ok'
                    })

    else:
        raise Http404


def upload_photo(request, pk):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.post = Post.objects.get(id=pk)
            photo.save()
            return HttpResponseRedirect('/')
    else:
        form = PhotoForm()
    return render(request, 'post/upload_photo.html', {'photo_form': form})

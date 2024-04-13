from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


def post_share(request, post_id):
    # Извлечь пост по идентификатору id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы увпешно прошли валидацию
            cd = form.cleaned_data
            # ... отправить электронное письмо
    else:
        form = EmailPostForm()
    return render(request, 'main/post/share.html', {'post': post, 'form': form})


class PostListView(ListView):
    """ Альтернативное представления списка постов"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'main/post/list.html'

# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         # Если page_number не целое число,
#         # то выдать превую страницу
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если page_number находится вне диапазона, то
#         # выдать последнюю страницу
#         posts = paginator.page(paginator.num_pages)
#
#     # return HttpResponse(posts)
#     return render(request, 'main/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    # return HttpResponse(post)
    return render(request, 'main/post/detail.html', {'post': post})



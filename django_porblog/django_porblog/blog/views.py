from django.db.models import fields
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from templates import blog
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)




# Create your views here.

def login(request):
    return render(request, "registration/login.html")

class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html', texto)

def blog_index(request):
    post_list = Post.objects.all().order_by('-created_on')
    context = {
        "posts": post_list,
    }
    return render(request, "blog/blog_index.html", context)



def blog_detail(request, id):
    post = Post.objects.get(id=id)

    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.isvalid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["author"])
            print("Comentario:" + form.cleaned_data["comment_body"])
            comment = Comment(
                author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["comment_body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, 'blog/blog_detail.html', context)

def post_detail(request, id):
    post= Post.objects.get(id=id)
    context={
        "post": post,
    }
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, id):
    post= Post.objects.get(id=id)
    context={
        "post": post,
    }
    return render(request, 'blog/post_detail', context)

def post_remove(request, id):
    post= Post.objects.get(id=id)
    context={
        "post": post,
    }
    return render(request, 'blog/post_detail', context)



class CreatePostView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    redirect_field_name='index_detail.html'

    form_class = PostForm

    model = Post

# def category(request):
#     return render(request, 'blog/blog_category.html', )

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "categorias/fin_de_la_pobreza.html", context)


@login_required
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    return redirect(request, 'blog/post_detail', id=id)


class CreateComment(CreateView, LoginRequiredMixin):
    model=Comment
    fields=['author', 'comment_body']
    

# @login_required
# def add_comment_to_post(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             comment = cd.save(commit=False)
#             comment.post = Post.objects.get(id=id)
#             print('idpost', comment.post)
#             comment.save()
#             return redirect('blog/post_detail', id=post.id)
#     else:
#         form = CommentForm()
#         return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def add_comment_to_post(request, id):
    post = Post.objects.get(id=id)
    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["author"])
            print("Comentario:" + form.cleaned_data["comment_body"])
            comment = Comment(
                author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["comment_body"],
                post=post
            )
            comment.save()
            comments = Comment.objects.filter(post=post)
            context = {
                "post": post,
                "comments": comments,
                "form": form,
            }

            return render(request, 'blog/blog_detail.html', context)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    post= comment.post.id
    comment.approve()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.id
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def contact(request, id):
    return render(request, 'index copy.html', {})


def nosotros(request):
    return render(request, 'miembros.html',{}) 
    






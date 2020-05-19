from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# get_object_or_404
# 객체를 가져오거나 객체가 없을 시 예외처리

def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드
    return render(request, 'home.html', {'blogs':blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋.메소드

# new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))


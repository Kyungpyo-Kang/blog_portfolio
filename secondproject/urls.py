from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
# 미디어를 활용할 때 추가적으로 임포트한다.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    # blog</int:blog_id> => path converter
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/new', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

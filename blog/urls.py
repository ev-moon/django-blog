from django.contrib import admin
from django.urls import path
import crud.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.home, name='home'),
    path('blog/<int:blog_id>', crud.views.detail, name='detail'),
    path('blog/new', crud.views.new, name='new'),
    path('blog/create', crud.views.create, name='create'),
    path('portfolio', portfolio.views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

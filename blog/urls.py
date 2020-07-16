from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.home, name='home'),
    path('blog/<int:blog_id>', crud.views.detail, name='detail'),
    path('blog/new', crud.views.new, name='new'),
    path('blog/create', crud.views.create, name='create')
]

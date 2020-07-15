from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.home, name='home'),
    path('blog/<int:blog_id>', crud.views.detail, name='detail')
]

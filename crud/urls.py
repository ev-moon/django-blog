from django.urls import path
import crud.views

urlpatterns = [
    path('<int:blog_id>', crud.views.detail, name='detail'),
    path('new', crud.views.new, name='new'),
    path('create', crud.views.create, name='create'),
]
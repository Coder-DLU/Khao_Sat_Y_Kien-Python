from django.urls import path
from django.views.generic import  TemplateView
from . import views

app_name ='polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.viewlist, name='views_list'),
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('<int:question_id>/', views.vote, name='vote'),
]
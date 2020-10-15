from django.urls import path
from .views import post_list , post_detial , New_post,Edit_post,post_delete
from . import views

app_name='blog'

urlpatterns=[
    path('',post_list),
    path('<int:post_id>',post_detial,name='blog_detial'),
    path('New/',New_post,name='newpost'),
    path('<int:post_id>/edit',Edit_post,name='editpost'),
    path('<int:post_id>/delete',post_delete,name='deletepost'),


    path('cbv/',views.post_lists.as_view(),name='all'),
    path('cbv/<int:pk>/detail/',views.detaillist.as_view(),name='detail'),
    path('cbv/new/',views.newlist.as_view(),name='New'),
    path('cbv/<int:pk>/edit/',views.editist.as_view(),name='edit'),
    
    

    

]
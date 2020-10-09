from django.urls import path
from .views import post_list , post_detial , New_post,Edit_post,post_delete

app_name='blog'

urlpatterns=[
    path('',post_list),
    path('<int:post_id>',post_detial,name='blog_detial'),
    path('New/',New_post,name='newpost'),
    path('<int:post_id>/edit',Edit_post,name='editpost'),
    path('<int:post_id>/delete',post_delete,name='deletepost'),
    

]
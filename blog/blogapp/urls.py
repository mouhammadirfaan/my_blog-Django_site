# from django.urls import re_path, url
# from django.urls import include, re_path 
from django.urls import re_path as url
from blogapp import views

urlpatterns =[
    url(r"^$", views.PostListView.as_view(), name="post_list"),
    url(r"^about/$", views.AboutView.as_view(), name="about"),
    url(r"^post/(?P<pk>\d+)$", views.PostListView.as_view(), name="post_Detail"),
    url(r"^post/new/$", views.CreatePostView.as_view(), name="post_new"),
    url(r"^post/(?P<pk>\d+)/edit/$", views.PostUpdateView.as_view(), name="post_edit"),
    url(r"^post/(?P<pk>\d+)/remove/$", views.PostDeleteView.as_view(), name="post_remove"),
    url(r"^drafts/$", views.PostDeleteView.as_view(), name="post_draft_list"),
    url(r"^post/(?P<pk>\d+)/comment/$", views.add_comment_to_post.as_view(), name="add_comment_to_post"),
    url(r"^comment/(?P<pk>\d+)/approve/$", views.comment_approve.as_view(), name="comment_approve"),
    url(r"^comment/(?P<pk>\d+)/remove/$", views.comment_remove.as_view(), name="comment_remove"),
    url(r"^post/(?P<pk>\d+)/publish/$", views.post_publish.as_view(), name="post_publish"),





]

 
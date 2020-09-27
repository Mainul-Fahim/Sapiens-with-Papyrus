from . import views
from django.urls import path

app_name='blog'

urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog_list'),
    path('blog/write/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog/details/<slug:slug>', views.Blog_Details, name='blog_detail'),
    path('blog/liked/<pk>/', views.liked, name='liked_post'),
    path('blog/unliked/<pk>/', views.unliked, name='unliked_post'),
]

"""At first i imported 'path' module from django.url library which we will use for url routing, 
then in urlpatterns section im telling django at which location or url which webpage should work.

For BlogList.as_view() i used 'blog/'
it tells django that on the very first page work as per the BlogList class
and then i choose a reference name for this url as 'blog_list' and mentioned it inside name.

Next is CreateBlog which will be loaded after the BlogList.
Then Blogdetail,Liked and Unliked will be loaded as per click.
on BlogDetail slug is passed as slug line of the post.
And on liked and unliked pk(primary key) is passed.

"""
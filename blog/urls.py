from django.urls import path
from . views import *


urlpatterns = [
    path('posts', post_list, name='post-list'),
    path('post-add', post_add, name='post-add'),

    path('detail/<int:post_id>', post_detail, name='post-detail'),
    path('authors', author_list, name='authors'),
    path('author-add', author_add, name='author-add'),
    path('authors/<author_name>', authors_post, name='author-post'),
    path('category/<category_name>', category_post, name='category-post'),
    path('category-add', category_add, name='category-add'),
]

from django.urls import path

from .views import *

urlpatterns = [
    # image model
    path('image', ImageUploadView.as_view(), name='upload-image'),
    path('image/<int:image_id>', ImageCRUDView.as_view(), name='crud-image'),

    # tag model
    path('tag', TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>', TagDetail.as_view(), name='tag-detail'),

    # comment model
    path('comment', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment-detail'),

    # like model
    path('like', LikeList.as_view(), name='like-list'),
    path('like/<int:pk>', LikeDetail.as_view(), name='like-detail'),
]

from django.urls import path

from .views import *

urlpatterns = [
    # image model
    path('image', ImageUploadView.as_view(), name='upload-image'),
    path('image/<int:image_id>', ImageCRUDView.as_view(), name='crud-image'),
    path('download/image/<int:image_id>', ImageDownload.as_view(), name='download-image'),
    path('image/info/<int:image_id>', ImageInfoView.as_view(), name='get-image-information'),
    path('change-visibilty/image/<int:image_id>', ChangeImageVisible.as_view(), name='change-the-visibility-image'),

    # tag model
    path('tag', TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>', TagDetail.as_view(), name='tag-detail'),

    # comment model
    path('comment', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment-detail'),
    path('comment/count/<int:image_id>', CommentCount.as_view(), name='count-the-number-of-comments'),
    path('comment/image/<int:image_id>', CommentImage.as_view(), name='comment-on-image'),

    # like model
    path('like', LikeList.as_view(), name='like-list'),
    path('like/<int:pk>', LikeDetail.as_view(), name='like-detail'),
    path('is-liked/<int:image_id>', IsLikedByUser.as_view(), name='is-image-liked-by-user'),
    path('dislike/<int:image_id>', DisLikeImage.as_view(), name='dislike-image'),
    path('like/count/<int:image_id>', CountLike.as_view(), name='count-the-number-of-likes'),
]

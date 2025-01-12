'''
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostMVS

router = DefaultRouter()
router.register('posts', PostMVS)

urlpatterns = [
]

urlpatterns += router.urls
'''

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostMVS, CommentMVS, LikeMVS
from rest_framework_nested.routers import NestedSimpleRouter

router = SimpleRouter()

router.register('posts', PostMVS)
router.register('comments', CommentMVS)
router.register('likes', LikeMVS)

post_base_router = NestedSimpleRouter(router, 'posts', lookup='post')
post_base_router.register('comments', CommentMVS, basename="comments")
post_base_router.register('likes', LikeMVS, basename="likes")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(post_base_router.urls))
]

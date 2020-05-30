from django.urls import re_path
from .views import ProductApiView, ProductDetailApiView, ImageApiView, ImageDetailApiView

urlpatterns = [
    re_path('^$', ProductApiView.as_view()),
    re_path('^image/$', ImageApiView.as_view()),
    re_path('^image/(?P<id>\d+)/$', ImageDetailApiView.as_view()),
    re_path(r'^(?P<id>\d+)/$', ProductDetailApiView.as_view()),
]

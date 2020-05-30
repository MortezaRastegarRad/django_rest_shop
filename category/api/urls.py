from django.urls import re_path
from .views import CategoryApiView, CategoryDetailApiView

urlpatterns = [
    re_path('^$', CategoryApiView.as_view()),
    re_path(r'^(?P<id>\d+)/$', CategoryDetailApiView.as_view()),
]

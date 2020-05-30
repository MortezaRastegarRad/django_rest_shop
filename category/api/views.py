from rest_framework import mixins, generics
from .models import Category
from .serializer import CategorySerializer


class CategoryApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

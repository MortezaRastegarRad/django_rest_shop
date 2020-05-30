from rest_framework import mixins, generics
from .models import Product, Image
from .serializer import ProductSerializer, ImageSerializer


class ProductApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ImageApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImageDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = []
    authentication_classes = []
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

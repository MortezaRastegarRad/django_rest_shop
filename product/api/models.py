from django.db import models
import jsonfield

from category.api.models import Category


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    images_path = models.CharField(max_length=1000, null=False, blank=False, editable=False)
    options = jsonfield.JSONField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.images_path = self.category.name + "/" + self.name
        super(Product, self).save(force_insert=False, force_update=False, using=None,
                                  update_fields=None)

    def __repr__(self) -> str:
        class_ = type(self)
        return "<%s.%s(pk=%r, name=%r)>" % (
            class_.__module__,
            class_.__name__,
            self.pk,
            self.name,
        )

    def __str__(self) -> str:
        return self.name


def get_image_filename(instance, filename):
    category_name = instance.product.category.name
    product_name = instance.product.name
    return f"{category_name}/{product_name}/{filename}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)

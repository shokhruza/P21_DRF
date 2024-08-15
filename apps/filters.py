from django.db.models import IntegerChoices
from django_filters import FilterSet, ChoiceFilter

from apps.models import Product


class ProductFilterSet(FilterSet):
    # min_price = NumberFilter(field_name='price', lookup_expr='gte')
    # max_price = NumberFilter(field_name='price', lookup_expr='lte')
    # category = ModelChoiceFilter(queryset=Category.objects.all())
    #
    # class Meta:
    #     model = Product
    #     fields = 'min_price', 'max_price', 'category'

    class Number(IntegerChoices):
        N1 = 1
        N2 = 2
        N3 = 3

    n = ChoiceFilter(choices=Number.choices)

    class Meta:
        model = Product
        fields = 'category',
    #
    # def get_user_type(self, queryset, name, value):
    #     return queryset.filter(owner__type=value)
    #
    # def get_length(self, queryset, name, value):
    #     return queryset.annotate(name_length=Length('name')).filter(name_length__gte=value)


# class CategoryFilterSet(FilterSet):
#     min_products = NumberFilter(field_name='products__count', lookup_expr='gte')
#     max_products = NumberFilter(field_name='products__count', lookup_expr='lte')
#
#     class Meta:
#         model = Category
#         fields = 'min_products', 'max_products'

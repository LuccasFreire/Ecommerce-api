from django_filters import rest_framework as filters

from .models import Produto

class ProdutoFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='nome',lookup_expr='icontains')
    min_preco = filters.NumberFilter(field_name='preco' or 0, lookup_expr='gte')
    max_preco = filters.NumberFilter(field_name='preco' or 1000000, lookup_expr='lte')

    class Meta:
        model = Produto
        fields = '__all__'
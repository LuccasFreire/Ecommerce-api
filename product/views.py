from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import ProdutoFilter
from .serializers import ProdutoSerializer
from .models import Produto
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET'])
def get_produtos(request):
    filterset = ProdutoFilter(request.GET, queryset=Produto.objects.all().order_by('id'))
    cont = filterset.qs.count()

    produtosPorPage = 2
    paginator = PageNumberPagination()
    paginator.page_size = produtosPorPage
    queryset = paginator.paginate_queryset(filterset.qs,request)

    serializer = ProdutoSerializer(queryset, many=True)
    return Response({
        "cont": cont,
        "prodPorPage": produtosPorPage,
        "produtos":serializer.data
        })

@api_view(['GET'])
def get_produto(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    serializer = ProdutoSerializer(produto, many=False)
    return Response({"produto":serializer.data})

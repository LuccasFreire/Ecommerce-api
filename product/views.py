from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import ProdutoFilter
from .serializers import ProdutoSerializer
from .models import Produto
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def get_produtos(request):
    filterset = ProdutoFilter(request.GET, queryset=Produto.objects.all().order_by('id'))
    serializer = ProdutoSerializer(filterset.qs, many=True)
    return Response({"produtos":serializer.data})

@api_view(['GET'])
def get_produto(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    serializer = ProdutoSerializer(produto, many=False)
    return Response({"produto":serializer.data})

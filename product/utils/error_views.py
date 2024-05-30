

from django.http import JsonResponse


def handler404(request, exception):
    message = ("Rota ou URL não encontrada")
    response = JsonResponse(data={'error':message})
    response.status_code = 404
    return response

def handler500(request):
    message = ("Erro interno do sistema")
    response = JsonResponse(data={'error':message})
    response.status_code = 500
    return response
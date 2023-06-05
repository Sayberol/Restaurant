from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from Restaurant.utils import authentication_user


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('username')
        token = authentication_user(username, password)
        if token:
            return JsonResponse({'token': token}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Имя пользовтеля или пароль указан неверно'},
                                status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse({'error': 'Неправильно указан метод запроса'}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not user.check_password(current_password):
            return Response({'error': 'Неправильный пароль'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save()

        return Response({'success': 'Пароль успешно изменён'}, status=status.HTTP_200_OK)

import json
from django.views import View
from django.http import JsonResponse
from .models import Account


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            email=data['email'],
            password=data['password']
        ).save()

        return JsonResponse({'message': '회원가입 완료'}, status=200)

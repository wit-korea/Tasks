from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FollowRelation
from django.db import IntegrityError

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect('/accounts/login')
    else:
        signup_form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'signup_form': signup_form})


@method_decorator(csrf_exempt, name="dispatch")
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)

# 팔로우 버튼을 눌렀을 때


@method_decorator(login_required, name="dispatch")
class RelationCreateView(BaseView):
    def post(self, request):
        try:  # 상대방의 아이디가 존재하는지 확인
            user_id = request.POST.get('id', '')
        except:  # 존재하지 않는 아이디
            return self.response(message='잘못된 요청입니다.', status=400)

        try:  # 내 관계망이 존재하는 지
            relation = FollowRelation.objects.get(follower=request.user)
        except:  # 없을 경우 새 객체 생성
            relation = FollowRelation.objects.create(follower=request.user)

        try:  # 내 아이디일경우 팔로우 x
            if user_id == request.user.id:
                raise IntegrityError
            relation.followee.add(user_id)  # 내 followee에 추가
            relation.save()
        except:
            return self.response(message='잘못된 요청입니다.', status=400)

        return self.response({})

# 언팔로우


@method_decorator(login_required, name='dispatch')
class RelationDeleteView(BaseView):
    def post(self, request):
        try:  # 상대 아이디 존재 확인
            user_id = request.POST.get('id', '')
        except:
            return self.response(message="잘못된 요청입니다.", status=400)

        try:  # 나의 관계망이 존재하는지 확인
            relation = FollowRelation.objects.get(follower=request.user)
        except:
            return self.response(message="잘못된 요청입니다.", status=400)

        try:
            if user_id == request.user.id:  # 자기 자신 언팔로우 불가
                raise IntegrityError
            relation.followee.remove(user_id)  # 언팔로우
            relation.save()
        except:
            return self.response(message="잘못된 요청입니다.", status=400)

        return self.response({})

# 친구 목록 페이지


@method_decorator(login_required, name='dispatch')
class RelationView(TemplateView):
    # template_name = 'relation.html' #템플릿으로 렌더링
    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)
        user = self.request.user

        try:
            followers = FollowRelation.objects.get(
                follower=user).followee.all()  # 내 followee를 모두 가져옴
            context['followees'] = followers
            context['followees_ids'] = list(
                followers.values_list('id', flat=True))

        except:  # 없을경우 넘어감
            pass
        # 나를 팔로우하는 사람, follower를 저장
        context['followers'] = FollowRelation.objects.select_related(
            'follower').filter(followee__in=[user])
        return context

# 사용자 검색


class UserInfoGetView(BaseView):
    def get(self, request):
        username = request.GET.get('username', '').strip()
        try:
            user = User.objects.get(username=username)
        except:
            self.response(message="사용자를 찾을 수 없습니다.", status=404)

        return self.response({'username': username, 'email': user.email, 'id': user.id})

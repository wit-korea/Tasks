from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo


# 가장 메인에서 보여줄 로직
class PhotoList(ListView):
    model = Photo
    template_name_suffic = '_list'


class PhotoCreate(CreateView):
    model = Photo                       # 북마크 모델 활용
    fields = ['text', 'image']          # 생성 시 채워야 할 필드
    template_name_suffix = '_create'    # 연결될 템플릿 이름은 bookmark_create
    succress_url = '/'                  # 성공하면 메인 페이지로 return


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    succress_url = '/'


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    succress_url = '/'


class PhotoDetail(DeleteView):
    model = Photo
    template_name_suffix = '_detail'

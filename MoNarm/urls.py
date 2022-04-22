from django.urls import path

from MoNarm.views import Hi, renderer, Becha, detailData

appName = "monarm"
urlpatterns = [
    path('data/<slug:slug>', detailData, name="detail"),
    path('', renderer, name="renderer"),
    path('hello/', Hi, name="Hi"),
    path('users/', Becha, name="Becha")
]

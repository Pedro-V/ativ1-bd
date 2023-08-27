from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from user_app import views

urlpatterns = [
    path('', views.UsuarioList.as_view()),
    path('<string:pk>/', views.UsuarioDetail.as_view()),
]

# permite tratamento apropriado de diferentes formatos
urlpatterns = format_suffix_patterns(urlpatterns)

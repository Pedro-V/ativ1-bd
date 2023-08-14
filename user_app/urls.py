from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from user_app import views

urlpatterns = [
    # either the empty path or users
    path('', views.UsuarioList.as_view()),
    path('users/', views.UsuarioList.as_view()), 
    path('users/<int:pk>/', views.UsuarioDetail.as_view()),
]

# permite tratamento apropriado de diferentes formatos
urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path 
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('authpage/', views.authpage, name='authpage'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

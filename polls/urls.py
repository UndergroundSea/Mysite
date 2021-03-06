from django.urls import path

from . import views

#from .views import reviewView

app_name = 'polls'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('<int:pk>/results/', reviewView, name='home'),
]
from django.urls import path
from . import views
urlpatterns = [
   # path('', views.index, name='index'),
    path('', views.tweeter_list, name='tweeter_list'),
    path('create/', views.tweeter_create, name='tweeter_create'),
    path('<int:tweet_id>/edit/', views.tweeter_edit, name='tweeter_edit'),
    path('<int:tweet_id>/delete/', views.tweeter_delete, name='tweeter_delete'),
    path('register/', views.register, name='register'),

]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

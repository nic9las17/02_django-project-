from django.urls import path
from . import views
urlpatterns = [
    path('v1/', views.v1_app2),
    path('v2/', views.v2_app2)
] 
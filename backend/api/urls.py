from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('candidates/', views.CandidateView.as_view()),
    path('insights/', views.PartyView.as_view()),
]

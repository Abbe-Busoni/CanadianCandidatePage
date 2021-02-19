from django.urls import include, path
from . import views

urlpatterns = [
    path('candidates/', views.CandidateView.as_view()),
    path('insights/', views.PartyView.as_view()),
]

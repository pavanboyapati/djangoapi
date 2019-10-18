from django.urls import path
from .views import ScoterListView, ScoterDetailView
urlpatterns = [
    path('/available', ScoterListView.as_view()),
    path('/available/<id>', ScoterDetailView.as_view())
]

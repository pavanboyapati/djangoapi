from django.urls import path, include
from .views import ScoterListView  # ScoterDetailView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('available', ScoterListView)
urlpatterns = [
    path('', include(router.urls))
    # path('/available/<id>', ScoterDetailView.as_view())
]

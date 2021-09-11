from rest_framework_nested import routers
from .views import RoundViewSet, ScoreViewSet
from django.urls import path, include
from django.conf.urls import url

rounds_router = routers.SimpleRouter()
rounds_router.register(r'rounds', RoundViewSet, basename='rounds')

scores_router = routers.NestedSimpleRouter(rounds_router, r'rounds', lookup='round')
scores_router.register(r'scores', ScoreViewSet, basename='round-scores')

urlpatterns = [
    url(r'^', include(rounds_router.urls)),
    url(r'^', include(scores_router.urls))
]

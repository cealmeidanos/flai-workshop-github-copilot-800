"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import (
    UserViewSet, TeamViewSet, ActivityViewSet,
    LeaderBoardViewSet, WorkoutViewSet
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root endpoint - provides links to all available API endpoints
    
    The API is accessible via:
    - Localhost: http://localhost:8000/api/
    - Codespace: https://$CODESPACE_NAME-8000.app.github.dev/api/
    
    Available endpoints:
    - /api/users/ - User management
    - /api/teams/ - Team management
    - /api/activities/ - Activity tracking
    - /api/leaderboard/ - Competitive leaderboard
    - /api/workouts/ - Personalized workout suggestions
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'admin': reverse('admin:index', request=request, format=format),
    })


# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderBoardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

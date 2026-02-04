from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, LeaderBoard, Workout, Coach
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderBoardSerializer, WorkoutSerializer, CoachSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'team']
    ordering_fields = ['created_at', 'name']
    
    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get users by team"""
        team = request.query_params.get('team', None)
        if team:
            users = User.objects.filter(team=team)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response({'error': 'Team parameter is required'}, status=400)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get team members"""
        team = self.get_object()
        return Response({'members': team.members})


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user_name', 'user_email', 'activity_type']
    ordering_fields = ['date', 'calories', 'duration']
    
    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities by user email"""
        email = request.query_params.get('email', None)
        if email:
            activities = Activity.objects.filter(user_email=email)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'Email parameter is required'}, status=400)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get activities by type"""
        activity_type = request.query_params.get('type', None)
        if activity_type:
            activities = Activity.objects.filter(activity_type=activity_type)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'Type parameter is required'}, status=400)


class LeaderBoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard
    """
    queryset = LeaderBoard.objects.all()
    serializer_class = LeaderBoardSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user_name', 'user_email', 'team']
    ordering_fields = ['rank', 'total_calories', 'total_duration', 'total_activities']
    
    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top N users from leaderboard"""
        limit = int(request.query_params.get('limit', 10))
        top_users = LeaderBoard.objects.all().order_by('rank')[:limit]
        serializer = self.get_serializer(top_users, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard by team"""
        team = request.query_params.get('team', None)
        if team:
            leaderboard = LeaderBoard.objects.filter(team=team).order_by('rank')
            serializer = self.get_serializer(leaderboard, many=True)
            return Response(serializer.data)
        return Response({'error': 'Team parameter is required'}, status=400)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'activity_type', 'difficulty']
    ordering_fields = ['created_at', 'duration', 'calories_estimate']
    
    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts by difficulty level"""
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            workouts = Workout.objects.filter(difficulty=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'Difficulty parameter is required'}, status=400)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get workouts by activity type"""
        activity_type = request.query_params.get('type', None)
        if activity_type:
            workouts = Workout.objects.filter(activity_type=activity_type)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'Type parameter is required'}, status=400)


class CoachViewSet(viewsets.ModelViewSet):
    """
    API endpoint for coaches
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'specialization']
    ordering_fields = ['created_at', 'name', 'years_experience']

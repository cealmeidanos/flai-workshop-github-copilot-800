from rest_framework import serializers
from .models import User, Team, Activity, LeaderBoard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'team', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'user_name', 'activity_type', 'duration', 
                  'calories', 'distance', 'date', 'notes']


class LeaderBoardSerializer(serializers.ModelSerializer):
    """Serializer for LeaderBoard model"""
    
    class Meta:
        model = LeaderBoard
        fields = ['id', 'user_email', 'user_name', 'team', 'total_activities', 
                  'total_calories', 'total_duration', 'rank', 'last_updated']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'difficulty', 'duration', 
                  'calories_estimate', 'activity_type', 'equipment_needed', 
                  'instructions', 'created_at']

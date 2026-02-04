from django.contrib import admin
from .models import User, Team, Activity, LeaderBoard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['id', 'name', 'email', 'team', 'created_at']
    list_filter = ['team', 'created_at']
    search_fields = ['name', 'email', 'team']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['id', 'name', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['id', 'user_name', 'activity_type', 'duration', 'calories', 'distance', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user_name', 'user_email', 'activity_type']
    ordering = ['-date']


@admin.register(LeaderBoard)
class LeaderBoardAdmin(admin.ModelAdmin):
    """Admin interface for LeaderBoard model"""
    list_display = ['id', 'user_name', 'team', 'rank', 'total_calories', 'total_duration', 'total_activities']
    list_filter = ['team', 'rank']
    search_fields = ['user_name', 'user_email', 'team']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['id', 'title', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    list_filter = ['difficulty', 'activity_type', 'created_at']
    search_fields = ['title', 'description', 'activity_type']
    ordering = ['-created_at']

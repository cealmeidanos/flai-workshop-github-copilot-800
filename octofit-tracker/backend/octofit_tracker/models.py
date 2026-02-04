from django.db import models
from django.utils import timezone


class User(models.Model):
    """Model for user profiles"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    team = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    """Model for teams"""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    members = models.JSONField(default=list)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    """Model for activity logs"""
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    distance = models.FloatField(null=True, blank=True)  # in km
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user_name} - {self.activity_type}"


class LeaderBoard(models.Model):
    """Model for leaderboard entries"""
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    rank = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']
    
    def __str__(self):
        return f"{self.user_name} - {self.total_calories} calories"


class Workout(models.Model):
    """Model for personalized workout suggestions"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    activity_type = models.CharField(max_length=100)
    equipment_needed = models.JSONField(default=list)
    instructions = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.title

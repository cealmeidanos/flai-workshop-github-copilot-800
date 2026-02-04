from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, LeaderBoard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Tests for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            email='test@example.com',
            name='Test User',
            password='testpass123',
            team='Test Team'
        )
    
    def test_user_creation(self):
        """Test user is created properly"""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team, 'Test Team')
    
    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    """Tests for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            members=['test1@example.com', 'test2@example.com']
        )
    
    def test_team_creation(self):
        """Test team is created properly"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
        self.assertEqual(len(self.team.members), 2)
    
    def test_team_str(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Tests for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            activity_type='Running',
            duration=30,
            calories=300,
            distance=5.0,
            notes='Morning run'
        )
    
    def test_activity_creation(self):
        """Test activity is created properly"""
        self.assertEqual(self.activity.user_email, 'test@example.com')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
    
    def test_activity_str(self):
        """Test activity string representation"""
        self.assertEqual(str(self.activity), 'Test User - Running')


class LeaderBoardModelTest(TestCase):
    """Tests for LeaderBoard model"""
    
    def setUp(self):
        self.entry = LeaderBoard.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            team='Test Team',
            total_activities=10,
            total_calories=3000,
            total_duration=300,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created properly"""
        self.assertEqual(self.entry.user_email, 'test@example.com')
        self.assertEqual(self.entry.total_activities, 10)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Tests for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout',
            difficulty='Intermediate',
            duration=45,
            calories_estimate=400,
            activity_type='HIIT',
            equipment_needed=['None'],
            instructions=['Step 1', 'Step 2']
        )
    
    def test_workout_creation(self):
        """Test workout is created properly"""
        self.assertEqual(self.workout.title, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'Intermediate')
        self.assertEqual(self.workout.duration, 45)
    
    def test_workout_str(self):
        """Test workout string representation"""
        self.assertEqual(str(self.workout), 'Test Workout')


class UserAPITest(APITestCase):
    """API tests for User endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            email='api@example.com',
            name='API User',
            password='apipass123',
            team='Team API'
        )
    
    def test_get_users(self):
        """Test retrieving users list"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_user(self):
        """Test creating a new user"""
        url = reverse('user-list')
        data = {
            'email': 'new@example.com',
            'name': 'New User',
            'password': 'newpass123',
            'team': 'New Team'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITest(APITestCase):
    """API tests for Team endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='API Team',
            description='Team for API testing',
            members=['test@example.com']
        )
    
    def test_get_teams(self):
        """Test retrieving teams list"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ActivityAPITest(APITestCase):
    """API tests for Activity endpoints"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            activity_type='Running',
            duration=30,
            calories=300
        )
    
    def test_get_activities(self):
        """Test retrieving activities list"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LeaderBoardAPITest(APITestCase):
    """API tests for LeaderBoard endpoints"""
    
    def setUp(self):
        self.entry = LeaderBoard.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            team='Test Team',
            total_activities=5,
            total_calories=1500,
            total_duration=150,
            rank=1
        )
    
    def test_get_leaderboard(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    """API tests for Workout endpoints"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title='API Workout',
            description='Workout for API testing',
            difficulty='Beginner',
            duration=30,
            calories_estimate=250,
            activity_type='Yoga',
            equipment_needed=['Yoga mat'],
            instructions=['Warm up', 'Cool down']
        )
    
    def test_get_workouts(self):
        """Test retrieving workouts list"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

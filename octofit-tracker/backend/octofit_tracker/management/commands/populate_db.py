from django.core.management.base import BaseCommand
from django.utils import timezone
from octofit_tracker.models import User, Team, Activity, LeaderBoard, Workout
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderBoard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data deleted'))
        
        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Defenders of Earth and beyond',
            members=[]
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Protectors of Justice',
            members=[]
        )
        
        self.stdout.write(self.style.SUCCESS('Teams created'))
        
        # Create Marvel users
        self.stdout.write('Creating Marvel superheroes...')
        marvel_users = [
            {
                'email': 'tony.stark@marvel.com',
                'name': 'Tony Stark',
                'password': 'ironman123',
                'team': 'Team Marvel'
            },
            {
                'email': 'steve.rogers@marvel.com',
                'name': 'Steve Rogers',
                'password': 'captainamerica123',
                'team': 'Team Marvel'
            },
            {
                'email': 'natasha.romanoff@marvel.com',
                'name': 'Natasha Romanoff',
                'password': 'blackwidow123',
                'team': 'Team Marvel'
            },
            {
                'email': 'bruce.banner@marvel.com',
                'name': 'Bruce Banner',
                'password': 'hulk123',
                'team': 'Team Marvel'
            },
            {
                'email': 'thor.odinson@marvel.com',
                'name': 'Thor Odinson',
                'password': 'thor123',
                'team': 'Team Marvel'
            },
        ]
        
        # Create DC users
        self.stdout.write('Creating DC superheroes...')
        dc_users = [
            {
                'email': 'bruce.wayne@dc.com',
                'name': 'Bruce Wayne',
                'password': 'batman123',
                'team': 'Team DC'
            },
            {
                'email': 'clark.kent@dc.com',
                'name': 'Clark Kent',
                'password': 'superman123',
                'team': 'Team DC'
            },
            {
                'email': 'diana.prince@dc.com',
                'name': 'Diana Prince',
                'password': 'wonderwoman123',
                'team': 'Team DC'
            },
            {
                'email': 'barry.allen@dc.com',
                'name': 'Barry Allen',
                'password': 'flash123',
                'team': 'Team DC'
            },
            {
                'email': 'arthur.curry@dc.com',
                'name': 'Arthur Curry',
                'password': 'aquaman123',
                'team': 'Team DC'
            },
        ]
        
        all_users_data = marvel_users + dc_users
        created_users = []
        
        for user_data in all_users_data:
            user = User.objects.create(**user_data)
            created_users.append(user)
        
        # Update team members
        team_marvel.members = [u.email for u in created_users if u.team == 'Team Marvel']
        team_marvel.save()
        
        team_dc.members = [u.email for u in created_users if u.team == 'Team DC']
        team_dc.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(created_users)} users'))
        
        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'HIIT']
        activities_count = 0
        
        for user in created_users:
            # Create 5-10 activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                distance = round(random.uniform(1, 20), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                days_ago = random.randint(0, 30)
                
                Activity.objects.create(
                    user_email=user.email,
                    user_name=user.name,
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    distance=distance,
                    date=timezone.now() - timedelta(days=days_ago),
                    notes=f'{activity_type} session completed by {user.name}'
                )
                activities_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_count} activities'))
        
        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in created_users:
            user_activities = Activity.objects.filter(user_email=user.email)
            total_activities = user_activities.count()
            total_calories = sum(a.calories for a in user_activities)
            total_duration = sum(a.duration for a in user_activities)
            
            LeaderBoard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_activities=total_activities,
                total_calories=total_calories,
                total_duration=total_duration
            )
        
        # Update ranks
        leaderboard_entries = LeaderBoard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(created_users)} leaderboard entries'))
        
        # Create workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'title': 'Super Soldier Strength Training',
                'description': 'Build strength like Captain America with this intense workout',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 600,
                'activity_type': 'Weightlifting',
                'equipment_needed': ['Barbell', 'Dumbbells', 'Pull-up bar'],
                'instructions': [
                    'Warm-up: 10 minutes light cardio',
                    'Bench press: 4 sets of 8-10 reps',
                    'Squats: 4 sets of 8-10 reps',
                    'Deadlifts: 3 sets of 6-8 reps',
                    'Pull-ups: 3 sets to failure',
                    'Cool-down: 10 minutes stretching'
                ]
            },
            {
                'title': 'Speed Force Sprint Training',
                'description': 'Improve your speed and agility like The Flash',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_estimate': 500,
                'activity_type': 'Running',
                'equipment_needed': ['Running shoes', 'Timer'],
                'instructions': [
                    'Warm-up: 5 minutes jogging',
                    '8x 100m sprints with 90 seconds rest',
                    '4x 200m tempo runs with 2 minutes rest',
                    'Cool-down: 5 minutes walking',
                    'Stretching: 10 minutes'
                ]
            },
            {
                'title': 'Warrior Yoga Flow',
                'description': 'Build flexibility and mental strength like Wonder Woman',
                'difficulty': 'Beginner',
                'duration': 30,
                'calories_estimate': 150,
                'activity_type': 'Yoga',
                'equipment_needed': ['Yoga mat'],
                'instructions': [
                    'Start in Mountain Pose',
                    'Flow through Sun Salutations: 5 rounds',
                    'Warrior I, II, and III poses: Hold each for 1 minute per side',
                    'Tree pose: 1 minute per side',
                    'End with Savasana: 5 minutes'
                ]
            },
            {
                'title': 'Aquatic Endurance Training',
                'description': 'Build underwater endurance like Aquaman',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_estimate': 400,
                'activity_type': 'Swimming',
                'equipment_needed': ['Pool', 'Goggles'],
                'instructions': [
                    'Warm-up: 200m easy swim',
                    '10x 100m freestyle with 30 seconds rest',
                    '5x 50m backstroke with 20 seconds rest',
                    '5x 50m breaststroke with 20 seconds rest',
                    'Cool-down: 200m easy swim'
                ]
            },
            {
                'title': 'Dark Knight Combat Training',
                'description': 'Master combat fitness like Batman',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 700,
                'activity_type': 'Boxing',
                'equipment_needed': ['Boxing gloves', 'Heavy bag', 'Jump rope'],
                'instructions': [
                    'Jump rope: 10 minutes',
                    'Shadow boxing: 3 rounds of 3 minutes',
                    'Heavy bag work: 5 rounds of 3 minutes',
                    'Speed bag: 3 rounds of 2 minutes',
                    'Core work: 15 minutes',
                    'Cool-down: 10 minutes stretching'
                ]
            },
            {
                'title': 'High-Tech HIIT',
                'description': 'Burn calories efficiently like Iron Man',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories_estimate': 400,
                'activity_type': 'HIIT',
                'equipment_needed': ['None'],
                'instructions': [
                    'Warm-up: 5 minutes light movement',
                    'Circuit (repeat 4 times):',
                    '- Burpees: 30 seconds',
                    '- Mountain climbers: 30 seconds',
                    '- Jump squats: 30 seconds',
                    '- High knees: 30 seconds',
                    '- Rest: 1 minute',
                    'Cool-down: 5 minutes stretching'
                ]
            },
            {
                'title': 'Power Cycling Challenge',
                'description': 'Build leg strength and endurance',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_estimate': 550,
                'activity_type': 'Cycling',
                'equipment_needed': ['Bike', 'Helmet'],
                'instructions': [
                    'Warm-up: 10 minutes easy pace',
                    'Main set: 40 minutes varied intensity',
                    '- 5 minutes moderate pace',
                    '- 2 minutes high intensity',
                    '- Repeat 5 times',
                    'Cool-down: 10 minutes easy pace'
                ]
            }
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Summary ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard Entries: {LeaderBoard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully!'))

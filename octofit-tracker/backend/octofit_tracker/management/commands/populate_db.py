from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='ironman@marvel.com', type='run', duration=30, date='2025-11-25'),
            Activity(user='captain@marvel.com', type='cycle', duration=45, date='2025-11-25'),
            Activity(user='batman@dc.com', type='swim', duration=60, date='2025-11-25'),
            Activity(user='wonderwoman@dc.com', type='yoga', duration=50, date='2025-11-25'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=175, rank=1)
        Leaderboard.objects.create(team='dc', points=110, rank=2)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body exercise', difficulty='easy'),
            Workout(name='Squats', description='Lower body exercise', difficulty='medium'),
            Workout(name='Plank', description='Core strength', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))

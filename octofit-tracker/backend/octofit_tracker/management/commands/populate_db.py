from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=tony, type='Running', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, type='Cycling', duration=45, date='2024-01-02')
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date='2024-01-03')
        Activity.objects.create(user=clark, type='Running', duration=50, date='2024-01-04')

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='All')
        Workout.objects.create(name='Speed Run', description='Speed and agility training', suggested_for='Marvel')
        Workout.objects.create(name='Flight Training', description='Flight and endurance', suggested_for='DC')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))

        # Ensure unique index on email
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({ "email": 1 }, { "unique": true })')
        self.stdout.write(self.style.SUCCESS('Ensured unique index on user email.'))

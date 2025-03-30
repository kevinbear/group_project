# filepath: /Users/kevin/Documents/GitHub/group_project/final_project/restaurant/management/commands/generate_dummy_data.py
from django.core.management.base import BaseCommand
from restaurant.models import CustomUser, UserProfile
from faker import Faker

class Command(BaseCommand):
    help = 'Generate dummy data for CustomUser and UserProfile'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create dummy managers
        for _ in range(5):
            manager = CustomUser.objects.create_user(
                email=fake.email(),
                password="password123",
                role="manager",
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(f"Manager created: {manager.email}")

        # Create dummy customers and profiles
        for _ in range(10):
            customer = CustomUser.objects.create_user(
                email=fake.email(),
                password="password123",
                role="customer"
            )
            profile = UserProfile.objects.create(
                user=customer,
                address=fake.address(),
                date_of_birth=fake.date_of_birth(),
                profile_picture=None
            )
            self.stdout.write(f"Customer created: {customer.email} with profile")
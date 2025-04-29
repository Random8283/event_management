from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import UserProfile

class Command(BaseCommand):
    help = 'Creates test users (admin and regular user)'

    def handle(self, *args, **options):
        # Create regular user
        user, created = User.objects.get_or_create(
            username='user',
            defaults={
                'email': 'user@email.com',
                'is_staff': False,
                'is_superuser': False
            }
        )
        if created:
            user.set_password('userpass123')
            user.save()
            UserProfile.objects.create(user=user, is_admin=False)
            self.stdout.write(self.style.SUCCESS('Regular user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Regular user already exists'))

        self.stdout.write(self.style.SUCCESS('Test users creation completed')) 
"""
Seed the database with demo data for marking / manual testing.

Creates:
- Default superuser
- Demo members
- Demo events
- Demo comments
"""

import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from events.models import Comment, Event

# Credentials are intentionally simple for marking. Documented in the README.
SUPERUSER = { "username": "admin", "password": "cannybyte-admin" }
DEMO_PASSWORD = "cannybyte-demo"


class Command(BaseCommand):
  help = "Seed demo users and events."

  def handle(self, *args, **options):
    admin = self._ensure_user(
      SUPERUSER["username"],
      SUPERUSER["password"],
      email="admin@cannybyte.local",
      is_staff=True,
      is_superuser=True,
    )
    alice = self._ensure_user("alice", DEMO_PASSWORD, email="alice@example.com")
    bob = self._ensure_user("bob", DEMO_PASSWORD, email="bob@example.com")

    food_bank = self._ensure_event(
      author=alice,
      title="Community Food Bank",
      date=datetime.date(2026, 6, 14),
      time=datetime.time(10, 0),
      location="Town Hall",
      description=(
        "Free food and a warm space - All Welcome."
        "needed."
      ),
    )
    self._ensure_event(
      author=bob,
      title="Budgeting Workshop",
      date=datetime.date(2026, 6, 18),
      time=datetime.time(18, 30),
      location="Library",
      description="Tips for making your money go further.",
    )
    self._ensure_event(
      author=alice,
      title="Tech Repairs",
      date=datetime.date(2026, 6, 21),
      time=datetime.time(13, 0),
      location="Community Centre",
      description="Bring broken items and fix them with our volunteers.",
    )

    self._ensure_comment(
      food_bank, bob, "Is parking available nearby?"
    )
    self._ensure_comment(
      food_bank, alice, "Yes, free car park behind the Town Hall."
    )

    self.stdout.write(self.style.SUCCESS("Seed complete."))



  def _ensure_user(self, username, password, **extra):
    """Get or create user"""
    user, created = User.objects.get_or_create(
      username=username, defaults=extra
    )
    if created:
      user.set_password(password)
      user.save()
    return user


  def _ensure_event(self, *, author, title, **fields):
    """Get or create event"""
    event, created = Event.objects.get_or_create(
      title=title, author=author, defaults=fields
    )
    return event


  def _ensure_comment(self, event, author, body):
    """Get or create comment"""
    comment, created = Comment.objects.get_or_create(
      event=event, author=author, body=body
    )
    return comment

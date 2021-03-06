import uuid
from django.conf import settings
from datetime import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date  # NEW 10

class Profile(models.Model):
    """Model representing a Profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )

    sessions = models.ManyToManyField(
        "Session",
        related_name="sessions",
        blank=True
    )

    sessions_owned = models.ManyToManyField(
        "Session",
        related_name="sessions_owned",
        blank=True
    )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username

class Session(models.Model):
    """Model representing a Session."""

    uuid = models.CharField(
        max_length=60,
        help_text="ID to uniquely identify a session",
        primary_key=True
    )

    name = models.CharField(
        max_length=100,
        help_text="Name of the session",
        null=True
    )

    profiles = models.ManyToManyField(
        "Profile"
    )

    owner = models.ForeignKey(
        "Profile",
        on_delete=models.SET_NULL,
        null=True,
        related_name="owner"
    )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    messages = models.ForeignKey(
        "Message",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        help_text="The session's location",
        default=""
    )

    online = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("session", args=[str(self.pk)])

    def get_join_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("join_session", args=[str(self.pk)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game(models.Model):
    """Model representing a Game."""

    title = models.CharField(
        max_length=100,
        help_text="The game's title",
        default=""
    )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    online = models.BooleanField(default=True)

    description = models.CharField(
        max_length=100,
        help_text="The game's description",
        default=""
    )

    link = models.CharField(
        max_length=100,
        help_text="A link to this game's website",
        default=""
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Platform(models.Model):
    """Model representing a Platform."""

    name = models.CharField(
        max_length=100,
        help_text="The name of the platform (e.g. PlayStation 4)",
        default=""
    )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Message(models.Model):
    """Model representing a Message."""

    text = models.CharField(
        max_length=100,
        help_text="The text content of the message",
        default=""
    )

    sender = models.ForeignKey(
        "Profile",
        on_delete=models.SET_NULL,
        null=True
    )

    context = models.ForeignKey(
        "Session",
        on_delete=models.SET_NULL,
        null=True
    )

    datetime = models.DateTimeField(
        default=timezone.now,
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return f"Message from: {self.sender} with text: {self.text}"

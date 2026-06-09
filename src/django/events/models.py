from django.conf import settings
from django.db import models
from django.urls import reverse


class Event(models.Model):
  """A community event posted by a member."""

  title = models.CharField(max_length=200)
  date = models.DateField()
  time = models.TimeField(blank=True, null=True)
  location = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to="events/", blank=True, null=True)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="events",
  )
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["date", "time"]

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    """Get the url from the view name and arguments"""
    return reverse("event_detail", kwargs={"pk": self.pk})



class Comment(models.Model):
  """A comment left by a member on an event."""

  event = models.ForeignKey(
    Event,
    on_delete=models.CASCADE,
    related_name="comments",
  )
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="comments",
  )
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["created_at"]

  def __str__(self):
    return f"Comment by {self.author} on {self.event}"

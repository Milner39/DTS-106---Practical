from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_date

from ..forms import CommentForm, EventForm, SignUpForm
from ..models import Event


def _can_modify(user, event):
  """An event may be changed by its author or any staff member."""
  return event.author_id == user.id or user.is_staff




# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------


def home(request):
  return render(request, "events/home.html")


def about(request):
  return render(request, "events/about.html")


def contact(request):
  return render(request, "events/contact.html")



# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------


def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(
        request, "Welcome to CannyByte! You've successfully singed-up."
      )
      return redirect("events")
  else:
    form = SignUpForm()
  return render(request, "events/signup.html", {"form": form})



# ---------------------------------------------------------------------------
# Events (members only)
# ---------------------------------------------------------------------------


@login_required
def events_list(request):
  search_title = request.GET.get("search_title", "").strip()
  date_str = request.GET.get("date", "").strip()

  events = Event.objects.select_related("author").all()
  if search_title:
    events = events.filter(title__icontains=search_title)
  if date_str:
    parsed = parse_date(date_str)
    if parsed:
      events = events.filter(date=parsed)

  return render(request, "events/events_list.html", {
    "events": events,
    "search_title": search_title,
    "date": date_str,
  })


@login_required
def event_detail(request, pk):
  event = get_object_or_404(Event, pk=pk)

  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.event = event
      comment.author = request.user
      comment.save()
      messages.success(request, "Comment posted.")
      return redirect("event_detail", pk=event.pk)
  else:
    form = CommentForm()

  return render(request, "events/event_detail.html", {
    "event": event,
    "comments": event.comments.select_related("author"),
    "form": form,
    "can_modify": _can_modify(request.user, event),
  })


@login_required
def event_create(request):
  if request.method == "POST":
    form = EventForm(request.POST, request.FILES)
    if form.is_valid():
      event = form.save(commit=False)
      event.author = request.user
      event.save()
      messages.success(request, "Event published.")
      return redirect(event)
  else:
    form = EventForm()
  return render(request, "events/event_form.html", {
    "form": form,
    "is_edit": False,
  })


@login_required
def event_edit(request, pk):
  event = get_object_or_404(Event, pk=pk)
  if not _can_modify(request.user, event):
    return HttpResponseForbidden("You cannot edit this event.")

  if request.method == "POST":
    form = EventForm(request.POST, request.FILES, instance=event)
    if form.is_valid():
      form.save()
      messages.success(request, "Event updated.")
      return redirect(event)
  else:
    form = EventForm(instance=event)
  return render(request, "events/event_form.html", {
    "form": form,
    "is_edit": True,
    "event": event,
  })


@login_required
def event_delete(request, pk):
  event = get_object_or_404(Event, pk=pk)
  if not _can_modify(request.user, event):
    return HttpResponseForbidden("You cannot delete this event.")

  if request.method == "POST":
    event.delete()
    messages.success(request, "Event deleted.")
    return redirect("my_events")
  return render(request, "events/event_confirm_delete.html", {
    "event": event,
  })


@login_required
def my_events(request):
  events = Event.objects.filter(author=request.user)
  return render(request, "events/my_events.html", {"events": events})


@user_passes_test(lambda u: u.is_staff)
def admin_events(request):
  search_title = request.GET.get("search_title", "").strip()
  events = Event.objects.select_related("author").all()
  if search_title:
    events = events.filter(title__icontains=search_title)
  return render(request, "events/admin_events.html", {
    "events": events,
    "search_title": search_title,
  })

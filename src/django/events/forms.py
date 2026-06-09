from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Event


def _add_bootstrap_class(fields):
  """
  Give every widget in `fields` Bootstrap's `form-control` class.

  Needed for the 2 special cases of the authentication forms where we are 
  extending a parent class and must add the attributes after.
  """

  for field in fields.values():
    field.widget.attrs.setdefault("class", "form-control")




# ---------------------------------------------------------------------------
# Authentication Forms
# ---------------------------------------------------------------------------


class SignUpForm(UserCreationForm):
  """Sing-Up form."""

  email = forms.EmailField(required=True)

  class Meta(UserCreationForm.Meta):
    model = User
    fields = ("username", "email", "password1", "password2")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    _add_bootstrap_class(self.fields)



class LoginForm(AuthenticationForm):
  """Login form."""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    _add_bootstrap_class(self.fields)



# ---------------------------------------------------------------------------
# Model Forms
# ---------------------------------------------------------------------------


class EventForm(forms.ModelForm):
  """Create / edit an event."""

  class Meta:
    model = Event
    fields = ("title", "date", "time", "location", "description", "image")
    widgets = {
      "title": forms.TextInput(attrs={"class": "form-control"}),
      "date": forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
      ),
      "time": forms.TimeInput(
        attrs={"type": "time", "class": "form-control"}
      ),
      "location": forms.TextInput(attrs={"class": "form-control"}),
      "description": forms.Textarea(
        attrs={"class": "form-control", "rows": 4}
      ),
      "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
    }


class CommentForm(forms.ModelForm):
  """Leave a comment on an event."""

  class Meta:
    model = Comment
    fields = ("body",)
    widgets = {
      "body": forms.Textarea(
        attrs={
          "class": "form-control",
          "rows": 3,
          "placeholder": "Add a comment…",
        }
      ),
    }

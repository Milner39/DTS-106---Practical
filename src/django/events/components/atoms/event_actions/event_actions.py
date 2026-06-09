"""
Event Actions

The Edit + Delete button pair for an event:
- Used on the event detail page (`icons=True`)
- Used on the event tables (`icons=False`)
"""

from typing import NamedTuple

from django_components import Component, register

from events.models import Event



@register("event_actions")
class EventActions(Component):
  template_file = "event_actions.html"


  class Kwargs(NamedTuple):
    event: Event
    icons: bool = False


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "event": kwargs.event,
      "icons": kwargs.icons,
    }

"""
Event Table

A table of events with Edit/Delete actions:
- Used by "My events" (`show_owner=False`)
- Used by the admin dashboard (`show_owner=True`)
"""

from typing import NamedTuple

from django.db.models import QuerySet
from django_components import Component, register

from events.models import Event



@register("event_table")
class EventTable(Component):
  template_file = "event_table.html"


  class Kwargs(NamedTuple):
    events: QuerySet[Event]
    show_owner: bool = False


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "events": kwargs.events,
      "show_owner": kwargs.show_owner,
    }

"""
Event Card

A Card summarising a single event:
- Used in the events list grid
"""

from typing import NamedTuple

from django_components import Component, register

from events.models import Event



@register("event_card")
class EventCard(Component):
  template_file = "event_card.html"


  class Kwargs(NamedTuple):
    event: Event


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "event": kwargs.event,
    }

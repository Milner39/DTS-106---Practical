"""
Event Search Form

The members' events filter:
- Search by title (`search_title`)
- Filter by date (`date`)
- Submitted as a single GET form. Inputs are repopulated from the current query.
"""

from typing import NamedTuple

from django_components import Component, register



@register("event_search_form")
class EventSearchForm(Component):
  template_file = "event_search_form.html"


  class Kwargs(NamedTuple):
    search_title: str = ""
    date: str = ""


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "search_title": kwargs.search_title,
      "date": kwargs.date,
    }

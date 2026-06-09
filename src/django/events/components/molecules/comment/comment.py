"""
Comment

A single comment on an event:
- Author
- Timestamp
- Body
"""

from typing import NamedTuple

from django_components import Component, register

from events.models import Comment



@register("comment")
class CommentCard(Component):
  template_file = "comment.html"


  class Kwargs(NamedTuple):
    comment: Comment


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "comment": kwargs.comment,
    }

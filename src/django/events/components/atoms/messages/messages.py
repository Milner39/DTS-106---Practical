"""
Messages

Renders Django's messages as dismissible alerts.
"""

from django_components import Component, register



@register("messages")
class Messages(Component):
  template_file = "messages.html"


  def get_template_data(self, args, kwargs, slots, context):
    # `messages` is provided by the messages context processor and is available
    # directly in the template.
    # Returning it here causes django-components to error.
    return {}

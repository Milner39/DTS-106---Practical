from django.utils.safestring import mark_safe

from ..components.organisms.base.base import Base


def _page(request, *, title, content):
  """Render a page inside the `base` component."""

  return Base.render_to_response(
    request=request,
    args=Base.Args(
      title=title
    ),
    slots=Base.Slots(
      content=mark_safe(content),
    ),
  )


def index(request):
  return _page(
    request,
    title="Home",
    content="<h1>Welcome to My Website</h1>",
  )


def about(request):
  return _page(
    request,
    title="About",
    content="<h1>About</h1><p>This site is a django-components demo.</p>",
  )


def contact(request):
  return _page(
    request,
    title="Contact",
    content="<h1>Contact</h1><p>Get in touch.</p>",
  )

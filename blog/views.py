from typing import Any

from django.views.generic import TemplateView

from blog.models import Book


class BookListView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = 'Test 1'
        return context_data

class AuthorListView(TemplateView):
    template_name = "list-author.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = 'Test 2'
        return context_data
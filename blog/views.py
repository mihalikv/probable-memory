from typing import Any

from django.views.generic import TemplateView

class BookListView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = 'Test 1'
        # Problems:
        # 1. show title first 10 books on URL http://127.0.0.1:8000/test-1/ 
        # 2. restrict books to just books with is_active=True or is_super_active=True
        # 3. show total number of books under list of books
        # 4. show author name next to book title 
        # 5. add link to html to redirect to list of authors(AuthorListView)
        return context_data

class AuthorListView(TemplateView):
    template_name = "list-author.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = 'Test 2'
        # Problems:
        # 1. show list of authors on URL http://127.0.0.1:8000/test-2/ 
        # 2. show number of books foe each author
        return context_data
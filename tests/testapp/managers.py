from django.db.models import QuerySet


class AuthorQuerySet(QuerySet):

    def for_user(self, user):
        if user.is_anonymous:
            return self.filter(active=True)
        return self

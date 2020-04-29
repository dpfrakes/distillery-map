from django.contrib import admin
from app.models import ABCInfo


class ABCInfoFilter(admin.SimpleListFilter):
    title = 'price range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('< $20', '< $20'),
            ('$20 - $50', '$20 - $50'),
            ('$50 - $100', '$50 - $100'),
            ('$100 - $200', '$100 - $200'),
            ('$200+', '$200+'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        kwargs = {}
        if self.value() == '< $20':
            kwargs = {'price__lte': 20}
        elif self.value() == '$20 - $50':
            kwargs = {'price__gte': 20, 'price__lte': 50}
        elif self.value() == '$50 - $100':
            kwargs = {'price__gte': 50, 'price__lte': 100}
        elif self.value() == '$100 - $200':
            kwargs = {'price__gte': 100, 'price__lte':200}
        elif self.value() == '$200+':
            kwargs = {'price__gte': 200}
        return queryset.filter(**kwargs)

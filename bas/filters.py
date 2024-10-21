import django_filters
import bas.models
from django.db.models import Q


class BusParkFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(method='filter_year', label='Автопарки, основанные после')
    address = django_filters.CharFilter(lookup_expr='icontains', label = 'Адрес')
    class Meta:
        model = bas.models.BusPark
        fields = ['title', 'address', 'year']


    def filter_year(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            year =int(value)
            return queryset.filter(year_found__gt=year)
        return queryset.filter(year_found=0)
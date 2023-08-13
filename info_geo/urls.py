from django.urls import path
from .views import CityDetailView, CityListView, CityComparisonView, CityAutocompleteView

urlpatterns = [
    path('city/<int:geonameid>/', CityDetailView.as_view(), name='city-detail'),
    path('cities/', CityListView.as_view(), name='cities'),
    path('compare-cities/', CityComparisonView.as_view(), name='compare-cities'),
    path('help_search/', CityAutocompleteView.as_view(), name='help_search')
]

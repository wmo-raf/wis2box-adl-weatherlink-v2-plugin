from django.forms import widgets

from .http import weatherlink_api


class WeatherLinkStationSelectWidget(widgets.Select):
    def __init__(self, attrs=None, choices=()):
        blank_choice = [("", "---------")]

        try:
            stations = weatherlink_api.get_stations()
            station_choices = [
                (station_id, f"{station['station_name']} - ({station_id})")
                for station_id, station in stations.items()
            ]
        except Exception as e:
            station_choices = []

        super().__init__(attrs, blank_choice + station_choices)

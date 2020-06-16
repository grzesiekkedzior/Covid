import requests

class RestGlobalData:
    def __init__(self):
        self.resp = requests.get('https://api.covid19api.com/summary')
        self.rest_data = self.resp.json()
        self.get_data()

    def get_data(self):
        self.new_confirmed = self.rest_data['Global']['NewConfirmed']
        self.total_confirmed = self.rest_data['Global']['TotalConfirmed']
        self.new_deaths = self.rest_data['Global']['NewDeaths']
        self.total_deaths = self.rest_data['Global']['TotalDeaths']
        self.new_recovered = self.rest_data['Global']['NewRecovered']
        self.total_recovered = self.rest_data['Global']['TotalRecovered']

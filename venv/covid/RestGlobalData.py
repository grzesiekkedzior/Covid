import requests
import matplotlib.pyplot as plt

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

    def show_all_cases_world(self, start_date, end_date):
        self.data = self.json_all_cases_world(start_date, end_date)
        plt.plot(self.data[0], label='NEW CONFIRMED')
        plt.plot(self.data[1], label='TOTAL CONFIRMED')
        plt.plot(self.data[2], label='NEW DEATHS')
        plt.plot(self.data[3], label='TOTAL DEATHS')
        plt.plot(self.data[4], label='NEW RECOVERED')
        plt.plot(self.data[5], label='TOTAL RECOVERED')
        plt.ylabel('CONFIRM ALL TYPE CASES IN THE WORLD')
        plt.xlabel('FROM ' + start_date + ' TO ' + end_date)
        plt.legend()
        plt.show()

    def json_all_cases_world(self, start_date, end_date):
        self.resp = requests.get('https://api.covid19api.com/world'
                                 + '?from=' + start_date + 'T00:00:00Z&to='
                                 + end_date + 'T00:00:00Z')

        self.rest_data = self.resp.json()
        self.list_of_confirmed_world_by_date = []
        self.list_of_total_confirmed_world_by_date = []
        self.list_of_deaths_world_by_date = []
        self.list_of_total_deaths_world_by_date = []
        self.list_of_new_recovered_world_by_date = []
        self.list_of_total_recovered = []

        i = 0;
        for l in self.rest_data:
            self.list_of_confirmed_world_by_date.append(self.rest_data[i]['NewConfirmed'])
            self.list_of_total_confirmed_world_by_date.append(self.rest_data[i]['TotalConfirmed'])
            self.list_of_deaths_world_by_date.append(self.rest_data[i]['NewDeaths'])
            self.list_of_total_deaths_world_by_date.append(self.rest_data[i]['TotalDeaths'])
            self.list_of_new_recovered_world_by_date.append(self.rest_data[i]['NewRecovered'])
            self.list_of_total_recovered.append(self.rest_data[i]['TotalRecovered'])
            i = i + 1

        self.all_by_date = (self.list_of_confirmed_world_by_date,
                            self.list_of_total_confirmed_world_by_date,
                            self.list_of_deaths_world_by_date,
                            self.list_of_total_deaths_world_by_date,
                            self.list_of_new_recovered_world_by_date,
                            self.list_of_total_recovered)

        return self.all_by_date

def get_all_countries():
    list_of_countries = []
    resp = requests.get('https://api.covid19api.com/countries')
    rest_data = resp.json()

    i = 0;
    for l in rest_data:
        list_of_countries.append(rest_data[i]['Country'])
        i = i + 1

    return list_of_countries

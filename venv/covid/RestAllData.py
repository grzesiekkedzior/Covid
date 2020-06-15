import requests
import matplotlib.pyplot as plt

class RestAllData:
    def __init__(self, country):
        self.resp = requests.get('https://api.covid19api.com/dayone/country/' + country)
        self.rest_data = self.resp.json()
        self.COUNTRY = self.rest_data[0]['Country'].upper()
        self.COUNTRYCODE = self.rest_data[0]['CountryCode']
        self.CASES = self.rest_data[0]['Confirmed']
        self.DEATHS = self.rest_data[0]['Deaths']
        self.ACTIVE = self.rest_data[0]['Active']
        self.RECOVERED = self.rest_data[0]['Recovered']
        self.START_DATE = self.rest_data[0]['Date']
        self.START_DATE = self.START_DATE[0:10]
        self.END_DATE = self.rest_data[len(self.rest_data) - 1]['Date']
        self.END_DATE = self.END_DATE[0:10]
        self.list_of_cases = []
        self.list_of_deaths = []
        self.list_of_active = []
        self.list_of_recoverded = []
        self.getData()

    def getData(self):
        i = 0;
        for l in self.rest_data:
            self.list_of_cases.append(self.rest_data[i]['Confirmed'])
            self.list_of_deaths.append(self.rest_data[i]['Deaths'])
            self.list_of_active.append(self.rest_data[i]['Active'])
            self.list_of_recoverded.append(self.rest_data[i]['Recovered'])
            i = i + 1

    def showData(self):
        plt.plot(self.list_of_cases, label='CONFIRMED')
        plt.plot(self.list_of_deaths, label='DEATHS')
        plt.plot(self.list_of_active, label='ACTIVE')
        plt.plot(self.list_of_recoverded, label='RECOVERED')
        plt.ylabel('CONFIRMED CASES IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
        plt.legend()
        plt.show()

    def showOneCountryCases(self):
        self.list_of_cases_max_day = []

        i = 0
        for l in self.list_of_cases:
            if i < len(self.list_of_cases) - 1:
                self.list_of_cases_max_day.append(self.list_of_cases[i + 1] - self.list_of_cases[i])
                i = i + 1

        plt.plot(self.list_of_cases_max_day, label='CONFIRMED EVERY DAY')
        plt.ylabel('CONFIRMED CASES IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
        plt.legend()
        plt.show()

    def showOneCountryDeaths(self):
        self.list_of_cases_max_day_dead = []

        i = 0
        for l in self.list_of_deaths:
            if i < len(self.list_of_deaths) - 1:
                self.list_of_cases_max_day_dead.append(self.list_of_deaths[i + 1] - self.list_of_deaths[i])
                i = i + 1

        plt.plot(self.list_of_cases_max_day_dead, label='DEAD EVERY DAY')
        plt.ylabel('CONFIRMED DEAD IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
        plt.legend()
        plt.show()

    def showOneCountryRecovered(self):
        self.list_of_cases_max_day_recovered = []

        i = 0
        for l in self.list_of_recoverded:
            if i < len(self.list_of_recoverded) - 1:
                self.list_of_cases_max_day_recovered.append(self.list_of_recoverded[i + 1] - self.list_of_recoverded[i])
                i = i + 1

        plt.plot(self.list_of_cases_max_day_recovered, label='RECOVERED EVERY DAY')
        plt.ylabel('CONFIRMED RECOVERED IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
        plt.legend()
        plt.show()

    def showOneCountryActive(self):
        self.list_of_cases_max_day_active = []

        i = 0
        for l in self.list_of_active:
            if i < len(self.list_of_active) - 1:
                self.list_of_cases_max_day_active.append(self.list_of_active[i + 1] - self.list_of_active[i])
                i = i + 1

        plt.plot(self.list_of_cases_max_day_active, label='ACTIVE EVERY DAY')
        plt.ylabel('CONFIRMED ACTIVE IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
        plt.legend()
        plt.show()

    #type must be confirmed, recovered, deaths
    def showDataCountryByDate(self, type, start_date, end_date):
        self.resp = requests.get('https://api.covid19api.com/total/country/'
                                 + self.COUNTRY + '/status/' + type
                                 + '?from=' + start_date + 'T00:00:00Z&to='
                                 + end_date + 'T00:00:00Z')

        self.rest_data = self.resp.json()
        self.list_of_type_by_date = []

        i = 0;
        for l in self.rest_data:
            self.list_of_type_by_date.append(self.rest_data[i]['Cases'])
            i = i + 1

        plt.plot(self.list_of_type_by_date, label=type.upper())
        plt.ylabel('CONFIRM ' + type.upper() + ' IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + start_date + ' TO ' + end_date)
        plt.legend()
        plt.show()

    def showAllDataCountryByDate(self, start_date, end_date):
        self.resp = requests.get('https://api.covid19api.com/country/'
                                 + self.COUNTRY
                                 + '?from=' + start_date + 'T00:00:00Z&to='
                                 + end_date + 'T00:00:00Z')

        self.rest_data = self.resp.json()
        self.list_of_confirmed_by_date = []
        self.list_of_recovered_by_date = []
        self.list_of_deaths_by_date = []
        self.list_of_active_by_date = []

        i = 0;
        for l in self.rest_data:
            self.list_of_confirmed_by_date.append(self.rest_data[i]['Confirmed'])
            self.list_of_recovered_by_date.append(self.rest_data[i]['Recovered'])
            self.list_of_deaths_by_date.append(self.rest_data[i]['Deaths'])
            self.list_of_active_by_date.append(self.rest_data[i]['Active'])
            i = i + 1

        plt.plot(self.list_of_confirmed_by_date, label='CONFIRMED')
        plt.plot(self.list_of_recovered_by_date, label='RECOVERED')
        plt.plot(self.list_of_deaths_by_date, label='DEATHS')
        plt.plot(self.list_of_active_by_date, label='ACTIVE')
        plt.ylabel('CONFIRM CASES IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + start_date + ' TO ' + end_date)
        plt.legend()
        plt.show()

def getAllCountries():
    list_of_countries = []
    resp = requests.get('https://api.covid19api.com/countries')
    rest_data = resp.json()

    i = 0;
    for l in rest_data:
        list_of_countries.append(rest_data[i]['Country'])
        i = i + 1

    return list_of_countries

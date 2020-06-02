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

    def getData(self):
        i = 0;
        for l in self.rest_data:
            self.list_of_cases.append(self.rest_data[i]['Confirmed'])
            self.list_of_deaths.append(self.rest_data[i]['Deaths'])
            self.list_of_active.append(self.rest_data[i]['Active'])
            self.list_of_recoverded.append(self.rest_data[i]['Recovered'])
            i = i + 1

    def showData(self):
        self.getData()
        plt.subplots()
        plt.plot(self.list_of_cases, label='CONFIRMED')
        plt.plot(self.list_of_deaths, label='DEATHS')
        plt.plot(self.list_of_active, label='ACTIVE')
        plt.plot(self.list_of_recoverded, label='RECOVERED')
        plt.ylabel('CONFIRM CASES IN ' + self.COUNTRY)
        plt.xlabel('FROM ' + self.START_DATE + ' TO ' + self.END_DATE)
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
    print(list_of_countries)

    return list_of_countries
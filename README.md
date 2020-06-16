This is simple application which show plots of covid disease.
App must be connect to network to get data.
All menu is intuitive and simple. All data are from https://covid19api.com/
Library used in project:

- requests
- matplotlib
- tkinter

Example
-

```python
import covid.RestAllData as rd

italy = rd.RestAllData('Italy')
italy.show_one_country_cases()
```
Module RestAllData:
-
- class RestAllData create object to manipulate rest data
```python
country = RestAllData('Germany')
```
- function getData() create lists of all days for (confirmed, active, deaths, recovered).
```python
country.get_data()
```

- function showData() show plots (confirmed, active, deaths, recovered).
```python
country.show_data()
```

- function showOneCountryCases() show confirmed cases for specific country.
```python
country.show_one_country_cases()
```

- function showOneCountryDeaths() show confirmed deaths for specific country.
```python
country.show_one_country_deaths()
```

- function showOneCountryRecovered() show confirmed recovered caseses for specific country
```python
country.show_one_country_recovered()
```

- function showOneCountryActive() show active cases for specific country
```python
country.showOneCountryActive()
```

- function showDataCountryByDate(type, start_date, end_date) show concret data for confirmed, recovered, deaths for specific period of time
```python
country.show_data_country_by_date('deaths', '2020-03-01', '2020-06-01')
```

- function showAllDataCountryByDate(start_date, end_date) show all data on one plot for confirmed, recovered, deaths for specific period of time
```python
country.show_all_data_country_by_date('2020-04-09', '2020-05-09')
```

- function show_one_country_all_data_after_date(date) show all data on one plot for confirmed, recovered, deaths after concret date. Sometimes after some date plots does not show plots.
```python
country.show_one_ountry_all_data_after_date('2020-04-30')
```

- function getAllCountries() return list of shortcut countries.
```python
get_all_countries()
```

Module RestGlobalData:
-

- class RestGlobalData create object to get only global data
```python
data = RestGlobalData()
```

- function getData() create attributes: new_confirmed, total_confirmed, new_deaths, total_deaths, new_recovered, total_recovered
```python
data.get_data()
```

Module Main is simple gui implementation for this api.
-

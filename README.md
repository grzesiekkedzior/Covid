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
- function get_data() create lists of all days for (confirmed, active, deaths, recovered).
```python
country.get_data()
```

- function show_data() show plots (confirmed, active, deaths, recovered).
```python
country.show_data()
```

- function show_one_country_cases() show confirmed cases for specific country.
```python
country.show_one_country_cases()
country.json_one_country_cases()    # return list of json data
```

- function show_one_country_deaths() show confirmed deaths cases for specific country.
```python
country.show_one_country_deaths()
country.json_one_country_deaths()    # return list of json data
```

- function show_one_country_recovered() show confirmed recovered cases for specific country
```python
country.show_one_country_recovered()
country.json_one_country_recovered()    # return list of json data
```

- function show_one_country_active() show confirmed active cases for specific country
```python
country.show_one_country_active()
country.json_one_country_active()    # return list of json data
```

- function show_data_country_by_date(type, start_date, end_date) show concret data for confirmed, recovered, deaths for specific period of time
```python
country.show_data_country_by_date('deaths', '2020-03-01', '2020-06-01')
country.json_country_by_date('deaths', '2020-03-01', '2020-06-01')    # return list of json data
```

- function show_all_data_country_by_date(start_date, end_date) show all data on one plot for confirmed, recovered, deaths for specific period of time
```python
country.show_all_data_country_by_date('2020-04-09', '2020-05-09')
country.json_all_data_country_by_date('2020-04-09', '2020-05-09')   # return tuple of json data lists
```

- function show_one_country_all_data_after_date(date) show all data on one plot for confirmed, recovered, deaths after concret date. Sometimes after some date plots does not show plots.
```python
country.show_one_ountry_all_data_after_date('2020-04-30')
country.json_one_country_all_date_after_date('2020-04-30')   # return tuple of json data lists
```

- function compare_two_countries_cases(country, country2) show plots for both countries
```python
compare_two_countries_cases('Spain', 'Italy')
json_compare_two_countries_cases('Spain', 'Italy')  # return tuple of json data lists
```

- function compare_two_countries_deaths(country, country2) show plots for both countries
```python
compare_two_countries_deaths('Germany', 'Italy')
json_compare_two_countries_deaths('Germany', 'Italy')  # return tuple of json data lists
```

- function compare_two_countries_recovered(country, country2) show plots for both countries
```python
compare_two_countries_recovered('Germany', 'Russia')
json_compare_two_countries_recovered('Germany', 'Russia')   # return tuple of json data lists
```

Module RestGlobalData:
-

- class RestGlobalData create object to get only global data
```python
data = RestGlobalData()
```

- function get_data() create attributes: new_confirmed, total_confirmed, new_deaths, total_deaths, new_recovered, total_recovered
```python
data.get_data()
```

- function show_all_cases_world() show all cases in the world.
```python
data.show_all_cases_world('2020-03-10', '2020-05-01')
data.json_all_cases_world('2020-03-10', '2020-05-01')   # return tuple of json data lists
```


- function get_all_countries() return list of shortcut countries.
```python
get_all_countries()
```

Module Main is simple gui implementation for this api.
-

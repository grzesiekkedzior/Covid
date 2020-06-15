This is simple application which show plots of covid disease.
App must be connect to network to get data.
All menu is intuitive and simple. All data are from https://covid19api.com/
Library used in project:

- requests
- matplotlib
- tkinter

Module RestAllData:
-
- class RestAllData create object to manipulate rest data
```python
country = RestAllData('Germany')
```
- function getData() create lists of all days for (confirmed, active, deaths, recovered).
```python
country.getData()
```

- function showData() show plots (confirmed, active, deaths, recovered).
```python
country.showData()
```

- function showOneCountryCases() show confirmed cases for specific country.
```python
country.showOneCountryCases()
```

- function showOneCountryDeaths show confirmed deaths for specific country.
```python
country.showOneCountryDeaths()
```

- function showDataCountryByDate(type, start_date, end_date) show concret data for confirmed, recovered, deaths for specific period of time
```python
country.showDataCountryByDate('deaths', '2020-03-01', '2020-06-01')
```

- function showAllDataCountryByDate(start_date, end_date) show all data on one plot for confirmed, recovered, deaths for specific period of time
```python
country.showAllDataCountryByDate('2020-04-09','2020-05-09')
```

- function getAllCountries() return list of shortcut countries.
```python
getAllCountries()
```

Module RestGlobalData:
-

- class RestGlobalData create object to get only global data
```python
data = RestGlobalData()
```

- function getData() create attributes: new_confirmed, total_confirmed, new_deaths, total_deaths, new_recovered, total_recovered
```python
data.getData()
```

Module Main is simple gui implementation for this api.
-

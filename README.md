# Scottish Distilleries

This project contains a database along with an interactive map to explore the history of and current information about all Scottish distilleries.

## Getting started

```sh
source ~/.virtualenv/scotland/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

### Notes

Data attributes

```txt
distillery
lat
long
location (town)
region
owner (recursive?)
year est
year closed
year demolished
inactive date range 1
inactive date range 2
inactive date range 3
tour hours
```

### Feature Ideas

- [ ] Latest products
- [ ] Tour hours
- [ ] Production estimate (liters produced annually)

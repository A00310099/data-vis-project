# Downloading the datasets
This project depends on datasets from Eurostat that are not included in this repository. Before running the python script, follow the steps below:

## Via commands (recommended):
Open a terminal in the [`data`](/data/) directory and run the following commands:

### On Windows:
```
curl -o data.csv  "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=TOTAL&c[sex]=T&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```
```
curl -o data2.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```

-----

### On Linux:
```
wget -O data.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=TOTAL&c[sex]=T&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```
```
wget -O data2.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```

## Manual installation:
If the commands aren't working for you, you can manually download the datasets instead by following these steps:

1. Download the first dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=TOTAL&c[sex]=T&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name)
and (re)name the file as `data.csv`.

2. Download the second dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name)
and (re)name the  file as `data2.csv`.

3. Place both downloaded `.csv` files in the [`data`](/data/) directory.
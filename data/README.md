# Downloading the datasets
This project depends on datasets from Eurostat that are not included in this repository. Before running the python script, follow the steps below:

## Via commands (recommended):
Open a terminal in the [`data`](/data/) directory and run the following commands:

### On Windows:
```
curl -o povertyData.csv  "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=Y11-15,Y15-19,Y20-24,Y25-49,Y50-64,Y65-74,Y_GE75&c[sex]=M,F&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```
```
curl -o PurchasingPowerParities.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101,A01010101,A01010102,A01010103,A01010104,A01010105,A01010106,A01010199,A010102&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```

-----

### On Linux:
```
wget -O povertyData.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=Y11-15,Y15-19,Y20-24,Y25-49,Y50-64,Y65-74,Y_GE75&c[sex]=M,F&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```
```
wget -O PurchasingPowerParities.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101,A01010101,A01010102,A01010103,A01010104,A01010105,A01010106,A01010199,A010102&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```

## Manual installation:
If the commands aren't working for you, you can manually download the datasets instead by following these steps:

1. Download the poverty index dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=PC&c[age]=Y11-15,Y15-19,Y20-24,Y25-49,Y50-64,Y65-74,Y_GE75&c[sex]=M,F&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only)
and (re)name the file as `povertyData.csv`.

2. Download the Purchasing Power Parities dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101,A01010101,A01010102,A01010103,A01010104,A01010105,A01010106,A01010199,A010102&c[geo]=BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only)
and (re)name the  file as `PurchasingPowerParities.csv`.

3. Place both downloaded `.csv` files in the [`data`](/data/) directory.

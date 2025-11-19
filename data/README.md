# Downloading the datasets
This project depends on datasets from Eurostat that are not included in this repository. Before running the python script, follow the steps below:

## Via commands (recommended):
Open a terminal in the [`data`](/data/) directory and run the following commands:

### On Windows:
```
curl -o povertyData.csv  "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=THS_PER,PC&c[age]=Y_LT6,Y6-10,Y6-11,Y11-15,Y12-17,Y15-19,Y15-24,Y15-29,Y_LT16,Y16-19,Y16-24,Y16-29,Y16-64,Y_GE16,Y_LT18,Y18-24,Y18-64,Y_GE18,Y20-24,Y20-29,Y25-29,Y25-49,Y25-54,Y50-64,Y55-64,Y_GE55,Y_LT60,Y_GE60,Y_LT65,Y65-74,Y_GE65,Y_LT75,Y_GE75&c[sex]=M,F&c[geo]=EU27_2020,EU28,EU27_2007,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```
```
curl -o data2.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```

-----

### On Linux:
```
wget -O povertyData.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=THS_PER,PC&c[age]=Y_LT6,Y6-10,Y6-11,Y11-15,Y12-17,Y15-19,Y15-24,Y15-29,Y_LT16,Y16-19,Y16-24,Y16-29,Y16-64,Y_GE16,Y_LT18,Y18-24,Y18-64,Y_GE18,Y20-24,Y20-29,Y25-29,Y25-49,Y25-54,Y50-64,Y55-64,Y_GE55,Y_LT60,Y_GE60,Y_LT65,Y65-74,Y_GE65,Y_LT75,Y_GE75&c[sex]=M,F&c[geo]=EU27_2020,EU28,EU27_2007,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only"
```
```
wget -O data2.csv "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name"
```

## Manual installation:
If the commands aren't working for you, you can manually download the datasets instead by following these steps:

1. Download the poverty index dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/ilc_peps01n/1.0/*.*.*.*.*?c[freq]=A&c[unit]=THS_PER,PC&c[age]=Y_LT6,Y6-10,Y6-11,Y11-15,Y12-17,Y15-19,Y15-24,Y15-29,Y_LT16,Y16-19,Y16-24,Y16-29,Y16-64,Y_GE16,Y_LT18,Y18-24,Y18-64,Y_GE18,Y20-24,Y20-29,Y25-29,Y25-49,Y25-54,Y50-64,Y55-64,Y_GE55,Y_LT60,Y_GE60,Y_LT65,Y65-74,Y_GE65,Y_LT75,Y_GE75&c[sex]=M,F&c[geo]=EU27_2020,EU28,EU27_2007,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,ME,MK,AL,RS,TR&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=1.0&lang=en&labels=label_only)
and (re)name the file as `povertyData.csv`.

2. Download the second dataset from
[here](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/prc_ppp_ind/1.0/*.*.*.*?c[freq]=A&c[na_item]=PLI_EU27_2020&c[ppp_cat]=A010101&c[geo]=EU27_2020,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,CPC1,BA,ME,MK,AL,RS,TR,XK,US,JP&c[TIME_PERIOD]=2024,2023,2022,2021,2020,2019,2018,2017,2016,2015&compress=false&format=csvdata&formatVersion=2.0&lang=en&labels=name)
and (re)name the  file as `data2.csv`.

3. Place both downloaded `.csv` files in the [`data`](/data/) directory.
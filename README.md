# sistemi-informativi
Sviluppo in locale di una dashboard su trend ICT europei:
- Tool
    - SDMX API
    - Python+DuckDB
    - [Apache Superset](https://superset.apache.org/)
- OLAP
    - visualizzazione grafica dei dati
    - aggregazione geografica
    - slicing temporale interattivo
    - visualizzazione eventuali correlazioni significative
- Dati [Eurostat](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0)
- [DSD Facts](http://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/datastructure/ESTAT/<id>/?compress=false)
- [DSD Dimensions](https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/codelist/ESTAT/<id>/?compress=false)

# Fact Tables
## ISOC_CISCE_RA(41.0)
> Security policy, measures, risks and staff awareness by size class of enterprise
- (freq, size_emp, nace_r2, indic_is, unit, geo, TIME_PERIOD).value x 8986 rows
- value : text/Double
- unit
    - PC_ENT_IUSE: Percentage of enterprises where persons employed have access to the internet
    - PC_ENT_CUSE: Percentage of the enterprises which use a computer
    - PC_ENT: Percentage of enterprises
    - PC_ENT_SECPOL1: Percentage of enterprises with an ICT security policy (as of 2015)
    - PC_ENT_SECPOL2: Percentage of enterprises with document(s) on measures, practices or procedures on ICT security (as of 2019)
- TIME_PERIOD=2015, 2019, 2022, 2024
- freq=A
- nace_r2=C10-S951_X_K
- size_emp: "Enterprises aggregated by size"
- indic_is: "Enterprises aggregated by ICT security measures"

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|size_emp|enum/ESTAT:SIZE_EMP(7.0)|Enterprise size class|
|nace_r2|enum/ESTAT:NACE_R2(17.0)|Economic activity|
|unit|enum/ESTAT:UNIT(69.0)|Measurement unit|
|indic_is|enum/ESTAT:INDIC_IS(25.2)|Indicator|

## ISOC_CISCE_IC(39.0)
> Security incidents and consequences by size class of enterprise
- (freq, size_emp, nace_r2, indic_is, unit, geo, TIME_PERIOD).value x 33845 rows
- value : text/Double
- unit
    - PC_ENT_CUSE: Percentage of the enterprises which use a computer
    - PC_ENT_IUSE: Percentage of enterprises where persons employed have access to the internet
    - PC_ENT: Percentage of enterprises
- TIME_PERIOD=2019, 2022, 2024
- freq=A
- nace_r2=C10-S951_X_K
- size_emp: "Enterprises aggregated by size"
- indic_is: "Enterprises aggregated by ICT security incidents"

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|size_emp|enum/ESTAT:SIZE_EMP(7.0)|Enterprise size class|
|nace_r2|enum/ESTAT:NACE_R2(17.0)|Economic activity|
|unit|enum/ESTAT:UNIT(69.0)|Measurement unit|
|indic_is|enum/ESTAT:INDIC_IS(25.2)|Indicator|

## ISOC_CISCI_PRV20(42.0)
> Privacy and protection of personal data (2020 onwards)
- (freq, ind_type, indic_is, unit, geo, TIME_PERIOD).value x 265172 rows
- value : text/Double
- unit
    - PC_IND_IU3: Percentage of individuals who used internet in the last 3 months
    - PC_IND: Percentage of individuals
- TIME_PERIOD=2020, 2021, 2023, 2025
- freq=A
- ind_type: "Subjects of incidents aggregate by age, education, location"
- indic_is: "Type of violations"

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|unit|enum/ESTAT:UNIT(69.0)|Measurement unit|
|indic_is|enum/ESTAT:INDIC_IS(25.2)|Indicator|
|ind_type|enum/ESTAT:IND_TYPE(9.0)|Type of indicator|

## TIN00074(28.0)
- (freq, nace_r2, geo, TIME_PERIOD).value x 1200 rows
- value : text/Double
    - Percentage of the ICT sector in Gross Value Added
- TIME_PERIOD=2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- freq=A
- nace_r2=G-U_ICT, C_ICT, ICT

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|nace_r2|enum/ESTAT:NACE_R2(17.0)|Economic activity|

## TIN00085(28.0)
- (freq, nace_r2, geo, TIME_PERIOD).value x 1146 rows
- value : text/Double
    - Percentage of ICT sector personnel in total employment
- TIME_PERIOD=2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- freq=A
- nace_r2=G-U_ICT, C_ICT, ICT

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|nace_r2|enum/ESTAT:NACE_R2(17.0)|Economic activity|
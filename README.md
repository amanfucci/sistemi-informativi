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
- Dati [Eurostat](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1)
- [DSD](http://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/datastructure/ESTAT/<id>/?compress=false)

# Fact Tables
## ISOC_CISCE_RA(41.0)
- (freq, size_emp, nace_r2, indic_is, unit, geo, TIME_PERIOD).value x 8986 rows
- value : text/Double
- Security policy, measures, risks and staff awareness by size class of enterprise

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
- (freq, size_emp, nace_r2, indic_is, unit, geo, TIME_PERIOD).value x 33845 rows
- value : text/Double
- Security incidents and consequences by size class of enterprise

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
- (freq, ind_type, indic_is, unit, geo, TIME_PERIOD).value x 265172 rows
- value : text/Double
- Privacy and protection of personal data (2020 onwards)

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

|dimensions|representation|meaning|
|---|---|---|
|TIME_PERIOD|text/ObservationalTimePeriod|Reference year|
|geo|enum/ESTAT:GEO(26.0)|Country/region code|
|freq|enum/ESTAT:FREQ(3.9)|Frequency of observation|
|nace_r2|enum/ESTAT:NACE_R2(17.0)|Economic activity|

# Dimension Tables
## ObservationalTimePeriod
- ISO-8601 time forma

## ESTAT:GEO(26.0)

## ESTAT:FREQ(3.9)
- A (Annual), Q (Quarterly), M (Monthly)

## ESTAT:UNIT(69.0)

## ESTAT:NACE_R2(17.0)

## ESTAT:INDIC_IS(25.2)

## ESTAT:IND_TYPE(9.0)

## ESTAT:SIZE_EMP(7.0)
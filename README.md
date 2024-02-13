# ai_group_project_1
AI Group Project 


## Objective

Our objective is to identify the primary drivers of inflation within the United States economy. Subsequently, we aim to analyze the repercussions of inflation on various socio-economic factors such as crime rates, unemployment levels, and mental health.

To achieve this, we will employ a multiple regression model. Our dataset will consist of a time series comprising monthly data spanning either the past decade or two decades.

## Data sets

Publicly available economic, mental health, and crime data were collected from multiple resources (cited below), and cleaned using python and MS Copilot in pandas and jupyter notebooks. After cleaning, data discovery was conducted using visualization and statistical analysis.  

We have the following data sources with citations.
| Data Name | Description | Link | Period |
| --------- | ----------- | ---- | ------ |
| Foreign Direct Investment | Quarterly data of Foreign Direct Investments | [Foreign Direct Investment](https://fred.stlouisfed.org/series/ROWFDIQ027S) | Quarterly |
| GDP | Quarterly data of GDP | [GDP](https://fred.stlouisfed.org/series/GDP) | Quarterly |
| Rate of Motor Vehicle Theft | Yearly overview of offenses for motor vehicle theft | [Motor Vehicle Theft](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Rate of Larceny | Yearly overview of offenses for larceny-theft | [Larceny Theft](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Rate of Burglary | Yearly overview of offenses for burglary | [Burglary](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Rate of Property Crime | Yearly overview of offenses for property crime | [Property Crime](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Rate of Aggravated Assault | Yearly overview of offenses Aggravated Assault | [Aggravated Assault](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Rate of Violent Crime | Yearly overview of offenses for violent crime | [Violent Crime](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend) | Yearly |
| Mental Health Client Level Data | Annual mental health data describing diagnoses of anxiety, depression, and substance abuse | [Mental Health](https://www.samhsa.gov/data/data-we-collect/mh-cld-mental-health-client-level-data) | Yearly |
| Federal Government Tax Receipts | Federal Reserve Economic Data, quarterly dataset showing the federal tax income | [Tax Receipts](https://fred.stlouisfed.org/series/W006RC1Q027SBEA) | Quarterly |
| Federal Government Surplus/Deficit | Federal Reserve Economic Data, monthly data overview of the federal budget surplus or deficit | [Surplus/Deficit](https://fred.stlouisfed.org/series/MTSDS133FMS) | Monthly |
| Consumer Price Index | A measure of core inflation calculated the Federal Reserve Bank of Cleveland and the Ohio State University | [Consumer Price Index](https://fred.stlouisfed.org/series/MEDCPIM158SFRBCLE) | Monthly |
| Federal Funds Effective | The central interest rate in the U.S. financial market | [Federal Funds Effective](https://fred.stlouisfed.org/series/FEDFUNDS) | Daily |
| Unemployment Rate | The number of unemployed as a percentage of the labor force | [Federal Funds Effective](https://fred.stlouisfed.org/series/UNRATE) | Monthly |



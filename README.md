# MeToo Movement Research: Factors Influencing Victims' Decision to Accuse Predators

## Overview
This research focuses on the MeToo movement, aiming to understand the factors influencing a victim's decision to publicly accuse predators of abuse or sexual harassment. The primary data source for this study is derived from [Vox.com](https://www.vox.com), which provides a comprehensive list of victims, predators, and related news sources.

## Data Collection and Expansion
The dataset is expanded using a web scraping script (`webscratching.ipynb`), which collects information from the aforementioned website.

## Challenges in Data Collection: Internet Volume Analysis (using `google_trend_data.ipynb`)
An essential aspect of our analysis involves evaluating the internet presence or fame of predators and victims, hypothesizing that this could influence their decision to come forward. We utilized the `gtab` package to standardize Google Trends search volume data across different locations and time frames. The accuracy and functionality of `gtab` in this context should be verified.

### Note on Google Trends Data Collection
Google Trends imposes limitations on rapid data collection, which may require IP address changes to continue data retrieval. The data collection script divides the predator and victim lists into sublists for trend analysis. If a maximum retry limit is reached, an IP change is needed to process the remaining lists.

A peculiar issue encountered involved inconsistent responses from Google Trends, where certain keywords initially marked as 'bad' would be accepted in a second attempt. To address this, the data collection process is executed twice: the first run encompasses all data, and the second run targets individuals marked as NA initially. The final output files are `victim_all.csv` and `predator_all.csv`.

## Data Processing
The collected data is integrated into a main Excel sheet, then transformed into a panel data format suitable for statistical analysis (using `transform_panel_data.ipynb`).

## Statistical Analysis in R
We perform fixed and random effects analysis using the `pglm` package in R. The model specification is:


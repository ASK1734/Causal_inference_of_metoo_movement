# MeToo Movement Research: Factors Influencing Victims' Decision to Accuse Predators

## Overview
This research focuses on the MeToo movement, aiming to understand the factors influencing a victim's decision to publicly accuse predators of abuse or sexual harassment. The primary data source for this study is derived from [Vox.com](https://www.vox.com), which provides a comprehensive list of victims, predators, and related news sources.

## Data Collection and Expansion
The dataset is expanded using a web scraping script (`webscratching.ipynb`), which collects information from the aforementioned website.

## Challenges in Data Collection: Internet Volume Analysis
To evaluate the internet presence or fame of predators and victims, and hypothesize its influence on the decision to come forward, we utilized the `gtab` package in conjunction with our custom script `google_trend_data.ipynb`.

### Normalization Tool:
- **Google Trends Normalization:** Using `gtab`, Google Trends data is normalized to provide a more accurate analysis of search terms across different regions and time periods, given that the original data is on a relative scale of 0 to 100.

### Calibration Reference:
- **Standardizing Search Data:** The calibration process involves comparing terms of interest to a set of anchor terms, allowing for more meaningful comparisons across different search terms and timeframes.

### Note on Google Trends Data Collection
- **Challenges with Data Retrieval:** Due to Google Trends' limitations on rapid data collection, our script categorizes predator and victim names into sublists for effective trend analysis. IP changes may be necessary for continuous data retrieval.
- **Handling Inconsistent Responses:** Inconsistent responses from Google Trends were addressed by running the data collection process twice – the first to encompass all data and the second to target initially missed data. The results are compiled into `victim_all.csv` and `predator_all.csv`.

## Data Processing
- **Integration and Transformation:** Data collected is meticulously integrated into a primary Excel sheet, which is then transformed into a panel data format using `transform_panel_data.ipynb`. This format is pivotal for the subsequent statistical analysis.


## Statistical Analysis in R
- **Analytical Approach:** Fixed and random effects analysis is conducted using the `pglm` package in R. This methodological choice is aimed at understanding the varied factors influencing victims' decisions to accuse their predators.

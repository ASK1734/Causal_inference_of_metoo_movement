# MeToo Movement Research: Factors Influencing Victims' Decision to Accuse Predators

## Overview
This research focuses on the MeToo movement, aiming to understand the factors influencing a victim's decision to publicly accuse predators of abuse or sexual harassment. The primary data source for this study is derived from [Vox.com](https://www.vox.com), which provides a comprehensive list of victims, predators, and related news sources.

## Data Collection and Expansion
The dataset is expanded using a web scraping script (`webscratching.ipynb`), which collects information from the aforementioned website.

## Challenges in Data Collection: Internet Volume Analysis
An essential aspect of our analysis involves evaluating the internet presence or fame of predators and victims, hypothesizing that this could influence their decision to come forward. For this purpose, we utilized the `gtab` package.

### Normalization Tool:
- **Google Trends Normalization:** Google Trends provides relative search interest data on a scale from 0 to 100. The `gtab` package is employed to normalize this data, allowing for a more accurate and comparable analysis of search terms across different regions and time periods.

### Calibration Reference:
- **Standardizing Search Data:** By comparing terms of interest to a set of anchor terms, `gtab` calibrates the Google Trends data to a more standardized scale. This step is crucial for ensuring meaningful comparisons in our analysis.

### Note on Google Trends Data Collection
- **Challenges with Data Retrieval:** Google Trends limits rapid data collection, occasionally necessitating IP address changes for continued access. Our script divides predator and victim names into sublists to manage this process effectively.
- **Handling Inconsistent Responses:** We encountered varying responses from Google Trends, with some keywords initially marked as 'bad' later being accepted. To combat this, we conducted two rounds of data collection – an initial run followed by a rerun for initially missed data. This approach ensures comprehensive data collection, culminating in `victim_all.csv` and `predator_all.csv`.

## Data Processing
- **Integration and Transformation:** The collected data is integrated into a primary Excel sheet and then transformed into a panel data format suitable for statistical analysis. This process is facilitated by the script `transform_panel_data.ipynb`.

## Statistical Analysis in R
- **Analytical Approach:** Fixed and random effects analysis is conducted using the `pglm` package in R. This methodological choice is aimed at understanding the varied factors influencing victims' decisions to accuse their predators.

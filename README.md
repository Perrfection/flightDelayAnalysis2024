# Flight Delay Analysis (U.S. Airlines 2024)

## Key Visualization: Airline Delay Performance

![Scatter plot comparing airline delay rate (percent of flights delayed) on the vertical axis versus average arrival delay in minutes on the horizontal axis. Each point represents an individual US carrier, with labels; the plot title reads Airline Delay Performance and the axes are labeled Delay rate (%) and Average delay (minutes). The chart has a white background with grid lines and a legend; overall tone is informational and analytical.](visuals/delay_rate_vs_avg_delay.png)

---

**Overview** Identification of drivers that most contribute to U.S. flight delays using a sample of 7M flights. Operational factors, primarily late aircraft, are the leading cause, and delays compound throughout the day. Airline performance varies significantly in both frequency and severity of delays.

---

## Key Results

* **Primary factor:** Late aircraft delays are the largest contributor to total delay minutes
* **Compounding effect:** Early flights (5–8 am) have the lowest delays; delays compound later throughout the day
* **Airline differences:** Wide spread in performance; some carriers show both higher delay rate and longer delays
* **Frequency vs. severity:** Some airlines have frequent large delays, others less frequent moderate delays

---

## What I Did

* **Cleaned** and **engineered** features (e.g., departure hour, delay indicator)
* **Analyzed** delays by time of day, airline, and cause
* **Compared** delay rate (%) vs. average delay (minutes) to separate frequency from severity
* **Built** clear visualizations and a final comparison view 
* **Translated** analytical findings into clear, actionable insights.

---

## Interactive Dashboard

[View 'Understanding the Primary Drivers of U.S. Flight Delays' on Tableau Public](https://public.tableau.com/app/profile/perrfection.peterkin/viz/USAirlineDelayDashboard/UnderstandingthePrimaryFactorsofU_S_FlightDelays)

---

## Technologies Used

* Python: pandas, numpy
* Notebook: jupyter
* Visualization: matplotlib, seaborn, tableau desktop
* Basic tests: pytest
* Modular code: 'scr/analysis.py'
* Data set: https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024

---

## Repo Structure

flightDelayAnalysis/
- data
    - flight_data_2024_sample.csv
    - flight_data_2024.csv
- notebooks/
    - analysis.ipynb
- src/
    - analysis.py
- tests/
    - test_analysis.py
- visuals/
    - avg_delay_by_carrier.png
    - avg_delay_by_dep_hour.png
    - delay_rate_by_carrier.png
    - delay_rate_vs_avg_delay.png (grouped by airline/carrier)
    - delay_totals_by_delay_type.png
    - most_common_biggest_delay_type_by_carrier.png
- README.md
- requirements_dev.txt
- requirements.txt

---

## How to Run

pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb

---

## Why It Matters

Identifies actionable insights (such as turnaround efficiency and  scheduling) that can reduce delays and improve carrier reliability.

---

## Next Steps

* Predictive model for delay classification
* Interactive dashboard (Tableau/Power BI)

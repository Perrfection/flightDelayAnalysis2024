# Flight Delay Analysis (U.S. Airlines)

## Key Visualization: Airline Delay Performance

![Airline Delay Performance](visuals/delay_rate_vs_arg_delay.png)

**Overview** Analyzed 7M+ flights to identify what factors cause delays. Operational factors, such as late aircraft, tend to be the leading cause and delays compound throughout the day. Airline performance varies significantly in both frequency and severity of delays.

---

## What I Did

* **Cleaned** and **engineered** features (e.g., departure hour, delay indicator)
* **Analyzed** delays by time of day, airline, and cause
* **Compared** delay rate (%) vs. average delay (minutes) to separate frequency from severity
* **Built** clear visualizations and a final comparison view 
* **Translated** analytical findings into clear, actionable insights.

---

## Key Results

* **Primary factor:** Late aircraft delays are the largest contributor to total delay minutes
* **Compunding effect:** Early flights (5–8 am) have the lowest delays; delays compound later throught the day
* **Airline differences:** Wide spread in performance; some carriers show both higher delay rate and longer delays
* **Frequency vs. severity:** Some airlines have frequent small large delays , others less frequent and moderate

---

## Tech

* Python: pandas, numpy
* Visualization: matplotlib, seaborn
* Notebook + modular code (`src/analysis.py`) + basic tests (pytest)

---

## Repo Structure

```
flight-delay-analysis/
├── notebooks/analysis.ipynb
├── src/analysis.py
├── tests/
├── visuals/
│   └── airline_performance_scatter.png
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

---

## Why It Matters

Pinpoints **actionable levers** (turnaround efficiency, scheduling) that can reduce delays and improve reliability.

---

## Next Steps

* Predictive model for delay classification
* Interactive dashboard (Tableau/Power BI)

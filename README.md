# RiskPulseAI

### Event-Driven Portfolio Stress Testing using Financial NLP

RiskPulseAI is an AI-powered financial risk analysis system that converts unstructured financial news and social media signals into actionable portfolio risk insights.

The system combines financial sentiment analysis, event classification, impact scoring, and scenario-based portfolio stress testing to help identify which events could have the greatest effect on a portfolio.

---

## Problem Statement

Financial markets react rapidly to events such as:

- Regulatory investigations
- Geopolitical disruptions
- Interest-rate changes
- Credit events
- Earnings surprises
- Product launches
- Revenue forecast changes

These signals are often scattered across financial news and social media, making it difficult to quickly understand their potential portfolio impact.

### Our Approach

RiskPulseAI follows an event-driven pipeline:

**Financial News + Social Media**

↓

**Text Preprocessing**

↓

**FinBERT Sentiment Analysis**

↓

**Event Classification**

↓

**Risk Impact Scoring**

↓

**Portfolio Stress Testing**

↓

**Interactive Risk Dashboard**

The system identifies the event type, determines sentiment, assigns an impact score, and maps the resulting risk to portfolio holdings.

---

## Key Features

- Financial sentiment analysis using **FinBERT**
- Rule-based financial event classification
- Event impact scoring from **1–10**
- Risk levels: **Low, Medium, High, Critical**
- Combined financial news and social media analysis
- Company-level risk aggregation
- Scenario-based portfolio stress testing
- Estimated portfolio loss calculation
- Top risk driver identification
- Explainable risk signals with event evidence
- Interactive Flask dashboard
- Automated tests for core risk components

---

## System Architecture

```text
                ┌─────────────────────────┐
                │ Financial News           │
                │ Social Media Signals     │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Data Ingestion           │
                │ CSV-based Input          │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Text Preprocessing       │
                │ Cleaning & Normalization │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ FinBERT Sentiment        │
                │ Positive / Neutral /     │
                │ Negative + Probability   │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Event Classification     │
                │ Geopolitical / Credit / │
                │ Regulatory / Earnings / │
                │ Macro / Product etc.    │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Impact Scoring           │
                │ Event Severity +         │
                │ Sentiment + Source       │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Portfolio Stress Engine  │
                │ Scenario Shock Rates     │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ RiskPulseAI Dashboard    │
                │ Risk Drivers + Loss +    │
                │ Portfolio Exposure       │
                └─────────────────────────┘

## Technology Stack
Programming & Backend
- Python
- Flask
- Pandas
- NumPy
NLP & Machine Learning
- Hugging Face Transformers
- ProsusAI/FinBERT
- Rule-based event classification
Frontend
- HTML
- CSS
- JavaScript
Data & Storage
- CSV-based datasets
- Synthetic financial news
- Synthetic social media signals
- Synthetic portfolio holdings
Testing
- Pytest
Dataset
The project uses synthetic data created specifically for the hackathon demonstration.
All project datasets are stored inside the data/ directory.
Financial News
File: data/news_data.csv
Contains financial news records with:
- Company
- Source
- Date
- Headline
- Text
Social Media
File: data/social_data.csv
Contains social media signals with:
- Company
- Source
- Date
- Author
- Text
Portfolio
File: data/portfolio.csv
Contains synthetic portfolio holdings with:
- Asset ID
- Company
- Asset type
- Portfolio value
- Portfolio weight
Generated Risk Signals
File: data/risk_signals.csv
Contains:
- Sentiment
- Event type
- Event evidence
- Impact score
- Risk level
Stress Test Results
File: data/stress_test_results.csv
Contains:
- Portfolio value
- Risk level
- Shock rate
- Estimated loss
- Stressed portfolio value
Risk Scoring Methodology
RiskPulseAI calculates an impact score using three components.
Event Severity
Different financial events have different baseline severities.
Event Type	Severity
Geopolitical	High
Macroeconomic	High
Credit Event	High
Regulatory	High
Earnings	Medium
Product Launch	Lower


Sentiment Severity
FinBERT produces positive, neutral, and negative probabilities.
The sentiment score is calculated as:
Sentiment Score = Positive Probability - Negative Probability

The magnitude of the sentiment is then incorporated into the impact score.
Source Weight
Financial news sources receive a higher source weight than social media signals.
The final impact score is constrained between:
1 and 10
Risk levels are mapped as:
Impact Score	Risk Level
1–3	Low
4–6	Medium
7–8	High
9–10	Critical


Portfolio Stress Testing
RiskPulseAI converts company-level risk into a scenario-based portfolio shock.
The current scenario assumptions are:
Risk Level	Shock Rate
Low	2%
Medium	5%
High	10%
Critical	20%


The system applies the maximum detected risk level for each company to its portfolio exposure.
Important: The estimated losses are scenario-based stress-test estimates, not predictions of actual market losses.

Key Results
The current synthetic portfolio contains approximately:
$9.5 million
in total exposure.
The RiskPulseAI pipeline analyzed:
20 risk signals
from financial news and social media.
Portfolio Stress Scenario
Metric	Result
Portfolio Value	$9.5M
Estimated Stress Loss	$1.2M
Stressed Portfolio Value	$8.3M
Portfolio Loss	12.63%
Total Risk Signals	20
Critical Events	1
High-Risk Events	12


Highest-Risk Event
The strongest detected event is:
Alpha Motors — Geopolitical Risk
- Impact Score: 10/10
- Risk Level: Critical
- Sentiment: Negative
- Sentiment Score: -0.953
- Evidence: Geopolitical + Supply Chain
This event produces a 20% scenario shock on Alpha Motors' portfolio exposure.
Explainability
RiskPulseAI does not only display a risk score.
For each major risk driver, the dashboard provides:
- Company
- Trigger event
- Event evidence
- Sentiment
- Impact score
- Risk level
- Original text
This allows users to understand why a company was flagged as high or critical risk.
Project Structure
RiskPulseAI/
│
├── data/
│   ├── news_data.csv
│   ├── social_data.csv
│   ├── portfolio.csv
│   ├── risk_signals.csv
│   └── stress_test_results.csv
│
├── docs/
│   ├── architecture.png
│   └── presentation.pdf
│
├── src/
│   ├── app/
│   ├── ingestion/
│   ├── nlp/
│   ├── portfolio/
│   ├── risk_engine/
│   └── utils/
│
├── tests/
│   └── test_risk_engine.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

Installation
Clone the Repository
git clone https://github.com/NSrivastava1012/RiskPulseAI.git
cd RiskPulseAI

Create a Virtual Environment
python -m venv venv

Activate the Virtual Environment
Windows PowerShell:
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Running the Project
Generate Risk Signals
python -m src.risk_engine.batch_analysis

This analyzes the financial news and social media datasets and generates:
data/risk_signals.csv

Run Portfolio Stress Testing
python -m src.portfolio.stress_test

This generates:
data/stress_test_results.csv

Start the Dashboard
python -m src.app.app

Open the dashboard in your browser:
http://127.0.0.1:5000/

API Endpoints
RiskPulseAI provides the following Flask API endpoints:
Endpoint	Purpose
/api/summary	Portfolio summary and risk metrics
/api/risk-signals	All detected risk signals
/api/stress-test	Portfolio stress-test results
/api/top-risk-events	Highest-impact risk events


Testing
Run the automated tests using:
pytest

Test Coverage
The current tests cover:
- Event classification
- Critical impact scoring
- End-to-end risk analysis
Current Result
3 passed

Limitations
- The current datasets are synthetic and intended for demonstration.
- Event classification uses transparent rule-based keyword matching.
- FinBERT sentiment predictions may not always perfectly capture financial context.
- Stress-test shock rates are predefined scenario assumptions.
- The current system does not use real-time market prices or live news APIs.
Future Improvements
Potential extensions include:
- Real-time financial news ingestion
- Live market price integration
- More advanced event classification using fine-tuned models
- Historical backtesting of stress scenarios
- Correlation-aware portfolio stress testing
- Sector-level risk aggregation
- Automated alerts for critical events
- Time-series risk monitoring
- More sophisticated portfolio optimization
Disclaimer
RiskPulseAI is a hackathon prototype designed for research and demonstration purposes.
The stress-test outputs are scenario-based estimates and should not be interpreted as financial advice or predictions of actual market performance.
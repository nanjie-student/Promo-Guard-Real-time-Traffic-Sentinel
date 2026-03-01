# Promo-Guard-Real-time-Traffic-Sentinel
Real-time E-commerce Anomaly Detection System using PyTorch (Transformers) & AWS Lambda (TypeScript). Features multimodal time-series modeling for clickstream data & temporal drift monitoring.

---

## Setup & Dependencies

This repository includes a small utility script (`gen_traffic.py`) to generate synthetic clickstream
traffic events. The script depends on **numpy** and **pandas**.

Install dependencies in a Python environment (virtualenv or system).

```bash
# create and activate a virtual environment (preferred)
python3 -m venv .venv        # or `venv` if you prefer
source .venv/bin/activate    # macOS/Linux
# install requirements
pip install -r requirements.txt
```

If you are **not** using a virtual environment, omit the `--user` flag on pip. The
repository already contains a `requirements.txt` with the necessary packages.

## Generating traffic data

Run the generator like so:

```bash
python gen_traffic.py        # within an activated venv, or using python3 directly
```

A file named `traffic_data.jsn` will be created in the project root.

---

Key Technical Features

    AI/ML (Python): Developed a TimeSeriesTransformer model using PyTorch and Hugging Face to capture complex temporal dependencies in non-uniform user behaviors.

    Backend (TypeScript): Scalable serverless architecture deployed on AWS Lambda, providing high-concurrency inference via GraphQL (AppSync).

    Rigorous Methodology: Implemented automated evaluation pipelines to detect Temporal Drift, ensuring model reliability during sudden traffic spikes.

    Frontend (React): Real-time dashboard for visualizing traffic health and anomaly distribution.

Key Technical Features

    AI/ML (Python): Developed a TimeSeriesTransformer model using PyTorch and Hugging Face to capture complex temporal dependencies in non-uniform user behaviors.

    Backend (TypeScript): Scalable serverless architecture deployed on AWS Lambda, providing high-concurrency inference via GraphQL (AppSync).

    Rigorous Methodology: Implemented automated evaluation pipelines to detect Temporal Drift, ensuring model reliability during sudden traffic spikes.

    Frontend (React): Real-time dashboard for visualizing traffic health and anomaly distribution.
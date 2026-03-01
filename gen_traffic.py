import os
import sys
import numpy as np
import pandas as pd
import time


# Ensure we are running inside a virtual environment
# (the project ships with a `.venv` directory).
def ensure_venv():
    # A common detection: prefix equals base_prefix when not in venv
    if getattr(sys, 'base_prefix', None) == sys.prefix:
        # also check VIRTUAL_ENV env var for completeness
        if not os.environ.get('VIRTUAL_ENV'):
            sys.stderr.write(
                "[ERROR] This script should be run inside a Python virtual environment.\n"
                "Activate the venv with `source .venv/bin/activate` or create one.\n"
            )
            sys.exit(1)


ensure_venv()


def generate_clickstream(num_samples=1000):

    data =[]

    for _ in range(num_samples):
        # Simulate a clickstream event with random features
        is_bot = np.random.choice([0, 1], p=[0.8, 0.2])  # 20% chance of being a bot
        if is_bot == 0:
            # 正常人的点击间隔：随机且较长
            intervals = np.random.exponential(scale=2.0, size=50)
        else:
            #机器人点击的间隔：较短且规律
            intervals = np.random.normal(loc= 0.1,scale=0.02,size=50)
            intervals = np.clip(intervals, a_min=0.01, a_max=0.5)  # Ensure non-negative intervals
        
        data.append({
            "intervals": intervals.tolist(),
            "label": is_bot
        })

    df = pd.DataFrame(data)
    df.to_json("traffic_data.json", orient="records", lines=True)
    print(f"Generated {num_samples} clickstream events and saved to traffic_data.jsn")


if __name__ == "__main__":

    #1.先检查环境是否正确
    ensure_venv()

    #2.再执行核心逻辑
    generate_clickstream(num_samples=1000)
 
    
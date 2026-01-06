import time
import random
import uuid
import pandas as pd
from datetime import datetime
import os

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data/events")
EVENTS_PER_BATCH = 10
INTERVAL_SECONDS = 5

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

EVENT_TYPES = ["view", "purchase"]

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "user_id": f"user_{random.randint(1, 100)}",
        "product_id": f"product_{random.randint(1, 50)}",
        "price": round(random.uniform(10.0, 500.0), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    print(f"Starting data generator. Writing to {DATA_DIR}...")
    try:
        while True:
            events = [generate_event() for _ in range(EVENTS_PER_BATCH)]
            df = pd.DataFrame(events)
            
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"events_{timestamp}.csv"
            filepath = os.path.join(DATA_DIR, filename)
            
            df.to_csv(filepath, index=False)
            print(f"Generated {len(events)} events -> {filename}")
            
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nStopping data generator.")

if __name__ == "__main__":
    main()

# Real-Time E-commerce Pipeline

## Overview
This project implements a real-time data pipeline for e-commerce events. It generates synthetic JSON/CSV data, processes it via Spark Structured Streaming, and stores it in PostgreSQL for analysis.

## Architecture
1. **Data Generator** (`data_generator.py`):
   - Produces CSV files in `real_time_ecommerce_pipeline/data/events`.
   - Simulates user actions: `view`, `purchase`, `cart_add`.
   - Fields: `event_id`, `user_id`, `product_id`, `price`, `event_type`, `timestamp`.

2. **Spark Streaming** (`spark_streaming_to_postgres.py`):
   - Watches `data/events` for new files.
   - **Schema Mapping**: Automatically renames `item_id` -> `product_id` and `timestamp` -> `event_time` to match the database.
   - **Security**: Loads database credentials securely from `.env` file.
   - **Processing**: Enforces strictly ordered columns before writing.

3. **PostgreSQL**:
   - Stores the processed events in the `user_events` table.
   - Schema: `event_id` (PK), `user_id`, `product_id`, `event_type`, `price`, `event_time`.

## Components
- `scripts/data_generator.py`: Python script for data simulation. Handles absolute path resolution.
- `scripts/spark_streaming_to_postgres.py`: Spark job with JDBC integration.
- `sql/postgres_setup.sql`: SQL script to initialize `ecommerce_db` and `user_events`.
- `.env`: Configuration file for sensitive credentials (e.g., `YOUR_POSTGRES_PASSWORD`).

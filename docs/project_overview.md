# Real-Time E-commerce Pipeline

## Overview
This project implements a real-time data pipeline for e-commerce events. It generates synthetic data, processes it via Spark Structured Streaming, and stores it in PostgreSQL for analysis.

## Architecture
1. **Data Generator**: Produces CSV files in `data/events` simulating user actions.
2. **Spark Streaming**: Watches the directory for new files, processes them, and writes to Postgres.
3. **PostgreSQL**: Stores the processed events in the `events` table.

## Components
- `scripts/data_generator.py`: Generates data.
- `scripts/spark_streaming_to_postgres.py`: ETL job.
- `sql/postgres_setup.sql`: Database schema.

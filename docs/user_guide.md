# User Guide

## Prerequisites
- Python 3.8+
- Apache Spark 3.x
- PostgreSQL 12+
- Java 8/11 (for Spark)

## Setup
1. **Install Dependencies**:
   ```bash
   pip install pandas pyspark faker psycopg2-binary
   ```
   Download the PostgreSQL JDBC driver (`postgresql-42.2.18.jar`) and place it in the `scripts` or a shared `lib` folder.

2. **Database Setup**:
   Run the SQL script in your Postgres instance:
   ```bash
   psql -U postgres -d ecommerce_db -f sql/postgres_setup.sql
   ```

## Running the Pipeline
1. **Start the Data Generator**:
   ```bash
   python scripts/data_generator.py
   ```
   This will start creating CSV files in `data/events`.

2. **Start the Spark Job**:
   ```bash
   python scripts/spark_streaming_to_postgres.py
   ```
   Ensure the JDBC driver jar is accessible. You might need to adjust the path in the script or run with `spark-submit`.

## Monitoring
Check the console output of the Spark job and query the `events` table in Postgres:
```sql
SELECT count(*) FROM events;
SELECT * FROM events ORDER BY timestamp DESC LIMIT 10;
```

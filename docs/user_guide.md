# User Guide

## Prerequisites
- Python 3.8+
- Apache Spark 3.x (or PySpark)
- PostgreSQL 12+
- VS Code (Recommended)

## Setup
1. **Install Python Dependencies**:
   ```bash
   pip install pandas pyspark faker psycopg2-binary python-dotenv
   ```
   *Note: The PostgreSQL JDBC driver is automatically handled by Spark (`org.postgresql:postgresql:42.6.0`).*

2. **Environment Configuration**:
   Create a `.env` file in the project root:
   ```env
   YOUR_POSTGRES_PASSWORD=your_actual_password
   ```

3. **Database Setup**:
   - Open `sql/postgres_setup.sql` in VS Code.
   - Run the query to create `ecommerce_db` and the `user_events` table.
   - Alternatively, connect via VS Code Database extension to verify.

## Running the Pipeline
You need **two separate terminals**.

### Terminal 1: Data Generator
```bash
python scripts/data_generator.py
```
- This script uses absolute paths, so it will correctly save files to `data/events` regardless of where you run it.

### Terminal 2: Spark Job
```bash
python scripts/spark_streaming_to_postgres.py
```
- Wait for the log: `Batch written to PostgreSQL successfully`.

## Monitoring
1. **Spark Logs**: Watch Terminal 2 for "Batch X processed" messages.
2. **Database Verification**:
   Run this SQL query in VS Code:
   ```sql
   SELECT count(*) FROM user_events;
   SELECT * FROM user_events ORDER BY event_time DESC LIMIT 10;
   ```
   *Repeatedly run the count query to see real-time growth.*

# Performance Metrics

## Observed Performance
Based on local execution logs:

1.  **Throughput**:
    -   **Batch Size**: ~1920 records per batch (observed in logs).
    -   **Processing Time**: Batches processed typically within 1-2 seconds.

2.  **Latency**:
    -   Time from "Batch Processed" to "Batch Written to PostgreSQL" is sub-second for small batches.

## Resource Usage
-   **Spark Driver**: Single-node local mode (`local[*]`).
-   **Memory**: Standard PySpark overhead (Java VM).
-   **Disk I/O**:
    -   Reads: CSV inputs from `data/events`.
    -   Writes: JDBC inserts to localhost PostgreSQL.

## Benchmarking Goals
-   Current: 10 events/batch (Generator setting).
-   Stress Test: Can scale `EVENTS_PER_BATCH` in `data_generator.py` to 1000+ to test Postgres insertion limits.

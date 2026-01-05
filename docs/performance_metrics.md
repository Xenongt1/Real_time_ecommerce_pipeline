# Performance Metrics

## Key Indicators
1. **Throughput**: Events processed per second (EPS).
2. **Latency**: Time diff between `timestamp` (event generation) and `processed_at` (db insertion).
3. **Batch Duration**: Time taken for Spark to process a micro-batch.

## Resource Usage
- **CPU**: Spark executor and driver CPU usage.
- **Memory**: Heap usage for Spark executors.
- **Disk I/O**: Write speed to PostgreSQL.

## Benchmarking
- Start with 10 events/batch (5s interval).
- Scale up to 100, 1000 events/batch to observe latency spikes.

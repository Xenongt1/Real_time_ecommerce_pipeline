# Test Cases

## Functional Testing
| ID | Description | Expected Result |
|----|-------------|-----------------|
| TC01 | Generate Data | CSV files appear in `data/events` every 5 seconds. |
| TC02 | Spark Job Startup | Job starts without errors and connects to Spark Session. |
| TC03 | Data Ingestion | Spark logs show batches being processed. |
| TC04 | Database Write | Records appear in `events` table in Postgres. |
| TC05 | Data Integrity | `event_id` in CSV matches `event_id` in DB. |

## Failure Scenarios
| ID | Description | Expected Result |
|----|-------------|-----------------|
| TC06 | Invalid CSV Format | Spark job handles or logs error, does not crash (resilient). |
| TC07 | DB Unavailable | Spark job retries or fails gracefully with clear error. |
| TC08 | Stop Generator | Spark job continues running, waiting for new files. |

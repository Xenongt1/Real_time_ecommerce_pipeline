# Test Cases

## Functional Testing
| ID | Description | Expected Result | Status |
|----|-------------|-----------------|--------|
| TC01 | **Generate Data** | CSV files appear in `real_time_ecommerce_pipeline/data/events` every 5 seconds. | ✅ Pass |
| TC02 | **Spark Job Startup** | Job starts, connects to Spark Session, and loads PostgreSQL driver. | ✅ Pass |
| TC03 | **Schema Mapping** | Spark correctly renames `item_id` to `product_id` and `timestamp` to `event_time`. | ✅ Pass |
| TC04 | **Data Ingestion** | Spark logs show "Batch written to PostgreSQL successfully". | ✅ Pass |
| TC05 | **Database Verification** | `SELECT count(*) FROM user_events` shows increasing count. | ✅ Pass |

## Failure & Resilience Scenarios
| ID | Description | Expected Result | Status |
|----|-------------|-----------------|--------|
| TC06 | **Column Order Mismatch** | Script explicitly selects columns (`event_id`, `user_id`...) to prevent positional errors. | ✅ Pass |
| TC07 | **Generator Unreachable** | Spark job explicitly waits for new files if generator stops. | ✅ Pass |
| TC08 | **Auth Failure** | Script fails fast if `.env` password is wrong (verified with `os.getenv`). | ✅ Pass |

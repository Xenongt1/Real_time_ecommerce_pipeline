from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set Hadoop environment variables for Windows
os.environ["HADOOP_HOME"] = r"C:\Users\MubarakTijani\.gemini\antigravity\scratch\real_time_ecommerce_pipeline\hadoop"
os.environ["PATH"] += r";C:\Users\MubarakTijani\.gemini\antigravity\scratch\real_time_ecommerce_pipeline\hadoop\bin"

# 1️⃣ Create Spark session
spark = SparkSession.builder \
    .appName("EcommerceStreamingTest") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
    .getOrCreate()

# 2️⃣ Define schema for CSV
# Matches schema from data_generator.py
schema = StructType() \
    .add("event_id", StringType()) \
    .add("event_type", StringType()) \
    .add("user_id", StringType()) \
    .add("item_id", StringType()) \
    .add("price", DoubleType()) \
    .add("timestamp", TimestampType())

# 3️⃣ Read streaming CSV
csv_stream = spark.readStream \
    .option("header", True) \
    .schema(schema) \
    .csv(r"C:\Users\MubarakTijani\.gemini\antigravity\scratch\real_time_ecommerce_pipeline\data\events")
  # folder we are watching



# 4️⃣ Process batch with logging
def process_batch(df, epoch_id):
    count = df.count()
    logger.info(f"Batch {epoch_id} processed. Record Count: {count}")
    
    if count > 0:
        # Transformation: Rename columns to match PostgreSQL schema
        df = df.withColumnRenamed("item_id", "product_id") \
               .withColumnRenamed("timestamp", "event_time")
        
        # Reorder columns to match PostgreSQL table strictly
        df = df.select("event_id", "user_id", "product_id", "event_type", "price", "event_time")

        # Converts top 5 rows to Pandas for pretty logging
        records = df.limit(5).toPandas().to_string(index=False)
        logger.info(f"Sample Records:\n{records}")

        # Write to PostgreSQL
        try:
            df.write \
                .format("jdbc") \
                .option("url", "jdbc:postgresql://localhost:5432/ecommerce_db") \
                .option("dbtable", "user_events") \
                .option("user", "postgres") \
                .option("password", os.getenv("YOUR_POSTGRES_PASSWORD")) \
                .option("driver", "org.postgresql.Driver") \
                .mode("append") \
                .save()
            logger.info("Batch written to PostgreSQL successfully.")
        except Exception as e:
            logger.error(f"Error writing to PostgreSQL: {e}")

query = csv_stream.writeStream \
    .outputMode("append") \
    .foreachBatch(process_batch) \
    .start()

query.awaitTermination()

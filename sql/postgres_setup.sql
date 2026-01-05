-- Create the database if it doesn't exist (manual step often required, but good to note)
-- CREATE DATABASE ecommerce_db;

-- Connect to ecommerce_db and run:

CREATE TABLE IF NOT EXISTS events (
    event_id VARCHAR(50) PRIMARY KEY,
    event_type VARCHAR(20),
    user_id VARCHAR(20),
    item_id VARCHAR(20),
    price DECIMAL(10, 2),
    timestamp VARCHAR(30),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_events_timestamp ON events(timestamp);
CREATE INDEX idx_events_type ON events(event_type);

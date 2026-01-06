-- 1️ Create database
CREATE DATABASE ecommerce_db;

-- 2️ Connect to the database
\c ecommerce_db;

-- 3 Create table for events
CREATE TABLE user_events (
    event_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    product_id VARCHAR(50),
    event_type VARCHAR(20),
    price NUMERIC(10,2),
    event_time TIMESTAMP
);

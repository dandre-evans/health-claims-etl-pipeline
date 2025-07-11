-- SQL script to create PostgreSQL tables

CREATE TABLE IF NOT EXISTS claims_cleaned (
    id SERIAL PRIMARY KEY,
    provider_name VARCHAR(255),
    procedure_code VARCHAR(10),
    average_submitted_charges NUMERIC,
    average_payment_amount NUMERIC,
    number_of_services INT
);
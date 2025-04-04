# etl_pipeline
ETL Pipeline orchestrated with Apache Airflow

## Overview
An ETL pipeline that **E**xtracts, **T**ransforms, and **L**oads employee data from the source location (local PC) to
its source destination (Aiven PostgreSQL database) that acts as the data warehouse. Transformation here was done with
Pandas. The goal of this project is to demonstrate the foundational concepts (steps) of building a data piepline and
automating it using a data orchestration tool like Airflow; which is what is used here.

## Requirements
This project made use of:
- Python (Pandas)
- Apache Airflow
- SQLAlchemy
- Aiven (for the POstgreSQL databases acting as the data warehouse)

To install requirements after project setup, run `pip install -r requirements.txt`

## Setup & Installation
- To run this project, run:
  - using SSH: `git clone git@github.com:Mimi97-aqua/etl_pipeline.git`
  - using HTTPS: `https://<PAT>@github.com/Mimi97-aqua/etl_pipeline.git`
- Install project requirements
- Navigate to Aiven or any database / data warehousing solution of your choice
- Create a `.env` file and in it, insert your database connection string as such `DB_URL="<db_conn_string>`
- 

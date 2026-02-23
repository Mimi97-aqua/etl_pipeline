# etl_pipeline
ETL Pipeline for employees data orchestrated with Apache Airflow

## Overview
An ETL pipeline that **E**xtracts, **T**ransforms, and **L**oads employee data from the source location (local PC) to
its prescribed destination (Aiven PostgreSQL database) that acts as the data warehouse. Transformation here was done with
Pandas. The goal of this project is to demonstrate the foundational concepts (steps) of building a data piepline and
automating it using a data orchestration tool like Airflow; which is what is used here.

## Requirements
This project made use of:
- Python
- Pandas
- OpenPyXL
- Apache Airflow
- SQLAlchemy
- Python Dotenv
- Aiven (for the PostgreSQL databases acting as the data warehouse)

To install requirements after project setup, run `pip install -r requirements.txt`

## Setup & Installation
- To clone this project, run: `git clone git@github.com:Mimi97-aqua/etl_pipeline.git`
- Install project requirements
- Create a `.env` file and in it, insert your database connection string as such `DB_URL="<db_conn_string>`

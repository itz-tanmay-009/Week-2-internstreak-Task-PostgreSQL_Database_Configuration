## Week 2 Task Completion

This project completed the following tasks:

1. Created PostgreSQL database tables with primary keys and constraints.
2. Added Python PostgreSQL connection code using psycopg2.
3. Implemented parameterized CRUD operations.
4. Added complex SQL queries using GROUP BY and aggregate functions.
5. Added a seed script containing mock students, courses, and enrollments.

### Database Details

- Database: PostgreSQL
- Database Name: internstreak_week2_db
- Tables: students, courses, enrollments
- Python Library: psycopg2-binary
# PostgreSQL Database Configuration

This repository contains the Week 2 project for my Python Full Stack Development Internship.

## Project Overview

This project focuses on SQL and PostgreSQL database configuration using Python.

The project demonstrates:

- PostgreSQL database setup
- Database schema creation using DDL
- Python database connectivity using psycopg2
- Parameterized SQL queries
- CRUD operations
- Complex SQL queries using GROUP BY and aggregations
- Database seeding with mock data

## Project Structure

```text
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries.sql
│
├── src/
│   ├── database_connection.py
│   └── crud_operations.py
│
├── tests/
├── .gitignore
└── README.md
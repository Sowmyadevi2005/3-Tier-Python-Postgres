# 3-Tier Python + PostgreSQL Application

This project is a 3-tier web application built using Python for the backend, with PostgreSQL as the database. The application consists of a presentation layer, a business logic layer, and a data access layer.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Setting Up Python Virtual Environment](#1-setting-up-python-virtual-environment)
  - [2. Installing PostgreSQL](#2-installing-postgresql)
  - [3. Setting Up PostgreSQL Database](#3-setting-up-postgresql-database)
- [Running the Application](#running-the-application)
- [License](#license)

## Prerequisites

Before setting up the project, ensure you have the following installed on your machine:

- Ubuntu (or another compatible Linux distribution)
- Python 3.12 or higher
- PostgreSQL

## Installation

### 1. Setting Up Python Virtual Environment

1. **Install the Python 3.12 virtual environment package:**

   ```bash
   sudo apt install python3.12-venv -y
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv myenv
   ```

3. **Activate the virtual environment:**

   ```bash
   source myenv/bin/activate
   ```

4. **Install required Python libraries from `requirements.txt`:**

   First, ensure `pip` is installed:

   ```bash
   sudo apt install python3-pip -y
   ```

   Then, install the required libraries:

   ```bash
   pip3 install -r requirements.txt
   ```

### 2. Installing PostgreSQL

To install and set up PostgreSQL, follow these steps:

1. **Install PostgreSQL and additional tools:**

   ```bash
   sudo apt-get install postgresql postgresql-contrib
   ```

2. **Start the PostgreSQL service:**

   ```bash
   sudo systemctl start postgresql
   ```

3. **Enable PostgreSQL to start on boot:**

   ```bash
   sudo systemctl enable postgresql
   ```

### 3. Setting Up PostgreSQL Database

1. **Switch to the PostgreSQL user:**

   ```bash
   sudo -i -u postgres

   
   psql
   ```

2. **Create a new PostgreSQL user:**

   ```sql
   CREATE USER root WITH PASSWORD 'root';
   ```

3. **Create a new PostgreSQL database:**

   ```sql
   CREATE DATABASE my_database;
   ```

4. **Grant all privileges on the database to the new user:**

   ```sql
   GRANT ALL PRIVILEGES ON DATABASE my_database TO root;
   ```

5. **Connect to the new database:**

   ```sql
   \c my_database
   ```

6. **Grant all privileges on the public schema to the user:**

   ```sql
   GRANT ALL PRIVILEGES ON SCHEMA public TO root;
   ```

7. **Grant create privileges on the database to the user:**

   ```sql
   GRANT CREATE ON DATABASE my_database TO root;
   ```

## Running the Application

Once the environment and database are set up, you can run the application with the following steps:

1. **Ensure your virtual environment is activated:**

   ```bash
   source myenv/bin/activate
   ```

2. **Run the application:**

   ```bash
   python run.py
   ```

   The application will start, and you can access it via the specified host and port in your configuration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# Django CSV Analysis

## Project Description

This project is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface. 
The application provides functionalities such as displaying the first few rows of the data, calculating summary statistics, identifying and handling missing values, and 
generating basic plots using matplotlib and seaborn.

## Features

- Upload CSV files for data analysis.
- Display the first few rows of the data.
- Calculate summary statistics (mean, median, standard deviation) for numerical columns.
- Identify and handle missing values.
- Generate and display histograms for numerical columns.

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) (for managing the Python environment and dependencies)
- Python 3.8 or higher
- Git (for version control)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/yourusername/django_csv_analysis.git
cd django_csv_analysis

### 2. Create a new conda environment and activate it:

conda create -n django_csv_analysis python=your_python_version
conda activate django_csv_analysis

### 3. Install Dependencies

Install the required Python libraries using conda:
conda install django pandas numpy matplotlib seaborn

### 4. Apply Migrations

Apply the initial migrations to set up the database schema:

python manage.py migrate


### 5. Run the Development Server

Start the Django development server:

python manage.py runserver


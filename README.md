# GreenKart Selenium Automation Framework

## Project Overview
End-to-End UI automation framework built using Selenium WebDriver with Python and Pytest for the GreenKart e-commerce application.

The framework follows Page Object Model design pattern to improve maintainability and scalability.

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- WebDriver Manager
- HTML Reports
- Git & GitHub

## Features
- Automated product search and add-to-cart flow
- End-to-End checkout validation
- Reusable Page Objects
- Pytest fixtures for browser setup
- Automatic screenshot capture on failure
- HTML execution reports

## Project Structure
project
│── pages  
│   ├── home_page.py  
│   └── checkout_page.py  
│  
│── tests  
│   └── test_launch.py  
│  
│── reports  
│── conftest.py  
│── requirements.txt  

## How to Run
1. Install dependencies  
   pip install -r requirements.txt  

2. Run tests  
   pytest -v --html=reports/report.html  

## Author
Gauri Deshmukh

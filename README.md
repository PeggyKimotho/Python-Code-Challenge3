# Python-Code-Challenge3

## Introduction
The Restaurant Review System is a Python project that demonstrates the use of SQLAlchemy for managing restaurant reviews. It allows users to create, view, and manage restaurant reviews. The project consists of three main models: `Restaurant`, `Customer`, and `Review`, and includes various methods to interact with the data.

## Features
- Create and manage restaurants and customers.
- Create, view, and manage restaurant reviews.
- Find a customer's favorite restaurant based on their reviews.
- Retrieve the fanciest restaurant based on price.
- View all reviews for a restaurant.


## Usage
1. Create and run the necessary migrations to set up your database.
2. Use the `seeds.py` file to populate the database with sample data.
3. You can now run your main application code, which interacts with the database and performs various operations based on your defined methods.

## Database Schema
- The project uses SQLAlchemy to define the following models:
- `Restaurant`: Represents a restaurant and its attributes.
- `Customer`: Represents a customer and their attributes.
- `Review`: Represents a review of a restaurant, linking customers and restaurants.

## Code Structure
- `models.py`: Contains the SQLAlchemy models for `Restaurant`, `Customer`, and `Review`.
- `seeds.py`: Provides sample data to populate the database for testing purposes.

## Sample Data
The `seeds.py` file includes sample data for restaurants, customers, and reviews. You can use this data to test your application and methods.


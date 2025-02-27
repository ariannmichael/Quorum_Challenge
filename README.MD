# QUORUM-CHALLENGE-ARIANN

# About this Project
    This is a test project that follows the Quorum specifications. 
    This projects displays the bills and the numbers of supporters and opposers of each bill, and also displays the legislators and the bill they supported and opposed.

# Overview
  This is a full stack project that uses Django Rest Framework as the backend and ReactJS as the frontend. The data is stored in a PostgreSQL database. The project is containerized using Docker.
  To showcase my skills effectively, I applied Domain-Driven Design (DDD) principles and followed Clean Architecture guidelines. The project is divided into three layers: application, domain, and infrastructure. The application layer contains the use cases, the domain layer contains the entities and the repositories, and the infrastructure layer contains the database and the API.

## Stack
    - Django Rest Framework
    - ReactJS
    - PostgreSQL
    - Docker

## Installation
### Backend
    - In the backend folder, activate the virtual environment:
        ```
        source venv/bin/activate
        ```
    - Install the requirements:
        ```
        pip install -r requirements.txt
        ```
    - Run the following command, to start the database:
        ```
        docker-compose up -d
        ```
    - Run the migrations:
        ```
        python manage.py migrate
        ```

### Frontend
    - Install the dependencies:
        ```
        npm install
        ```
    - Run the server:
        ```
        npm run dev
        ```

## Running the Project
### Backend
    - Run the server:
        ```
        python manage.py runserver
        ```
    - Open the browser and go to the following URL:
        ```
        http://localhost:8000/api/
        ```
    - The API will be displayed.
    - The bills, legislators, votes and votes_results can be accessed through the following URLs:
        ```
        http://localhost:8000/api/bills/
        http://localhost:8000/api/legislators/
        http://localhost:8000/api/votes/
        http://localhost:8000/api/votes/results/
        ```
    - The bills, legislators, votes and votes_results can be updated by sending a csv file through the following URLs:
        ```
        http://localhost:8000/api/bills/import/
        http://localhost:8000/api/legislators/import/
        http://localhost:8000/api/votes/import/
        http://localhost:8000/api/votes/results/import/
        ```
    - The bills details, and legislators details can be accessed through the following URLs:
        ```
        http://localhost:8000/api/bills/analytics/
        http://localhost:8000/api/legislators/analytics/
        ``` 

### Frontend
    - Open the browser and go to the following URL:
        ```
        http://localhost:3000/
        ```
    - The bills and the legislators will be displayed through the routes:
        ```
        http://localhost:3000/bills
        http://localhost:3000/legislators
        ```

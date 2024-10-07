# Cat Exhibition — REST API

This project is a REST API for managing cats, breeds, and ratings as part of an online cat exhibition. The API includes user authentication via JWT and provides endpoints.

## Prerequisites

- Python 3.9 or higher
- pip
- PostgreSQL (if running outside of Docker)
- Docker
- Docker Compose

## Setup

Follow these steps to set up the project:

1. **Clone the repository**

    ```
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create .env file in the root of the project and add the following environment variables in it**

    ```
    touch .env

    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY=your_secret_key
    ```

3. **Use Docker Compose to run the project**

    ```
    docker-compose up -d
    ```

4. **Apply migrations**

    ```
    docker-compose exec cat_exhibition python manage.py migrate
    ```

## Testing the API

**Send a POST request to /auth/users/ to create a new user**

```
{
  "username": "testuser",
  "password": "testpassword"
}
```

**Send a POST request to /auth/jwt/create/ to obtain an access token**

```
{
  "username": "testuser",
  "password": "testpassword"
}
```

**Authenticate requests**

```
Authorization: Bearer your_access_token
```

**Creating a cat via the /cats/**

```
{
    "breed": "Siamese",
    "color": "black",
    "age": 4,
    "description": "красивая"
}
```

**Creating a breed via the /breeds/**

```
{
    "name": "Siamese",
    "description": "very beatiful"
}
```

**Creating a rating via the /ratings/**

```
{
  "cat": 4,
  "rating": 5
}
```

## API Documentation

```
After starting the project, navigate to http://127.0.0.1:8000/swagger/. The documentation describes how your API should work. The documentation is presented in Swagger format.
```

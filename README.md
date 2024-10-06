# Cat Exhibition — REST API

This project is a REST API for managing cats, breeds, and ratings as part of an online cat exhibition. The API includes user authentication via JWT and provides endpoints.

## Prerequisites

- Python 3.9 or higher
- pip
- PostgreSQL

## Setup

Follow these steps to set up the project:

1. **Clone the repository**

    ```
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create and activate a virtual environment**

    ```
    python -m venv venv
    ```

    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source venv/bin/activate
      ```

3. **Install the required packages**

    ```
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**

    ```
    touch .env

    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_KEY=your_secret_key
    ```

5. **Apply migrations**

    ```
    python manage.py migrate
    ```

## Running the Project

```
python manage.py runserver
```

## Testing the API

**Send a POST request to /auth/users/ to create a new user:**

```
{
  "username": "testuser",
  "password": "testpassword"
}
```

**Send a POST request to /auth/jwt/create/ to obtain an access token:**

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

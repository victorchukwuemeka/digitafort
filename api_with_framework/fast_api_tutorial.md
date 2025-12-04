# FastAPI Tutorial: Setup and Project Building

This tutorial will guide you through setting up a FastAPI project, creating a basic API, and structuring your project for scalability.

## 1. Prerequisites

Before you start, make sure you have Python 3.7+ and `pip` (the Python package installer) installed on your system.

## 2. Installation

First, you need to install FastAPI and an ASGI server to run your application. We will use Uvicorn, a lightning-fast ASGI server.

Open your terminal and run the following command:

```bash
pip install "fastapi" "uvicorn[standard]"
```

This command installs:
- `fastapi`: The core framework.
- `uvicorn`: The server to run your API, with standard dependencies for better performance.

## 3. Create a "Hello World" API

Now, let's create your first API.

1.  Create a file named `main.py`.
2.  Add the following code to `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

**Code Explanation:**
- `from fastapi import FastAPI`: Imports the `FastAPI` class.
- `app = FastAPI()`: Creates an instance of the `FastAPI` class.
- `@app.get("/")`: This is a "decorator" that tells FastAPI that the function below it is responsible for handling requests that go to:
    - the path `/`
    - using a `get` operation.
- `def read_root(): ...`: This is the function that will be called when a request to the `/` path is received.
- `return {"Hello": "World"}`: FastAPI will automatically convert this dictionary to JSON and send it as the response.

## 4. Run the Development Server

Now, run your API using Uvicorn. In your terminal, in the same directory as your `main.py` file, run:

```bash
uvicorn main:app --reload
```

**Command Explanation:**
- `main`: refers to the `main.py` file.
- `app`: refers to the `app` object you created inside `main.py`.
- `--reload`: makes the server restart after code changes. Only use this for development.

You will see output similar to this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
INFO:     Started server process [12347]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Your API is now running! Open your browser and go to `http://12.0.0.1:8000`. You should see the JSON response: `{"Hello":"World"}`.

## 5. Explore the Automatic API Documentation

FastAPI automatically generates interactive API documentation for you.

- **Swagger UI**: Go to `http://127.0.0.1:8000/docs`. You'll see an interactive UI where you can test your API endpoints directly from the browser.
- **ReDoc**: Go to `http://127.0.0.1:8000/redoc`. You'll see alternative documentation.

## 6. Building a Simple Project: Handling Data

Let's create an endpoint that accepts data using a `POST` request.

1.  **Define a data model with Pydantic**: FastAPI uses Pydantic for data validation. You declare the "shape" of your data as a class.

    Update your `main.py` file with the following:

    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        description: str | None = None
        price: float
        tax: float | None = None

    @app.post("/items/")
    def create_item(item: Item):
        return item
    ```

    **Code Explanation:**
    - `from pydantic import BaseModel`: Imports the `BaseModel` class from Pydantic.
    - `class Item(BaseModel): ...`: Defines a data model for an item. `name` is a required string, `price` is a required float, and `description` and `tax` are optional.
    - `@app.post("/items/")`: Creates an endpoint that accepts `POST` requests to `/items/`.
    - `def create_item(item: Item): ...`: The `item` parameter is type-hinted with the `Item` model. FastAPI will automatically:
        - Read the body of the `POST` request as JSON.
        - Validate the data against the `Item` model.
        - If the data is invalid, it will return a clear error message.
        - If the data is valid, it will convert the JSON to an `Item` object and pass it to your function.

2.  **Test the new endpoint**: Go to your interactive docs at `http://127.0.0.1:8000/docs`. You will see your new `/items/` endpoint. You can use it to send a test request and see the response.

## 7. Suggested Project Structure

For larger applications, it's a good practice to organize your files. Here is a common project structure:

```
.
├── main.py
├── requirements.txt
└── my_project
    ├── __init__.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    ├── schemas
    │   ├── __init__.py
    │   └── item.py
    └── crud
        ├── __init__.py
        └── item.py
```

- **`main.py`**: The entry point of your application. It will import and include the routers from the `routers` directory.
- **`routers/`**: Contains the different API "routers" for your application (e.g., `items`, `users`).
- **`schemas/`**: Contains your Pydantic models (data schemas).
- **`crud/`**: Contains the functions that interact with your database (Create, Read, Update, Delete).

This structure helps to keep your code organized and maintainable as your project grows.

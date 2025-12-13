    # fastapi-tortoise-mysql
    This is the Example of Fast API with Pydantic v2, Tortoise ORM with MySQL Database

    ## Setup

    ### Prerequisites
    - Python 3.8 or higher
    - MySQL database

    ### Installation

    1. Clone the repository:
    ```
    git clone <repository-url>
    cd fastapi-tortoise-mysql
    ```

    2. Create a virtual environment:
    ```
    python -m venv venv
    ```

    3. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source venv/bin/activate
        ```

    4. Install the required libraries:
    ```
    pip install -r requirements.txt
    ```

    5. Set up environment variables:
    Create a `.env` file in the root directory and add your database URL:
    ```
    DATABASE_URL=mysql://user:password@localhost:3306/database_name
    ```

    6. Run database migrations:
    ```
    aerich upgrade
    ```

    7. Start the application:
    ```
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

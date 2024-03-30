# flask-book-api

## Installation

1. Clone the repository:
git clone https://github.com/mrdhirajbhosale/flask-book-api

2. Navigate to the project directory:
cd flask-book-api

3. Install dependencies:
pip install -r requirements.txt


## Usage

1. Start the Flask application:
python app.py


2. Use Postman or curl to interact with the API endpoints.

### Endpoints

- **POST /api/login** - Authenticate and receive a JWT token. Default username/password: admin/admin.
- **POST /api/books** - Create a new book. Requires JWT token.
- **GET /api/books** - Retrieve books. Supports filtering by author and publisher. Requires JWT token.
- **DELETE /api/books/{id}** - Delete a book by ID. Requires JWT token.

### Token Authentication

To access protected endpoints, you need to obtain a JWT token by sending a POST request to `/api/login` with the default username and password.

Example:
POST /api/login
Body: {"username": "admin", "password": "admin"}


The token received in the response should be included in the Authorization header of subsequent requests as `'Bearer <token>'`.

## Configuration

- **SECRET_KEY**: Set a secret key for JWT token generation. Update it in `app.py` and `auth.py`.
- **SQLALCHEMY_DATABASE_URI**: SQLite database URI. Change it in `app.py` if needed.

## Default Username/Password

- Username: admin
- Password: admin

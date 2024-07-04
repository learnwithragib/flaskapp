# README.md
# Groqbook

Groqbook is a Flask-based web application that allows users to generate book outlines using the Groq AI API. Users can register, log in, create books, and view their generated book outlines.

## Features

- User registration and authentication
- Book generation using Groq AI API
- View and manage generated books
- Responsive design using Bootstrap

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/groqbook.git
   cd groqbook
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Groq API key and secret key:
   ```
   GROQ_API_KEY=your_groq_api_key
   SECRET_KEY=your_secret_key
   ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   python run.py
   ```

7. Open your web browser and navigate to `http://localhost:5000` to use the application.

## Usage

1. Register a new account or log in to an existing account.
2. Click on "Create Book" to generate a new book outline.
3. Enter a book title and click "Generate Book" to create a new book outline.
4. View your generated books on the "My Books" page.
5. Click on a book title to view its full outline.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

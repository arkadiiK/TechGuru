# Tech Guru Django App

## Overview

This is a basic Django web application for managing products in an online shop.

## Prerequisites

Before you start, make sure you have the following installed:

- Python (3.8 or newer)
- Django

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/arkadiiK/TechGuru.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd TechGuru
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Database Setup**

    - Open `settings.py` in your `TechGuru` folder.
    - Configure the database settings according to your preference (default is SQLite).

2. **Static Files**

    - Make sure you have configured the static files in `settings.py`.

## Running the App

1. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser (Optional)**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

3. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

4. **Access the App**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the app.

    - Products List: `http://127.0.0.1:8000/`
    - Add Product: `http://127.0.0.1:8000/add-product/`
    - Login: `http://127.0.0.1:8000/login/`
    - Register: `http://127.0.0.1:8000/register/`

## Usage

- Navigate to the Products List to view existing products.
- Use the Add Product page to add new products to the shop.
- Login to access protected areas (if you have created a superuser/admin account).

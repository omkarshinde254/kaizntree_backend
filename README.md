# kaizntree_backend

This Django project provides a RESTful API for managing categories, items, and user authentication in an e-commerce application.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/django-e-commerce-api.git
    ```

2. Navigate into the project directory:

    ```
    cd django-e-commerce-api
    ```

3. Create a virtual environment:

    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

    - On Windows:

    ```
    venv\Scripts\activate
    ```

5. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```
    python manage.py migrate
    ```

7. Start the development server:

    ```
    python manage.py runserver
    ```

## Usage

### Endpoints

-   **Register**: `POST /register/`

    -   Create a new user account.

-   **Login**: `POST /login/`

    -   Authenticate user and generate JWT token for subsequent requests.

-   **User Profile**: `GET /user/`

    -   Retrieve user profile information.

-   **Logout**: `POST /logout/`

    -   Log out user and invalidate JWT token.

-   **Category Count**: `GET /category/count/`

    -   Retrieve count of categories.

-   **Item Count**: `GET /item/count/`

    -   Retrieve count of items.

-   **Create Category**: `POST /category/create/`

    -   Create a new category.

-   **Create Item**: `POST /item/create/`

    -   Create a new item.

-   **List Categories**: `GET /category/list/`

    -   Retrieve a list of categories.

-   **List Items**: `GET /item/list/`

    -   Retrieve a list of items.

-   **Filter Categories**: `GET /filter/category/?category=category_name`

    -   Filter categories by name.

-   **Filter Items**: `GET /filter/item/?sku=sku&name=name&tags=tags&category=category&in_stock=in_stock&available=available`
    -   Filter items by SKU, name, tags, category, in stock status, and availability.

### Authentication

-   JWT (JSON Web Token) is used for authentication.
-   When a user logs in, a JWT token is generated and provided in the response.
-   The token should be included in the Authorization header of subsequent requests as `Bearer <token>`.

## Deployed Version

This API is deployed on Vercel at [https://kaizntree-backend.vercel.app/](https://kaizntree-backend.vercel.app/).

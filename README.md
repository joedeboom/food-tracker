# Food Product Tracker

Food Product Tracker is a web application that lets you track food products by entering their barcodes. It retrieves product details from the Open Food Facts API, saves the information to an SQL database, and displays a searchable list of products.

## Features

- **Barcode Input:** Easily input product barcodes.
- **API Integration:** Fetches detailed product data from the [Open Food Facts API](https://world.openfoodfacts.org/).
- **Data Persistence:** Saves product information using SQLAlchemy.
- **Responsive Interface:** Displays products in a user-friendly layout.

## Project Structure

```
food-product-tracker
├── .gitignore
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── database.py          # Handles database connections and operations
│   ├── food_data.py         # Fetches product data from the Open Food Facts API
│   ├── models.py            # Defines the SQLAlchemy models (e.g. [`Product`](app/models.py))
│   ├── routes.py            # Defines application routes, including detail and delete routes (see [`main.product_detail`](app/routes.py))
│   ├── utils.py             # Utility functions (e.g. [`product_tuple_to_dict`](app/utils.py))
│   ├── static               # Contains static assets
│   │   ├── css
│   │   │   └── style.css    # Styles for the application
│   │   └── js
│   │       └── main.js      # JavaScript for client-side interactivity
│   └── templates            # Contains HTML templates for the application
│       ├── base.html        # Base HTML template
│       ├── index.html       # Homepage template displaying the product list
│       ├── product_detail.html  # Detailed product view template
│       └── error.html       # Error page template
├── config.py                # Configuration settings for the application
├── products.db              # SQLite database file for storing product information
├── README.md                # Project documentation
├── requirements.txt         # Lists project dependencies
└── run.py                   # Application entry point
```

## Recommended for MacOS: Install Homebrew, python and pip
1. Install Homebrew:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install python using Homebrew, which also inlcudes pip:
    ```
    brew install python
    ```

## Installation
1. Navigate to a directory of your preference:
   ```
   mkdir ~/projects
   cd ~/projects
   ```

2. Create a python virtual environment and activate it:

   **For Linux and macOS:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   **For Windows (Command Prompt):**
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. Clone the repository and navigate into it:
   ```
   git clone https://github.com/joedeboom/food-tracker.git
   cd food-tracker
   ``` 

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python run.py
   ```

6. Open your web browser and navigate to `http://127.0.0.1:51515` to access the application.

## Usage

- Enter a barcode in the input field and submit the form to fetch product details.
- The product information will be saved in the database and displayed on the homepage.


## Roadmap

- Add search, sorting, and filtering functionality of products in the database.
- Add camera functionality to scan real barcodes.
- Generate shopping lists from previously scanned products.

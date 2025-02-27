# Food Product Tracker

Food Product Tracker is a web application that lets you track food products by entering their barcodes. It retrieves product details from the Open Food Facts API, saves the information to a SQLite database, and displays a searchable list of products.

## Features

- **Barcode Input:** Easily input product barcodes.
- **API Integration:** Fetches detailed product data from the [Open Food Facts API](https://world.openfoodfacts.org/).
- **Data Persistence:** Saves product information using SQLite.
- **Responsive Interface:** Displays products in a user-friendly layout.

## Project Structure

```
food-product-tracker
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── database.py          # Handles database connections and operations
│   ├── food_data.py         # Fetches product data from the API
│   ├── routes.py            # Defines application routes
│   └── templates            # Contains HTML templates
│       ├── base.html        # Base template for the application
│       └── index.html       # Main template for the homepage
├── static                   # Contains static files (CSS, JS)
│   ├── css
│   │   └── style.css        # Styles for the application
│   └── js
│       └── main.js          # JavaScript for client-side interactivity
├── config.py                # Configuration settings for the application
├── requirements.txt         # Lists project dependencies
├── run.py                   # Entry point to run the application
├── products.db              # SQLite database file for storing product information
└── README.md                # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd food-product-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python run.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

- Enter a barcode in the input field and submit the form to fetch product details.
- The product information will be saved in the database and displayed on the homepage.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

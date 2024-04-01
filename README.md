# Premier League Match Statistics Scraper

This Python script is designed to scrape match statistics from the Premier League website using Selenium, a web scraping library. It retrieves data such as possession, shots on target, shots, touches, passes, tackles, clearances, corners, offsides, yellow cards, and fouls conceded for each match.

## Features

- Utilizes Selenium WebDriver for web scraping.
- Extracts detailed match statistics from the Premier League website.
- Formats the extracted data into a structured format using Pandas DataFrames.
- Saves the formatted data into CSV files for further analysis or storage.

## Installation

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/yourusername/premier-league-stats-scraper.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd premier-league-stats-scraper
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Ensure you have Python installed on your system.**
2. **Run `import_selenium.py` to scrape match statistics from the Premier League website:**

    ```bash
    python import_selenium.py
    ```

3. **The extracted data will be saved in CSV format in the project directory.**

## Notes

- This project is intended for educational purposes and should be used responsibly and in compliance with the terms of use of the Premier League website.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

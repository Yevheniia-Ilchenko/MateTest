# MateTest Web Scraper
This project is a web scraper that uses Selenium to extract information about courses from the landing page of the Mate Academy website. The scraper gathers the following information for each course:

- Course name
- Short description
- Course type (full-time or flex)

Additionally, the scraper extracts the following details for each course:

- Number of Modules
 - Number of Topics
- Course Duration

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

 - Python 3.x
 - Google Chrome
 - ChromeDriver (Ensure the version matches your installed Chrome browser)

You can install the necessary Python packages using the requirements.txt file provided.

### Installation

- Clone the repository:
```
git clone https://github.com/Yevheniia-Ilchenko/MateTest.git
```

- Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Install the required Python packages:

```
pip install -r requirements.txt
```

### Usage

To run the scraper, execute the following command:
```
python manage.py
```
### Notes
- Ensure that the version of ChromeDriver matches the installed version of Google Chrome.
- The script uses a headless browser to avoid opening a GUI window during scraping.
- Adjust the CSS selectors if the website's structure changes.

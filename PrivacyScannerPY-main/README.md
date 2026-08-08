# Privacy Scanner

Privacy Scanner is a simple Python tool that analyzes a website for privacy-related elements such as cookies, trackers, scripts, and HTTPS security. It generates a privacy score and grade based on the detected elements.

## Features

* Detects cookies used by a website
* Identifies common trackers (Google Ads, Facebook Pixel, etc.)
* Checks if the website uses HTTPS
* Calculates a privacy score
* Assigns a privacy grade

## Requirements

* Python 3.8 or higher
* Firefox browser
* GeckoDriver
* Required Python packages

Install dependencies:

```
pip install selenium requests beautifulsoup4 streamlit
```

Download GeckoDriver and add it to your system PATH.

GeckoDriver download:
https://github.com/mozilla/geckodriver/releases

## Project Structure

```
PrivacyScanner/
│
├── main.py
├── trackers.json
└── README.md
```

## How to Run

1. Open terminal in the project folder

2. Run the scanner

```
streamlit run main.py
```

3. Enter the website URL when prompted

Example:

```
Enter website URL: https://example.com
```

## Example Output

```
Total 41 cookies found

Trackers found:
[
0: "Google Ads"
]

HTTPS: Secure

Privacy Score: 50
Privacy Grade: C
```

## Privacy Score System

Score is calculated based on:

* Number of cookies
* Presence of trackers
* HTTPS security

Grade scale:

```
90 – 100 : A
80 – 89  : B
70 – 79  : C
60 – 69  : D
Below 60 : F
```

## Disclaimer

This tool provides a basic privacy analysis and should not be considered a complete security audit. It only detects known trackers and visible cookies.

## License

This project is open source and free to use.

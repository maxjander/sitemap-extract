# Sitemap Title Fetcher

This Python script downloads a sitemap in XML format, extracts URLs, fetches each page, and collects the titles from each page. The results are saved in both Excel and CSV formats.

## Requirements

- Python 3.12.4  
  **Note:** The script has only been tested with this version of Python.

### Python Libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `lxml` (used for XML parsing with `ElementTree`)

## Use Case

This script is useful for fetching and analyzing page titles from a sitemap. It can be applied in SEO audits, content inventory, or just checking titles for consistency across a site.

## Installation

### Step 1: Create a virtual environment using `.python-version`

If you use **pyenv** and have a `.python-version` file with `3.12.4` in your project, you can create and activate a virtual environment with the following commands:

```bash
# Install the correct Python version (if using pyenv)
pyenv install 3.12.4

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# Or on Windows:
# .\venv\Scripts\activate
```

### Step 2: Install the required libraries

After activating the virtual environment, install the required libraries:

```bash
pip install -r requirements.txt
```

You can generate the `requirements.txt` file if it’s not already provided by running:

```bash
pip freeze > requirements.txt
```

### Step 3: Running the Script

You can run the script with the following command:

```bash
python script_name.py --sitemap <SITEMAP_URL> --count <NUMBER_OF_URLS> --output <OUTPUT_FILENAME>
```

- `--sitemap`: The URL of the sitemap to fetch from (required).
- `--count`: Number of URLs to fetch (default is 10).
- `--all`: Fetch all URLs from the sitemap (use this flag if you want to fetch all).
- `--output`: Output file name without extension (default is "sitemap_titles").

Example:

```bash
python script_name.py --sitemap https://example.com/sitemap.xml --count 20 --output my_titles
```

This will fetch titles from the first 20 URLs in the sitemap and save them as `my_titles.xlsx` and `my_titles.csv`.

### Output Files

The script generates two files:

- An Excel file (`.xlsx`)
- A CSV file (`.csv`)

Both files will contain columns for the URL, the site title, and the page title.

### Random Delay to Avoid Detection

To minimize the risk of being detected as a bot or overwhelming the server, the script adds a **random delay** between each request. The delay is randomly chosen between **0 and 0.5 seconds**. This ensures that requests are spaced out and the script behaves more like a human browsing the website.

```python
# Delay between each request (0–0.5 seconds)
sleep_time = random.uniform(0, 0.5)
time.sleep(sleep_time)
```

This makes the script safer to run and less likely to be flagged by the website's server.

## Notes

- The script adds a random delay (between 0–0.5 seconds) between requests to avoid overloading the server.
- The sitemap XML must follow the standard sitemap format.

Enjoy fetching your titles!

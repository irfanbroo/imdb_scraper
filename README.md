# IMDb Movie Scraper 🎬

## Overview

Timport csv

from colorama import Fore, Style

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected\_conditions as EC

import time



\# Setting up Selenium WebDriver

option = webdriver.ChromeOptions()

\#option.add\_argument("--headless")    (uncommenting this will prevent the browser from opening up) &#x20;

driver = webdriver.Chrome(options=option)



\# Function to search for a movie on IMDb

def search\_imdb(movie\_title):

&#x20;   search\_url = "https\://www\.imdb.com/"

&#x20;   driver.get(search\_url)



&#x20;   try:

&#x20;       \# searching for the search box for the inputs&#x20;

&#x20;       search\_box = driver.find\_element(By.XPATH, "//\*[@id='suggestion-search']")

&#x20;       search\_box.send\_keys(movie\_title)

&#x20;       search\_box.send\_keys(Keys.RETURN)



&#x20;       \# Waiting for search results

&#x20;       WebDriverWait(driver, 8).until(

&#x20;           EC.presence\_of\_element\_located((By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]"))

&#x20;       )



&#x20;       \# Get first search result ( i noticed some issues where if the first search result is an upcomming movie,then the review fetching gets a bit messed up)

&#x20;       first\_result = driver.find\_element(By.XPATH, "(//li[contains(@class, 'ipc-metadata-list-summary-item')])[1]")



&#x20;       \# ✅ Extract movie link

&#x20;       movie\_link = first\_result.find\_element(By.XPATH, ".//a[contains(@href, '/title/')]").get\_attribute("href")



&#x20;       \#  Extracting Movie ID from URL (format: /title/tt1234567/)

&#x20;       return movie\_link.split("/")[4]



&#x20;   except Exception as e:

&#x20;       print(f"Error finding movie: {e}")

&#x20;  &#x20;

&#x20;   return None



\# Function to scrape movie details

def scrape\_movie(movie\_id):

&#x20;   movie\_url = f"https\://www\.imdb.com/title/{movie\_id}"

&#x20;   driver.get(movie\_url)



&#x20;   \# Wait for title to load

&#x20;   WebDriverWait(driver, 6).until(EC.presence\_of\_element\_located((By.TAG\_NAME, "h1")))



&#x20;   title = driver.find\_element(By.TAG\_NAME, "h1").text.strip()





&#x20;   \# Extracting rating

&#x20;   try:

&#x20;       rating\_elem = driver.find\_element(By.CSS\_SELECTOR, "div[data-testid='hero-rating-bar\_\_aggregate-rating'] span")

&#x20;       rating = rating\_elem.text.strip().split("\n")[0]

&#x20;   except:

&#x20;       rating = "N/A"



&#x20;   return title, rating



\# Function to scrape reviews

def scrap\_review(movie\_id):

&#x20;   reviews\_url = f"https\://www\.imdb.com/title/{movie\_id}/reviews"

&#x20;   driver.get(reviews\_url)



&#x20;   try:

&#x20;       WebDriverWait(driver, 5).until(

&#x20;           EC.presence\_of\_element\_located((By.TAG\_NAME, "body"))

&#x20;       )



&#x20;      &#x20;

&#x20;       review\_elements = driver.find\_elements(By.XPATH, "//div[contains(@class, 'text')]")





&#x20;       if not review\_elements:

&#x20;           return ["No reviews found"] &#x20;



&#x20;       reviews = []

&#x20;       for review in review\_elements[:5]:  # Getting first 5 reviews

&#x20;           try:

&#x20;               review\_txt = driver.execute\_script("return arguments[0].textContent;", review).strip()

&#x20;               if review\_txt.lower () != "user reviews":

&#x20;                   reviews.append(review\_txt)

&#x20;           except:

&#x20;               continue  # skipping if no text found



&#x20;       return reviews if reviews else ["No reviews found"]



&#x20;   except Exception as e:

&#x20;       print(f"Error while scraping reviews: {e}")

&#x20;       return ["No reviews found"]



\# Main execution

movie\_title = input("Enter the name of the movie: ")

movie\_id = search\_imdb(movie\_title)



if movie\_id:

&#x20;   title, rating = scrape\_movie(movie\_id)

&#x20;   reviews = scrap\_review(movie\_id)



&#x20;   \# Lets save it to a file&#x20;

&#x20;   file\_name = f"{title.replace(' ','\_')}\_imdb.txt"



&#x20;   with open(file\_name, "w", encoding="utf-8") as file:

&#x20;       file.write(f"🎬  Movie: {title}\n")

&#x20;       file.write(f"⭐  IMDb Rating: {rating}/10\n\n")

&#x20;       file.write("📝  Top 5 Reviews:\n")

&#x20;       file.write("-----------------------------------\n")

&#x20;       for review in reviews:

&#x20;           file.write(f"💬  {review}\n")

&#x20;       file.write("-----------------------------------\n")

&#x20;  &#x20;

&#x20;  &#x20;

&#x20;  &#x20;

&#x20;   \# Display time

&#x20;   print(Fore.CYAN + "\n🎬  Movie: " + Fore.YELLOW + title + Style.RESET\_ALL)

&#x20;   print(Fore.GREEN + "⭐  IMDb Rating: " + Fore.YELLOW + rating + "/10" + Style.RESET\_ALL)



&#x20;   print(Fore.MAGENTA + "\n📝  Top 5 Reviews:" + Style.RESET\_ALL)

&#x20;   print(Fore.WHITE + "-----------------------------------" + Style.RESET\_ALL)

&#x20;   for i, review in enumerate(reviews[:5], start=1):

&#x20;       print(Fore.LIGHTBLUE\_EX + f"💬  {review}" + Style.RESET\_ALL)

&#x20;   print(Fore.WHITE + "-----------------------------------" + Style.RESET\_ALL)







else:

&#x20;   print("Movie not found.")



driver.quit()🚀 Features

✅ **Automated Movie Search** – Searches IMDb and extracts the most relevant result.
✅ **Scrapes IMDb Rating** – Retrieves the official IMDb rating.
✅ **Extracts Top 5 User Reviews** – Gathers reviews for better insights into the movie.
✅ **Saves Data to a TXT File** – Automatically stores movie details in a neatly formatted file.
✅ **Terminal Output with Colors** – Uses `colorama` for better readability in the console.
✅ **Headless Mode Support** – Runs without opening a browser for a smooth experience.

---

## 🛠 Technologies Used

### 🔹 **Selenium** (Web Scraping)

[Selenium](https://www.selenium.dev/) is a powerful tool for automating web browsers. It is commonly used for:

- Web scraping
- Automating repetitive browser tasks
- Testing web applications

This script uses **Selenium WebDriver** to:

- Open IMDb in a browser
- Search for a movie title
- Navigate to the movie’s page
- Extract relevant details (title, rating, and reviews)

### 🔹 **Colorama** (Enhanced Terminal Output)

[Colorama](https://pypi.org/project/colorama/) adds color and style to the terminal output, making it visually appealing.

### 🔹 **Python** (Core Scripting Language)

This project is written in Python and leverages its built-in features for efficiency and ease of use.

---

## 📜 Installation Guide

### Step 1️⃣: Clone the Repository

```sh
git clone https://github.com/yourusername/imdb-movie-scraper.git
cd imdb-movie-scraper
```

### Step 2️⃣: Install Dependencies

Ensure you have Python installed, then install the required libraries using:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
selenium
colorama
```

### Step 3️⃣: Setup Selenium WebDriver

You need to have **Google Chrome** and **ChromeDriver** installed. Download the appropriate **ChromeDriver** for your browser version from [here](https://chromedriver.chromium.org/downloads) and place it in your system's PATH or project folder.

### Step 4️⃣: Run the Script

```sh
python imdb_scraper.py
```

---

## 📌 How to Use

1️⃣ Run the script and **enter a movie name** when prompted.
2️⃣ The script will search IMDb and retrieve the **best match**.
3️⃣ The **IMDb rating** and **top 5 user reviews** will be displayed.
4️⃣ The results will also be saved in a `.txt` file.

Example output in the terminal:

```
🎬  Movie: Inception
⭐  IMDb Rating: 8.8/10

📝  Top 5 Reviews:
-----------------------------------
💬  "A mind-bending masterpiece!"
💬  "Nolan’s best work."
💬  "A movie that requires multiple watches."
💬  "Fantastic visuals and story!"
💬  "A sci-fi film like no other."
-----------------------------------
```

A text file named `Inception_imdb.txt` will also be created with the same details.

---

## 🚨 Troubleshooting

### Issue 1️⃣: Selenium WebDriver Error

**Solution:** Ensure you have the correct version of ChromeDriver matching your browser version.

### Issue 2️⃣: `chromedriver` Not Found

**Solution:** Add ChromeDriver to your system’s PATH or specify the exact path in the script:

```python
driver = webdriver.Chrome(executable_path="/path/to/chromedriver", options=option)
```

### Issue 3️⃣: No Reviews Found

**Solution:** Some movies may not have user reviews on IMDb. Try another movie title.

---

## 🚀 Future Enhancements

🔹 **CSV Output Support** – Save movie details in a structured format.
🔹 **Multiple Movie Search** – Allow batch searching.
🔹 **GUI Interface** – Develop a simple UI for non-technical users.
🔹 **Better Review Filtering** – Exclude irrelevant or duplicate reviews.

---

## 🤝 Contributing

1️⃣ Fork the repo
2️⃣ Create a new branch (`git checkout -b feature-branch`)
3️⃣ Commit your changes (`git commit -m "Added new feature"`)
4️⃣ Push to your branch (`git push origin feature-branch`)
5️⃣ Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – you are free to modify and distribute it.

---

## 🌟 Acknowledgments

🎉 Thanks to **Selenium** and **IMDb** for making this project possible! Happy Scraping! 🚀


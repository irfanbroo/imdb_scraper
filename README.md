# IMDb Movie Scraper 🎬

Use this for scrapping imdb for reviews and ratings, this scipt uses selenium because Selenium acts as a browser automation tool, enabling us to interact with the IMDb website just like a real user would. Many websites try to block scrapers by requiring JavaScript execution. Selenium, running a real browser, makes our scraper appear as a legitimate user. 

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


import csv
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up Selenium WebDriver
option = webdriver.ChromeOptions()
option.add_argument("--headless")  #  you can comment this out to see how this works 
driver = webdriver.Chrome(options=option)

# Function to search for a movie on IMDb
def search_imdb(movie_title):
    search_url = "https://www.imdb.com/"
    driver.get(search_url)

    try:
        # searching for the search box for the inputs 
        search_box = driver.find_element(By.XPATH, "//*[@id='suggestion-search']")
        search_box.send_keys(movie_title)
        search_box.send_keys(Keys.RETURN)

        # Waiting for search results
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]"))
        )

        # Get first search result ( i noticed some issues where if the first search result is an upcomming movie,then the review fetching gets a bit messed up)
        first_result = driver.find_element(By.XPATH, "(//li[contains(@class, 'ipc-metadata-list-summary-item')])[1]")

        # ✅ Extract movie link
        movie_link = first_result.find_element(By.XPATH, ".//a[contains(@href, '/title/')]").get_attribute("href")

        #  Extracting Movie ID from URL (format: /title/tt1234567/)
        return movie_link.split("/")[4]

    except Exception as e:
        print(f"Error finding movie: {e}")
    
    return None

# Function to scrape movie details
def scrape_movie(movie_id):
    movie_url = f"https://www.imdb.com/title/{movie_id}"
    driver.get(movie_url)

    # Wait for title to load
    WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    title = driver.find_element(By.TAG_NAME, "h1").text.strip()


    # Extracting rating
    try:
        rating_elem = driver.find_element(By.CSS_SELECTOR, "div[data-testid='hero-rating-bar__aggregate-rating'] span")
        rating = rating_elem.text.strip().split("\n")[0]
    except:
        rating = "N/A"

    return title, rating

# Function to scrape reviews
def scrap_review(movie_id):
    reviews_url = f"https://www.imdb.com/title/{movie_id}/reviews"
    driver.get(reviews_url)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        
        review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'text')]")


        if not review_elements:
            return ["No reviews found"]  

        reviews = []
        for review in review_elements[:5]:  # Getting first 5 reviews
            try:
                review_txt = driver.execute_script("return arguments[0].textContent;", review).strip()
                if review_txt.lower () != "user reviews":
                    reviews.append(review_txt)
            except:
                continue  # skipping if no text found

        return reviews if reviews else ["No reviews found"]

    except Exception as e:
        print(f"Error while scraping reviews: {e}")
        return ["No reviews found"]

# Main execution
movie_title = input("Enter the name of the movie: ")
movie_id = search_imdb(movie_title)

if movie_id:
    title, rating = scrape_movie(movie_id)
    reviews = scrap_review(movie_id)

    # Lets save it to a file 
    file_name = f"{title.replace(' ','_')}_imdb.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"🎬  Movie: {title}\n")
        file.write(f"⭐  IMDb Rating: {rating}/10\n\n")
        file.write("📝  Top 5 Reviews:\n")
        file.write("-----------------------------------\n")
        for review in reviews:
            file.write(f"💬  {review}\n")
        file.write("-----------------------------------\n")
    
    
    
    # Display time
    print(Fore.CYAN + "\n🎬  Movie: " + Fore.YELLOW + title + Style.RESET_ALL)
    print(Fore.GREEN + "⭐  IMDb Rating: " + Fore.YELLOW + rating + "/10" + Style.RESET_ALL)

    print(Fore.MAGENTA + "\n📝  Top 5 Reviews:" + Style.RESET_ALL)
    print(Fore.WHITE + "-----------------------------------" + Style.RESET_ALL)
    for i, review in enumerate(reviews[:5], start=1):
        print(Fore.LIGHTBLUE_EX + f"💬  {review}" + Style.RESET_ALL)
    print(Fore.WHITE + "-----------------------------------" + Style.RESET_ALL)



else:
    print("Movie not found.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_instagram(username, limit=20):

    driver = webdriver.Chrome()

    driver.get("https://www.instagram.com/")
    print("Log into Instagram manually...")
    time.sleep(20)

    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(5)

    posts = driver.find_elements(By.CSS_SELECTOR, "article a")

    captions = []

    for post in posts[:limit]:

        post.click()
        time.sleep(3)

        try:
            caption = driver.find_element(By.CSS_SELECTOR, "h1").text
            captions.append(caption)
        except:
            pass

        driver.back()
        time.sleep(2)

    driver.quit()

    return captions


if __name__ == "__main__":

    username = "instagram_username_here"

    data = scrape_instagram(username)

    with open("scraped_posts.txt", "w", encoding="utf-8") as f:
        for post in data:
            f.write(post + "\n")

    print("Posts saved to scraped_posts.txt")
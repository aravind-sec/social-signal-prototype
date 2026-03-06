from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_instagram(username, limit=20):

    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\aravi\AppData\Local\Microsoft\Edge\User Data")
    options.add_argument("profile-directory=Default")

    driver = webdriver.Edge(options=options)

    driver.get(f"https://www.instagram.com/{username}/")

    wait = WebDriverWait(driver, 15)

    posts = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article a"))
    )

    print("Posts detected:", len(posts))

    post_links = []

    for post in posts[:limit]:
        link = post.get_attribute("href")
        post_links.append(link)

    captions = []

    for link in post_links:

        driver.get(link)
        time.sleep(3)

        try:
            caption = driver.find_element(By.CSS_SELECTOR, "h1").text
            captions.append(caption)
        except:
            try:
                caption = driver.find_element(By.CSS_SELECTOR, "div._a9zs").text
                captions.append(caption)
            except:
                pass

    driver.quit()

    return captions


if __name__ == "__main__":

    username = "natgeo"

    data = scrape_instagram(username)

    with open("scraped_posts.txt", "w", encoding="utf-8") as f:
        for post in data:
            f.write(post + "\n")

    print("Posts saved to scraped_posts.txt")
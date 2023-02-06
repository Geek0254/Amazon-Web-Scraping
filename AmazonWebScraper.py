from bs4 import BeautifulSoup
from selenium import webdriver

def get_product_info(product_name):
    # Initialize a headless browser
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    browser = webdriver.Firefox(options=options)

    # Make a GET request to the Amazon website using Selenium
    browser.get(f"https://www.amazon.com/s?field-keywords={product_name}")

    # Parse the HTML content of the search results page
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # Find all the product cards on the page
    product_cards = soup.find_all("div", class_="s-result-item")

    # Create a list to store the product information
    products = []

    # Loop through each product card
    for card in product_cards:
        # Get the product title
        title_element = card.find("span", class_="a-size-medium a-color-base a-text-normal")
        title = title_element.text if title_element else ""

        # Get the product link
        link_element = card.find("a", class_="s-underline-text")
        link = "https://www.amazon.com" + link_element["href"] if link_element else ""

        # Get the product price
        price_element = card.find("span", class_="a-offscreen")
        price = price_element.text if price_element else ""

        # Get the product rating
        rating_element = card.find("span", class_="a-icon-alt")
        rating = rating_element.text if rating_element else ""

        # Add the product information to the list
        products.append({
            "title": title,
            "price": price,
            "rating": rating,
            "link": link
        })

    browser.quit()
    return products

def main():
    # Get the product name from the user
    product_name = input("Enter the product name: ")

    # Get the product information
    products = get_product_info(product_name)

    # Print the product information
    if products:
        for product in products:
            print(f"Title: {product['title']}")
            print(f"Price: {product['price']}")
            print(f"Rating: {product['rating']}")
            print(f"Link: {product['link']}\n")
    else:
        print("No products found")

if __name__ == "__main__":
    main()

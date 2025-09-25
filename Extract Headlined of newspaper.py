import requests
from bs4 import BeautifulSoup

def fetch_india_today_headlines():
    url = "https://www.indiatoday.in/top-stories"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    # Step 1: Fetch the page
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f" Failed to retrieve the page. Status code: {response.status_code}")
        return

    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find headline elements
    headlines = soup.find_all('h2')

    # Step 4: Extract and clean text
    top_headlines = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]
    top_headlines = top_headlines[:10]  # Limit to top 10

    # Step 5: Print headlines
    print("\nTop India Today Headlines:\n")
    for i, text in enumerate(top_headlines, start=1):
        print(f"{i}. {text}")

    # Step 6: Save to file
    with open("india_today_headlines.txt", "w", encoding="utf-8") as file:
        for i, text in enumerate(top_headlines, start=1):
            file.write(f"{i}. {text}\n")

    print("\n Headlines saved to 'india_today_headlines.txt'")

# Run the function
fetch_india_today_headlines()
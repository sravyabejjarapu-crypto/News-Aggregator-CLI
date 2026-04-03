import requests
import pandas as pd

API_KEY = "15ed2edba2b44b28b95af0b1cecce632"
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(country="us", category=None):
    params = {
        "apiKey": API_KEY,
        "country": country
    }

    if category:
        params["category"] = category

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching news:", response.json())
        return []

    data = response.json()
    return data.get("articles", [])


def filter_news(articles, keyword=None):
    if not keyword:
        return articles

    filtered = []
    for article in articles:
        if keyword.lower() in (article["title"] or "").lower():
            filtered.append(article)
    return filtered


def save_to_csv(articles):
    news_list = []

    for article in articles:
        news_list.append({
            "Title": article["title"],
            "Source": article["source"]["name"],
            "Published At": article["publishedAt"],
            "URL": article["url"]
        })

    df = pd.DataFrame(news_list)
    df.to_csv("news_output.csv", index=False)
    print("✅ News saved to news_output.csv")


def display_news(articles):
    if not articles:
        print("No news found!")
        return

    for i, article in enumerate(articles, start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Date: {article['publishedAt']}")
        print(f"   URL: {article['url']}")


def main():
    print("📰 News Aggregator CLI")

    country = input("Enter country code (us/in/gb): ").strip()
    category = input("Enter category (business/technology/sports) or press Enter: ").strip()
    keyword = input("Enter keyword to filter or press Enter: ").strip()

    articles = fetch_news(country, category if category else None)
    articles = filter_news(articles, keyword if keyword else None)

    display_news(articles)

    save_option = input("\nDo you want to save results to CSV? (yes/no): ").strip().lower()
    if save_option == "yes":
        save_to_csv(articles)


if __name__ == "__main__":
    main()
    #CALL FUNCTIONS (VERY IMPORTANT)
    articles = fetch_news()
    print("\n---NEWS ARTICLES--\n")

    for article in articles:
        print("Title:",article.get("title"))
        print("Description:",article.get("description"))
        print("-"*50)
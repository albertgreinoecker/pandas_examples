from playwright.sync_api import sync_playwright

def scrape_example():
    # Startet Playwright im synchronen Modus
    with sync_playwright() as p:
        # Browser starten (hier: Chromium, headless)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Webseite laden
        page.goto("https://news.ycombinator.com/")

        # Titel der Seite
        print("Seitentitel:", page.title())

        # Alle Links mit Titel auf der Seite sammeln
        articles = page.query_selector_all("a.storylink, span.titleline > a")

        print("\nArtikel auf der Seite:\n")
        for a in articles:
            title = a.inner_text()
            href = a.get_attribute("href")
            print(f"- {title} ({href})")

        # Browser schließen
        browser.close()

if __name__ == "__main__":
    scrape_example()

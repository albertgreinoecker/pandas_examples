from playwright.sync_api import sync_playwright
import pandas as pd
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def scrape_moodle_courses(username: str, password: str, moodle_url: str):
    """Loggt sich automatisch in Moodle ein und exportiert alle Kurse als CSV."""

    with sync_playwright() as p:
        # Headless = True → kein sichtbares Browserfenster
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login-Seite aufrufen
        login_url = f"{moodle_url.rstrip('/')}/login/index.php"
        page.goto(login_url, wait_until="domcontentloaded")

        # Login-Formular ausfüllen und absenden
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#loginbtn")

        # Auf Dashboard warten (nach erfolgreichem Login)
        page.wait_for_selector(".dashboard-card, .coursebox, .course-summaryitem", timeout=10000)

        # Kurse auslesen
        courses = []
        for selector in [".dashboard-card", ".coursebox", ".course-summaryitem"]:
            for course in page.query_selector_all(selector):
                link_elem = course.query_selector("a")
                if link_elem:
                    name = link_elem.inner_text().strip()
                    href = link_elem.get_attribute("href")
                    if name and href:
                        courses.append({"Kursname": name, "Link": href})

        df = pd.DataFrame(courses)
        print(df.head())

        # Ergebnisse anzeigen
        print(f"{len(courses)} Kurse gefunden.")
        for c in courses:
            print(f"- {c['Kursname']} ({c['Link']})")

        # Export als CSV
        df = pd.DataFrame(courses)
        df.to_csv("moodle_kurse.csv", index=False, encoding="utf-8-sig")

        browser.close()
        print("\n✅ Export abgeschlossen: moodle_kurse.csv")


if __name__ == "__main__":
    # 🧠 Diese Werte anpassen
    scrape_moodle_courses(
        username=os.getenv("MOODLE_USER"),
        password=os.getenv("MOODLE_PASS"),
        moodle_url=os.getenv("MOODLE_URL")
    )

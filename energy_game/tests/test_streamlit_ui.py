from playwright.sync_api import sync_playwright

def test_streamlit_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("http://localhost:8501")

        page.click("text=Start New Game")
        page.click("text=Play Day")

        page.wait_for_selector("text=Leaderboard")

        browser.close()

        print("✔ Streamlit UI basic flow OK")

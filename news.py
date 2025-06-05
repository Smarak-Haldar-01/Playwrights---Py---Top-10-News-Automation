from playwright.sync_api import  sync_playwright
import pandas as pd

def page_pdf_generator(page):
    browser = page.chromium.launch(headless=True)

    page = browser.new_page()


    try:
        page.goto("https://timesofindia.indiatimes.com/india/timestopten.cms", timeout=1200)
    except Exception as E:
        print(E)
    # page.goto("https://foundryco.com/our-solutions/events/")

    contents = page.locator(".news_title").all_inner_texts()

    # print(content)

    json = [

    ]

    for content in contents:

        sub_content = content.split('. ')

        if len(sub_content) == 1:
            continue

        # print(content.split('. '))

        json.append(sub_content[1])

    print(json)

    page.close()

    pd.DataFrame(json).to_csv('top10news.csv')

with sync_playwright() as plywrt:
    page_pdf_generator(plywrt)


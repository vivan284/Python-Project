from selenium import webdriver
import time
import streamlit as st
from urllib.parse import urlparse
import pandas as pd

st.title("Website Privacy Scanner")

url = st.text_input("Enter Website URL")

if st.button("Scan"):

    if url == "":
        st.write("Please enter a URL")

    else:

        if not url.startswith("http"):
            url = "https://" + url

        driver = None

        try:

            with st.spinner("Scanning website..."):

                driver = webdriver.Firefox()
                driver.get(url)

                time.sleep(5)

                cookies = driver.get_cookies()

                tracker_db = {
                "google-analytics": "Google Analytics",
                "googletagmanager": "Google Tag Manager",
                "doubleclick": "Google Ads",
                "facebook.net": "Facebook Pixel",
                "connect.facebook": "Facebook Tracker",
                "hotjar": "Hotjar",
                "mixpanel": "Mixpanel Analytics",
                "segment": "Segment Analytics",
                "matomo": "Matomo Analytics",
                "amplitude": "Amplitude Analytics",
                "quantserve": "Quantcast Tracker",
                "taboola": "Taboola Ads",
                "outbrain": "Outbrain Ads",
                "adservice": "Google Ad Services",
                "adsystem": "Amazon Ads",
                "bing": "Microsoft Ads",
                "linkedin": "LinkedIn Insight Tag",
                "twitter": "Twitter Pixel",
                "tiktok": "TikTok Pixel",
                "pinterest": "Pinterest Tracker",
                "sentry": "Sentry Monitoring",
                "newrelic": "New Relic Monitoring"
                }

                scripts = driver.find_elements("tag name", "script")

                trackers = set()

                for script in scripts:
                    src = script.get_attribute("src")

                    if src:
                        src = src.lower()

                        for key in tracker_db:
                            if key in src:
                                trackers.add(tracker_db[key])

                page_source = driver.page_source.lower()

                for key in tracker_db:
                    if key in page_source:
                        trackers.add(tracker_db[key])

                site_domain = urlparse(url).netloc

                third_party_cookies = []

                for cookie in cookies:
                    cookie_domain = cookie.get("domain")

                    if cookie_domain and site_domain not in cookie_domain:
                        third_party_cookies.append(cookie["name"])

                score = 100

                if len(cookies) > 10:
                    score -= 20

                score -= len(trackers) * 10

                if not url.startswith("https"):
                    score -= 30

                if len(third_party_cookies) > 0:
                    score -= 20

                score = max(score, 0)

                if 80 <= score <= 100:
                    grade = "A"
                elif 60 <= score < 80:
                    grade = "B"
                elif 40 <= score < 60:
                    grade = "C"
                elif 20 <= score < 40:
                    grade = "D"
                else:
                    grade = "F"

                st.subheader("Results")

                st.write("Privacy Score:", score)
                st.write("Privacy Grade:", grade)
                st.write("HTTPS:", "Secure" if url.startswith("https") else "Not Secure")

                st.subheader("Cookie Analysis")

                cookie_data = pd.DataFrame({
                "Type": ["Total Cookies", "Third Party Cookies"],
                "Count": [len(cookies), len(third_party_cookies)]
                })

                st.bar_chart(cookie_data.set_index("Type"))

                st.subheader("Tracker Analysis")

                tracker_data = pd.DataFrame({
                "Metric": ["Trackers Found"],
                "Count": [len(trackers)]
                })

                st.bar_chart(tracker_data.set_index("Metric"))

                st.subheader("Detected Trackers")
                st.write(list(trackers))
                st.write("Thank you! for waiting.")
        except Exception as e:
            st.write("Error scanning the website")
            st.write(e)

        finally:
            if driver:
                driver.quit()
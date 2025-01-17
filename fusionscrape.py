
from playwright.sync_api import sync_playwright
import time

LOGIN_URL = "https://intl.fusionsolar.huawei.com/unisso/login.action?service=%2Funisess%2Fv1%2Fauth%3Fservice%3D%252Fnetecowebext%252Fhome%252Findex.html#/LOGIN"
BATTERY_URL = "https://uni003eu5.fusionsolar.huawei.com/uniportal/pvmswebsite/assets/build/cloud.html?app-id=smartpvms&instance-id=smartpvms&zone-id=region-3-e22df372-3e7c-4ed1-825c-301ee373a36d#/view/device/NE=135108743/battery/details"
BATTERY_STATUS_SELECTOR = '#root > div > div > div > div > div.main-content-wrapper.flex-wrapper.light-content > div.main-content > div > div.nco-device-realtime-page.tab-content > div > div > div > div > div > div > div.other-data-wrapper > div:nth-child(1) > div:nth-child(1) > div > div > div > div > div > div > div:nth-child(10) > div > div.nco-info-card-value-area > span.nco-info-card-value.top-7 > span'

def get_battery_status(username,password):
    battery_status = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True,slow_mo=50)
        page = browser.new_page()
        page.goto(LOGIN_URL)
        page.fill('input#username', username)
        page.fill('input#value', password)
        page.keyboard.press("Enter")

        #New code to bypass the question to join the user experience program
        time.sleep(3)
        page.click('button[type="button"]')
        #end new code to pass the user experience program

        time.sleep(1)
        page.goto(BATTERY_URL)

        page.is_visible('//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[10]')
        html = page.inner_html('//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[10]')
        battery_status = float(html.strip('%'))


    return float(battery_status)




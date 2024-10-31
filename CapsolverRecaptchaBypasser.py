from botasaurus.browser import browser, Driver, cdp
import capsolver
import time

@browser()
def solve(driver : Driver, data):
    capsolver.api_key = data['api_key']

    solution = capsolver.solve({
        "type": "ReCaptchaV2TaskProxyless",
        "websiteURL": data['page_url'],
        "websiteKey": data['page_key'],
    })

    driver.run_cdp_command(cdp.network.set_user_agent_override(
        solution["userAgent"]
    ))

    time.sleep(.1)

    driver.run_js(f"document.getElementById('g-recaptcha-response').value = '{solution['gRecaptchaResponse']}';")

    time.sleep(.1)


def solve_captcha(page_url, page_key, api_key):
    data = {}
    data['page_url'] = page_url
    data['page_key'] = page_key
    data['api_key'] = api_key
    solve(data)
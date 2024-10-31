from CapsolverRecaptchaBypasser import solve_captcha
from botasaurus.browser import Driver
import time

CAPSOLVER_API_KEY = "YOUR_CAPSOLVER_API_KEY"
page_url = "https://google.com/recaptcha/api2/demo"
page_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-" # This can be found in the data-sitekey attribute of the reCaptcha element


print("Solving reCaptcha v2...")
t0 = time.time()
solve_captcha(page_url, page_key, CAPSOLVER_API_KEY)
print( f"Time elapsed: {time.time() - t0:.2f} seconds" )

input("Press Enter to close the browser")


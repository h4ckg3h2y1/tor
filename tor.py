#python3 tor-browser for youtube click player uv
#evry video evry xpath verifier like womendege2
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
import requests
from tbselenium.tbdriver import TorBrowserDriver    
from os.path import dirname, join, realpath, getsize
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#out_img = join(dirname(realpath(__file__)), "screenshot.png")
with TorBrowserDriver("/root/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/") as driver:
# print("----"*100)
# driver.get_screenshot_as_file(out_img)
# print("----"*100)
#print("Screenshot is saved as %s (%s bytes)" % (out_img, getsize(out_img)))
# driver.click()
#time.sleep(30)
   '''
   option = TorBrowserDriver_options()
   option.add_argument("--headless")
   option.add_argument("--disable-gpu")
   option.add_argument('--no-sandbox')
   option.add_argument('--disable-dev-shm-usage')
   driver = driver.TorBrowserDriver(TorBrowserDriver_options=option)

  
   #  driver.load_url('https://www.youtube.com', wait_for_page_body=True)
      search = driver.find_element_by_name('search_query')
      search.send_keys("chessecake")
      search.send_keys(Keys.RETURN)
      time.sleep(5)
      driver.delete_all_cookies()
      time.sleep(5)
   '''
   driver.load_url('https://www.youtube.com/watch?v=d0J4imqRr7Y', wait_for_page_body=True)
   element = WebDriverWait(driver, 35).until(
      EC.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[32]/div[2]/div[1]/button'))
    )
   #time.sleep(5)
   element.click()
   time.sleep(260)#time wait player video
   print(driver.get_cookies())
driver.delete_all_cookies()
time.sleep(15)
driver.quit()

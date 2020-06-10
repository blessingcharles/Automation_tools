import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
        |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
        |                    /              \               0        ___     0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000                                         0
        |                                                                                             0
                                                        --- THE H04X
''',"red" , attrs=["bold" , "underline"])
)


def views():
    driver.get(url)
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    time.sleep(40)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
url = input("ENTER THE URL TO INCREASE VIEWS :")
n = int(input("\n\nENTER THE TIMES TO INCREASE THE VIEWS : "))
try:
    print("\n\n\t\t\t\t\t\tFOR EVERY VIEW TO GET COUNT 30 SEC NEEDED\n\n")
    for i in range(n):
        print(colored(F"\rVIEWS ------->{i}","red"), end="")
        views()
except Exception as e:
    print(e)
    print("\n SOMETHING WENT WRONG")

#driver.close()


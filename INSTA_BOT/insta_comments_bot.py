try:
    from selenium import webdriver
    import time
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import random
    from selenium.webdriver.common.keys import Keys
    from termcolor import colored
except ModuleNotFoundError as e:
    print(e)
    print("install the required modules using pip3")

print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
        |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
        |                    /              \               0        ___     0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000                                         0
        |                                                                                             0



											--- THE H04X
'''
              ,"blue",attrs=["underline" , "bold"]))


class insta_bot():
    def __init__(self):
        self.uname = input(colored("enter your user name :","green"))
        self.passwd = input(colored("\nenter your password: ","green"))
        self.name = input(colored("\n\nenter the victim name :","green"))
        self.comment = input(colored("\nenter the comments :","blue"))
        count = input(colored("\nenter the times :","blue"))
        self.count = int(count)
        post = input(colored("\nenter the position of the post of the post in the victim page:","green"))
        self.post = int(post)
        self.post = self.post - 1;
        self.login()

    def login(self):
        driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(
            self.uname)
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(
            self.passwd)
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        wait = WebDriverWait(driver, 10)
        print(colored(f"\n\n\n[+]llogged in as {self.uname}[+]","red" ))

        note = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
        note.click()
        time.sleep(2)

    def start_bot(self):

        k = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        time.sleep(2)
        action = ActionChains(driver)
        k.send_keys(self.name)
        time.sleep(3)
        # action.double_click(k).perform()
        driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/span").click()
        # accessing the instagram post
        time.sleep(8)
        self.get_image_links()

    def get_image_links(self):

        for i in range(7):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        href_found = driver.find_elements_by_tag_name("a")
        pic_href = [ele.get_attribute('href') for ele in href_found if '.com/p' in ele.get_attribute('href')]
        self.ele = pic_href[self.post]
        self.send_comments()

    def send_comments(self):
        print(colored("\t\t\t\t\tFOR EACH COMMENTS 25 SECONDS WILL BE TAKEN\n\n\n","yellow"))
        for j in range(self.count):
            print(colored(f"\rNO OF COMMENTS COMMENTED -----> {j}","red"),end="")
            time.sleep(20)
            driver.get(self.ele)
            time.sleep(3)
            entry = lambda: driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea")
            entry().click()
            entry().clear()

            for i in self.comment:
                entry().send_keys(i)
                time.sleep(random.randint(1, 7) / 30)

            entry().send_keys(Keys.ENTER)



try:
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    driver = webdriver.Firefox(options=option)
    driver.get("https://www.instagram.com/?hl=en")
    bot = insta_bot()
    bot.start_bot()
except Exception as e :
    print(e)
    print("\n\nSOMETHING WENT WRONG\n\n "
          "\n\nCHECK YOUR INTERNET CONNECTION"
          "ENTER A VALID USERNAME OR PASSWORD\n\n"
          "or enter a valid victim names or post number")
driver.close()

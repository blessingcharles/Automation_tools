try:
    from selenium import webdriver
    import time
    from termcolor import colored
except ModuleNotFoundError as e:
    print(e)
    print("SOME MODULES ARE NOT FOUND\n\ntry install using pip3 ............/ ")

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
  ,"red",attrs=["underline"]))

def bot(name):
    person = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
    person.send_keys(name)
    time.sleep(5)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    send_msg()
    #driver.switch_to.frame("main")Z Z
def send_msg():
    msg_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")
        button.click()

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
names = []
n = int(input(colored("enter the number of user to bot:","green")))
for i in range(0,n):
    ele = input(colored("\nenter the name of user :", "yellow"))
    names.append(ele)
msg = input(colored("\nenter your message :","green"))
count = int(input("\nenter the times :"))
input(colored("\n\n\t\t\t\t\t\t\tpress enter after scanning qr code ....","red"))
time.sleep(3)
for name in names:
    bot(name)

driver.close()



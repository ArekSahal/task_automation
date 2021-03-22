from selenium import webdriver
from time import sleep

def create_github_rep(project_name, cred):

    username = cred[0]
    password = cred[1]

    driver = webdriver.Safari()
    #driver.get("http://github.com/login")
    driver.get("http://github.com/new")

    user_form = driver.find_element_by_id('login_field')
    pass_form = driver.find_element_by_id('password')
    submit = driver.find_element_by_name("commit")
    user_form.send_keys(username)
    pass_form.send_keys(password)
    submit.click()



    #driver.get("http://github.com/new")

    sleep(3)
    rep_name = driver.find_element_by_id('repository_name')
    create = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    sleep(2)
    rep_name.send_keys(project_name)
    sleep(1)
    create.click()

    sleep(2)

    clone_link = driver.find_element_by_id("empty-setup-clone-url")
    git_clone_link = clone_link.get_attribute("value")

    driver.close()

    return git_clone_link
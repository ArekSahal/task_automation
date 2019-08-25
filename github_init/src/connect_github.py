from selenium import webdriver
from time import sleep

def create_github_rep(project_name, cred):

    username = cred[0]
    password = cred[1]

    driver = webdriver.Chrome()
    driver.get("http://github.com/login")

    user_form = driver.find_element_by_id('login_field')
    pass_form = driver.find_element_by_id('password')
    submit = driver.find_element_by_name("commit")
    user_form.send_keys(username)
    pass_form.send_keys(password)
    submit.click()

    driver.get("http://github.com/new")

    rep_name = driver.find_element_by_id('repository_name')
    create = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')

    rep_name.send_keys(project_name)
    sleep(1)
    create.click()

    clone_link = driver.find_element_by_id("empty-setup-clone-url")
    git_clone_link = clone_link.get_attribute("value")

    driver.close()

    return git_clone_link
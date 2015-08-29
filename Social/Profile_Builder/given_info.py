__author__ = 'brekru212'

import csv
from selenium import webdriver

def given_info(info,type_of_info):

    '''
    Given an email address it will link it to other things
    :param type_of_info: someone's information
    :param info: information to create profile
    :return: a profile built from that email
    '''

    if type_of_info == 'email':
        email = info
        peoplesmart = selenium_finder(email, 'peoplesmart', 'https://www.peoplesmart.com/email')
        searchbug = selenium_finder(email, 'searchbug', 'http://www.searchbug.com/peoplefinder/find-people-by-email.aspx#pageTop')
        thatsthem = selenium_finder(email, 'thatsthem', 'http://thatsthem.com/')
        searchtool = selenium_finder(email, 'emailsearchtool', 'http://emailsearchtool.com/')
        facebook = selenium_finder(email, 'facebook', 'https://www.facebook.com/')
        csvFile = email + '.csv'


    elif type_of_info == 'phone':
        phone = info
        searchtool = selenium_finder(phone, 'syncme', 'https://sync.me/')
        peoplesmart = selenium_finder(phone, 'peoplesmart', 'https://www.peoplesmart.com/phone')
        searchbug = selenium_finder(phone, 'searchbug', 'http://www.searchbug.com/peoplefinder/reverse-phone.aspx')
        thatsthem = selenium_finder(phone, 'thatsthem', 'http://thatsthem.com/')
        facebook = selenium_finder(phone, 'facebook', 'https://www.facebook.com/')
        csvFile = phone + '.csv'

    makeCSV = csv.writer(csvFile)
    profileCSV = makeCSV.writerows(facebook,peoplesmart,searchbug,thatsthem,searchtool)
    return profileCSV

def selenium_finder(info,which_website, website):
    '''

    :param info: the info of someone to search
    :param website: the url of the website to search for that person on selenium
    :param which_website: which website am I going through
    :return: the info from the website
    '''
    driver = webdriver.Firefox()

    if which_website == 'peoplesmart':
        website = driver.get(website)
    if which_website == 'searchbug':
        website = driver.get(website)
    if which_website == 'thatsthem':
        website = driver.get(website)
    if which_website == 'emailsearchtool':
        website = driver.get(website)
    if which_website == 'facebook':
        website = driver.get(website)
    if which_website == 'syncme':
        website = driver.get(website)
    return website



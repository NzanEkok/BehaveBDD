from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('launch chrome browser')
def lauchbrowser(context):
    context.driver=webdriver.Chrome(r"C:\Users\Ekok\Desktop\y\drivers\chromedriver.exe")


@when('open test application')
def OpenApp(context):
    context.driver.get("http://192.168.0.123:3000/")


@when('enter First Name "Patrick"')
def firstname(context):
    context.driver.find_element(By.ID, "first-name").send_Keys("Patrick")

@when('enter Middle Name "Ekok"')
def middlename(context):
    context.driver.find_element(By.ID, "middle-name").send_keys("Ekok")


@when('enter Last Name "Nzan"')
def lastname(context):
    context.driver.find_element(By.ID, "last-name").send_keys("Nzan")


@when('enter Phone Number "8093893394"')
def phonenumber(context):
    context.driver.find_element(By.ID, "phone-number").send_keys("8093893394")

@when('Select Date of birth "11/15/2022"')
def dob(context):
    context.driver.find_element(By.ID, "dob").send_keys("11/15/2022")


@when('enter Address "Road 5 Epe, Lagos"')
def address(context):
    context.driver.find_element_by_id("address").send_keys("Road 5 Epe, Lagos")

@when('click on "Add New User" button')
def submit(context):
    context.driver.find_element(By.ID, "submit-btn").click()


@then(u'Add new user!')
def userinfo(context):
    text=context.driver.find_element(By.ID, "user-info").text()
    assert text == "Patric Ekok Nzan"
    context.driver.close()

    
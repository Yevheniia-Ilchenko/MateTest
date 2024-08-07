from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://mate.academy/")


course_elements = driver.find_elements(By.CSS_SELECTOR, "a.typography_landingH3__vTjok.ProfessionCard_title__Zq5ZY.mb-12 h3")
course_describe = driver.find_elements(By.CSS_SELECTOR, "p.typography_landingTextMain__Rc8BD.mb-32")


with open("mate.csv", "w", encoding="utf-8") as file:
    for course, describe in zip(course_elements, course_describe):
        file.write(f"{course.text} : {describe.text}   \n")


driver.close()


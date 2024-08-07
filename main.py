from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://mate.academy/")

# with open("mate.csv", "w", encoding="utf-8") as file:
#     file.write("Course: Description -> Modules type\n")

courses = []

course_wrappers = driver.find_elements(By.CSS_SELECTOR, "div.ProfessionCard_cardWrapper__JQBNJ")

for wrapper in course_wrappers:

    title_element = wrapper.find_element(By.CSS_SELECTOR, "a.typography_landingH3__vTjok.ProfessionCard_title__Zq5ZY.mb-12 h3")
    title = title_element.text

    description_element = wrapper.find_element(By.CSS_SELECTOR, "p.typography_landingTextMain__Rc8BD.mb-32")
    description = description_element.text

    schedule_elements = wrapper.find_elements(By.CSS_SELECTOR, "span.ButtonBody_buttonText__FMZEg")
    schedules = [schedule.text for schedule in schedule_elements]

    courses.append({
        "title": title,
        "description": description,
        "schedules": schedules,
        "modules": "Not Found"
    })


with open("mate.csv", "w", encoding="utf-8") as file:
    file.write("Course: Description -> Schedules, Modules\n")

course_links = driver.find_elements(By.CSS_SELECTOR, "a.typography_landingH3__vTjok.ProfessionCard_title__Zq5ZY.mb-12")

course_hrefs = [link.get_attribute("href") for link in course_links]

for i, href in enumerate(course_hrefs):
    driver.get(href)

    try:
        number_modules = driver.find_element(By.CSS_SELECTOR,
                                             "p.typography_landingTextMain__Rc8BD.CourseModulesHeading_text__bBEaP")
        courses[i]["modules"] = number_modules.text
    except:
        courses[i]["modules"] = "Not Found"


with open("mate.csv", "a", encoding="utf-8") as file:
    for course in courses:
        file.write(f"{course['title']}: {course['description']} -> {' / '.join(course['schedules'])} -> {course['modules']}\n")
driver.close()

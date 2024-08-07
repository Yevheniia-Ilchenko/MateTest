from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get("https://mate.academy/")


def find_element_with_fallback(driver, css_selector, fallback="Not Found"):
    try:
        return driver.find_element(By.CSS_SELECTOR, css_selector).text
    except NoSuchElementException:
        return fallback


def collect_data():
    courses = []

    course_wrappers = driver.find_elements(
        By.CSS_SELECTOR, "div.ProfessionCard_cardWrapper__JQBNJ"
    )

    for wrapper in course_wrappers:

        title_element = wrapper.find_element(
            By.CSS_SELECTOR,
            "a.typography_landingH3__vTjok."
            "ProfessionCard_title__Zq5ZY.mb-12 h3",
        )
        title = title_element.text

        description_element = wrapper.find_element(
            By.CSS_SELECTOR, "p.typography_landingTextMain__Rc8BD.mb-32"
        )
        description = description_element.text

        schedule_elements = wrapper.find_elements(
            By.CSS_SELECTOR, "span.ButtonBody_buttonText__FMZEg"
        )
        schedules = [schedule.text for schedule in schedule_elements]

        courses.append(
            {
                "title": title,
                "description": description,
                "schedules": schedules,
                "modules": None,
                "topics": None,
                "duration": None,
            }
        )
    return courses


with open("mate.csv", "w", encoding="utf-8") as file:
    file.write("Course: Description -> "
               "Schedules, Modules, Topics, Duration \n")

courses = collect_data()

course_links = driver.find_elements(
    By.CSS_SELECTOR, "a.typography_landingH3__vTjok."
                     "ProfessionCard_title__Zq5ZY.mb-12"
)

course_hrefs = [link.get_attribute("href") for link in course_links]

for i, href in enumerate(course_hrefs):
    driver.get(href)

    courses[i]["modules"] = find_element_with_fallback(
        driver,
        "div.CourseModulesHeading_modulesNumber__UrnUh "
        "p.typography_landingTextMain__Rc8BD.CourseModulesHeading_text__bBEaP",
    )

    courses[i]["topics"] = find_element_with_fallback(
        driver,
        "div.CourseModulesHeading_topicsNumber__5IA8Z "
        "p.typography_landingTextMain__Rc8BD.CourseModulesHeading_text__bBEaP",
    )

    courses[i]["duration"] = find_element_with_fallback(
        driver,
        "div.CourseModulesHeading_courseDuration__qu2Lx "
        "p.typography_landingTextMain__Rc8BD.CourseModulesHeading_text__bBEaP",
    )

with open("mate.csv", "a", encoding="utf-8") as file:
    for course in courses:
        file.write(
            f"{course['title']}: {course['description']} ->"
            f" {' / '.join(course['schedules'])} -> {course['modules']},"
            f" {course['topics']}, {course['duration']} \n"
        )
driver.close()

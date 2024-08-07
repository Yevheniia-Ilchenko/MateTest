from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://mate.academy/")

with open("mate.csv", "w", encoding="utf-8") as file:
    file.write("Course: Description -> Schedules\n")

    course_wrappers = driver.find_elements(By.CSS_SELECTOR, "div.ProfessionCard_cardWrapper__JQBNJ")

    for wrapper in course_wrappers:

        title_element = wrapper.find_element(By.CSS_SELECTOR, "a.typography_landingH3__vTjok.ProfessionCard_title__Zq5ZY.mb-12 h3")
        title = title_element.text

        description_element = wrapper.find_element(By.CSS_SELECTOR, "p.typography_landingTextMain__Rc8BD.mb-32")
        description = description_element.text

        schedule_elements = wrapper.find_elements(By.CSS_SELECTOR, "span.ButtonBody_buttonText__FMZEg")
        schedules = [schedule.text for schedule in schedule_elements]

        file.write(f"{title}: {description} -> {' / '.join(schedules)}\n")


driver.close()

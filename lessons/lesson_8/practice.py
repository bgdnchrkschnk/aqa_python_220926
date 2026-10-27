from pprint import pprint
from typing import Optional


class ITEmployee:
    mindset = 'analytical'

    def __init__(self, name: str, years_of_experience: int | float, profession: str, is_active_search: bool) -> None:
        self.name = name
        self.years_of_experience = years_of_experience
        self.profession = profession
        self.is_active_search = is_active_search
        self.department = "IT"
        self.skills = []

    def add_skills(self, *skills: str): # tuple(...)
        list_skills = list(skills)
        self.skills.extend(list_skills)

    def cv(self) -> Optional[dict]: # dict | None
        cv_dict = self.__dict__
        if not cv_dict.get("skills"):
            print(f"{self.name} has no skills! Recommended to add skills for better efficiency")
            return None
        cv_dict['mindset'] = ITEmployee.mindset
        return cv_dict

vasya = ITEmployee("Vasya", 0.5, "Junior AQA Python", True)

# vasya.add_skills("Testing theory", "Python base", "SQL", "Log analyze", "API testing", "Playwright")
# vasya.add_skills("AI knowledge")
pprint(vasya.cv())


print(ITEmployee.mindset)
import time


class VacancyDTO:

    def __init__(self, vacancy):
        dt: int = int(round(time.time()))
        self.post = vacancy.get('header', 'Title')
        self.responsibilities = None
        self.min_salary = vacancy.get('salary_min', 0)
        self.max_salary = vacancy.get('salary_max', 0)
        self.qualification_requirements = None
        self.created_at = dt
        self.updated_at = dt

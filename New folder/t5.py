class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        return f"{self.first_name} {self.last_name}, age {self.age}"


class Application(Person):
    def __init__(self, first_name, last_name, age, position):
        super().__init__(first_name, last_name, age)
        self.position = position

    def apply(self):
        if self.age >= 18:
            print("Application accepted")
        else:
            print("You are not of legal age, application has been rejected.")
            return False
        return True


class JobRoles(Application):
    job_list = []  # This stores all job applications
    def __init__(self, first_name, last_name, age, position):
        super().__init__(first_name, last_name, age, position)
        self.job = {
            "Frontend Developer": 1000,
            "Backend Developer": 1200,
            "Full-Stack Developer": 1500,
            "Mobile App Developer": 1300,
            "Game Developer": 1400,
            "Software Engineer": 1600,
            "Data Scientist": 2000,
            "Data Analyst": 1800,
            "Machine Learning Engineer": 2200,
        }

    def accept(self, work_hours: int = 40):
        self.work_hours = work_hours
        if self.work_hours < 40:
            print("According to company rules, working less than 40 hours per week is not allowed.")
            return  

        if self.position in self.job.keys():
            result = input(
                f'''We have reviewed your application. Position: {self.position}, work hours: {self.work_hours}.
Is this acceptable to you? (YES/NO): '''
            ).lower()
            if result == 'yes':
                salary_response = input(
                    f'''You will be paid {self.job[self.position]} monthly for the position of {self.position}.
Is this salary acceptable to you? (YES/NO): '''
                ).lower()
                if salary_response == 'yes':
                    print("Congratulations, you have been hired!")
                    JobRoles.job_list.append(
                        f"{self.get_info()} {self.position} monthly salary {self.job[self.position]} work hours {self.work_hours}"
                    )
                else:
                    print("Unfortunately, we cannot offer you a higher salary.")
            else:
                print("Application cancelled.")
        else:
            print("Sorry, the position you chose is not available.")

    @classmethod
    def get_all_info(cls):
        if not cls.job_list:
            return "There are no accepted jobs."
        return "\n".join(cls.job_list)


employees = [
    JobRoles("Fazliddin", "Narzullayev", 26, "Backend Developer"),
    JobRoles("Husniddin", "Abduhalilov", 17, "Frontend Developer"),
    JobRoles("Abror", "Toraqulov", 16, "Full-Stack Developer"),
    JobRoles("Faxri", "Bekmirzayev", 26, "Software Engineer")
]

for employee in employees:
    print(employee.get_info())
    if employee.apply():  # Apply only if the age condition is met
        employee.accept(40)
    print("-" * 50)

print("All employees:")
print(JobRoles.get_all_info())

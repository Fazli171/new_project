from enum import Enum
from typing import List

class level(Enum):
    JUIOR = 'juior'
    MIDDLE = 'middle'
    SENIOR = 'senior'
    def __str__(self):
        return self.value

class Skill:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"skill : {self.name}"
s1 = Skill('Python')
s2 = Skill("javaScript")
s3 = Skill("HTML")
s4 = Skill("grafik dizayner")
s5 = Skill("mobile programmung")
skills = [s1, s2, s3]
skills1 = [s3, s1, s4]
skills2 = [s5, s3, s2]
    
class Programmer:
    def __init__(self, fullNmae, age, passportID, level, skill : List[Skill]):
        self.fullName = fullNmae.title()
        self.age = age
        self.passportID =passportID
        self.level = level
        self.skill = skill
    
    def get_skill(self):
        tma = [f"{i} . {v} " for i , v in enumerate(self.skill, 1)]
        return  "\n".join(tma)
    def __str__(self):
        return f"full name {self.fullName} \nage {self.age} \npassport id {self.passportID} \nlevel {self.level} \n{self.get_skill()}"
w = Programmer('fazliddin narzullayev', 26, 'QW345366', level.JUIOR, skills )
w2 = Programmer("muslim sagdullayev", 24, 'AS367464', level, skills1)

programmers = [w, w2]
class Team:
    def __init__(self, name, programmer :List[Programmer]):
        self.name = name
        self.programmer = programmer

    def get_team(self):
        tim = [f"{i} >>>  {v}" for i , v in enumerate(self.programmer, 1)]
        return '\n'. join(tim)

    def __str__(self):
        return f"name : {self.name} \nteam : {self.get_team()}"
    
swe = Team('GT_group', programmers)
# print(swe)

class Project:
    def __init__(self, name , team : Team):
        self.name = name
        self.team = team

    def __str__(self):
        return f"project name {self.name} \nteam {self.team}"
    
project1 = Project('clik', swe)
project2 = Project('payme', swe)
project3 = Project('upay', swe)
projects = [project1, project2, project3]

class IT_company:
    def __init__(self, name, project: List[Project]):
        self.name = name
        self.project = project 
    def get_project(self):
        fig = [f"{i} > {v}" for i, v in enumerate(self.project, 1)]
        return "\n".join(fig)

    def __str__(self):
        return f"IT company name : {self.name}\nProjects:\n{self.get_project()}"

    
it = IT_company('GET_IT',projects)
    
print(it)
        
        

        
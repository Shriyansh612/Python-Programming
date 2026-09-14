class UniversityMember:
    def __init__(self,name,university_id):
        self.name = name
        self.university_id = university_id

class Student(UniversityMember):
    def __init__(self,name,university_id,course):
        super().__init__(name,university_id)
        self.course = course

class ResearchStudent(Student):
    def __init__(self,name,university_id,course,research_topic):
        super().__init__(name,university_id,course)
        self.research_topic = research_topic

    def display(self):
        print(self.name)        
        print(self.university_id)        
        print(self.course)        
        print(self.research_topic)        

s1 = ResearchStudent("Shriyansh",101,"Python","OOPS")        
s1.display()
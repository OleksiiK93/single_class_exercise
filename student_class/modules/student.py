class Student:
    def __init__(self, name, cohort) -> None:
        self.name = name
        self.cohort = cohort
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, lang):
        return f"I love {lang}"
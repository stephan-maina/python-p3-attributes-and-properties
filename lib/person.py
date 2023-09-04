APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Stephan Maina", job="Admin"):
        self.name = name
        self.job = job
        self.skills = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (isinstance(name, str)) and (1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

    job = property(get_job, set_job)

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} has acquired the skill: {skill}")

    def list_skills(self):
        if self.skills:
            return f"{self.name}'s skills: {', '.join(self.skills)}"
        else:
            return f"{self.name} has no skills yet."

    def __str__(self):
        return f"Name: {self.name}\nJob: {self.job}\nSkills: {', '.join(self.skills)}"

if __name__ == "__main__":
    person1 = Person("Stephorinho", "Customer Service")
    person2 = Person("Noel", "ITC")

    person1.add_skill("Communication")
    person2.add_skill("Programming")
    person2.add_skill("Networking")

    print(person1.list_skills())
    print(person2.list_skills())

    print("Person 1 Info:")
    print(person1)

    print("Person 2 Info:")
    print(person2)

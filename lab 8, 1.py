class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} выполняет общие рабочие обязанности."
    
    def get_info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary} руб."


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def write_code(self):
        return f"{self.name} пишет код на {self.programming_language}."

    def work(self):
        return self.write_code()

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Язык программирования: {self.programming_language}"


class Designer(Employee):
    def __init__(self, name, salary, software):
        super().__init__(name, salary)
        self.software = software
    
    def design(self):
        return f"{self.name} создает дизайн в {self.software}."

    def work(self):
        return self.design()

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Программное обеспечение: {self.software}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def manage(self):
        return f"{self.name} управляет командой из {self.team_size} человек."

    def work(self):
        return self.manage()

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Размер команды: {self.team_size} чел."


employees = [
    Developer("Иван Петров", 120000, "Python"),
    Developer("Анна Смирнова", 130000, "Java"),
    Designer("Елена Кузнецова", 100000, "Figma"),
    Designer("Ольга Иванова", 95000, "Adobe Photoshop"),
    Manager("Сергей Васильев", 150000, 5),
    Manager("Дмитрий Николаев", 160000, 8)
]

print("=" * 60)
print("ИНФОРМАЦИЯ О СОТРУДНИКАХ")
print("=" * 60)

for emp in employees:
    print(emp.get_info())
    print(emp.work())
    print("-" * 40)

print("\n" + "=" * 60)
print("ПОЛИМОРФИЗМ: все сотрудники выполняют work()")
print("=" * 60)

for emp in employees:
    print(f"{emp.name}: {emp.work()}")
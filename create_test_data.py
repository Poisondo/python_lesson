import random
from django.utils.text import gettext_lazy as _
from faker import Faker

from people.models import Branch, Department, Employee

fake = Faker('ru_RU')

def create_test_data():
    # Очистка старых данных
    Employee.objects.all().delete()
    Department.objects.all().delete()
    Branch.objects.all().delete()

    # Создаем филиалы
    branches = [
        Branch.objects.create(
            address=fake.address(),
            short_name=fake.city() + " филиал"
        )
        for _ in range(3)
    ]

    # Список возможных должностей
    positions = [
        'Менеджер', 'Разработчик', 'Аналитик', 'Дизайнер',
        'Тестировщик', 'Бухгалтер', 'HR', 'Маркетолог'
    ]

    # Создаем отделы в каждом филиале
    departments = []
    for branch in branches:
        # От 2 до 5 отделов в каждом филиале
        for _ in range(random.randint(2, 5)):
            dept = Department.objects.create(
                name=fake.company_suffix() + " отдел",
                floor=random.randint(1, 5),
                branch=branch
            )
            departments.append(dept)

    # Создаем сотрудников в каждом отделе
    for department in departments:
        # От 1 до 30 сотрудников в каждом отделе
        for _ in range(random.randint(1, 30)):
            Employee.objects.create(
                full_name=fake.name(),
                position=random.choice(positions),
                phone=fake.phone_number(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
                email=fake.email() if random.random() > 0.2 else None,  # 20% без email
                department=department
            )

    print("Тестовые данные успешно созданы!")
    print(f"Создано: {Branch.objects.count()} филиалов, "
          f"{Department.objects.count()} отделов, "
          f"{Employee.objects.count()} сотрудников")

if __name__ == '__main__':
    create_test_data()

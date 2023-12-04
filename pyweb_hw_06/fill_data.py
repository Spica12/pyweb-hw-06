import random
from datetime import datetime

from faker import Faker

from tools import perform_insert, read_scripst_from_file

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_RATINGS = 20

SUBJECTS = [
    "Mathematic",
    "Computer Science",
    "Software",
    "Farm Management",
    "Agriculture",
    "Astronomy",
    "Chemistry",
    "Biology",
    "Physics",
    "Geography",
]

fake = Faker("uk")


def generate_fake_data():
    """Generate fake data for testing db"""
    fake_students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    fake_groups = []
    fake_subjects = random.sample(SUBJECTS, k=NUMBER_SUBJECTS)
    fake_teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]

    first_letters_for_group = ["M", "E", "C", "D", "B"]
    second_letters_for_group = ["a", "f", "b", "c"]

    for _ in range(NUMBER_GROUPS):
        random_first_letter = random.choice(first_letters_for_group)
        random_second_letter = random.choice(second_letters_for_group)
        randdom_number_for_group = random.randint(1, 5)
        fake_group = (
            f"{random_first_letter}0{randdom_number_for_group}{random_second_letter}"
        )
        fake_groups.append(fake_group)

    return fake_students, fake_groups, fake_teachers, fake_subjects


def prepare_fake_data_for_students(students):
    fake_data_for_db = []
    for student in students:
        fake_data_for_db.append((student, random.randint(1, NUMBER_GROUPS)))

    return fake_data_for_db


def prepare_fake_data_for_groups(groups):
    fake_data_for_db = []
    for group in groups:
        fake_data_for_db.append((group,))

    return fake_data_for_db


def prepare_fake_data_for_teachers(teachers):
    fake_data_for_db = []
    for teacher in teachers:
        fake_data_for_db.append((teacher,))

    return fake_data_for_db


def prepare_fake_data_for_subjects(subjects):
    fake_data_for_db = []
    for subject in subjects:
        fake_data_for_db.append((subject, random.randint(1, NUMBER_TEACHERS)))

    return fake_data_for_db


def prepare_fake_data_for_ratings(subjects):
    fake_data_for_db = []
    for student_id in range(1, NUMBER_STUDENTS):
        for _ in range(1, random.randint(2, 4)):
            random_subject_id = random.randint(1, NUMBER_SUBJECTS)
            rating = random.randint(60, 99)
            date_of_rating = datetime(
                year=2023, month=random.randint(1, 12), day=random.randint(1, 28)
            ).date()

            fake_data_for_db.append(
                (student_id, random_subject_id, rating, date_of_rating)
            )

    return fake_data_for_db


def insert_fake_data_to_database():
    """Insert fake data to database"""
    students, groups, teachers, subjects = generate_fake_data()

    data_for_students = prepare_fake_data_for_students(students)
    data_for_groups = prepare_fake_data_for_groups(groups)
    data_for_teachers = prepare_fake_data_for_teachers(teachers)
    data_for_subjects = prepare_fake_data_for_subjects(subjects)
    data_for_ratings = prepare_fake_data_for_ratings(subjects)

    # Insert data to table groups
    sql_base_insert_to_groups = read_scripst_from_file("insert_values_groups.sql")
    perform_insert(sql_base_insert_to_groups, data_for_groups)

    # Insert data to table students
    sql_base_insert_to_students = read_scripst_from_file("insert_values_students.sql")
    perform_insert(sql_base_insert_to_students, data_for_students)

    # Insert data to table teachers
    sql_base_insert_to_teachers = read_scripst_from_file("insert_values_teachers.sql")
    perform_insert(sql_base_insert_to_teachers, data_for_teachers)

    # Insert data to table subjects
    sql_base_insert_to_subjects = read_scripst_from_file("insert_values_subjects.sql")
    perform_insert(sql_base_insert_to_subjects, data_for_subjects)

    # Insert data to table ratings
    sql_base_insert_to_ratings = read_scripst_from_file("insert_values_ratings.sql")
    perform_insert(sql_base_insert_to_ratings, data_for_ratings)


if __name__ == "__main__":
    insert_fake_data_to_database()

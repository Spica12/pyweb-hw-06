import psycopg2
from contextlib import contextmanager
import fill_data


@contextmanager
def create_connection():
    """Create a database connection to a SQL database"""
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pyhomedb",
            user="postgres",
            password="pass",
        )
        yield conn
        conn.commit()

    except psycopg2.Error as err:
        print(err)
        conn.rollback()

    finally:
        conn.close()


def perform_querry(querry, is_result=False):
    """Perform querry"""
    result = ""
    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(querry)
            if is_result:
                result = cur.fetchall()
            cur.close()
        else:
            print("Error! Can't create the database connection")

    return result


def perform_insert(insert: str, values: list[tuple]):
    """Perform insert data to database"""

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.executemany(insert, values)
            cur.close()
        else:
            print("Error! Can't create the database connection")


def read_scripst_from_file(file):
    """Read the script from file"""
    with open(file, "r") as file:
        sql = file.read()

    return sql


def create_tables():
    """Create tables in database"""
    sql_create_tables = read_scripst_from_file("../sql_querry/create_tables.sql")
    perform_querry(sql_create_tables)


def insert_fake_data_to_database():
    """Insert fake data to database"""
    students, groups, teachers, subjects = fill_data.generate_fake_data()

    data_for_students = fill_data.prepare_fake_data_for_students(students)
    data_for_groups = fill_data.prepare_fake_data_for_groups(groups)
    data_for_teachers = fill_data.prepare_fake_data_for_teachers(teachers)
    data_for_subjects = fill_data.prepare_fake_data_for_subjects(subjects)
    data_for_ratings = fill_data.prepare_fake_data_for_ratings(subjects)

    # Insert data to table groups
    sql_base_insert_to_groups = read_scripst_from_file("../sql_querry/insert_values_groups.sql")
    perform_insert(sql_base_insert_to_groups, data_for_groups)


    # Insert data to table students
    sql_base_insert_to_students = read_scripst_from_file("../sql_querry/insert_values_students.sql")
    perform_insert(sql_base_insert_to_students, data_for_students)

    # Insert data to table teachers
    sql_base_insert_to_teachers = read_scripst_from_file("../sql_querry/insert_values_teachers.sql")
    perform_insert(sql_base_insert_to_teachers, data_for_teachers)

    # Insert data to table subjects
    sql_base_insert_to_subjects = read_scripst_from_file("../sql_querry/insert_values_subjects.sql")
    perform_insert(sql_base_insert_to_subjects, data_for_subjects)

    # Insert data to table subjects
    sql_base_insert_to_ratings = read_scripst_from_file("../sql_querry/insert_values_ratings.sql")
    perform_insert(sql_base_insert_to_ratings, data_for_ratings)


def main():
    # Create tables
    create_tables()

    # Insert fake data to database
    insert_fake_data_to_database()


if __name__ == "__main__":
    main()

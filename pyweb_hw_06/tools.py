import psycopg2
from contextlib import contextmanager
from pathlib import Path


BASE_DIR_SQL = Path("../sql_querry")


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
        if conn is not None:
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
    with open(BASE_DIR_SQL / file, "r") as file:
        sql = file.read()

    return sql


def perform_querry_from_file(head, sql_file):
    sql_querry = read_scripst_from_file(sql_file)
    raw_result = perform_querry(sql_querry, is_result=True)

    result = head + '\n'
    for i, student in enumerate(raw_result, start=1):
        result += f"{i}. {student}\n"

    print(result)

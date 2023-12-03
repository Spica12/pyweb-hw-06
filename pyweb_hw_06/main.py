import psycopg2
from contextlib import contextmanager


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


def read_scripst_from_file(file):
    """Read the script from file"""
    with open(file, "r") as file:
        sql = file.read()

    return sql


def main():
    # Create tables
    sql_create_tables = read_scripst_from_file("../sql_querry/create_tables.sql")
    perform_querry(sql_create_tables)

    # Insert fake data to database


if __name__ == "__main__":
    main()

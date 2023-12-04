from tools import perform_querry, read_scripst_from_file


def create_tables():
    """Create tables in database"""
    sql_create_tables = read_scripst_from_file("../sql_querry/create_tables.sql")
    perform_querry(sql_create_tables)


if __name__ == "__main__":
    # Create tables
    create_tables()


# pyhomedb=# \dt
#           List of relations
#  Schema |   Name   | Type  |  Owner
# --------+----------+-------+----------
#  public | groups   | table | postgres
#  public | ratings  | table | postgres
#  public | students | table | postgres
#  public | subjects | table | postgres
#  public | teachers | table | postgres
# (5 rows)

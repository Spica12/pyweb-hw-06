from create_tables import create_tables
from fill_data import insert_fake_data_to_database
from querries import perform_querries


def main():
    # Create tables on DB
    create_tables()

    # Insert fake data to DB
    insert_fake_data_to_database()

    # Perform Hometask querries
    perform_querries()


if __name__ == "__main__":
    main()

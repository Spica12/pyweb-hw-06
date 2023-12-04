from tools import perform_querry_from_file


def perform_querries():
    print("---- Querry 1 ----")
    querry_1_sql_file = "querry_1.sql"
    querry_1_head = "Знайти 5 студентів із найбільшим середнім балом з усіх предметів:"
    perform_querry_from_file(querry_1_head, querry_1_sql_file)

    print("---- Querry 2 ----")
    querry_2_sql_file = "querry_2.sql"
    querry_2_head = "Знайти студента із найвищим середнім балом з певного предмета:"
    perform_querry_from_file(querry_2_head, querry_2_sql_file)

    print("---- Querry 3 ----")
    querry_3_sql_file = "querry_3.sql"
    querry_3_head = "Знайти середній бал у групах з певного предмета:"
    perform_querry_from_file(querry_3_head, querry_3_sql_file)

    print("---- Querry 4 ----")
    querry_4_sql_file = "querry_4.sql"
    querry_4_head = "Знайти середній бал на потоці (по всій таблиці оцінок):"
    perform_querry_from_file(querry_4_head, querry_4_sql_file)

    print("---- Querry 5 ----")
    querry_5_sql_file = "querry_5.sql"
    querry_5_head = "Знайти які курси читає певний викладач:"
    perform_querry_from_file(querry_5_head, querry_5_sql_file)

    print("---- Querry 6 ----")
    querry_6_sql_file = "querry_6.sql"
    querry_6_head = "Знайти список студентів у певній групі:"
    perform_querry_from_file(querry_6_head, querry_6_sql_file)

    print("---- Querry 7 ----")
    querry_7_sql_file = "querry_7.sql"
    querry_7_head = "Знайти оцінки студентів у окремій групі з певного предмета:"
    perform_querry_from_file(querry_7_head, querry_7_sql_file)

    print("---- Querry 8 ----")
    querry_8_sql_file = "querry_8.sql"
    querry_8_head = (
        "Знайти середній бал, який ставить певний викладач зі своїх предметів:"
    )
    perform_querry_from_file(querry_8_head, querry_8_sql_file)

    print("---- Querry 9 ----")
    querry_9_sql_file = "querry_9.sql"
    querry_9_head = "Знайти список курсів, які відвідує студент:"
    perform_querry_from_file(querry_9_head, querry_9_sql_file)

    print("---- Querry 10 ----")
    querry_10_sql_file = "querry_10.sql"
    querry_10_head = "Список курсів, які певному студенту читає певний викладач:"
    perform_querry_from_file(querry_10_head, querry_10_sql_file)

    print("---- Querry 11 Additional ----")
    querry_11_sql_file = "querry_11_add.sql"
    querry_11_head = "Середній бал, який певний викладач ставить певному студентові:"
    perform_querry_from_file(querry_11_head, querry_11_sql_file)

    print("---- Querry 12 Additional ----")
    querry_12_sql_file = "querry_12_add.sql"
    querry_12_head = (
        "Оцінки студентів у певній групі з певного предмета на останньому занятті:"
    )
    perform_querry_from_file(querry_12_head, querry_12_sql_file)


if __name__ == "__main__":
    perform_querries()

from tools import perform_querry, read_scripst_from_file

def perform_sql_querry(head, sql_file):
    sql_querry = read_scripst_from_file(sql_file)
    raw_result = perform_querry(sql_querry, is_result=True)

    result = head + '\n'
    for i, student in enumerate(raw_result, start=1):
        result += f"{i}. {student}\n"

    print(result)


def perform_querries():
    print('---- Querry 1 ----')
    querry_1_sql_file = "../sql_querry/querry_1.sql"
    querry_1_head = 'Student with max average ratings:'
    perform_sql_querry(querry_1_head, querry_1_sql_file)

    print('---- Querry 2 ----')
    querry_2_sql_file = "../sql_querry/querry_2.sql"
    querry_2_head = 'Student with max average rating in the subject:'
    perform_sql_querry(querry_2_head, querry_2_sql_file)

    print('---- Querry 3 ----')
    querry_3_sql_file = "../sql_querry/querry_3.sql"
    querry_3_head = 'Average rating in the subject in groups :'
    perform_sql_querry(querry_3_head, querry_3_sql_file)

    print('---- Querry 4 ----')
    querry_4_sql_file = "../sql_querry/querry_4.sql"
    querry_4_head = 'Average rating in all groups :'
    perform_sql_querry(querry_4_head, querry_4_sql_file)

    print('---- Querry 5 ----')
    querry_5_sql_file = "../sql_querry/querry_5.sql"
    querry_5_head = 'Average rating in all groups :'
    perform_sql_querry(querry_5_head, querry_5_sql_file)

    print('---- Querry 6 ----')
    querry_6_sql_file = "../sql_querry/querry_6.sql"
    querry_6_head = 'Students in the group:'
    perform_sql_querry(querry_6_head, querry_6_sql_file)

    print('---- Querry 7 ----')
    querry_7_sql_file = "../sql_querry/querry_7.sql"
    querry_7_head = 'Ratings of students in a separate group for a specific subject:'
    perform_sql_querry(querry_7_head, querry_7_sql_file)

    print('---- Querry 8 ----')
    querry_8_sql_file = "../sql_querry/querry_8.sql"
    querry_8_head = 'Ratings of students in a separate group for a specific subject:'
    perform_sql_querry(querry_8_head, querry_8_sql_file)

    print('---- Querry 9 ----')
    querry_9_sql_file = "../sql_querry/querry_9.sql"
    querry_9_head = 'List of subjects a student is taking.:'
    perform_sql_querry(querry_9_head, querry_9_sql_file)

    print('---- Querry 10 ----')
    querry_10_sql_file = "../sql_querry/querry_10.sql"
    querry_10_head = 'A list of subjects taught to a specific student by a specific teacher:'
    perform_sql_querry(querry_10_head, querry_10_sql_file)

    print('---- Querry 11 Additional ----')
    querry_11_sql_file = "../sql_querry/querry_11_add.sql"
    querry_11_head = 'The average rating given by a particular teacher to a particular student:'
    perform_sql_querry(querry_11_head, querry_11_sql_file)

    print('---- Querry 12 Additional ----')
    querry_12_sql_file = "../sql_querry/querry_12_add.sql"
    querry_12_head = 'Ratings in a certain group in a certain subject in the last lesson.:'
    perform_sql_querry(querry_12_head, querry_12_sql_file)



if __name__ == "__main__":
    perform_querries()

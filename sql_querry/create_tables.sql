DROP TABLE IF EXISTS ratings;

DROP TABLE IF EXISTS students;

DROP TABLE IF EXISTS subjects;

DROP TABLE IF EXISTS teachers;

DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name_group VARCHAR(30),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    group_id INTEGER,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_group
        FOREIGN KEY (group_id) REFERENCES groups(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    subject VARCHAR(30),
    teacher_id INT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_teacher
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
);

CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    rating INT,
    date_of DATE NOT NULL,
    CONSTRAINT fk_student
        FOREIGN KEY (student_id) REFERENCES students(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
    CONSTRAINT fk_subject
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
);

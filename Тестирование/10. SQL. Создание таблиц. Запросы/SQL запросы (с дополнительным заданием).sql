-- ID (поле user_id) пользователя с почтой houston42@gmail.com (таблица users).
select user_id from users where user_email='houston42@gmail.com';

-- Уровень (поле level) студента с user_id = 44133 (таблица student).
select level from student where user_id=44133;

-- Предмет (поле subject_title) с id = 8 (таблица subject).
select subject_title from subject where subject_id = 8;

-- Email учителя группы с group_id = 80 (таблица teacher).
select email from teacher where group_id=80;

-- Уникальные форматы обучения (education_form) для студента с user_id = 12203 (таблица student).
select distinct education_form from student where user_id=12203;

-- ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ

-- Создание таблиц (поля, тип данных, размерность значений)
CREATE TABLE salary ( 
    teacher_id  INTEGER,
    salary_amt  NUMERIC(16,2),
    salary_val  CHAR(3)
);

CREATE TABLE rooms ( 
    room_id  INTEGER,
    teacher_id  INTEGER,
    floor_num  INTEGER
);

-- Добавление записей (заполнение строк) таблиц
INSERT INTO salary (teacher_id, salary_amt, salary_val)
VALUES
(965, 70000, 'RUR'),
(29091, 100000, 'RUR'),
(29410, 1000, 'EUR'),
(33576, 1800, 'USD'),
(33902, 1200, 'EUR');

INSERT INTO rooms (room_id, teacher_id, floor_num)
VALUES
(1, 965, 1),
(2, 29091, 1),
(3, 29410, 1),
(10, 33576, 2),
(11, 33902, 2);

-- 1. ID учителей с кабинетами на втором этаже
select teacher_id from rooms where floor_num = 2;

-- 2. ID учетелей, которые получают ЗП в евро
select teacher_id from salary where salary_val = 'EUR';
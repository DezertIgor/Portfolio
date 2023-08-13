-- Уровень студента с id = 9651. При этом задайте алиас (псевдоним) для колонки как stud_level, а для таблицы — s.
Select level as stud_level from student as s where user_id = 9651;

-- Email учителей с id 30019 и 31433 (в одном запросе).
Select email from teacher where teacher_id = 30019 or teacher_id =31433;

-- Данные о пользователях с уровнем Advanced, занимающихся в группах (group), и о пользователях с уровнем Upper-Intermediate, занимающихся индивидуально (personal).
Select * from student where (level = 'Advanced' and education_form = 'group')
or (level='Upper-Intermediate' and education_form = 'personal');

-- Данные об учителях из групп от 180 до 190 (group_id).
Select * from teacher where group_id between 180 and 190;

-- Данные о пользователях, у которых email заканчивается на yahoo.com
Select * from users where user_email like '%yahoo.com';

-- Дополнительное задание

-- Создание таблиц

create table posts (
post_id integer,
	text_len integer,
	post_date date);

Create table tags (
	post_id integer,
	tag text);

-- Заполнение таблиц

insert into posts (post_id, text_len, post_date)
values
(1, 6799, '2023.03.09'),
(2, 7800, '2023.03.12'),
(3, 6907, '2023.03.19'),
(4, 8890, '2023.03.22'),
(5, 9802, '2023.03.30');

insert into tags (post_id, tag)
values
(1, 'nofilter'),
(2, 'happy'),
(3, 'joy'),
(4, 'music'),
(5, 'dark');

-- 1. Выведите данные по постам, которые длиннее 8000 символов.
select * from posts where text_len > 8000;

-- 2. Выведите id постов, которые отмечены тегами happy или joy.
select post_id from tags where tag = 'happy' or tag = 'joy';

-- 3. Выведите id постов, которые были размещены до 10 марта 2023.
select post_id from posts where post_date < '2023.03.10';

-- 4. Добавьте пост с id 6, сделанный 31 марта 2023, содержащий 10782 символ и отмеченный тегом love (два INSERT в обе таблицы).

INSERT INTO posts (post_id, text_len, post_date)
VALUES (6, 10782, '2023-03-31');

INSERT INTO tags (post_id, tag)
VALUES (6, 'love');

-- 5. Измените тег для поста с id =5 c dark на live.
update tags set tag='live' where post_id= 5;
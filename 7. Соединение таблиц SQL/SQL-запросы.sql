-- 1. Ученики и все группы, в которых преподает учитель с почтой blanda.jamil@yahoo.com
Select s.user_id, t.group_id
from teacher as t join group_student as s
on s.group_id=t.group_id
where t.email='blanda.jamil@yahoo.com';

-- 2. Уровень ученика с почтой gpagac@jacobs.com
select s.level
from student as s join users as u
on s.user_id=u.user_id
where u.user_email='gpagac@jacobs.com';

-- 3. Уникальные названия предметов, которые изучает ученик c user_id=11300
select distinct(s.subject_title)
from subject as s join users as u
on s.subject_id=u.subject_id
where u.user_id=11300;

-- 4. Уникальные уровни учеников, которые занимаются в группе с id = 10
select distinct(s.level)
from group_student as g join student as s
on s.user_id = g.user_id
where g.group_id=10;

-- ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ 😊

-- Создание таблицы "Positions"
create table Positions (
id_check integer,
id_pos integer,
art text,
quantity integer);

-- Создание таблицы "Products"
create table Products (
art text,
product text,
category text);

-- Заполнение таблицы "Positions"
insert into positions (id_check, id_pos, art, quantity)
values
(1,1,'A1',1),
(1,2,'A4',3),
(1,3,'A2',2),
(1,4,'A10',1),
(1,5,'A8',4),
(2,1,'A5',1),
(2,2,'A7',1),
(2,3,'A3',2),
(3,1,'A2',1),
(3,2,'A9',1),
(3,3,'A5',2),
(3,4,'A6',1),
(3,5,'A3',3),
(4,1,'A1',3),
(4,2,'A2',1),
(5,1,'A2',1),
(5,2,'A8',5),
(5,3,'A3',1),
(5,4,'A4',1),
(5,5,'A5',1);

-- Заполнение таблицы "Products"
insert into products (art, product, category)
values
('A1','кроссовки','обувь'),
('A2','кеды','обувь'),
('A3','сланцы','обувь'),
('A4','куртка','одежда'),
('A5','ветровка','одежда'),
('A6','шорты','одежда'),
('A7','палатка','туризм'),
('A8','коврик','туризм'),
('A9','спальник','туризм'),
('A10','рюкзак','туризм'),
('A11','туфли','обувь'),
('A12','солнечные очки','аксессуары');

-- 1. Названия уникальных категорий, которые были куплены в чеке с id = 3
select distinct (p.category)
from positions as c join products as p
on c.art=p.art
where c.id_check=3;

-- 2. Артикулы продуктов, которые не покупали (т. е. они не встречаются ни в одном чеке)
select p.art
from positions as c right join products as p
on c.art=p.art
where c.id_check is null;

-- 3. Количество чеков, в которых куплено больше двух пар одинаковой обуви
select count(distinct(id_check))
from positions as c join products as p
on p.art=c.art
where p.category='обувь' and c.quantity>2;

-- 4. Количество чеков, в которых куплено больше двух позиций любой одежды
select count (distinct(x.id_check))
from (select c.id_check, count(*) as количество_ПОЗИЦИЙ_Одежды_в_чеке
	from positions as c join products as p
	on p.art=c.art
	where p.category='одежда'
	group by c.id_check) as x
where количество_ПОЗИЦИЙ_Одежды_в_чеке > 2;
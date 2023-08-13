-- Создание таблицы "animal_classes"

create table animal_classes (
id integer,
class text);

-- Создание таблицы "animal_info"

create table animal_info (
name text,
class integer,
owner text);

-- Заполнение таблицы "animal_classes"

insert into animal_classes (id, class)
values
(1, 'кошка'),
(2, 'собака');

-- Заполнение таблицы "animal_info"

insert into animal_info (name, class, owner)
values
('Кити', 1, 'Ваня'),
('Мити', 2, 'Ваня'),
('Пити', 1, 'Петя');

-- 1. Сколько всего животных у Вани
Select count (owner)
from animal_info
where owner = 'Ваня';

-- 2. Уникальные имена всех кошек отсортированные по алфавиту
Select distinct (name) as имена_кошек_по_алфавиту
from animal_info join animal_classes
on animal_classes.id = animal_info.class
where animal_classes.class = 'кошка'
order by имена_кошек_по_алфавиту;

-- 3. Количество животных каждого класса (количество и имя класса)

Select count (animal_classes.class) as количество_животных, animal_classes.class as имя_класса
from animal_info join animal_classes
on animal_classes.id = animal_info.class
group by animal_classes.class;
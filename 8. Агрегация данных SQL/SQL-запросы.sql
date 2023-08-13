-- 1. Общее количество индивидуально обучающихся студентов для каждого уровня:

select level, education_form, count(user_id)
from student
where education_form = 'personal'
group by level, education_form;

-- 2. Общее количество учащихся школы с уровнем Advanced для каждой формы обучения:

select education_form, count(user_id)
from student
where level='Advanced'
group by education_form;

/* 3. Общее количество учащихся школы в разрезе уровня и формы обучения,
отсортированных по уровню в порядке возрастания и по форме обучения в порядке убывания: */

select level, education_form, count(*)
from student
group by level, education_form
order by level, education_form desc;

-- 4. Максимальное и минимальное id группы (одним запросом):

select max(group_id), min(group_id)
from group_student;

-- 5. Количество учеников и id группы, в которой наибольшее количество учеников:

select count(user_id), group_id
from group_student
group by group_id
order by count desc
limit 1;

-- ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ

-- Создание таблицы "customers":

create table customers (
customer_id integer,
customer_nm varchar(255));

-- Создание таблицы "sales":

create table sales (
sale_id integer,
store_id integer,
customer_id integer,
dt date,
amt numeric(10,2));

-- Заполнение таблицы "customers":

insert into customers (customer_id, customer_nm)
values
(1, 'Ларс фон Триер'),
(2, 'Андрей Тарковский'),
(3, 'Мартин Мак Дона'),
(4, 'Николас Виндинг Рефн'),
(5, 'Гильермо дель Торо');

-- Заполнение таблицы "sales":

insert into sales (sale_id, store_id, customer_id, dt, amt)
values
(123,1,1,'1956.04.30',56000.88),
(456,2,2,'1932.04.04',32000.77),
(789,3,3,'1970.03.26',70.30),
(147,1,4,'1970.09.29',1),
(258,2,5,'1964.10.09',900),
(369,3,1,'1957.05.31',14.08),
(951,1,2,'1933.05.05',20.05),
(753,2,3,'1971.04.27',99),
(161,3,1,'1958.06.01',1000),
(666,1,2,'1934.06.06',99999.99);

-- 1. Максимальная сумма покупки:

select max(amt)
from sales;

-- 2. Минимальная дата покупки:

select min(dt)
from sales;

-- 3. Средняя сумма покупок для customer_id=1:

select avg (amt)
from sales
where customer_id =1;

-- 4. Минимальная и максимальная сумма покупки, совершённой в магазине с store_id=3 или покупателем с customer_id=2:

-- ДЕФОЛТНЫЙ:
select min(amt), max(amt)
from sales
where store_id=3 or customer_id=2;

-- ИСЧЕРПЫВАЮЩИЙ (в ответе указывается не просто два числа, а ещё покупатель и магазин, им соответствующие):
SELECT amt, customer_id, store_id
FROM sales
WHERE amt = (
    SELECT MIN(amt)
    FROM sales
    WHERE store_id = 3 OR customer_id = 2)
UNION ALL
SELECT amt, customer_id, store_id
FROM sales
WHERE amt = (
    SELECT MAX(amt)
    FROM sales
    WHERE store_id = 3 OR customer_id = 2);

-- 5. Количество уникальных имён покупателей:

select count(distinct(customer_id))
from customers;
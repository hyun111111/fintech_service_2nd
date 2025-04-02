use db_model_prectics;
SELECT * FROM sampledb.customers;
drop database world;
USE mydb;
insert into department values( 1, '수학');
insert into department values( 2, '국문학');
insert into department values( 3, '정보통신공학');
insert into department values( 4, '모바일공학');

insert into student values( 1, '가길동', 177, 1);
insert into student values( 2, '나길동', 178, 1);
insert into student values( 3, '다길동', 179, 1);
insert into student values( 4, '라길동', 180, 2);
insert into student values( 5, '마길동', 170, 2);
insert into student values( 6, '바길동', 172, 3);
insert into student values( 7, '사길동', 166, 4);
insert into student values( 8, '아길동', 192, 4);

insert into professor values( 1, '가교수', 1);
insert into professor values( 2, '나교수', 2);
insert into professor values( 3, '다교수', 3);
insert into professor values( 4, '빌게이츠', 4);
insert into professor values( 5, '스티브잡스', 3);

insert into course(course_id, course_name, professor_id, start_date, end_date) values( 1, '교양영어', 1, '2016/9/2','2016/11/30');

insert into course(course_id, course_name, professor_id, start_date, end_date) 
values( 2, '데이터베이스 입문', 3, '2016/8/20','2016/10/30');

insert into course(course_id, course_name, professor_id, start_date, end_date) 
values( 3, '회로이론', 2, '2016/10/20','2016/12/30');

insert into course(course_id, course_name, professor_id, start_date, end_date) 
values( 4, '공업수학', 4, '2016/11/2','2017/1/28');

insert into course(course_id, course_name, professor_id, start_date, end_date) 
values( 5, '객체지향프로그래밍', 3, '2016/11/1','2017/1/30');

# 문제 1
select student_id, student_name, heigth, s.department_id, department_name from student s inner join department d on  s.department_id=d.department_id;

# 문제 2 
select professor_id from professor where professor_name = "가교수";

# 문제 3 x
select * from professor;
select d.department_name, count(p.deparment_id) as '교수의 수' 
from department d left join professor p 
on  p.department_id = d.department_id group by d.department_name;

# 문제 4
select * from student s left join department d 
on s.department_id = d.department_id where d.department_name = "정보통신공학";

# 문제 5
select * from professor p left join department d 
on p.department_id = d.department_id where d.department_name = "정보통신공학";

# 과제 6
select student_name, department_name
from student s left join department d
on  s.department_id = d.department_id where student_name like "아%";

# 문제 7
select count(student_name) as "학생수" from student s
where heigth between 180 and 190;

# 문제 8
select department_name, max(heigth) as '최고키', avg(heigth) "평균키" 
from department d left join student s
on  s.department_id = d.department_id group by department_name;

# 문제 9 세모 
select * from student;
select student_name
from student s left join department d
on  s.department_id = d.department_id where s.department_id = 1;

# 문제 10 x
select * from course;
select s.student_name, c.course_name 
from student s join student_course t
on  s.student_id = t.student_id
 join course c
on  t.course_id = c.course_id
where start_date LIKE "2016/11/%" ;
DESC course; 


SELECT COUNT(*) FROM course WHERE start_date LIKE '2016/11/%';

# 문제 11 x
select student_name
from student s join student_course t
on  s.student_id = t.student_id
join course c
on  t.course_id = c.course_id
where course_name = '데이터베이스 입문' ;


# 문제 12 x 
select count(student_name)
from student s left join student_course t
on  s.student_id = t.student_id
left join course c
on  t.course_id = c.course_id
left join professor p
on  c.professor_id =  p.professor_id
where p.professor_name = "빌게이츠" ;

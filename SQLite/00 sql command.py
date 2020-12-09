
select std_id ,std_name
from student

 


select std_name
from student
where std_id = 'S006'

 


select *
from student
where sex = 'F'

 

select *
from record
where rcd < 60

 


select record.std_id, student.std_name,  course.course_name, record.rcd
from record , course , student 
where record.course_id = course.course_id
  and record.std_id = student.std_id

 

 

----------------
update record
set rcd = 55
where rcd < 50

 


 

---------

 


delete from student where std_id = 'AAAA'

 


select * from student where std_id like 'A%'
#start from A
select * from student where std_id like 'S02%'
#start from S02
select * from student where std_id like 'S02%9'
#start from S02 ends with 9
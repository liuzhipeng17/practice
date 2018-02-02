-- #2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
		-- step1: 刷选成生物成绩表
		-- step2: 刷选出物理成绩表
		-- step3: 连表查询，根据student_id, （采用Inner join,过滤掉只有一科成绩的）
		-- step4: 过滤出连表where 生物成绩 > 物理成绩
select A.student_id, A.num as "生物成绩",B.num as "物理成绩"
from
	(select student_id, course_id, num from score where course_id=(select cid from course where cname="生物")) as A
inner join (
	select student_id, course_id, num from score where course_id=(select cid from course where cname="物理")) as B
on A.student_id = B.student_id
where A.num > B.num ;


-- #3、查询平均成绩大于60分的同学的学号和平均成绩；
		-- group by student
		-- 计算平均成绩avg(num)
		-- having 二次刷选
select score.student_id, avg(num)  from score group by score.student_id having avg(num) > 60;


-- #4、查询所有同学的学号、姓名、选课数、总成绩；
		-- group by student.id
		-- sum(course_id)
		-- sum(num)
		-- 连表student
select student.sid, student.sname, B.courses, B.nums from student left join
	(select student_id, sum(course_id) as courses, sum(num) as nums from score group by score.student_id) as B 
on student.sid=B.student_id;


-- 5、查询姓“李”的老师的个数；
		-- like 
		-- count(1)
select count(1) from teacher where teacher.tname like '李%' ;


-- 6、查询没学过“叶平”老师课的同学的学号、姓名；
		-- 逆向思维，查询学过叶平老师课的学生

select student.sid, student.sname from student where student.sid not in(
	select distinct student_id from score 
	where 
		course_id in (select course.cid from course left join teacher on teacher.tid=course.teacher_id where teacher.tname="李平老师" )
);


-- 7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
		-- 刷选出学过001或者002课程的表A
		-- 按学生分组group by student_id 
		-- having count(1) > 1
		
select student.sid, student.sname from student left join
(select student_id, count(1) from score where course_id in (1,2) group by student_id having count(1) >1) as B
on B.student_id= student.sid;



-- 8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；
		-- 刷选出李平老师所教课程id 和id数
		-- 从score刷选出上过李平老师课的学生
		-- 分组,并统计course_id = 李平老师教的课程总数

select student.sid,student.sname from student where sid in(
select student_id from score where course_id in
	( select course.cid from course left join teacher on course.teacher_id=teacher.tid where teacher.tname="李平老师")
group by 
	student_id having count(1) = (select count(1) from course left join teacher on course.teacher_id=teacher.tid where teacher.tname="李平老师"));



-- 9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；

		-- 刷选出002课程的成绩表A
		-- 刷选出001课程的成绩表B
		-- 连表AB查询 wher A.num < B.num

select student.sid, student.sname from student where student.sid in 
(
	select A.student_id from 
		(select student_id, num from score where score.course_id=2) as A 
	left join
		(select student_id, num from score where score.course_id=1) as B on A.student_id = B.student_id where A.num < B.num
);


-- 10、查询有课程成绩小于60分的同学的学号、姓名；
		-- 从score刷选课程低于60分学生，并去重
		-- 连表
		
		
select student.sid, student.sname from student 
where student.sid 
	in (select distinct student_id  from score where num < 60);


-- 11、查询没有学全所有课的同学的学号、姓名；
		-- 逆向思维，刷选出学全所有课的学生

select student.sid, student.sname from student where student.sid not in(
select student_id from score group by student_id having count(1) = (select count(1) from course));


-- 12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
	
		-- 刷选出001学号学生的所学课程表， in

select student.sid, student.sname from student where student.sid in
(select distinct student_id from score where course_id in (select course_id from score where student_id=1) and student_id !=1);


-- 13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；

		-- 和12一样
		

-- 14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
		-- 刷选出学生表A，学生所学课程总数=002学生所学课程总数
		-- 刷选出学生表B，至少学过 002学生所有课程
		-- 连表AB查询
		-- note: 存在学生,不仅仅学了002学生的所有课程，还学其他课程

select student.sid, student.sname from student where student.sid in 
(
	select A.student_id from 
		(select student_id from score where student_id !=2 group by student_id 
																											having count(1) = (select count(1) from score where student_id=2)) as A
	inner join 
		(select student_id from score where student_id !=2 and course_id in (select course_id from score where student_id=2) 
																	 group by student_id having count(1) = (select count(1) from score where student_id=2)) as B
	on A.student_id = B.student_id
);
-- 
-- 15 --16 pass

-- 17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

-- 映射，双重循环

select student_id as "学生ID", 
				biology as "生物", 
				sport as "体育", 
				physics as "物理", 
				courses as "有效课程数",
				(total/courses) as "有效平均分"
from 
(
		select student_id, 
					biology,
					sport,
					physics,
					(if(isnull(biology),0,1) + if(isnull(sport),0,1) + if(isnull(physics),0,1)) as courses,
					(if(isnull(biology),0,biology) + if(isnull(sport),0,sport) + if(isnull(physics),0,physics)) as total 
					
		from 
				(select student_id,
					(select s1.num from score s1 where s1.student_id = s2.student_id and s1.course_id=(select cid from course where cname="生物")) as biology,
					(select s1.num from score s1 where s1.student_id = s2.student_id and s1.course_id=(select cid from course where cname="体育")) as sport,
					(select s1.num from score s1 where s1.student_id = s2.student_id and s1.course_id=(select cid from course where cname="物理")) as physics

				from score s2 )  
				
		as B

		group by B.student_id
) as C;
-- 
































































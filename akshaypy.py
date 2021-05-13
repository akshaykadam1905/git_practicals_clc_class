print("version v1 updates to v2")
	
	1-1
	1-M/M-1
	M-M
	
						Database --> sql --. not case sensitive
									ven --> multiple products --.
	
	create table prod_info(
		prod_id int,
		prod_name varchar(30),
		prod_qty  int,
		prod_price float,
		prod_ven int unique true,
		prod_remark varchar(30),
		primary key(prod_id),
		foreign key(prod_ven) references vendor_info(ven_id)
	)
	
	insert into prod_info values(1111,"Mobile",12,12898.23, -129,'xxxx')
	
	
	create table vendor_info(
		ven_id int,
		ven_name varchar(30) not null,
		ven_email varchar(30) unique not null,				
		ven_mobile bigint unique,
		ven_remark varchar(30) default 'NA',
		primary key(ven_id)	
	)
		
unique ---> cannot be duplicate
	
	
	unique --> cannot be duplicate --> duplicate values not allowed + single null allowed -- can be changed
	primary -> cannot be duplicate  --> duplicate value not allowed + no null,not event single null allowed --. cannot be changed
	
	fk --. refers to pk for another table.
	
	candidate --> 
	super key --. 
	
	

	--> create database sampledb
	--> use sampledb
	--> show databases
	--> create table --> refer above
	--> show tables  --> 
	--> desc tables --> 
	
	
	insert into vendor_info values(222,'VVVV','acb@gmail.com',1289222,'FFFFFF')
	update vendor_info set ven_mobile = 12971922 where ven_id = 1212
	delete from vendor_info where ven_id=122
	delete from vendor_info where ven_mobile > 800000000;		-->
	

		
			6 7 8 9	--> 10 digits
			2^31--
				21	47	48	36	47
				6
	4byte memory ---> NO --> 
	
						unique-True
	pid  pnm   page  permobile		VALUE PRESENT ASLI PAHIJE + UNIQUE + NO GOING TO CHANGE -> PK
	1    AA    20    21982			VALUE PRESENT ASLI PAHIJE + UNIQUE + SINGLE NULL ALLOWED -> CAN CHANGED
	2    BB    23    12992
	3	 CC	   34	 null
	
	BEST --> PK							CHANGE			DUPLICATE			PERSON
				AADHR CARD				NO					NO				 
				PASSPORTNUMBER
				PANCARD 
				
	
	Keys		--> 				PK -->  Unique + not null
									UK -->  UNIQUE + SINGLE NULL
									FK -->  
			Primary Key		--> one table -- 1 column -- jo uniquely identify karel any record within that table  ---> 		primary key = unique + not null --> single
							prod_id  --> unique + not null --> single --> any product la given table
							uniquely identify karu shkto
			
			
			ForeignKey
							jr --> if we specify relationship between two tables -->
							eka table chi fk --> jr table madhe use krt asel --> fk
			
			Unique Key -->  unique + single null allowed
			Candidate Key
			Super Key
			and so -->
	
	
	Constraints
	
create table VENDOR(
	ven_id int,
	ven_name varchar(30) not null,
	primary key(ven_id)	
)
create table PRODUCT(
		prod_id int,
		prod_name varchar(30),
		prod_qty  int,
		ven_id int null,
		primary key(prod_id),
		FOREIGN KEY (ven_id) REFERENCES VENDOR(ven_id)
);



insert into vendor values
(101,'Flipkart'),
(102,'Amazon'),
(103,'Snapdeal');

insert into product values
(1,'Mobile1',233,101),(2,'Mobile2',263,101),(3,'Mobile3',53,101),(4,'Mobile4',23,101),(5,'Mobile5',263,101),
(71,'Laptp1',253,102),(72,'Latop2',243,102),(73,'Latop3',223,102),(74,'Laptop4',234,102),(75,'Laptop5',283,102),(91,'TV',23,null),(92,'Remote',23,null);






select prod_id,prod_name,v.ven_id,ven_name from vendor v left join product p on v.ven_id=p.ven_id;


self-->

we are going to pick the data from two/more tables --  join 

t1		t2		-->  common property ---> 	join karun thevl ahe --> ven_id

select prod_id,prod_name,ven_id from lefthand lef join righthand on joinkrrproperty


	
	st1 -->  p  c  m					--> 
	        55  66 77					78
			
	st2		77	67	88					67
	
				priority --> 
							per--> same ---> pcm --> 
							
							
							
	 select * from prod_info where prod_Qty>=2 and prod_qty<=23;
	 
	 
	 
	 like 
		'%m'		--> shud end with m
		'm%'		--> start with m
		'%m%'		--> in between kuthe hi
		'__m%'		-->3rd position m ---> shvti kahi chalel 
		'%__m'		--> shvti m--> atleast any 2  chars
		
where clauses		
		and
		or
		between
		in
		conditions -->	
						>
						<
						>=
						<=
						==
		order by -- asc/desc
		limit
		
Joins --> 
		two tables relationship -- >
		
		set operations -->	maths-->
				un
		
		
	
create table employee (
  eid  int,
  firstname varchar(30),
  lastname varchar(30),
  manager_id int,
  primary key(eid)
);


insert into employee values
(4529,'Nancy','Young',4125),
(4238,'John','Simon',43290),
(4329,'Martina','Candreva',4125),
(4009,'Klaus','Koch',4329),
(4125,'Mafalda','Ranieri',NULL),
(4500,'Jakub','Hrabal',4529),
(4118,'Moira','Areas',4952),
(4012,'Jon','Nilssen',4952),
(4952,'Sandra','Rajkovic',4529),
(4444,'Seamus','Quinn',4329);
sshoe

SELECT 
	e1.eid,
    e1.firstname,
    e1.lastname,
    count(e1.eid)
FROM employee e1 
JOIN employee e2 
ON e1.manager_id = e2.eid;
GROUP BY e1.eid, e1.firstname, e1.lastname;



manager--> no of emps reported to

SELECT 
	sup.eid manager_id,
    sup.firstname manager_name,
    sup.lastname manager_last_name,
    COUNT(sub.eid) AS number_of_employees
FROM employee sub 
JOIN employee sup 
ON sub.manager_id = sup.eid
GROUP BY sup.eid, sup.firstname, sup.lastname;


--find-- manager for an employee
SELECT 
	sub.eid AS subordinate_id,
    sub.firstname AS subordinate_first_name,
    sub.lastname AS subordinate_last_name,
    sup.eid AS superior_id,
    sup.firstname AS superior_first_name,
    sup.lastname AS superior_last_name
FROM employee sub 
JOIN employee sup 
ON sub.manager_id = sup.eid
ORDER BY superior_id;
		
		
		



create table prod_info(
		prod_id int,
		prod_name varchar(30),
		prod_qty  int,
		prod_price float,
		prod_ven varchar(30),
		prod_remark varchar(30),
		primary key(prod_id)
);
insert into prod_info values
(101,'Mobile',2,129.23,'Flikart1','XXX1'),
(102,'Mobile',43,1289.23,'Flikart2','XXX4'),
(103,'Laptop',53,1283.23,'Flikart3','XXX3'),
(104,'SmartMobile',37,7289.23,'Flikart4','X5XX'),
(105,'Remote',233,61289.23,'Flikart','XXX4'),
(106,'lappy',2,12859.23,'Flikart1','XXX3'),
(107,'charger',3,41289.23,'Flikart1','2XXX'),
(108,'Tv',26,12839.23,'Flikart1','XXX'),
(109,'Motherboard',273,12689.23,'Flikart','XXX1'),
(110,'Cpu',23,12895.23,'Flikart2','XXX'),
(111,'battery',233,14289.23,'Flikart2','XXX1'),
(112,'Mouse',233,12389.23,'Flikart2','XXX1');




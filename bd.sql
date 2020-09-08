drop database bd_task4;
create database bd_task4;
use bd_task4;
create table tb_user (
    id int auto_increment primary key not null ,
    name varchar(30) not null,
    a_p varchar(30) not null ,
    a_m varchar(30) not null ,
    edad char(3) ,
    correo varchar(30) ,
    telefono varchar(30)
);

insert into tb_user values (null, 'Golang', 'Go', 'Google', '18', 'golang.go.com', '6000')
select id, concat(name,' ',a_p,' ',a_m) ,correo
       from tb_user;
       
select * from tb_user;
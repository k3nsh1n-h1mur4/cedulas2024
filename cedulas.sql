use flaskapi;

delimiter //
create procedure insertUser(username varchar(15), password varchar(250), is_admin tinyint)
begin
	INSERT INTO users(username, password, is_admin) VALUES(username, password, is_admin);
end //


select * from users;

delimiter //
create procedure getUsers()
begin
	select * from users;
end //

delimiter //
create procedure getUser(in username varchar(15))
begin
	select * from flaskapi.users s where s.username = username;
end //

drop procedure getUser;

call getUser('k3nsh1n');

create table cedula(id integer not null auto_increment primary key, app varchar(100) not null, apm varchar(100) not null, nombre varchar(100) not null, domicilio varchar(100) not null, colonia varchar(100) not null, mcpio varchar(100) not null, cp varchar(10) not null, local varchar(100) not null, num_cel varchar(15) not null, email varchar(100) not null, l_nac varchar(100) not null, f_nac varchar(50) not null, nss varchar(11) not null, rfc varchar(13), curp varchar(18) not null, edo_civil varchar(15) not null, sexo varchar(15) not null, matricula varchar(15)not null, categoria varchar(150), adsc varchar(150), turno varchar(50), t_contr varchar(40), f_ingr varchar(50), antiguedad varchar(30), createdat timestamp not null default NOW());

delimiter //
create procedure insertCedula(app varchar(100), apm varchar(100), nombre varchar(100), domicilio varchar(100), colonia varchar(100), mcpio varchar(100), cp varchar(10), local varchar(100), num_cel varchar(15), email varchar(100), l_nac varchar(100), f_nac varchar(50), nss varchar(11), rfc varchar(13), curp varchar(18), edo_civil varchar(15), sexo varchar(15), matricula varchar(15), categoria varchar(150), adsc varchar(150), turno varchar(50), t_contr varchar(40), f_ingr varchar(50), antiguedad varchar(30))
begin
 INSERT INTO cedula(app, apm, nombre, domicilio, colonia, mcpio, cp, local, num_cel, email, l_nac, f_nac, nss, rfc, curp, edo_civil, sexo, matricula, categoria, adsc, turno, t_contr, f_ingr, antiguedad) VALUES(app, apm, nombre, domicilio, colonia, mcpio, cp, local, num_cel, email, l_nac, f_nac, nss, rfc, curp, edo_civil, sexo, matricula, categoria, adsc, turno, t_contr, f_ingr, antiguedad);
end //

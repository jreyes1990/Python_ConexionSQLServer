select * from pais;
select * from cine;

insert into pais (idpais,nombre) values(5,'EEUU');
insert into pais (idpais,nombre) values(6,'España');

CREATE TABLE cine (
id_cine INT PRIMARY KEY NOT NULL,
nombre VARCHAR(25) NOT NULL,
id_tipo_cine INT,
direccion VARCHAR(50),
fecha_apertura DATETIME,
b_habilitado INT
);

insert into cine values(1,'Cine Cas',1,'Paseo Colon','15-03-2021',1);
insert into cine values(2,'Cine Lark',2,'Paseo Rincon','15-12-2011',1);
insert into cine values(3,'Cine Rest',3,'Paseo Market','14-05-2012',1);
insert into cine values(4,'Super Cinemax',1,'En la esquina','09-11-2019',0);

create procedure uspListarPais
as
begin
	select idpais,nombre 
	from pais;
end;

create procedure uspCantidadPais
as
begin
	select count(*) 
	from pais;
end;

create procedure uspFiltrarPais(@id int)
as
begin
	select idpais,nombre 
	from pais
	where idpais=@id;
end;

exec uspListarPais;
exec uspCantidadPais;
exec uspFiltrarPais 4;
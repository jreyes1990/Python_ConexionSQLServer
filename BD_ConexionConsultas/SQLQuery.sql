select * from pais;

insert into pais (idpais,nombre) values(5,'EEUU');
insert into pais (idpais,nombre) values(6,'España');

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

exec uspListarPais;
exec uspCantidadPais;
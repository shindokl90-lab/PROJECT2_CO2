
--select country,
--       sum( solid_fuel + liquid_fuel + gas_fuel + cement + gas_flaring) as total
--  from co2_values
--  group by country
--  order by total desc;
  
copy (
select country, total from co2_dirty30
	)
to 'C:\Users\Salty\co2_dirty30.txt' WITH DELIMITER ',';
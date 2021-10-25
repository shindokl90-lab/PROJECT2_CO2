-- Table: public.CO2_Table_Raw

-- DROP TABLE public."CO2_Table_Raw";
DROP TABLE if exists CO2_Countries cascade; 
DROP TABLE if exists CO2_Values;

CREATE TABLE CO2_Countries(
	country varchar(50) primary key
);

CREATE TABLE CO2_Values(
	year bigint, 
	country text,  
	solid_fuel bigint, 
	liquid_fuel bigint, 
	gas_fuel bigint, 
	cement bigint, 
	gas_flaring bigint, 
	per_capita double precision,
	primary key (year, country),
	foreign key (country) references CO2_Countries(country)
);

Insert into CO2_Countries(country) SELECT distinct "Country" from "CO2_Table_Raw";

Insert into CO2_Values(year, country, solid_fuel, liquid_fuel, 
					   gas_fuel, cement, gas_flaring, per_capita) 
SELECT "Year", "Country", "Solid Fuel", "Liquid Fuel",
       "Gas Fuel", "Cement", "Gas Flaring", "Per Capita"
	   from "CO2_Table_Raw"; 

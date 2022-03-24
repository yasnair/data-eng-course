DROP  TABLE "fact_trip";
DROP  TABLE "dim_bike";
DROP  TABLE "dim_date";
DROP TABLE "dim_station";

DROP  TABLE "dim_user_type";

DROP TABLE "dim_gender";
DROP TABLE "rawdata";

CREATE TABLE IF NOT EXISTS dim_station(  
    station_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitud VARCHAR(255),
    longitude  VARCHAR(255)

);

CREATE TABLE IF NOT EXISTS dim_bike(  
    bike_id INT NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS dim_user_type(  
    user_type_id SERIAL PRIMARY KEY,
    user_type VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_gender(  
    gender_id INT PRIMARY KEY,
    gender VARCHAR(20) NOT NULL
);


CREATE TABLE IF NOT EXISTS rawdata(  
  tripduration            INT, 
  starttime               TIMESTAMP, 
  stoptime                TIMESTAMP, 
  start_station_id        INT, 
  start_station_name      VARCHAR(255),  
  start_station_latitude  VARCHAR(255),
  start_station_longitude VARCHAR(255),
  end_station_id          INT, 
  end_station_name        VARCHAR(255),
  end_station_latitude    VARCHAR(255),
  end_station_longitude   VARCHAR(255) ,
  bike_id                 INT,                     
  user_type               VARCHAR(20),
  birth_year              INT,     
  gender                  INT
);


CREATE TABLE IF NOT EXISTS dim_date
(
  date_id                  INT NOT NULL,
  date_actual              DATE NOT NULL,
  day_suffix               VARCHAR(4) NOT NULL,
  day_name                 VARCHAR(9) NOT NULL,
  day_of_week              INT NOT NULL,
  day_of_month             INT NOT NULL,
  day_of_quarter           INT NOT NULL,
  day_of_year              INT NOT NULL,
  week_of_month            INT NOT NULL,
  week_of_year             INT NOT NULL,
  week_of_year_iso         CHAR(10) NOT NULL,
  month_actual             INT NOT NULL,
  month_name               VARCHAR(9) NOT NULL,
  month_name_abbreviated   CHAR(3) NOT NULL,
  quarter_actual           INT NOT NULL,
  quarter_name             VARCHAR(9) NOT NULL,
  year_actual              INT NOT NULL,
  first_day_of_week        DATE NOT NULL,
  last_day_of_week         DATE NOT NULL,
  first_day_of_month       DATE NOT NULL,
  last_day_of_month        DATE NOT NULL,
  first_day_of_quarter     DATE NOT NULL,
  last_day_of_quarter      DATE NOT NULL,
  first_day_of_year        DATE NOT NULL,
  last_day_of_year         DATE NOT NULL,
  mmyyyy                   CHAR(6) NOT NULL,
  mmddyyyy                 CHAR(10) NOT NULL,
  weekend_indr             BOOLEAN NOT NULL
);

ALTER TABLE public.dim_date ADD CONSTRAINT dim_date_date_id_pk PRIMARY KEY (date_id);

CREATE INDEX dim_date_date_actual_idx
  ON dim_date(date_actual);



CREATE TABLE IF NOT EXISTS fact_trip(  
    start_station_id      INT REFERENCES  dim_station,
    end_station_id        INT REFERENCES  dim_station,
    bike_id               INT REFERENCES  dim_bike,
    user_type_id          INT REFERENCES  dim_user_type,
    date_id               INT REFERENCES  dim_date,
    start_time            TIMESTAMP NOT NULL,
    stop_time             TIMESTAMP NOT NULL,
    trip_duration         INT NOT NULL, 
    birth_year            INT,
    gender                INT,
    constraint pk primary key (start_station_id, end_station_id ,bike_id, user_type_id, date_id, start_time, stop_time)
    
);


DROP TABLE if exists fact_trip;
DROP TABLE if exists dim_station;
DROP TABLE if exists dim_bike;
DROP TABLE if exists dim_user_type;
DROP TABLE if exists dim_date;
CREATE TABLE dim_station(  
    station_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitud POINT NOT  NULL,
    longitude POINT NOT  NULL

);

CREATE TABLE dim_bike(  
    bike_id INT NOT NULL PRIMARY KEY
);

CREATE TABLE dim_user_type(  
    user_type_id INT NOT NULL PRIMARY KEY,
    user_type VARCHAR(20) NOT NULL
);

CREATE TABLE dim_date
(
  date_id              INT NOT NULL,
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



CREATE TABLE fact_trip(  
    station_id      INT REFERENCES  dim_station,
    bike_id         INT REFERENCES  dim_bike,
    user_type_id    INT REFERENCES  dim_user_type,
    date_id         INT REFERENCES  dim_date,
    trip_duration   INT NOT NULL, 
    start_time      TIMESTAMP NOT NULL,
    stop_time       TIMESTAMP NOT NULL,
    birth_year      INT,
    gender          INT,
    constraint pk primary key (station_id ,bike_id, user_type_id, date_id)
    

);


CREATE TABLE rawdata(  
  tripduration           INT,
  starttime               TIMESTAMP,
  stoptime                TIMESTAMP,
  start_station_id        INT,
  start_station_name      VARCHAR(255),  
  start_station_latitude  POINT,
  start_station_longitude POINT,
  end_station_id          INT,
  end_station_name        VARCHAR(255),
  end_station_latitude    POINT,
  end_station_longitude   POINT ,
  bike_id                 INT,                    
  user_type               VARCHAR(20),
  birth_year              INT,      
  gender                  INT
);





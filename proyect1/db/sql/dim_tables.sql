
/* DIM_STATION */
INSERT  INTO "dim_station"
SELECT * FROM
(
  SELECT DISTINCT start_station_id as station_id,
                start_station_name as station_name,
                start_station_latitude as station_latitude,
                start_station_longitude as station_longitude
  FROM "rawdata"
  UNION
  SELECT DISTINCT end_station_id as station_id,
                  end_station_name as station_name,
                  end_station_latitude as station_latitude,
                  end_station_longitude as station_longitude
  FROM "rawdata"
) as station_raw
where station_raw.station_id NOT IN
(
  SELECT station_id FROM "dim_station"
)
order by station_raw.station_id ASC;

SELECT COUNT(*) FROM "dim_station";

/* DIM_BIKE*/ 
INSERT INTO "dim_bike"
  SELECT DISTINCT bike_id
  FROM "rawdata" AS bike_raw
  WHERE bike_id NOT IN (
    SELECT bike_id FROM "dim_bike"
  ) ORDER BY bike_id ASC;

SELECT COUNT(*) FROM "dim_bike";

/* DIM_USER_TYPE*/ 
INSERT INTO dim_user_type(user_type) 
SELECT user_type
FROM(
  SELECT DISTINCT user_type
  FROM "rawdata" 
  WHERE user_type NOT IN(
    SELECT user_type FROM "dim_user_type"
  ) 
)AS usertype_raw;
SELECT COUNT(*) FROM "dim_user_type";

UPDATE "rawdata" SET user_type = 'DUMMY' where user_type is NULL;

INSERT INTO fact_trip(
    start_station_id,
    end_station_id,
    bike_id,
    user_type_id,
    date_id,
    start_time,
    stop_time,
    trip_duration, 
    birth_year,
    gender
)
SELECT rd.start_station_id,
       rd.end_station_id,
       rd.bike_id,
       ut.user_type_id ,
       CAST(to_char(date(rd.starttime), 'YYYYMMDD') as INTEGER) as date_id,
       rd.starttime,
       rd.stoptime,
       rd.tripduration,
       rd.birth_year,
       rd.gender 
FROM "rawdata" as rd
JOIN "dim_station" AS st_1 ON rd.start_station_id = st_1.station_id
JOIN "dim_station" AS st_2 ON rd.end_station_id = st_2.station_id
JOIN "dim_bike" AS bike ON rd.bike_id = bike.bike_id
JOIN "dim_user_type" AS ut ON rd.user_type = ut.user_type;
SELECT COUNT(*) FROM "fact_trip";










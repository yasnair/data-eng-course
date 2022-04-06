SELECT  dd.year_actual, 
	    dd.week_of_year,
        dd.day_name,
        count(ft.trip_duration),
        sum(ft.trip_duration),
        AVG(ft.trip_duration)
FROM fact_trip as ft
  JOIN dim_date as dd ON dd.date_id = ft.date_id
  GROUP BY dd.day_name, dd.year_actual, dd.week_of_year
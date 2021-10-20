SELECT A.ID, A.NAME
  FROM SUBWAY_STATIONS A
     , LINE_ROUTES B
 WHERE A.ID = B.STATION_ID
   AND NOT EXISTS (SELECT 1
                     FROM LINE_ROUTES C
                    WHERE A.ID = C.STATION_ID
                      AND C.LINE_COLOR IN ('Red', 'Green'))
 ORDER BY A.ID


 SELECT A.ID, A.NAME
  FROM SUBWAY_STATIONS A
 WHERE NOT EXISTS (SELECT 1
                     FROM LINE_ROUTES C
                    WHERE A.ID = C.STATION_ID
                      AND C.LINE_COLOR IN ('Red', 'Green'))
 ORDER BY A.ID
SELECT DISTINCT [fuel-type] AS fueltype,
       [aspiration],
       [num-of-doors] AS doors,
       [body-style] AS body,
       [drive-wheels] AS drive,
       [engine-location] AS engineloc,
       [wheel-base] AS wheelbase,
       [length],
       [width],
       [height],
       [curb-weight] AS weight,
       [engine-type] AS enginetype,
       CASE
        WHEN [num-of-cylinders] IN ('two', 'three', 'four') THEN 'four-or-less'
        WHEN [num-of-cylinders] IN ('five', 'six') THEN 'five-six'
        WHEN [num-of-cylinders] IN ('eight', 'twelve') THEN 'eight-twelve'
        ELSE 'other'        
       END
       AS cylinders,
       [engine-size] AS enginesize,
       [fuel-system] AS fuelsystem,
       [bore],
       [stroke],
       [compression-ratio] AS compression,
       [horsepower],
       [peak-rpm] AS rpm,
       [city-mpg] AS citympg,
       [highway-mpg] AS highwaympg,
       [price],
       [make],
       log([price]) AS lnprice
FROM T1
INNER JOIN T2
ON T1.[make-id] = T2.[make-id]
WHERE  [fuel-type] IS NOT NULL AND
       [aspiration] IS NOT NULL AND
       [num-of-doors] IS NOT NULL AND
       [body-style] IS NOT NULL AND
       [drive-wheels] IS NOT NULL AND
       [engine-location] IS NOT NULL AND
       [wheel-base] IS NOT NULL AND
       [length] IS NOT NULL AND
       [width] IS NOT NULL AND
       [height] IS NOT NULL AND
       [curb-weight] IS NOT NULL AND
       [engine-type] IS NOT NULL AND
       [num-of-cylinders] IS NOT NULL AND
       [engine-size] IS NOT NULL AND
       [fuel-system] IS NOT NULL AND
       [bore] IS NOT NULL AND
       [stroke] IS NOT NULL AND
       [compression-ratio] IS NOT NULL AND
       [horsepower] IS NOT NULL AND
       [peak-rpm] IS NOT NULL AND
       [city-mpg] IS NOT NULL AND
       [highway-mpg] IS NOT NULL AND
       [price] IS NOT NULL AND
       [make] IS NOT NULL;

SELECT
    CASE
        WHEN T.A + T.B <= T.C OR T.B + T.C <= T.A OR T.A + T.C <= T.B THEN 'Not A Triangle'
        WHEN T.A = T.B AND T.B = T.C THEN 'Equilateral'
        WHEN T.A = T.B OR T.B = T.C OR T.C = T.A THEN 'Isosceles'
        ELSE 'Scalene'
    END as triangle_types
FROM TRIANGLES T
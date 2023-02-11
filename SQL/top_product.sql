with transaction_table AS (
  SELECT 1 AS transaction,1 AS product_id,5 AS quantity UNION ALL
  SELECT 1, 2, 7 UNION ALL
  SELECT 2, 3, 1 UNION ALL
  SELECT 3, 2, 3
),
product AS (
  SELECT 1 AS product_id, 'aa' AS product_name,10 AS retail_price,1 AS product_class_id UNION ALL
  SELECT 2, 'bb', 20, 1 UNION ALL
  SELECT 3, 'cc', 30, 2
),
product_class AS (
  SELECT 1 AS product_class_id,'Class A' AS product_class_name UNION ALL
  SELECT 2 ,'Class B' UNION ALL
  SELECT 3, 'Class C'
)

SELECT 
product_class_name
,RANK() over (partition by product_class_name ORDER by sales_value DESC) as ranking
,product_name
,sales_value
FROM (
SELECT 
pc.product_class_name
,p.product_name
,SUM(tc.quantity * p.retail_price) AS sales_value
FROM transaction_table tc 
LEFT JOIN product p ON tc.product_id = p.product_id
LEFT JOIN product_class pc ON p.product_class_id = pc.product_class_id
GROUP BY 
pc.product_class_name
,p.product_name
)
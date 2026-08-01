-- Databricks notebook source
WITH tb_freq AS (

  SELECT descUF,
        count(*) AS freqAbsoluta
  FROM silver.olist.vendedor
  GROUP BY ALL

)

SELECT *,
       freqAbsoluta / (SELECT sum(freqAbsoluta) FROM tb_freq) AS freqRelativa,
       sum(freqAbsoluta / (SELECT sum(freqAbsoluta) FROM tb_freq)) OVER (ORDER BY freqAbsoluta DESC) AS freqRelativaAcum

FROM tb_freq

-- COMMAND ----------

SELECT 
      descUf,
      count(*) AS FreqAbsoluta,
      count(*) / SUM(COUNT(*)) over () AS freqRelativa,
      sum(count(*) / SUM(COUNT(*)) over ()) over (order by count(*) desc) AS freqRelativaAcum

FROM silver.olist.vendedor

group by all
order by freqRelativa desc

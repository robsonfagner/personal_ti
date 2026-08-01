-- Databricks notebook source
SELECT
      avg(Receita) AS avgReceita,
      median(Receita) AS medianReceita,
      percentile(Receita, 0.25) AS Quartile1Receita,
      percentile(Receita, 0.75) AS Quartile3Receita,
      var_pop(Receita) AS varReceita,
      stddev_pop(Receita) AS stdReceita,
      max(Receita) - min(Receita) AS amplitudeReceita,

      avg(Frequencia) AS avgFrequencia,
      median(Frequencia) AS medianFrequencia,
      percentile(Frequencia, 0.25) AS Quartile1Frequencia,
      percentile(Frequencia, 0.75) AS Quartile3Frequencia

FROM sandbox.teomewhy.vendedores_fv

-- COMMAND ----------

SELECT

      t2.descUF,
      ROUND(avg(Receita),2) AS avgReceita,
      ROUND(median(Receita),2) AS medianReceita,
      ROUND(percentile(Receita, 0.25),2) AS Quartile1Receita,
      ROUND(percentile(Receita, 0.75),2) AS Quartile3Receita,
      ROUND(var_pop(Receita),2) AS varReceita,
      ROUND(stddev_pop(Receita),2) AS stdReceita,
      ROUND(max(Receita) - min(Receita),2) AS amplitudeReceita,

      avg(Frequencia) AS avgFrequencia,
      median(Frequencia) AS medianFrequencia,
      percentile(Frequencia, 0.25) AS Quartile1Frequencia,
      percentile(Frequencia, 0.75) AS Quartile3Frequencia

FROM sandbox.teomewhy.vendedores_fv AS t1

LEFT JOIN silver.olist.vendedor AS t2
ON t1.idVendedor = t2.idVendedor

GROUP BY ALL

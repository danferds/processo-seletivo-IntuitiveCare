-- Lista as 10 operadoras com maiores despesas no último trimestre de 2024 (terceiro trimestre) que tem a descrição a baixo 
SELECT o.razao_social AS operadora,
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis_2024 d
JOIN operadoras_ativas_ans o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND d.trimestre = 'terceiro trimestre'
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- Lista as 10 operadoras com maiores despesas no ano de 2024 que tem a descrição a baixo 
SELECT o.razao_social AS operadora,
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis_2024 d
JOIN operadoras_ativas_ans o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND EXTRACT(YEAR FROM d.data) = 2024
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
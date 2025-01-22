-- Demonstrações contábeis do ano de 2023 (trimestres: primeiro, segundo, terceiro e quarto)
CREATE TABLE demonstracoes_contabeis_2023 (
    data DATE NOT NULL,
    reg_ans INTEGER NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT,
    vl_saldo_inicial NUMERIC(18, 2),
    vl_saldo_final NUMERIC(18, 2),
	trimestre TEXT NOT NULL
);

COPY demonstracoes_contabeis_2023 (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final, trimestre)
FROM 'C:\dev\processo_seletivo_intuitivecare\datasets\demonstracoes_contabeis_2023\df_demonstracoes_contabeis_2023_v1.csv'
DELIMITER ';'
CSV HEADER;

-- Demonstrações contábeis do ano de 2024 (trimestres: primeiro, segundo e terceiro)
CREATE TABLE demonstracoes_contabeis_2024 (
    data DATE NOT NULL,
    reg_ans INTEGER NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT,
    vl_saldo_inicial NUMERIC(18, 2),
    vl_saldo_final NUMERIC(18, 2),
	trimestre TEXT NOT NULL
);

COPY demonstracoes_contabeis_2024 (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final, trimestre)
FROM 'C:\dev\processo_seletivo_intuitivecare\datasets\demonstracoes_contabeis_2024\df_demonstracoes_contabeis_2024_v1.csv'
DELIMITER ';'
CSV HEADER;

-- Operadoras ativas na ans
CREATE TABLE operadoras_ativas_ans (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao INT,
    data_registro_ans DATE
);

copy operadoras_ativas_ans( registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    regiao_de_comercializacao,
    data_registro_ans
) 
FROM 'C:\dev\processo_seletivo_intuitivecare\datasets\dados_cadastrais_das_operadoras_ativas_na_ans\Relatorio_cadop.csv'
DELIMITER ';' 
CSV HEADER 
QUOTE '"';
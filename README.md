# Documentação do Teste

## Estrutura de Pastas

### **controller**

- **operator_controller.py**: Responsável pela camada controller da API.

### **datasets**

- Armazena os arquivos de dados utilizados e gerados durante o processo.

### **docs**

- Contém arquivos notebooks, coleções Postman e anexos.

### **main**

- **initialize_api.py**: Responsável por inicializar a API.
- **process_medical_procedure_data.py**: Executa os scripts de extração e estruturação dos dados.

### **repository**

- **operator_repository.py**: Responsável pela camada repository da API.

### **scripts**

- **dataset_column_utils.py**: Renomeia as colunas do dataset para o teste de transformação de dados.
- **extraction_pdf.py**: Extrai tabelas do PDF rol de procedimentos e eventos em saúde.
- **queries.sql**: Realiza as  consultas SQL solicitadas no teste de banco de dados.
- **setup_and_import.sql**: Estrutura as tabelas e importa os dados para o teste de banco de dados.

### **service**

- **operator_service.py**: Responsável pela camada service da API.

---

## Tecnologias e Ferramentas Utilizadas

- **Python**
- **Flask**
- **Pandas**
- **Tabula**
- **PostgreSQL**
- **Postman**

---

## Descrição dos Testes Realizados

### Teste de Web Scraping

- Dois arquivos PDF foram baixados e utilizados na etapa de transformação de dados.

### Teste de Transformação de Dados

1. **Extração de Tabelas**:
    - Utilizei o Tabula para extrair tabelas do PDF rol procedimentos e eventos em saúde, gerando um arquivo CSV com os dados brutos extraídos.
2. **Renomeação de Colunas**:
    - Renomeei as colunas “OD” e “AMB” como solicitado. Além disso, renomeei todas as demais colunas do dataset para deixar padronizado. O resultado foi um novo arquivo CSV com as colunas renomeadas.
3. **Etapas Adicionais**:
    - **Demonstrações contábeis de 2023**:
        - Combinei quatro arquivos CSV de demonstrações contábeis de 2023 em um único CSV.
        - Adicionei uma nova coluna chamada “trimestre” para identificar os trimestres de 2023.
        - Realizei tratamentos para facilitar a manipulação dos dados no banco.
    - **Demonstrações contábeis de 2024**:
        - Combinei três arquivos CSV de demonstrações contábeis dos três primeiros trimestres de 2024 em um único CSV.
        - Adicionei uma nova coluna chamada “trimestre” para identificar os trimestres de 2024.
        - Realizei tratamentos para facilitar a manipulação dos dados no banco.
    - **Limpeza de Dados**:
        - Realizei a limpeza do dataset de “rol_de_procedimentos_e_eventos_em_saude”, gerando um novo arquivo CSV com os dados tratados.

### Teste de Banco de Dados

- Desenvolvi um script para:
    1. Criação das tabelas necessárias.
    2. Importação dos arquivos CSV para o banco de dados PostgreSQL.
- Outro script foi criado para realizar as consultas solicitadas no teste.

### Teste de API

- Adotei o padrão MVC com as seguintes camadas:
    1. **Controller**: Gerencia as requisições.
    2. **Service**: Contém as funções necessárias.
    3. **Repository**: Interage com o CSV  “Relatorio_cadop.csv”.
- Criei duas rotas GET:
    1. Listar todas as operadoras.
    2. Buscar uma operadora pelo CNPJ.
- Utilizei o Postman para testar as rotas implementadas.

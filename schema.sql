-- Alexandre Nobuharu Sato, Ribeirão Pires - SP, 24 de novembro de 2021
-- rateio-de-custos-server.postgres.database.azure.com dbname=postgres

-- Creating a test table
CREATE TABLE contratos (
    id          SERIAL     NOT NULL,
    contrato    INT,
    fornecedor  CHAR(50),
    objeto      CHAR(255),
    valor       INT,
    mes         INT,
    PRIMARY KEY (id)
);

-- Imputing some values on the test table
INSERT INTO contratos (contrato, fornecedor, objeto, valor, mes) VALUES (1001777, 'FoobarLtda', 'Prestação de serviços de enxugação de gelo de para de o Metrô', 17777, 10);
INSERT INTO contratos (contrato, fornecedor, objeto, valor, mes) VALUES (1001666, 'DevFullStackSA', 'Prestação de serviços de PenTest alheio', 17666, 10);
INSERT INTO contratos (contrato, fornecedor, objeto, valor, mes) VALUES (1001333, 'ForaBozoLtda', 'Prestação de serviços de erradicação de comportamento inaltêntico coordenado para o Metrô', 7131313, 10);


-- Creating a user table
CREATE TABLE usuarios (
    id          SERIAL      NOT NULL,
    nome        CHAR(50),
    email       CHAR(50)    UNIQUE,
    senha       CHAR(255),
    PRIMARY KEY (id)
);

-- Imputing some values on the test table
INSERT INTO usuarios (nome, email, senha) VALUES ('foo', 'foo@bar.com', 'bar');
INSERT INTO usuarios (nome, email, senha) VALUES ('pepa', 'pepa@pig.com', 'pig');
INSERT INTO usuarios (nome, email, senha) VALUES ('luke', 'luke@skywalker.com', 'skywalker');


-- Creating a lista_cns table
CREATE TABLE lista_cns (
    id              SERIAL      NOT NULL,
    cn              BIGINT         UNIQUE,
    empresa         CHAR(100),
    objeto          CHAR(500),
    data_termino    CHAR(50),
    analista        CHAR(255),
    substituto      CHAR(255),
    coordenadoria   CHAR(50),
    alias           CHAR(50),
    PRIMARY KEY (id)
);

COPY mytable FROM '/path/to/csv/file' WITH CSV HEADER; -- must be superuser
COPY lista_cns FROM '/mnt/e/filho/Prototipos_Metro/sites/lista_cns.csv' WITH CSV HEADER;

-- charge from csv 
\copy mytable [ ( column_list ) ] FROM '/path/to/csv/file' WITH CSV HEADER
\copy lista_cns  ( cn, empresa, objeto, data_termino, analista, substituto, coordenadoria, alias )  FROM '/mnt/e/filho/Prototipos_Metro/sites/lista_cns.csv' WITH delimiter ';' CSV HEADER encoding 'windows-1251';

-- fix utf8 encoding error
command$: file lista_cns.csv
output: lista_cns.csv: ISO-8859 text, with very long lines, with CRLF, LF line terminators

-- converting ISO-8859 > utf-8
iconv -c -t utf-8 lista_cns.csv > lista_cns.utf8.csv
\copy lista_cns  ( cn, empresa, objeto, data_termino, analista, substituto, coordenadoria, alias )  FROM '/mnt/e/filho/Prototipos_Metro/sites/lista_cns.utf8.csv' WITH delimiter ';' CSV HEADER;


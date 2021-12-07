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

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
INSERT INTO contratos (CONTRATO, FORNECEDOR, OBJETO, VALOR, MES) VALUES (1001777, 'FoobarLtda', 'Prestação de serviços de enxugação de gelo de para de o Metrô', 17777, 10);
INSERT INTO contratos (CONTRATO, FORNECEDOR, OBJETO, VALOR, MES) VALUES (1001666, 'DevFullStackSA', 'Prestação de serviços de PenTest alheio', 17666, 10);
INSERT INTO contratos (CONTRATO, FORNECEDOR, OBJETO, VALOR, MES) VALUES (1001333, 'ForaBozoLtda', 'Prestação de serviços de erradicação de comportamento inaltêntico coordenado para o Metrô', 7131313, 10);


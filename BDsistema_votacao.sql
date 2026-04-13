CREATE DATABASE sistema_votacao;

USE sistema_votacao;

CREATE TABLE eleitores (
	eleitor_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    eleitor_nome VARCHAR (50) NOT NULL,
    eleitor_titulo VARCHAR (12) UNIQUE NOT NULL,
    eleitor_cpf VARCHAR (11) UNIQUE NOT NULL,
    eleitor_mesario BOOL DEFAULT FALSE NOT NULL,
    eleitor_horavoto DATETIME,
    eleitor_chaveacesso CHAR (7),
    eleitor_situacao BOOL DEFAULT FALSE NOT NULL /*SE A PESSOA JÁ VOTOU OU NÃO*/
);

CREATE TABLE candidatos (
	cand_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    can_nome VARCHAR(50),
    cand_numero INT NOT NULL,
    cand_partido VARCHAR (20)
);

CREATE TABLE votos (
	voto_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    voto_horario DATETIME,
    voto_candnumero INT,
    voto_protocolo INT
);
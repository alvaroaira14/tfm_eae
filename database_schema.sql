CREATE TABLE IF NOT EXISTS `tfm_database`.`ciudad` (
    `id_ciudad` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NULL DEFAULT NULL,
    `pais` VARCHAR(45) NULL DEFAULT NULL,
    `provincia` VARCHAR(45) NULL DEFAULT NULL,
    `municipio` VARCHAR(45) NULL DEFAULT NULL,
    PRIMARY KEY (`id_ciudad`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`direccion` (
    `id_direccion` INT NOT NULL AUTO_INCREMENT,
    `id_ciudad` INT NULL DEFAULT NULL,
    `calle` VARCHAR(45) NULL DEFAULT NULL,
    `numero` INT NULL DEFAULT NULL,
    `piso` VARCHAR(45) NULL DEFAULT NULL,
    `distrito` VARCHAR(45) NULL DEFAULT NULL,
    `subdistrito` VARCHAR(45) NULL DEFAULT NULL,
    `codigo_postal` INT NULL DEFAULT NULL,
    `latitud` POINT NULL DEFAULT NULL,
    `longitud` POINT NULL DEFAULT NULL,
    PRIMARY KEY (`id_direccion`),
    FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad`(`id_ciudad`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`propietario`(
    `id_propietario` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NULL DEFAULT NULL,
    `apellidos` VARCHAR(45) NULL DEFAULT NULL,
    `num_inmuebles` INT NULL DEFAULT NULL,
    `val_inmuebles` FLOAT NULL DEFAULT NULL,
    PRIMARY KEY (`id_propietario`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`inmueble`(
    `id_inmueble` INT NOT NULL AUTO_INCREMENT,
    `id_propietario` INT NULL DEFAULT NULL,
    `id_direccion` INT NULL DEFAULT NULL,
    `descripcion` VARCHAR(45) NULL DEFAULT NULL,
    `num_habitaciones` INT NULL DEFAULT NULL,
    `num_baños` INT NULL DEFAULT NULL,
    `superficie` INT NULL DEFAULT NULL,
    `disponibilidad` TINYINT NULL DEFAULT NULL,
    `tipo_cama` VARCHAR(45) NULL DEFAULT NULL,
    `num_camas` INT NULL DEFAULT NULL,
    `tipo_propiedad` VARCHAR(45) NULL DEFAULT NULL,
    `exterior` TINYINT NULL DEFAULT NULL,
    `ascensor` TINYINT NULL DEFAULT NULL,
    `parking` TINYINT NULL DEFAULT NULL,
    `terraza` TINYINT NULL DEFAULT NULL,
    `balcon` TINYINT NULL DEFAULT NULL,
    `piscina` TINYINT NULL DEFAULT NULL,
    `num_fotos` INT NULL DEFAULT NULL,
    `estado` VARCHAR(45) NULL DEFAULT NULL,
    `orientacion` VARCHAR(45) NULL DEFAULT NULL,
    PRIMARY KEY (`id_inmueble`),
    FOREIGN KEY (`id_direccion`) REFERENCES `direccion`(`id_direccion`),
    FOREIGN KEY (`id_propietario`) REFERENCES `propietario`(`id_propietario`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`plataforma`(
    `id_plataforma` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NULL DEFAULT NULL,
    `num_clientes` INT NULL DEFAULT NULL,
    `num_inmuebles` INT NULL DEFAULT NULL,
    `num_disponibles` INT NULL DEFAULT NULL,
    PRIMARY KEY (`id_plataforma`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`anuncio`(
    `id_anuncio` INT NOT NULL AUTO_INCREMENT,
    `id_inmueble` INT NOT NULL,
    `id_plataforma` INT NOT NULL,
    `price` DECIMAL(10, 2),
    `date` DATE,
    `type` VARCHAR(50),
    PRIMARY KEY (`id_anuncio`),
    FOREIGN KEY (`id_inmueble`) REFERENCES `inmueble`(`id_inmueble`),
    FOREIGN KEY (`id_plataforma`) REFERENCES `plataforma`(`id_plataforma`)
);

CREATE TABLE IF NOT EXISTS `tfm_database`.`prueba`(
    `id_anuncio` INT NOT NULL AUTO_INCREMENT,
    `id_inmueble` INT NOT NULL,
    `id_plataforma` INT NOT NULL,
    `price` DECIMAL(10, 2),
    `date` DATE,
    `type` VARCHAR(50),
    PRIMARY KEY (`id_anuncio`),
    FOREIGN KEY (`id_inmueble`) REFERENCES `inmueble`(`id_inmueble`),
    FOREIGN KEY (`id_plataforma`) REFERENCES `plataforma`(`id_plataforma`)
);
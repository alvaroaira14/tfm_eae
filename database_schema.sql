CREATE TABLE IF NOT EXISTS `tfm_database`.`ciudad` (
    `id_ciudad` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(255) NULL DEFAULT NULL,
    `pais` VARCHAR(255) NULL DEFAULT NULL,
    `provincia` VARCHAR(255) NULL DEFAULT NULL,
    `municipio` VARCHAR(255) NULL DEFAULT NULL,
    PRIMARY KEY (`id_ciudad`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`direccion` (
    `id_direccion` INT NOT NULL AUTO_INCREMENT,
    `id_ciudad` INT NOT NULL,
    `calle` VARCHAR(255) NULL DEFAULT NULL,
    `numero` INT NULL DEFAULT NULL,
    `piso` VARCHAR(255) NULL DEFAULT NULL,
    `distrito` VARCHAR(255) NULL DEFAULT NULL,
    `subdistrito` VARCHAR(255) NULL DEFAULT NULL,
    `codigo_postal` INT NULL DEFAULT NULL,
    `latitud` POINT NULL DEFAULT NULL,
    `longitud` POINT NULL DEFAULT NULL,
    PRIMARY KEY (`id_direccion`),
    FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad`(`id_ciudad`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`inmueble`(
    `id_inmueble` INT NOT NULL AUTO_INCREMENT,
    `id_direccion` INT NULL DEFAULT NULL,
    `descripcion` VARCHAR(255) NULL DEFAULT NULL,
    `num_habitaciones` INT NULL DEFAULT NULL,
    `num_lavabos` INT NULL DEFAULT NULL,
    `superficie` INT NULL DEFAULT NULL,
    `tipo_cama` VARCHAR(255) NULL DEFAULT NULL,
    `num_camas` INT NULL DEFAULT NULL,
    `tipo_propiedad` VARCHAR(255) NULL DEFAULT NULL,
    `exterior` VARCHAR(255) NULL DEFAULT NULL,
    `ascensor` TINYINT NULL DEFAULT NULL,
    `parking` TINYINT NULL DEFAULT NULL,
    `terraza` TINYINT NULL DEFAULT NULL,
    `balcon` TINYINT NULL DEFAULT NULL,
    `piscina` TINYINT NULL DEFAULT NULL,
    `estado` VARCHAR(255) NULL DEFAULT NULL,
    `orientacion` VARCHAR(255) NULL DEFAULT NULL,
    PRIMARY KEY (`id_inmueble`),
    FOREIGN KEY (`id_direccion`) REFERENCES `direccion`(`id_direccion`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`plataforma`(
    `id_plataforma` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(255) NULL DEFAULT NULL,
    `num_clientes` INT NULL DEFAULT NULL,
    `num_inmuebles` INT NULL DEFAULT NULL,
    `num_disponibles` INT NULL DEFAULT NULL,
    PRIMARY KEY (`id_plataforma`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`anuncio`(
    `id_anuncio` INT NOT NULL AUTO_INCREMENT,
    `id_inmueble` INT NOT NULL,
    `id_plataforma` INT NOT NULL,
    `precio` DECIMAL(10, 2),
    `fecha` DATE,
    `tipo` VARCHAR(50),
    PRIMARY KEY (`id_anuncio`),
    FOREIGN KEY (`id_inmueble`) REFERENCES `inmueble`(`id_inmueble`),
    FOREIGN KEY (`id_plataforma`) REFERENCES `plataforma`(`id_plataforma`)
)AUTO_INCREMENT = 1;
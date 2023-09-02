CREATE TABLE IF NOT EXISTS `tfm_database`.`direccion` (
    `id_direccion` INT NOT NULL AUTO_INCREMENT,
    `ciudad` VARCHAR(255) NULL DEFAULT NULL,
    `distrito` VARCHAR(255) NULL DEFAULT NULL,
    `subdistrito` VARCHAR(255) NULL DEFAULT NULL,
    `codigo_postal` INT NULL DEFAULT NULL,
    `ha_zonasverdes` FLOAT NULL DEFAULT NULL,
    PRIMARY KEY (`id_direccion`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`inmueble`(
    `id_inmueble` INT NOT NULL AUTO_INCREMENT,
    `id_direccion` INT NOT NULL,
    `descripcion` VARCHAR(255) NULL DEFAULT NULL,
    `num_habitaciones` INT NULL DEFAULT NULL,
    `num_lavabos` INT NULL DEFAULT NULL,
    `superficie` INT NULL DEFAULT NULL,
    `tipo_propiedad` VARCHAR(255) NULL DEFAULT NULL,
    `exterior` BOOL NULL DEFAULT NULL,
    `ascensor` BOOL NULL DEFAULT NULL,
    `parking` BOOL NULL DEFAULT NULL,
    `terraza` BOOL NULL DEFAULT NULL,
    `balcon` BOOL NULL DEFAULT NULL,
    `piscina` BOOL NULL DEFAULT NULL,
    `piso` VARCHAR(255) NULL DEFAULT NULL,
    `orientacion` VARCHAR(255) NULL DEFAULT NULL,
    `certificado_energetico` VARCHAR(255) NULL DEFAULT NULL,
    PRIMARY KEY (`id_inmueble`),
    FOREIGN KEY (`id_direccion`) REFERENCES `direccion`(`id_direccion`)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `tfm_database`.`plataforma`(
    `id_plataforma` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(255) NULL DEFAULT NULL,
    `num_inmuebles` INT NULL DEFAULT NULL,
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
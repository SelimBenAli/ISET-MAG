-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 20 jan. 2025 à 09:46
-- Version du serveur : 8.3.0
-- Version de PHP : 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `iset_mag_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `IDAdmin` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Prenom` varchar(255) NOT NULL,
  `Mail` varchar(255) NOT NULL,
  `MDP` varchar(255) NOT NULL,
  PRIMARY KEY (`IDAdmin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `admin`
--

INSERT INTO `admin` (`IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP`) VALUES
(1, 'Ben Ali', 'Selim', 'selimbenali2003@gmail.com', '123');

-- --------------------------------------------------------

--
-- Structure de la table `bloc`
--

DROP TABLE IF EXISTS `bloc`;
CREATE TABLE IF NOT EXISTS `bloc` (
  `IDBloc` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  PRIMARY KEY (`IDBloc`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `bloc`
--

INSERT INTO `bloc` (`IDBloc`, `Nom`) VALUES
(1, 'B'),
(2, 'A');

-- --------------------------------------------------------

--
-- Structure de la table `etat`
--

DROP TABLE IF EXISTS `etat`;
CREATE TABLE IF NOT EXISTS `etat` (
  `IDEtat` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Description` text NOT NULL,
  PRIMARY KEY (`IDEtat`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `etat`
--

INSERT INTO `etat` (`IDEtat`, `Nom`, `Description`) VALUES
(1, 'Bonne Etat', ''),
(2, 'Panne', '');

-- --------------------------------------------------------

--
-- Structure de la table `fournisseur`
--

DROP TABLE IF EXISTS `fournisseur`;
CREATE TABLE IF NOT EXISTS `fournisseur` (
  `IDFournisseur` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Tel` varchar(255) NOT NULL,
  PRIMARY KEY (`IDFournisseur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `fournisseur`
--

INSERT INTO `fournisseur` (`IDFournisseur`, `Nom`, `Tel`) VALUES
(1, 'SBAd', '12345677'),
(2, 'SBA', '12345678'),
(3, 'aaa', '12345678'),
(5, 'selim', '1234');

-- --------------------------------------------------------

--
-- Structure de la table `hardware`
--

DROP TABLE IF EXISTS `hardware`;
CREATE TABLE IF NOT EXISTS `hardware` (
  `IDHardware` int NOT NULL AUTO_INCREMENT,
  `IDModel` int NOT NULL,
  `IDFournisseur` int DEFAULT NULL,
  `IDMagasin` int DEFAULT NULL,
  `IDSalle` int DEFAULT NULL,
  `NumeroInventaire` varchar(255) NOT NULL,
  `DateAchat` datetime DEFAULT NULL,
  `DateAjout` datetime NOT NULL,
  `DateMiseEnService` datetime DEFAULT NULL,
  `Code` text NOT NULL,
  `IDEtat` int NOT NULL DEFAULT '1',
  `HistoriqueRelation` json DEFAULT NULL,
  PRIMARY KEY (`IDHardware`),
  KEY `IDModel` (`IDModel`),
  KEY `IDMagasin` (`IDMagasin`),
  KEY `IDFournisseur` (`IDFournisseur`),
  KEY `IDSalle` (`IDSalle`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `hardware`
--

INSERT INTO `hardware` (`IDHardware`, `IDModel`, `IDFournisseur`, `IDMagasin`, `IDSalle`, `NumeroInventaire`, `DateAchat`, `DateAjout`, `DateMiseEnService`, `Code`, `IDEtat`, `HistoriqueRelation`) VALUES
(1, 1, 2, 1, 2, '12345678', NULL, '2025-01-11 15:14:16', NULL, 'aaaaaaaaaaaaaaa', 2, NULL),
(2, 2, 5, 2, 2, '444', '2025-01-02 14:34:22', '2025-01-12 14:37:56', '2025-01-08 00:00:00', '123', 2, NULL),
(5, 2, 5, 1, 1, '123', NULL, '2025-01-16 15:44:24', NULL, '123', 1, NULL),
(6, 2, 5, NULL, 4, '123', NULL, '2025-01-16 15:45:10', NULL, '123', 1, NULL),
(7, 1, 1, NULL, 4, '8888', NULL, '2025-01-16 15:51:51', NULL, '333', 1, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `intervention`
--

DROP TABLE IF EXISTS `intervention`;
CREATE TABLE IF NOT EXISTS `intervention` (
  `IDIntervention` int NOT NULL AUTO_INCREMENT,
  `IDUtilisateur` int NOT NULL,
  `DateDebut` datetime NOT NULL,
  `DateFin` datetime DEFAULT NULL,
  `IDSalle` int DEFAULT NULL,
  `IDHardware` int NOT NULL,
  `IDAdmin` int NOT NULL,
  PRIMARY KEY (`IDIntervention`),
  KEY `IDHardware` (`IDHardware`),
  KEY `IDSalle` (`IDSalle`),
  KEY `IDUtilisateur` (`IDUtilisateur`),
  KEY `IDAdmin` (`IDAdmin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `intervention`
--

INSERT INTO `intervention` (`IDIntervention`, `IDUtilisateur`, `DateDebut`, `DateFin`, `IDSalle`, `IDHardware`, `IDAdmin`) VALUES
(1, 1, '2025-01-18 17:53:35', NULL, NULL, 5, 1);

-- --------------------------------------------------------

--
-- Structure de la table `louer_hardware`
--

DROP TABLE IF EXISTS `louer_hardware`;
CREATE TABLE IF NOT EXISTS `louer_hardware` (
  `IDLocation` int NOT NULL AUTO_INCREMENT,
  `DateDebutEstime` datetime NOT NULL,
  `DateFinEstimee` datetime NOT NULL,
  `IDUtilisateur` int NOT NULL,
  `IDHardware` int NOT NULL,
  `Quantite` int NOT NULL,
  `Confirmation` int NOT NULL DEFAULT '-1',
  `IDAdmin` int NOT NULL,
  `DateConfirmation` datetime NOT NULL,
  PRIMARY KEY (`IDLocation`),
  KEY `IDAdmin` (`IDAdmin`),
  KEY `IDHardware` (`IDHardware`),
  KEY `IDUtilisateur` (`IDUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `magasin`
--

DROP TABLE IF EXISTS `magasin`;
CREATE TABLE IF NOT EXISTS `magasin` (
  `IDMagasin` int NOT NULL AUTO_INCREMENT,
  `IDSalle` int DEFAULT NULL,
  `Nom` varchar(255) NOT NULL,
  PRIMARY KEY (`IDMagasin`),
  KEY `IDSalle` (`IDSalle`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `magasin`
--

INSERT INTO `magasin` (`IDMagasin`, `IDSalle`, `Nom`) VALUES
(1, 1, 'Mag 1'),
(2, 4, 'mag 2');

-- --------------------------------------------------------

--
-- Structure de la table `marque`
--

DROP TABLE IF EXISTS `marque`;
CREATE TABLE IF NOT EXISTS `marque` (
  `IDMarque` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  PRIMARY KEY (`IDMarque`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `marque`
--

INSERT INTO `marque` (`IDMarque`, `Nom`) VALUES
(1, 'HP'),
(3, 'DELL'),
(5, 'ASUS');

-- --------------------------------------------------------

--
-- Structure de la table `model_hardware`
--

DROP TABLE IF EXISTS `model_hardware`;
CREATE TABLE IF NOT EXISTS `model_hardware` (
  `IDModel` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `IDMarque` int DEFAULT NULL,
  PRIMARY KEY (`IDModel`),
  KEY `IDMarque` (`IDMarque`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `model_hardware`
--

INSERT INTO `model_hardware` (`IDModel`, `Nom`, `IDMarque`) VALUES
(1, 'Ecran', 5),
(2, 'Unité', 1);

-- --------------------------------------------------------

--
-- Structure de la table `reclamation_hardware`
--

DROP TABLE IF EXISTS `reclamation_hardware`;
CREATE TABLE IF NOT EXISTS `reclamation_hardware` (
  `IDReclamation` int NOT NULL AUTO_INCREMENT,
  `IDHardware` int NOT NULL,
  `IDUtilisateur` int NOT NULL,
  `IDIntervention` int DEFAULT NULL,
  `DateReclamation` datetime NOT NULL,
  `Description` text NOT NULL,
  `IDEtat` int NOT NULL,
  PRIMARY KEY (`IDReclamation`),
  KEY `IDEtat` (`IDEtat`),
  KEY `IDIntervention` (`IDIntervention`),
  KEY `IDHardware` (`IDHardware`),
  KEY `IDUtilisateur` (`IDUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `relation_hardware`
--

DROP TABLE IF EXISTS `relation_hardware`;
CREATE TABLE IF NOT EXISTS `relation_hardware` (
  `IDRelation` int NOT NULL AUTO_INCREMENT,
  `IDHardware1` int DEFAULT NULL,
  `IDHardware2` int DEFAULT NULL,
  PRIMARY KEY (`IDRelation`),
  KEY `IDHardware1` (`IDHardware1`),
  KEY `IDHardware2` (`IDHardware2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `role`
--

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
  `IDRole` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  PRIMARY KEY (`IDRole`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `role`
--

INSERT INTO `role` (`IDRole`, `Nom`) VALUES
(1, 'Enseignant');

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

DROP TABLE IF EXISTS `salle`;
CREATE TABLE IF NOT EXISTS `salle` (
  `IDSalle` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `IDBloc` int DEFAULT NULL,
  PRIMARY KEY (`IDSalle`),
  KEY `IDBloc` (`IDBloc`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `salle`
--

INSERT INTO `salle` (`IDSalle`, `Nom`, `IDBloc`) VALUES
(1, 'B117', 1),
(2, 'B002', 1),
(3, 'A015', 2),
(4, 'B016', 1);

-- --------------------------------------------------------

--
-- Structure de la table `software`
--

DROP TABLE IF EXISTS `software`;
CREATE TABLE IF NOT EXISTS `software` (
  `IDSoftware` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `DateAchat` date DEFAULT NULL,
  `DateAjout` datetime NOT NULL,
  `Lien` text NOT NULL,
  PRIMARY KEY (`IDSoftware`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `IDUtilisateur` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Prenom` varchar(255) NOT NULL,
  `Mail` varchar(255) NOT NULL,
  `Tel` varchar(255) NOT NULL,
  `MDP` text NOT NULL,
  `Role` int DEFAULT NULL,
  `Code` text NOT NULL,
  PRIMARY KEY (`IDUtilisateur`),
  KEY `Role` (`Role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`IDUtilisateur`, `Nom`, `Prenom`, `Mail`, `Tel`, `MDP`, `Role`, `Code`) VALUES
(1, 'ESSAI', 'essai', 'essai@gmail.com', '12345678', '000', 1, '123'),
(2, 'ESSAI', 'essai', 'selimbenali2003@gmail.com', '12345678', '000', 1, '123');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `hardware`
--
ALTER TABLE `hardware`
  ADD CONSTRAINT `hardware_ibfk_1` FOREIGN KEY (`IDModel`) REFERENCES `model_hardware` (`IDModel`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hardware_ibfk_2` FOREIGN KEY (`IDMagasin`) REFERENCES `magasin` (`IDMagasin`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hardware_ibfk_3` FOREIGN KEY (`IDFournisseur`) REFERENCES `fournisseur` (`IDFournisseur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hardware_ibfk_4` FOREIGN KEY (`IDSalle`) REFERENCES `salle` (`IDSalle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `intervention`
--
ALTER TABLE `intervention`
  ADD CONSTRAINT `intervention_ibfk_1` FOREIGN KEY (`IDHardware`) REFERENCES `hardware` (`IDHardware`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervention_ibfk_2` FOREIGN KEY (`IDSalle`) REFERENCES `salle` (`IDSalle`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervention_ibfk_3` FOREIGN KEY (`IDUtilisateur`) REFERENCES `utilisateur` (`IDUtilisateur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervention_ibfk_4` FOREIGN KEY (`IDAdmin`) REFERENCES `admin` (`IDAdmin`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `louer_hardware`
--
ALTER TABLE `louer_hardware`
  ADD CONSTRAINT `louer_hardware_ibfk_1` FOREIGN KEY (`IDAdmin`) REFERENCES `admin` (`IDAdmin`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `louer_hardware_ibfk_2` FOREIGN KEY (`IDHardware`) REFERENCES `hardware` (`IDHardware`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `louer_hardware_ibfk_3` FOREIGN KEY (`IDUtilisateur`) REFERENCES `utilisateur` (`IDUtilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `magasin`
--
ALTER TABLE `magasin`
  ADD CONSTRAINT `magasin_ibfk_1` FOREIGN KEY (`IDSalle`) REFERENCES `salle` (`IDSalle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `model_hardware`
--
ALTER TABLE `model_hardware`
  ADD CONSTRAINT `model_hardware_ibfk_1` FOREIGN KEY (`IDMarque`) REFERENCES `marque` (`IDMarque`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `reclamation_hardware`
--
ALTER TABLE `reclamation_hardware`
  ADD CONSTRAINT `reclamation_hardware_ibfk_1` FOREIGN KEY (`IDEtat`) REFERENCES `etat` (`IDEtat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reclamation_hardware_ibfk_2` FOREIGN KEY (`IDIntervention`) REFERENCES `intervention` (`IDIntervention`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reclamation_hardware_ibfk_3` FOREIGN KEY (`IDHardware`) REFERENCES `hardware` (`IDHardware`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reclamation_hardware_ibfk_4` FOREIGN KEY (`IDUtilisateur`) REFERENCES `utilisateur` (`IDUtilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `relation_hardware`
--
ALTER TABLE `relation_hardware`
  ADD CONSTRAINT `relation_hardware_ibfk_1` FOREIGN KEY (`IDHardware1`) REFERENCES `hardware` (`IDHardware`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `relation_hardware_ibfk_2` FOREIGN KEY (`IDHardware2`) REFERENCES `hardware` (`IDHardware`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `salle`
--
ALTER TABLE `salle`
  ADD CONSTRAINT `salle_ibfk_1` FOREIGN KEY (`IDBloc`) REFERENCES `bloc` (`IDBloc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD CONSTRAINT `utilisateur_ibfk_1` FOREIGN KEY (`Role`) REFERENCES `role` (`IDRole`) ON DELETE SET NULL ON UPDATE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

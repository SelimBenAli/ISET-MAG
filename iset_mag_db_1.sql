-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 01 fév. 2025 à 02:00
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `admin`
--

INSERT INTO `admin` (`IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP`) VALUES
(1, 'Ben Ali', 'Selim', 'selimbenali2003@gmail.com', '123'),
(2, 'Ben Ali', 'Selim', 'try', '123');

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `hardware`
--

INSERT INTO `hardware` (`IDHardware`, `IDModel`, `IDFournisseur`, `IDMagasin`, `IDSalle`, `NumeroInventaire`, `DateAchat`, `DateAjout`, `DateMiseEnService`, `Code`, `IDEtat`, `HistoriqueRelation`) VALUES
(1, 1, 2, 1, 2, '12345678', NULL, '2025-01-11 15:14:16', NULL, '563', 2, NULL),
(2, 2, 5, 2, 2, '444', '2025-01-02 14:34:22', '2025-01-12 14:37:56', '2025-01-08 00:00:00', '123', 2, NULL),
(5, 2, 5, 1, 1, '123', NULL, '2025-01-16 15:44:24', NULL, '1234', 1, NULL),
(6, 2, 5, NULL, 4, '1235', NULL, '2025-01-16 15:45:10', NULL, '1239', 1, NULL),
(7, 1, 1, NULL, 4, '8888', NULL, '2025-01-16 15:51:51', NULL, '333', 1, NULL),
(8, 6, 2, 1, 3, '55', '2025-01-03 02:23:13', '2025-01-29 02:22:09', '2025-01-17 02:23:23', '55', 1, NULL),
(9, 6, 2, 1, 3, '56', '2025-01-03 02:23:13', '2025-01-29 02:22:09', '2025-01-17 02:23:23', '56', 1, NULL),
(10, 6, 2, 1, 3, '57', '2025-01-03 02:23:13', '2025-01-29 02:22:09', '2025-01-17 02:23:23', '57', 1, NULL),
(11, 6, 3, 2, 3, '32', '2025-01-04 02:28:38', '2025-01-29 02:28:24', '2025-01-15 02:28:46', '32', 1, NULL),
(12, 5, 5, 1, 3, '100', NULL, '2025-01-29 14:37:15', NULL, '77', 1, NULL);

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `intervention`
--

INSERT INTO `intervention` (`IDIntervention`, `IDUtilisateur`, `DateDebut`, `DateFin`, `IDSalle`, `IDHardware`, `IDAdmin`) VALUES
(1, 1, '2025-01-18 17:53:35', '2025-01-22 14:31:04', 2, 5, 1),
(2, 1, '2025-01-23 17:53:35', NULL, NULL, 5, 1);

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
  `IDModel` int NOT NULL,
  `Quantite` int NOT NULL,
  `Confirmation` int NOT NULL DEFAULT '-1',
  `IDAdmin` int DEFAULT NULL,
  `DateConfirmation` datetime DEFAULT NULL,
  `DateAjout` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`IDLocation`),
  KEY `IDAdmin` (`IDAdmin`),
  KEY `IDHardware` (`IDModel`),
  KEY `IDUtilisateur` (`IDUtilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `louer_hardware`
--

INSERT INTO `louer_hardware` (`IDLocation`, `DateDebutEstime`, `DateFinEstimee`, `IDUtilisateur`, `IDModel`, `Quantite`, `Confirmation`, `IDAdmin`, `DateConfirmation`, `DateAjout`) VALUES
(1, '2025-01-25 16:20:00', '2025-01-26 16:20:00', 1, 4, 1, -1, 1, '2025-01-26 03:11:06', '2025-01-30 19:42:31'),
(2, '2025-01-24 16:20:00', '2025-01-26 16:20:00', 1, 2, 2, 1, 1, '2025-01-26 03:11:05', '2025-01-30 19:42:31'),
(3, '2025-01-24 16:20:00', '2025-01-26 16:20:00', 1, 2, 2, 1, 1, '2025-01-26 20:18:47', '2025-01-30 19:42:31'),
(4, '2025-01-24 16:20:00', '2025-01-26 16:20:00', 1, 2, 3, -1, 1, '2025-01-26 20:19:08', '2025-01-30 19:42:31'),
(5, '2025-01-24 16:20:00', '2025-01-26 16:20:00', 1, 1, 3, -1, 1, '2025-02-01 02:41:12', '2025-01-30 19:42:31'),
(6, '2025-01-30 13:25:00', '2025-01-30 16:25:00', 1, 5, 2, 1, 1, '2025-01-30 13:26:23', '2025-01-30 19:42:31'),
(7, '2025-01-31 20:21:00', '2025-02-08 20:21:00', 1, 1, 3, -1, 1, '2025-01-31 20:22:22', '2025-01-31 20:21:50');

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
-- Structure de la table `message`
--

DROP TABLE IF EXISTS `message`;
CREATE TABLE IF NOT EXISTS `message` (
  `IDMessage` int NOT NULL AUTO_INCREMENT,
  `IDUtilisateur` int DEFAULT NULL,
  `Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Sujet` varchar(255) NOT NULL,
  `Contenu` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Vu` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`IDMessage`),
  KEY `IDUtilisateur` (`IDUtilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `message`
--

INSERT INTO `message` (`IDMessage`, `IDUtilisateur`, `Date`, `Sujet`, `Contenu`, `Vu`) VALUES
(2, 2, '2025-01-16 17:41:35', '123', 'dddddddddddddddddddddddddddddddd', '1;'),
(3, 1, '2025-01-29 19:30:54', 'bonjour', 'try', '1;'),
(4, 1, '2025-01-29 19:38:21', 'aaaa', 'aaaaa', '1;'),
(5, 1, '2025-01-30 12:54:33', 'salut', 'hello', '1;'),
(6, 1, '2025-01-30 12:56:22', 'essai45', 'essai45', '1;'),
(7, 1, '2025-01-30 12:57:04', '88', '88', '1;'),
(8, 1, '2025-01-30 13:30:17', 'reunion', 'bonjour', '1;'),
(9, 1, '2025-01-30 16:22:45', '11', '11', '1;'),
(10, 1, '2025-01-30 16:23:37', '66', '66', '1;'),
(11, 1, '2025-01-30 16:23:58', '667', '77', '1;'),
(12, 1, '2025-01-30 17:45:56', '11', '22', '1;'),
(13, 1, '2025-01-30 17:46:25', '33', '33', '');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `model_hardware`
--

INSERT INTO `model_hardware` (`IDModel`, `Nom`, `IDMarque`) VALUES
(1, 'Ecran', 5),
(2, 'Unité', 1),
(4, 'Unité', 5),
(5, 'Clavier', 1),
(6, 'Souris', 1);

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
  `DateReclamation` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Description` text NOT NULL,
  `IDEtat` int DEFAULT NULL,
  `Vu` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`IDReclamation`),
  KEY `IDEtat` (`IDEtat`),
  KEY `IDIntervention` (`IDIntervention`),
  KEY `IDHardware` (`IDHardware`),
  KEY `IDUtilisateur` (`IDUtilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `reclamation_hardware`
--

INSERT INTO `reclamation_hardware` (`IDReclamation`, `IDHardware`, `IDUtilisateur`, `IDIntervention`, `DateReclamation`, `Description`, `IDEtat`, `Vu`) VALUES
(1, 5, 2, NULL, '2025-01-09 00:07:02', 'aaaa', NULL, '1;'),
(3, 5, 1, NULL, '2025-01-21 02:31:52', 'eeee', NULL, '1;'),
(4, 2, 1, NULL, '2025-01-21 02:32:39', 'mm', NULL, '1;'),
(5, 2, 1, NULL, '2025-01-30 13:28:13', 'panne', NULL, '1;'),
(6, 7, 1, NULL, '2025-01-31 20:24:39', '', NULL, '1;'),
(7, 9, 1, NULL, '2025-02-01 02:31:06', 'cable', NULL, '1;');

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `relation_hardware`
--

INSERT INTO `relation_hardware` (`IDRelation`, `IDHardware1`, `IDHardware2`) VALUES
(1, 1, 2),
(2, 6, 7),
(3, 2, 8),
(4, 6, 9),
(10, 2, 12),
(12, 7, 10);

-- --------------------------------------------------------

--
-- Structure de la table `role`
--

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
  `IDRole` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  PRIMARY KEY (`IDRole`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `role`
--

INSERT INTO `role` (`IDRole`, `Nom`) VALUES
(1, 'Enseignant'),
(2, 'Technicien');

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
(2, 'B002', 2),
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
  `MDP` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Role` int DEFAULT NULL,
  `Code` text NOT NULL,
  `Compte` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`IDUtilisateur`),
  KEY `Role` (`Role`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`IDUtilisateur`, `Nom`, `Prenom`, `Mail`, `Tel`, `MDP`, `Role`, `Code`, `Compte`) VALUES
(1, 'ESSAI1', 'essai1', 'essai@gmail.com', '123456781', '0', 2, '1231', 1),
(2, 'ESSAI', 'essai', 'selimbenali2003@gmail.com', '12345678', '1', 1, '123', 0),
(3, 'aa', 'bb', 'cc', '123', '2', 2, 'aa', 0),
(4, 'ee', 'ee', 'ee', '123', '3', 2, 'ee', 1);

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
  ADD CONSTRAINT `louer_hardware_ibfk_3` FOREIGN KEY (`IDUtilisateur`) REFERENCES `utilisateur` (`IDUtilisateur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `louer_hardware_ibfk_4` FOREIGN KEY (`IDModel`) REFERENCES `model_hardware` (`IDModel`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `magasin`
--
ALTER TABLE `magasin`
  ADD CONSTRAINT `magasin_ibfk_1` FOREIGN KEY (`IDSalle`) REFERENCES `salle` (`IDSalle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `message_ibfk_1` FOREIGN KEY (`IDUtilisateur`) REFERENCES `utilisateur` (`IDUtilisateur`) ON DELETE CASCADE ON UPDATE CASCADE;

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

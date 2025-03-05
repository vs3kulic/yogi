-- MySQL dump 10.13  Distrib 9.2.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: fellowship_db
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_artifacts`
--

DROP TABLE IF EXISTS `app_artifacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_artifacts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `character_id` bigint NOT NULL,
  `artifact_name` varchar(100) NOT NULL,
  `offensive_property` int DEFAULT '0',
  `defensive_property` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `character_id` (`character_id`),
  CONSTRAINT `app_artifacts_ibfk_1` FOREIGN KEY (`character_id`) REFERENCES `app_character` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_artifacts`
--

LOCK TABLES `app_artifacts` WRITE;
/*!40000 ALTER TABLE `app_artifacts` DISABLE KEYS */;
INSERT INTO `app_artifacts` VALUES (1,59,'Andúril (Sword)',50,0),(2,59,'Ranger\'s Cloak',0,30),(3,59,'Elven Brooch',0,20),(4,60,'Sting (Dagger)',25,0),(5,60,'Mithril Coat',0,40),(6,60,'The One Ring',50,-10),(7,61,'Bow of the Galadhrim',50,0),(8,61,'Elven Quiver',10,0),(9,61,'Elven Boots',0,20),(10,62,'Battle Axe',60,0),(11,62,'Dwarven Shield',0,40),(12,62,'Helm of Durin',0,30),(13,63,'Glamdring (Sword)',45,0),(14,63,'Wizard\'s Staff',30,20),(15,63,'Narya (Ring of Fire)',0,20),(16,64,'Mace of Sauron',80,0),(17,64,'Dark Armor',0,50),(18,64,'The One Ring',50,-10),(19,65,'Staff of Saruman',40,20),(20,65,'Palantír (Seeing Stone)',20,-10),(21,65,'Robe of Deception',0,30),(22,66,'Sharp Claws',20,0),(23,66,'Precious Amulet',10,-5),(24,66,'Cave Dweller’s Cloak',0,20),(25,67,'Morgul Blade',30,-5),(26,67,'Black Robes',-5,25),(27,67,'Ring of Power',20,-10),(28,68,'Dark Blade',30,-5),(29,68,'Robeslasher',-5,25),(30,68,'Power dagger',20,-10);
/*!40000 ALTER TABLE `app_artifacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_battleoutcome`
--

DROP TABLE IF EXISTS `app_battleoutcome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_battleoutcome` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `main_artifact_id` int DEFAULT NULL,
  `opponent_artifact_id` int DEFAULT NULL,
  `outcome` varchar(255) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `coin_toss_result` varchar(100) DEFAULT NULL,
  `opponent_character_id` bigint DEFAULT NULL,
  `player_character_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_battleoutcome_opponent_character_i_6765f9d8_fk_app_chara` (`opponent_character_id`),
  KEY `app_battleoutcome_player_character_id_6903734c_fk_app_chara` (`player_character_id`),
  CONSTRAINT `app_battleoutcome_opponent_character_i_6765f9d8_fk_app_chara` FOREIGN KEY (`opponent_character_id`) REFERENCES `app_character` (`id`),
  CONSTRAINT `app_battleoutcome_player_character_id_6903734c_fk_app_chara` FOREIGN KEY (`player_character_id`) REFERENCES `app_character` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=341 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_battleoutcome`
--

LOCK TABLES `app_battleoutcome` WRITE;
/*!40000 ALTER TABLE `app_battleoutcome` DISABLE KEYS */;
INSERT INTO `app_battleoutcome` VALUES (1,NULL,NULL,'Win','2025-02-12 19:58:03.902612',NULL,NULL,NULL),(2,NULL,NULL,'Win','2025-02-12 19:58:13.666440',NULL,NULL,NULL),(3,NULL,NULL,'Win','2025-02-12 20:00:23.105498',NULL,NULL,NULL),(4,NULL,NULL,'Win','2025-02-12 20:05:38.038356',NULL,NULL,NULL),(5,NULL,NULL,'Lose','2025-02-12 20:05:52.555403',NULL,NULL,NULL),(6,NULL,NULL,'Lose','2025-02-12 20:05:58.869356',NULL,NULL,NULL),(7,NULL,NULL,'Win','2025-02-12 20:06:21.997664',NULL,NULL,NULL),(8,NULL,NULL,'Lose','2025-02-12 20:07:15.035938',NULL,NULL,NULL),(9,NULL,NULL,'Lose','2025-02-12 22:22:03.347422',NULL,NULL,NULL),(10,NULL,NULL,'Win','2025-02-12 22:25:44.661003',NULL,NULL,NULL),(11,NULL,NULL,'Win','2025-02-12 22:35:44.009545',NULL,NULL,NULL),(12,NULL,NULL,'Lose','2025-02-12 22:36:37.306774',NULL,NULL,NULL),(13,NULL,NULL,'Win','2025-02-12 22:40:31.562823',NULL,NULL,NULL),(14,NULL,NULL,'Lose','2025-02-13 09:04:23.814129',NULL,NULL,NULL),(15,NULL,NULL,'Lose','2025-02-13 09:04:36.761512',NULL,NULL,NULL),(16,NULL,NULL,'Win','2025-02-13 09:04:46.784583',NULL,NULL,NULL),(17,NULL,NULL,'Lose','2025-02-13 09:05:23.939970',NULL,NULL,NULL),(18,NULL,NULL,'Lose','2025-02-13 09:05:31.866367',NULL,NULL,NULL),(19,NULL,NULL,'Win','2025-02-13 09:05:41.089855',NULL,NULL,NULL),(20,NULL,NULL,'Lose','2025-02-13 09:10:00.121710',NULL,NULL,NULL),(21,NULL,NULL,'Win','2025-02-13 09:10:10.731317',NULL,NULL,NULL),(22,NULL,NULL,'Lose','2025-02-13 09:10:24.436819',NULL,NULL,NULL),(23,NULL,NULL,'Win','2025-02-13 09:26:59.088056',NULL,NULL,NULL),(24,NULL,NULL,'Win','2025-02-13 09:31:42.933810',NULL,NULL,NULL),(25,NULL,NULL,'Lose','2025-02-13 09:36:46.626425',NULL,NULL,NULL),(26,NULL,NULL,'Win','2025-02-13 10:38:55.945069',NULL,NULL,NULL),(27,NULL,NULL,'Win','2025-02-13 10:39:06.485201',NULL,NULL,NULL),(28,NULL,NULL,'Win','2025-02-13 10:44:14.049631',NULL,NULL,NULL),(29,NULL,NULL,'Win','2025-02-13 10:47:20.644127',NULL,NULL,NULL),(30,NULL,NULL,'Win','2025-02-13 10:58:46.691317',NULL,NULL,NULL),(31,NULL,NULL,'Win','2025-02-13 10:58:49.733687',NULL,NULL,NULL),(32,NULL,NULL,'Win','2025-02-13 11:42:27.130343',NULL,NULL,NULL),(33,NULL,NULL,'Win','2025-02-13 11:42:36.032087',NULL,NULL,NULL),(34,NULL,NULL,'Win','2025-02-13 11:42:43.836199',NULL,NULL,NULL),(35,NULL,NULL,'Win','2025-02-13 11:42:56.305636',NULL,NULL,NULL),(36,NULL,NULL,'Player wins!','2025-02-13 13:41:04.701639',NULL,NULL,NULL),(37,NULL,NULL,'Player wins!','2025-02-13 13:45:58.111147',NULL,NULL,NULL),(38,NULL,NULL,'Player wins!','2025-02-13 13:50:41.735449',NULL,NULL,NULL),(39,NULL,NULL,'Player wins!','2025-02-13 13:53:42.377945',NULL,NULL,NULL),(40,NULL,NULL,'Player wins!','2025-02-13 18:20:45.125268',NULL,NULL,NULL),(41,NULL,NULL,'win','2025-02-13 19:05:35.378298',NULL,NULL,NULL),(42,NULL,NULL,'lose','2025-02-13 19:05:35.380186',NULL,NULL,NULL),(43,NULL,NULL,'win','2025-02-13 19:06:52.603495',NULL,NULL,NULL),(44,NULL,NULL,'lose','2025-02-13 19:06:52.606292',NULL,NULL,NULL),(45,NULL,NULL,'win','2025-02-13 19:07:04.760643',NULL,NULL,NULL),(46,NULL,NULL,'lose','2025-02-13 19:07:04.763749',NULL,NULL,NULL),(47,NULL,NULL,'win','2025-02-13 19:07:13.864469',NULL,NULL,NULL),(48,NULL,NULL,'lose','2025-02-13 19:07:13.866750',NULL,NULL,NULL),(49,NULL,NULL,'Win','2025-02-13 19:08:27.318298',NULL,NULL,NULL),(50,NULL,NULL,'Loss','2025-02-13 19:08:27.321806',NULL,NULL,NULL),(51,NULL,NULL,'Win','2025-02-13 19:08:39.595274',NULL,NULL,NULL),(52,NULL,NULL,'Loss','2025-02-13 19:08:39.597750',NULL,NULL,NULL),(53,NULL,NULL,'Win','2025-02-13 19:09:31.129734',NULL,NULL,NULL),(54,NULL,NULL,'Loss','2025-02-13 19:09:31.131780',NULL,NULL,NULL),(55,NULL,NULL,'Win','2025-02-13 19:10:28.461986',NULL,NULL,NULL),(56,NULL,NULL,'Loss','2025-02-13 19:10:28.464012',NULL,NULL,NULL),(57,NULL,NULL,'Win','2025-02-13 20:11:56.200833',NULL,NULL,NULL),(58,NULL,NULL,'Loss','2025-02-13 20:11:56.204557',NULL,NULL,NULL),(59,NULL,NULL,'Win','2025-02-13 20:12:29.858038',NULL,NULL,NULL),(60,NULL,NULL,'Loss','2025-02-13 20:12:29.860246',NULL,NULL,NULL),(61,NULL,NULL,'Win','2025-02-13 20:14:54.314123',NULL,NULL,NULL),(62,NULL,NULL,'Loss','2025-02-13 20:14:54.317336',NULL,NULL,NULL),(63,NULL,NULL,'Win','2025-02-13 20:16:31.837555',NULL,NULL,NULL),(64,NULL,NULL,'Loss','2025-02-13 20:16:31.838887',NULL,NULL,NULL),(65,NULL,NULL,'Win','2025-02-13 20:16:44.558582',NULL,NULL,NULL),(66,NULL,NULL,'Loss','2025-02-13 20:16:44.562275',NULL,NULL,NULL),(67,NULL,NULL,'Win','2025-02-13 20:17:06.485080',NULL,NULL,NULL),(68,NULL,NULL,'Loss','2025-02-13 20:17:06.487777',NULL,NULL,NULL),(69,NULL,NULL,'Win','2025-02-13 20:20:12.969152',NULL,NULL,NULL),(70,NULL,NULL,'Loss','2025-02-13 20:20:12.971547',NULL,NULL,NULL),(71,NULL,NULL,'Win','2025-02-13 20:20:31.265748',NULL,NULL,NULL),(72,NULL,NULL,'Loss','2025-02-13 20:20:31.267786',NULL,NULL,NULL),(73,NULL,NULL,'Win','2025-02-14 14:32:57.819619',NULL,NULL,NULL),(74,NULL,NULL,'Loss','2025-02-14 14:32:57.821459',NULL,NULL,NULL),(75,NULL,NULL,'Win','2025-02-14 14:34:09.703281',NULL,NULL,NULL),(76,NULL,NULL,'Win','2025-02-14 14:34:32.318330',NULL,NULL,NULL),(77,NULL,NULL,'Win','2025-02-14 14:36:40.814362',NULL,NULL,NULL),(78,NULL,NULL,'Win','2025-02-14 14:36:55.125557',NULL,NULL,NULL),(79,NULL,NULL,'Win','2025-02-14 14:42:32.653115',NULL,NULL,NULL),(80,NULL,NULL,'Win','2025-02-14 14:42:48.292592',NULL,NULL,NULL),(81,NULL,NULL,'lose','2025-02-14 14:44:53.937861',NULL,NULL,NULL),(82,NULL,NULL,'Loss','2025-02-14 14:45:42.158053',NULL,NULL,NULL),(83,NULL,NULL,'Loss','2025-02-14 14:45:55.126712',NULL,NULL,NULL),(84,NULL,NULL,'Win','2025-02-14 14:46:15.554476',NULL,NULL,NULL),(85,NULL,NULL,'Win','2025-02-14 14:51:08.768955',NULL,NULL,NULL),(86,NULL,NULL,'Win','2025-02-14 15:00:15.742640',NULL,NULL,NULL),(87,NULL,NULL,'Loss','2025-02-14 15:01:27.103079',NULL,NULL,NULL),(88,NULL,NULL,'Win','2025-02-14 15:06:12.727204',NULL,NULL,NULL),(89,NULL,NULL,'Loss','2025-02-14 15:13:04.869572',NULL,NULL,NULL),(90,NULL,NULL,'Loss','2025-02-14 15:13:19.062993',NULL,NULL,NULL),(91,NULL,NULL,'Loss','2025-02-14 16:33:19.021242',NULL,NULL,NULL),(92,NULL,NULL,'Loss','2025-02-14 16:34:03.502652',NULL,NULL,NULL),(93,NULL,NULL,'Loss','2025-02-14 16:34:29.913630',NULL,NULL,NULL),(94,NULL,NULL,'Loss','2025-02-14 16:36:22.953670',NULL,NULL,NULL),(95,NULL,NULL,'Win','2025-02-16 10:33:07.187582',NULL,NULL,NULL),(96,NULL,NULL,'Win','2025-02-16 10:33:25.559345',NULL,NULL,NULL),(97,NULL,NULL,'Loss','2025-02-17 14:55:27.789502',NULL,NULL,NULL),(98,NULL,NULL,'Win','2025-02-17 15:02:42.416170',NULL,NULL,NULL),(99,NULL,NULL,'Loss','2025-02-17 15:13:39.571537',NULL,NULL,NULL),(100,NULL,NULL,'Loss','2025-02-17 15:13:55.590225',NULL,NULL,NULL),(101,NULL,NULL,'Loss','2025-02-17 15:14:35.797479',NULL,NULL,NULL),(102,NULL,NULL,'Win','2025-02-17 15:15:11.880657',NULL,NULL,NULL),(103,NULL,NULL,'Loss','2025-02-17 15:15:35.086186',NULL,NULL,NULL),(104,NULL,NULL,'Win','2025-02-17 15:15:49.539878',NULL,NULL,NULL),(105,NULL,NULL,'Loss','2025-02-17 15:19:01.462368',NULL,NULL,NULL),(106,NULL,NULL,'Win','2025-02-19 09:47:13.867181',NULL,NULL,NULL),(107,NULL,NULL,'Loss','2025-02-19 21:10:48.949145',NULL,NULL,NULL),(108,NULL,NULL,'Win','2025-02-19 21:11:38.019176',NULL,NULL,NULL),(109,NULL,NULL,'Win','2025-02-19 21:13:42.178762',NULL,NULL,NULL),(110,NULL,NULL,'Win','2025-02-20 07:41:39.377503',NULL,NULL,NULL),(111,NULL,NULL,'Win','2025-02-20 09:29:10.602329',NULL,NULL,NULL),(112,NULL,NULL,'Win','2025-02-20 09:29:21.731793',NULL,NULL,NULL),(113,NULL,NULL,'Loss','2025-02-20 10:36:25.323867',NULL,NULL,NULL),(114,NULL,NULL,'Loss','2025-02-20 11:28:28.651756',NULL,NULL,NULL),(115,NULL,NULL,'Win','2025-02-20 11:29:32.779114',NULL,NULL,NULL),(116,NULL,NULL,'Loss','2025-02-20 13:35:54.122416',NULL,NULL,NULL),(117,NULL,NULL,'Win','2025-02-20 13:36:40.622119',NULL,NULL,NULL),(118,NULL,NULL,'Loss','2025-02-20 13:42:55.033623',NULL,NULL,NULL),(119,NULL,NULL,'Win','2025-02-20 13:43:05.204243',NULL,NULL,NULL),(120,NULL,NULL,'Win','2025-02-20 13:45:14.708238',NULL,NULL,NULL),(121,NULL,NULL,'Loss','2025-02-20 14:12:21.098492',NULL,NULL,NULL),(122,NULL,NULL,'Loss','2025-02-20 14:12:33.658517',NULL,NULL,NULL),(123,NULL,NULL,'Win','2025-02-20 14:50:30.936845',NULL,NULL,NULL),(124,NULL,NULL,'Loss','2025-02-21 08:38:02.130024',NULL,NULL,NULL),(125,NULL,NULL,'Loss','2025-02-21 08:39:15.215973',NULL,NULL,NULL),(126,NULL,NULL,'Loss','2025-02-21 08:42:42.746777',NULL,NULL,NULL),(127,NULL,NULL,'Loss','2025-02-21 08:43:11.084565',NULL,NULL,NULL),(128,NULL,NULL,'Loss','2025-02-21 08:46:45.716100',NULL,NULL,NULL),(129,NULL,NULL,'Win','2025-02-21 08:49:25.658039',NULL,NULL,NULL),(130,NULL,NULL,'Win','2025-02-21 09:04:07.721543',NULL,NULL,NULL),(131,NULL,NULL,'Loss','2025-02-21 09:06:43.556822',NULL,NULL,NULL),(132,NULL,NULL,'Loss','2025-02-21 09:07:04.781402',NULL,NULL,NULL),(133,NULL,NULL,'Loss','2025-02-21 09:07:38.947045',NULL,NULL,NULL),(134,NULL,NULL,'Loss','2025-02-21 09:09:40.768284',NULL,NULL,NULL),(135,NULL,NULL,'Loss','2025-02-21 09:09:56.067198',NULL,NULL,NULL),(136,NULL,NULL,'Loss','2025-02-21 09:10:10.618233',NULL,NULL,NULL),(137,NULL,NULL,'Loss','2025-02-21 09:14:11.538729',NULL,NULL,NULL),(138,NULL,NULL,'Loss','2025-02-21 09:14:27.922764',NULL,NULL,NULL),(139,NULL,NULL,'Win','2025-02-21 09:32:12.452794',NULL,NULL,NULL),(140,NULL,NULL,'Win','2025-02-21 09:38:45.431513',NULL,NULL,NULL),(141,NULL,NULL,'Win','2025-02-21 09:51:51.823494',NULL,NULL,NULL),(142,NULL,NULL,'Win','2025-02-21 10:05:59.880871',NULL,NULL,NULL),(143,NULL,NULL,'Win','2025-02-21 10:44:30.949216',NULL,NULL,NULL),(144,NULL,NULL,'Win','2025-02-21 10:46:37.087784',NULL,NULL,NULL),(145,NULL,NULL,'Win','2025-02-21 13:46:43.231050',NULL,NULL,NULL),(146,NULL,NULL,'Loss','2025-02-21 13:51:26.121698',NULL,NULL,NULL),(147,NULL,NULL,'Win','2025-02-21 14:13:04.705606',NULL,NULL,NULL),(148,NULL,NULL,'Win','2025-02-21 14:13:48.101200',NULL,NULL,NULL),(149,NULL,NULL,'Loss','2025-02-21 14:14:07.480579',NULL,NULL,NULL),(150,NULL,NULL,'Loss','2025-02-21 14:40:20.431579',NULL,NULL,NULL),(151,NULL,NULL,'Win','2025-02-21 14:55:20.331446',NULL,NULL,NULL),(152,NULL,NULL,'Win','2025-02-21 14:58:27.901052',NULL,NULL,NULL),(153,NULL,NULL,'Loss','2025-02-21 14:58:46.844604',NULL,NULL,NULL),(154,NULL,NULL,'Win','2025-02-21 17:49:48.426034',NULL,NULL,NULL),(155,NULL,NULL,'Win','2025-02-21 21:40:11.584125',NULL,NULL,NULL),(156,NULL,NULL,'Win','2025-02-21 21:54:33.335957',NULL,NULL,NULL),(157,NULL,NULL,'Loss','2025-02-21 22:05:06.250563',NULL,NULL,NULL),(158,NULL,NULL,'Loss','2025-02-21 22:06:39.486335',NULL,NULL,NULL),(159,NULL,NULL,'Loss','2025-02-21 22:07:28.168926',NULL,NULL,NULL),(160,NULL,NULL,'Loss','2025-02-21 22:16:47.237735',NULL,NULL,NULL),(161,NULL,NULL,'Loss','2025-02-21 22:18:06.617526',NULL,NULL,NULL),(162,NULL,NULL,'Loss','2025-02-21 22:18:18.857816',NULL,NULL,NULL),(163,NULL,NULL,'Loss','2025-02-21 22:18:57.102128',NULL,NULL,NULL),(164,NULL,NULL,'Loss','2025-02-21 22:19:14.756739',NULL,NULL,NULL),(165,NULL,NULL,'Loss','2025-02-21 22:19:26.149022',NULL,NULL,NULL),(166,NULL,NULL,'Loss','2025-02-21 22:19:45.004796',NULL,NULL,NULL),(167,NULL,NULL,'Win','2025-02-21 22:21:24.219356',NULL,NULL,NULL),(168,NULL,NULL,'Loss','2025-02-21 22:23:11.622961',NULL,NULL,NULL),(169,NULL,NULL,'Loss','2025-02-21 22:25:11.964183',NULL,NULL,NULL),(170,NULL,NULL,'Loss','2025-02-21 22:25:26.831004',NULL,NULL,NULL),(171,NULL,NULL,'Win','2025-02-21 22:25:41.302270',NULL,NULL,NULL),(172,NULL,NULL,'Loss','2025-02-21 22:28:05.790686',NULL,NULL,NULL),(173,NULL,NULL,'Win','2025-02-21 22:29:03.109415',NULL,NULL,NULL),(174,NULL,NULL,'Win','2025-02-22 08:12:45.503584',NULL,NULL,NULL),(175,NULL,NULL,'Loss','2025-02-22 08:13:18.653667',NULL,NULL,NULL),(176,NULL,NULL,'Win','2025-02-22 08:13:53.729365',NULL,NULL,NULL),(177,NULL,NULL,'Loss','2025-02-22 08:14:46.434379',NULL,NULL,NULL),(178,NULL,NULL,'Win','2025-02-22 08:18:44.051392',NULL,NULL,NULL),(179,NULL,NULL,'Loss','2025-02-22 08:20:11.703889',NULL,NULL,NULL),(180,NULL,NULL,'Win','2025-02-22 08:20:54.934549',NULL,NULL,NULL),(181,NULL,NULL,'Win','2025-02-22 08:21:31.782486',NULL,NULL,NULL),(182,NULL,NULL,'Loss','2025-02-22 08:22:13.039549',NULL,NULL,NULL),(183,NULL,NULL,'Loss','2025-02-22 08:23:02.368365',NULL,NULL,NULL),(184,NULL,NULL,'Win','2025-02-22 08:27:36.626308',NULL,NULL,NULL),(185,NULL,NULL,'Win','2025-02-22 10:39:48.249432',NULL,NULL,NULL),(186,NULL,NULL,'Win','2025-02-22 10:43:18.513803',NULL,NULL,NULL),(187,NULL,NULL,'Win','2025-02-22 10:44:12.957010',NULL,NULL,NULL),(188,NULL,NULL,'Win','2025-02-22 10:44:27.351288',NULL,NULL,NULL),(189,NULL,NULL,'Win','2025-02-22 10:46:49.750281',NULL,NULL,NULL),(190,NULL,NULL,'Loss','2025-02-22 10:47:06.836588',NULL,NULL,NULL),(191,NULL,NULL,'Loss','2025-02-22 10:47:42.703029',NULL,NULL,NULL),(192,NULL,NULL,'Win','2025-02-22 11:11:39.965001',NULL,NULL,NULL),(193,NULL,NULL,'Loss','2025-02-22 11:15:09.320746',NULL,NULL,NULL),(194,NULL,NULL,'Win','2025-02-22 11:16:38.637312',NULL,NULL,NULL),(195,NULL,NULL,'Loss','2025-02-22 11:16:56.359525',NULL,NULL,NULL),(196,NULL,NULL,'Win','2025-02-22 11:19:14.025517',NULL,NULL,NULL),(197,NULL,NULL,'Win','2025-02-22 11:19:31.008662',NULL,NULL,NULL),(198,NULL,NULL,'Loss','2025-02-22 11:19:47.936928',NULL,NULL,NULL),(199,NULL,NULL,'Loss','2025-02-22 15:04:56.734411',NULL,NULL,NULL),(200,NULL,NULL,'Win','2025-02-22 15:05:14.992529',NULL,NULL,NULL),(201,NULL,NULL,'Win','2025-02-22 15:40:27.534101',NULL,NULL,NULL),(202,NULL,NULL,'Win','2025-02-22 19:11:16.608651',NULL,NULL,NULL),(203,NULL,NULL,'Win','2025-02-23 15:31:39.353581',NULL,NULL,NULL),(204,NULL,NULL,'Win','2025-02-23 15:31:53.264249',NULL,NULL,NULL),(205,NULL,NULL,'Loss','2025-02-23 15:32:12.678729',NULL,NULL,NULL),(206,NULL,NULL,'Loss','2025-02-25 08:35:10.740890',NULL,NULL,NULL),(207,NULL,NULL,'Loss','2025-02-25 08:38:12.764263',NULL,NULL,NULL),(208,NULL,NULL,'Win','2025-02-25 08:39:18.186816',NULL,NULL,NULL),(209,NULL,NULL,'Loss','2025-02-25 08:41:30.251251',NULL,NULL,NULL),(210,NULL,NULL,'Win','2025-02-26 08:42:12.921579',NULL,NULL,NULL),(211,4,25,'Win','2025-02-26 08:49:29.645186',NULL,NULL,NULL),(212,8,24,'Win','2025-02-26 08:55:27.507256',NULL,NULL,NULL),(213,10,20,'Loss','2025-02-26 08:57:56.832931',NULL,NULL,NULL),(214,8,16,'Win','2025-02-26 09:06:10.970163',NULL,NULL,NULL),(215,15,30,'Loss','2025-02-26 09:08:00.754081',NULL,NULL,NULL),(216,8,23,'Win','2025-02-26 09:38:29.021523',NULL,NULL,NULL),(217,9,26,'Win','2025-02-26 09:38:46.273282',NULL,NULL,NULL),(218,9,26,'Win','2025-02-26 09:40:18.527972',NULL,NULL,NULL),(219,8,25,'Win','2025-02-26 09:43:19.825497',NULL,NULL,NULL),(220,7,16,'Win','2025-02-26 09:46:02.621048',NULL,NULL,NULL),(221,7,16,'Win','2025-02-26 09:46:19.893885',NULL,NULL,NULL),(222,7,16,'Win','2025-02-26 09:48:17.615125',NULL,NULL,NULL),(223,7,16,'Win','2025-02-26 09:48:40.344447',NULL,NULL,NULL),(224,7,16,'Win','2025-02-26 09:48:56.981968',NULL,NULL,NULL),(225,7,16,'Win','2025-02-26 09:49:59.387295',NULL,NULL,NULL),(226,5,21,'Loss','2025-02-26 09:55:31.346017',NULL,NULL,NULL),(227,11,18,'Loss','2025-02-26 10:37:56.364883',NULL,NULL,NULL),(228,7,22,'Win','2025-02-26 11:35:38.625988',NULL,NULL,NULL),(229,6,26,'Win','2025-02-26 11:40:28.415202',NULL,NULL,NULL),(230,4,26,'Win','2025-02-26 11:42:00.546756',NULL,NULL,NULL),(231,7,16,'Win','2025-02-26 11:44:50.223953',NULL,NULL,NULL),(232,6,30,'Loss','2025-02-26 11:45:24.732348',NULL,NULL,NULL),(233,8,26,'Win','2025-02-26 14:00:42.972656',NULL,NULL,NULL),(234,10,18,'Loss','2025-02-26 14:03:07.929508',NULL,NULL,NULL),(235,10,18,'Loss','2025-02-26 14:04:28.815936',NULL,NULL,NULL),(236,11,24,'Loss','2025-02-26 14:04:43.023826',NULL,NULL,NULL),(237,10,21,'Loss','2025-02-26 14:05:05.409324',NULL,NULL,NULL),(238,11,26,'Win','2025-02-26 14:05:22.453061',NULL,NULL,NULL),(239,11,30,'Win','2025-02-26 14:06:20.338279',NULL,NULL,NULL),(240,11,23,'Win','2025-02-26 14:15:09.430911',NULL,NULL,NULL),(241,14,18,'Win','2025-02-26 14:26:45.587975',NULL,NULL,NULL),(242,14,16,'Win','2025-02-27 08:01:39.489312',NULL,NULL,NULL),(243,7,21,'Win','2025-02-28 15:25:54.892330',NULL,NULL,NULL),(244,7,21,'Win','2025-02-28 16:39:53.540750',NULL,NULL,NULL),(245,7,21,'Win','2025-02-28 16:42:29.161534',NULL,NULL,NULL),(246,7,21,'Win','2025-02-28 16:42:48.965952',NULL,NULL,NULL),(247,7,21,'Win','2025-02-28 16:43:19.018039',NULL,NULL,NULL),(248,7,21,'Win','2025-02-28 16:44:56.610797',NULL,NULL,NULL),(249,7,21,'Win','2025-02-28 16:47:01.565526',NULL,NULL,NULL),(250,7,21,'Win','2025-02-28 16:48:25.862185',NULL,NULL,NULL),(251,7,21,'Win','2025-02-28 16:48:44.616416',NULL,NULL,NULL),(252,7,21,'Win','2025-02-28 16:49:48.296333',NULL,NULL,NULL),(253,7,21,'Win','2025-02-28 16:49:54.745639',NULL,NULL,NULL),(254,7,21,'Win','2025-02-28 16:50:37.722423',NULL,NULL,NULL),(255,1,20,'Loss','2025-02-28 16:51:09.313814',NULL,NULL,NULL),(256,10,17,'Win','2025-02-28 16:58:49.183650',NULL,NULL,NULL),(257,10,17,'Win','2025-02-28 16:59:00.579129',NULL,NULL,NULL),(258,10,17,'Win','2025-02-28 16:59:48.209509',NULL,NULL,NULL),(259,4,30,'Loss','2025-02-28 17:01:32.245545',NULL,NULL,NULL),(260,12,21,'Win','2025-02-28 17:07:31.084943',NULL,NULL,NULL),(261,12,21,'Win','2025-02-28 17:16:05.773097',NULL,NULL,NULL),(262,7,16,'Win','2025-02-28 17:21:18.427482',NULL,NULL,NULL),(263,7,16,'Win','2025-02-28 17:21:48.531932',NULL,NULL,NULL),(264,7,16,'Win','2025-02-28 17:22:08.435163',NULL,NULL,NULL),(265,8,24,'Win','2025-03-01 09:26:19.680605',NULL,NULL,NULL),(266,12,27,'Win','2025-03-01 09:28:07.678227',NULL,NULL,NULL),(267,5,23,'Win','2025-03-01 09:44:53.833121',NULL,NULL,NULL),(268,1,17,'Loss','2025-03-01 09:47:38.891889',NULL,NULL,NULL),(269,7,26,'Win','2025-03-01 09:53:06.759067',NULL,NULL,NULL),(270,9,20,'Win','2025-03-01 09:54:51.359262',NULL,NULL,NULL),(271,13,21,'Win','2025-03-01 09:56:06.913321',NULL,NULL,NULL),(272,1,21,'Loss','2025-03-01 09:57:09.844859',NULL,NULL,NULL),(273,7,29,'Loss','2025-03-01 10:00:41.980552',NULL,NULL,NULL),(274,1,26,'Win','2025-03-01 13:17:29.456340',NULL,NULL,NULL),(275,1,26,'Win','2025-03-01 13:18:58.235141',NULL,NULL,NULL),(276,1,26,'Win','2025-03-01 13:19:22.382429',NULL,NULL,NULL),(277,8,22,'Win','2025-03-01 13:58:17.331230','lose',NULL,NULL),(278,7,23,'Win','2025-03-01 14:04:13.451542','lost',NULL,NULL),(279,2,24,'Loss','2025-03-01 14:07:40.518596','Lost',NULL,NULL),(280,4,17,'Defeat','2025-03-01 14:08:52.423635','Lost',NULL,NULL),(281,8,23,'Victory','2025-03-01 14:22:35.127087','Won',NULL,NULL),(282,9,20,'Victory','2025-03-01 14:23:46.177740','Won',NULL,NULL),(283,5,26,'Victory','2025-03-01 14:24:12.121505','Lost',NULL,NULL),(284,11,22,'Victory','2025-03-01 14:24:34.542734','Won',NULL,NULL),(285,11,22,'Victory','2025-03-01 14:25:39.799229','Won',NULL,NULL),(286,5,16,'Victory','2025-03-01 14:25:54.888415','Won',NULL,NULL),(287,6,18,'Defeat','2025-03-01 14:26:18.137672','Lost',NULL,NULL),(288,5,19,'Defeat','2025-03-01 14:26:42.532566','Lost',NULL,NULL),(289,8,18,'Victory','2025-03-01 16:31:59.596614','Won',NULL,NULL),(290,3,28,'Defeat','2025-03-01 16:32:26.690074','Won',NULL,NULL),(291,4,18,'Victory','2025-03-02 08:23:20.692843','Won',NULL,NULL),(292,5,18,'Defeat','2025-03-02 08:27:54.599882','Lost',NULL,NULL),(293,9,29,'Defeat','2025-03-02 08:28:25.413015','Lost',NULL,NULL),(294,11,24,'Victory','2025-03-02 08:28:47.084871','Won',NULL,NULL),(295,11,18,'Victory','2025-03-02 08:29:07.217615','Lost',NULL,NULL),(296,9,22,'Victory','2025-03-02 08:37:54.966368','Lost',NULL,NULL),(297,5,29,'Defeat','2025-03-02 14:40:23.224486','Won',NULL,NULL),(298,9,16,'Victory','2025-03-02 15:07:46.636062','Lost',NULL,NULL),(299,9,16,'Victory','2025-03-02 15:08:37.494527','Lost',NULL,NULL),(300,9,16,'Victory','2025-03-02 15:09:46.616044','Lost',NULL,NULL),(301,9,16,'Victory','2025-03-02 15:12:36.700883','Lost',NULL,NULL),(302,9,16,'Victory','2025-03-02 15:13:16.030477','Lost',NULL,NULL),(303,9,16,'Victory','2025-03-02 15:15:04.049313','Lost',NULL,NULL),(304,5,17,'Defeat','2025-03-02 16:58:04.511081','Lost',NULL,NULL),(305,9,24,'Victory','2025-03-02 17:05:23.050632','Lost',NULL,NULL),(306,11,19,'Victory','2025-03-02 17:05:51.897193','Lost',NULL,NULL),(307,2,28,'Defeat','2025-03-02 19:36:17.863929','Won',NULL,NULL),(308,9,23,'Victory','2025-03-03 21:18:09.220305','Won',NULL,NULL),(309,7,28,'Defeat','2025-03-03 21:18:44.589630','Lost',NULL,NULL),(310,9,19,'Victory','2025-03-03 21:42:13.042121','Lost',NULL,NULL),(311,5,18,'Defeat','2025-03-03 21:42:39.914297','Lost',NULL,NULL),(312,11,24,'Victory','2025-03-04 13:08:49.581953','Won',NULL,NULL),(313,6,24,'Defeat','2025-03-04 13:09:15.947639','Lost',NULL,NULL),(314,11,28,'Victory','2025-03-04 14:05:41.159143','Won',NULL,NULL),(315,12,29,'Defeat','2025-03-04 14:25:40.471306','Lost',NULL,NULL),(316,15,23,'Victory','2025-03-04 14:26:10.661646','Lost',NULL,NULL),(317,9,30,'Defeat','2025-03-04 14:29:39.703085','Lost',NULL,NULL),(318,9,23,'Victory','2025-03-04 17:51:16.362172','Lost',NULL,NULL),(319,7,23,'Victory','2025-03-04 20:37:12.715968','Lost',NULL,NULL),(320,9,18,'Victory','2025-03-04 22:51:29.870906','Lost',NULL,NULL),(321,7,19,'Victory','2025-03-05 08:30:37.958349','Lost',65,61),(322,4,26,'Victory','2025-03-05 08:31:06.427837','Lost',67,60),(323,7,29,'Victory','2025-03-05 08:37:04.857829','Won',68,61),(324,9,27,'Victory','2025-03-05 08:37:29.744851','Won',67,61),(325,10,19,'Victory','2025-03-05 08:37:50.089518','Lost',65,62),(326,1,17,'Defeat','2025-03-05 08:38:10.360015','Lost',64,59),(327,10,27,'Victory','2025-03-05 08:38:30.507930','Won',67,62),(328,13,27,'Victory','2025-03-05 08:38:46.540374','Lost',67,63),(329,4,16,'Victory','2025-03-05 08:39:01.645457','Won',64,60),(330,10,25,'Victory','2025-03-05 08:57:20.288363','Won',67,62),(331,8,28,'Victory','2025-03-05 08:58:29.623695','Won',68,61),(332,10,28,'Defeat','2025-03-05 08:59:40.759794','Lost',68,62),(333,8,18,'Victory','2025-03-05 09:15:11.257548','Lost',64,61),(334,1,28,'Defeat','2025-03-05 09:15:38.562040','Lost',68,59),(335,2,20,'Defeat','2025-03-05 09:16:01.209688','Lost',65,59),(336,10,17,'Victory','2025-03-05 09:16:20.496648','Won',64,62),(337,13,21,'Victory','2025-03-05 12:11:28.291142','Lost',65,63),(338,14,25,'Victory','2025-03-05 12:11:53.207549','Won',67,63),(339,4,18,'Defeat','2025-03-05 12:12:15.430300','Lost',64,60),(340,1,16,'Defeat','2025-03-05 12:12:31.126725','Won',64,59);
/*!40000 ALTER TABLE `app_battleoutcome` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_character`
--

DROP TABLE IF EXISTS `app_character`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_character` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `is_main_character` tinyint(1) NOT NULL,
  `is_antagonist` tinyint(1) NOT NULL,
  `attacks` int NOT NULL DEFAULT '10',
  `life_points` int NOT NULL DEFAULT '100',
  `defense` int NOT NULL DEFAULT '5',
  `quotes` json NOT NULL DEFAULT (_utf8mb3'[]'),
  `race` varchar(100) NOT NULL DEFAULT 'Human',
  `special_ability` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_character`
--

LOCK TABLES `app_character` WRITE;
/*!40000 ALTER TABLE `app_character` DISABLE KEYS */;
INSERT INTO `app_character` VALUES (59,'Aragorn',1,0,12,-2,5,'[\"Tis the Lady of L\'thien. The Elf Maiden who gave her love to Beren ... a mortal.\"]','Human',NULL),(60,'Frodo',1,0,14,-2,5,'[\"What do you want?\"]','Hobbit',NULL),(61,'Legolas',1,0,14,66,9,'[\"Govannas v\'n gwennen le, Haldir o L\'rien.\"]','Elf',NULL),(62,'Gimli',1,0,13,81,10,'[\"Legolas! Two already!\"]','Dwarf',NULL),(63,'Gandalf',1,0,10,100,10,'[\"It\'s only a matter of time. He has suffered a defeat, yes, but behind the walls of Mordor our enemy is regrouping.\"]','Wizard',NULL),(64,'Sauron',0,1,11,32,8,'[]','Maia',NULL),(65,'Saruman',0,1,10,0,9,'[]','Wizard',NULL),(66,'Gollum',0,1,15,0,4,'[]','Hobbit',NULL),(67,'Nazgul',0,1,10,0,6,'[]','Wraith',NULL),(68,'Lurtz',0,1,13,76,10,'[]','Uruk-hai',NULL);
/*!40000 ALTER TABLE `app_character` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `sqlite_autoindex_auth_group_1` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq_1` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_FK_0_0` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_FK_1_0` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq_1` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `auth_permission_FK_0_0` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add battle outcome',7,'add_battleoutcome'),(26,'Can change battle outcome',7,'change_battleoutcome'),(27,'Can delete battle outcome',7,'delete_battleoutcome'),(28,'Can view battle outcome',7,'view_battleoutcome'),(29,'Can add character',8,'add_character'),(30,'Can change character',8,'change_character'),(31,'Can delete character',8,'delete_character'),(32,'Can view character',8,'view_character'),(33,'Can add artifact',9,'add_artifact'),(34,'Can change artifact',9,'change_artifact'),(35,'Can delete artifact',9,'delete_artifact'),(36,'Can view artifact',9,'view_artifact');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `sqlite_autoindex_auth_user_1` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq_1` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  CONSTRAINT `auth_user_groups_FK_0_0` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_FK_1_0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_un_1` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_FK_0_0` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_FK_1_0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_FK_0_0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_FK_1_0` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq_1` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'app','artifact'),(7,'app','battleoutcome'),(8,'app','character'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-19 20:41:06.459534'),(2,'auth','0001_initial','2025-02-19 20:41:06.597526'),(3,'admin','0001_initial','2025-02-19 20:41:06.634950'),(4,'admin','0002_logentry_remove_auto_add','2025-02-19 20:41:06.641529'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-19 20:41:06.645908'),(6,'app','0001_initial','2025-02-19 20:41:06.652197'),(11,'contenttypes','0002_remove_content_type_name','2025-02-19 20:41:06.747135'),(12,'auth','0002_alter_permission_name_max_length','2025-02-19 20:41:06.768681'),(13,'auth','0003_alter_user_email_max_length','2025-02-19 20:41:06.782594'),(14,'auth','0004_alter_user_username_opts','2025-02-19 20:41:06.788092'),(15,'auth','0005_alter_user_last_login_null','2025-02-19 20:41:06.806282'),(16,'auth','0006_require_contenttypes_0002','2025-02-19 20:41:06.807539'),(17,'auth','0007_alter_validators_add_error_messages','2025-02-19 20:41:06.813299'),(18,'auth','0008_alter_user_username_max_length','2025-02-19 20:41:06.834831'),(19,'auth','0009_alter_user_last_name_max_length','2025-02-19 20:41:06.854453'),(20,'auth','0010_alter_group_name_max_length','2025-02-19 20:41:06.864719'),(21,'auth','0011_update_proxy_permissions','2025-02-19 20:41:06.870688'),(22,'auth','0012_alter_user_first_name_max_length','2025-02-19 20:41:06.894263'),(23,'sessions','0001_initial','2025-02-19 20:41:06.904558'),(25,'app','0006_auto_20250222_1051','2025-02-22 10:52:16.902482'),(27,'app','0002_character','2025-02-22 19:47:51.058740'),(28,'app','0003_auto_20250212_1922','2025-02-22 19:47:55.138512'),(29,'app','0004_character_attack_points_character_life_points','2025-02-22 19:47:58.585862'),(30,'app','0005_rename_attack_points_character_attacks_and_more','2025-02-22 19:48:02.336236'),(31,'app','0006_auto_20250222_2024','2025-02-22 20:27:17.132477'),(32,'auth','0006_auto_20250222_1918','2025-02-23 11:59:06.631238'),(33,'app','0007_auto_20250223_1207','2025-02-23 12:09:41.708446'),(34,'app','0008_remove_character_secret_weapon','2025-02-23 12:15:29.626128'),(35,'app','0009_battleoutcome_coin_toss_result','2025-03-01 13:54:39.508682'),(36,'app','0010_alter_battleoutcome_outcome','2025-03-05 08:09:32.759907'),(37,'app','0011_auto_20250305_0818','2025-03-05 08:18:07.536549');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`),
  KEY `django_session_expire_date_a5c62663_1` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7iwojxd8tt6srtn0nz24a3vzv6rxy51u','.eJxVjEEKgCAUBe_y1i4qSqiLtBSxHwnmF7VVdPcsiGr3GN7MjkSOTKZJmUVHXVZUdsLQ9QIcAnvy-QayFe9Xx2zncsaApoKAYetV5pRUpLS5i4_s8Uk8xt2qpcCqi_KnxwkJwDIG:1tpnby:IXBdtV2bBokj6ORrjX-wUl30mq8U4fbZgYwsDOeVPpQ','2025-03-19 12:12:30.343287'),('g8in2u8lg7knca7zv5sn6ns44ot3j1pb','.eJyrVipOzUlNLklNic9ILcpXslLySU3Pz0ksVtJRyi8oyM9LzSsBCZYWlVQBheCKkzMSixKBrKL4zBQlKyOEYjDfohYAdGwfOA:1tjESo:69AO4Nhl00POImjFxMEiQIUyijWoDufkQorcccoYYeU','2025-03-01 09:27:54.356873'),('qd6m5c8g2b87gb0wgyd3xu8ypt1ga83y','eyJzZWxlY3RlZF9jaGFyYWN0ZXJfaWQiOjYwLCJvcHBvbmVudF9pZCI6NjR9:1tlQXP:3YbTS0y4YAP6FxF5CH-KiCmrBm0i-s-QpEDR_23QGKU','2025-03-07 10:45:43.006426'),('vrxtch95przimpjt05i8uq3mncq3jyg0','eyJzZWxlY3RlZF9oZXJvIjoiQXJhZ29ybiJ9:1tidJY:u5It_Oq294vVUaob1V0lYQtLqwqiVC5RGZotXaL-Z4Y','2025-02-27 17:47:52.906025'),('w84q87f50h8z62eafefdlovclfcs9dek','eyJzZWxlY3RlZF9jaGFyYWN0ZXJfaWQiOjYwLCJvcHBvbmVudF9pZCI6NjV9:1tlQV1:OvIPjgyii9yAI26SaW-YwFtlwIZ6UfgYoaFWREE8SD0','2025-03-07 10:43:15.558459');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-05 15:33:45

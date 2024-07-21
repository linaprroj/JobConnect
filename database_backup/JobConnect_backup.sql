-- MySQL dump 10.13  Distrib 9.0.0, for macos14 (arm64)
--
-- Host: localhost    Database: JobConnect
-- ------------------------------------------------------
-- Server version	9.0.0

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
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_seeker_id` int DEFAULT NULL,
  `job_offer_id` int DEFAULT NULL,
  `status` enum('Applied','Interview Scheduled','Accepted','Rejected','Cancelled') DEFAULT NULL,
  `applied_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `job_seeker_id` (`job_seeker_id`),
  KEY `job_offer_id` (`job_offer_id`),
  CONSTRAINT `applications_ibfk_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seekers` (`id`),
  CONSTRAINT `applications_ibfk_2` FOREIGN KEY (`job_offer_id`) REFERENCES `job_offers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
INSERT INTO `applications` VALUES (1,1,1,'Applied','2024-07-21 19:00:55',NULL,'2024-07-21 19:29:35'),(2,2,2,'Applied','2024-07-21 19:00:55',NULL,'2024-07-21 19:29:35'),(3,3,3,'Applied','2024-07-21 19:00:55',NULL,'2024-07-21 19:29:35'),(4,4,4,'Applied','2024-07-21 19:00:55',NULL,'2024-07-21 19:29:35'),(5,5,5,'Applied','2024-07-21 19:00:55',NULL,'2024-07-21 19:29:35');
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interviews`
--

DROP TABLE IF EXISTS `interviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_seeker_id` int DEFAULT NULL,
  `job_offer_id` int DEFAULT NULL,
  `interview_date` datetime DEFAULT NULL,
  `interview_status` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `job_seeker_id` (`job_seeker_id`),
  KEY `job_offer_id` (`job_offer_id`),
  CONSTRAINT `interviews_ibfk_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seekers` (`id`),
  CONSTRAINT `interviews_ibfk_2` FOREIGN KEY (`job_offer_id`) REFERENCES `job_offers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interviews`
--

LOCK TABLES `interviews` WRITE;
/*!40000 ALTER TABLE `interviews` DISABLE KEYS */;
INSERT INTO `interviews` VALUES (1,1,1,'2024-08-01 10:00:00','Scheduled','2024-07-21 19:26:04',NULL,'2024-07-21 19:29:35'),(2,2,2,'2024-08-02 14:00:00','Scheduled','2024-07-21 19:26:04',NULL,'2024-07-21 19:29:35'),(3,3,3,'2024-08-03 09:00:00','Completed','2024-07-21 19:26:04',NULL,'2024-07-21 19:29:35'),(4,4,4,'2024-08-04 11:00:00','Scheduled','2024-07-21 19:26:04',NULL,'2024-07-21 19:29:35'),(5,5,5,'2024-08-05 15:00:00','Cancelled','2024-07-21 19:26:04',NULL,'2024-07-21 19:29:35');
/*!40000 ALTER TABLE `interviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_offers`
--

DROP TABLE IF EXISTS `job_offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_offers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_title` varchar(100) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `description` text,
  `requirements` text,
  `salary` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_job_offer_title` (`job_title`),
  CONSTRAINT `chk_salary` CHECK (regexp_like(`salary`,_utf8mb4'^[0-9]+(.[0-9]{1,2})?$'))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_offers`
--

LOCK TABLES `job_offers` WRITE;
/*!40000 ALTER TABLE `job_offers` DISABLE KEYS */;
INSERT INTO `job_offers` VALUES (1,'Data Scientist','Tech Innovators Inc.','San Francisco, CA','Seeking a data scientist to analyze large datasets and develop predictive models.','Experience with Python, R, and machine learning algorithms.','120000','2024-07-21 19:00:35',NULL,'2024-07-21 19:31:25'),(2,'Full-Stack Developer','Web Solutions LLC','New York, NY','Looking for a full-stack developer to build and maintain web applications.','Proficiency in JavaScript, React, Node.js, and SQL.','110000','2024-07-21 19:00:35',NULL,'2024-07-21 19:31:25'),(3,'Robotics Engineer','Automation Experts','Boston, MA','Hiring a robotics engineer to design and develop robotic systems.','Knowledge of ROS, C++, and mechanical design principles.','100000','2024-07-21 19:00:35',NULL,'2024-07-21 19:31:25'),(4,'Embedded Systems Engineer','IoT Innovations','Austin, TX','Need an embedded systems engineer to develop firmware for IoT devices.','Experience with C, C++, and microcontroller programming.','105000','2024-07-21 19:00:35',NULL,'2024-07-21 19:31:25'),(5,'Process Engineer','Sustainable Energy Corp.','Seattle, WA','Seeking a process engineer to optimize manufacturing processes for energy efficiency.','Background in chemical engineering and process simulation software.','95000','2024-07-21 19:00:35',NULL,'2024-07-21 19:31:25');
/*!40000 ALTER TABLE `job_offers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_seekers`
--

DROP TABLE IF EXISTS `job_seekers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_seekers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `resume` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `idx_job_seeker_email` (`email`),
  CONSTRAINT `chk_email_format` CHECK ((`email` like _utf8mb4'%_@__%.__%'))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_seekers`
--

LOCK TABLES `job_seekers` WRITE;
/*!40000 ALTER TABLE `job_seekers` DISABLE KEYS */;
INSERT INTO `job_seekers` VALUES (1,'Alice','Smith','alice.smith@example.com','hashed_password_1','Experienced data scientist with expertise in machine learning and big data analytics.','2024-07-21 19:00:28',NULL,'2024-07-21 19:29:35'),(2,'Bob','Johnson','bob.johnson@example.com','hashed_password_2','Software engineer with a strong background in full-stack development and cloud computing.','2024-07-21 19:00:28',NULL,'2024-07-21 19:29:35'),(3,'Carol','Williams','carol.williams@example.com','hashed_password_3','Mechanical engineer with extensive experience in robotics and automation.','2024-07-21 19:00:28',NULL,'2024-07-21 19:29:35'),(4,'David','Brown','david.brown@example.com','hashed_password_4','Electrical engineer specializing in embedded systems and IoT devices.','2024-07-21 19:00:28',NULL,'2024-07-21 19:29:35'),(5,'Eve','Davis','eve.davis@example.com','hashed_password_5','Chemical engineer with a focus on process engineering and sustainable energy solutions.','2024-07-21 19:00:28',NULL,'2024-07-21 19:29:35');
/*!40000 ALTER TABLE `job_seekers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender_id` int DEFAULT NULL,
  `receiver_id` int DEFAULT NULL,
  `sender_type` enum('job_seeker','job_offerer') DEFAULT NULL,
  `receiver_type` enum('job_seeker','job_offerer') DEFAULT NULL,
  `message_content` text,
  `sent_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `job_seekers` (`id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `job_seekers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-21 15:36:11

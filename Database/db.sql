/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - ai_sas
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `ai_sas`;

USE `ai_sas`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `chat_msg` */

DROP TABLE IF EXISTS `chat_msg`;

CREATE TABLE `chat_msg` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `msg` varchar(1000) DEFAULT NULL,
  `user_` varchar(100) DEFAULT NULL,
  `time_` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=latin1;

/*Data for the table `chat_msg` */

insert  into `chat_msg`(`sno`,`msg`,`user_`,`time_`) values (93,'Hello','chatbot','2024-09-22 16:52:16'),(94,'Dear a','chatbot','2024-09-22 16:52:16'),(95,'How can I help you..','chatbot','2024-09-22 16:52:16'),(96,'hhdf','a','2024-09-22 16:53:45'),(97,'Sorry, I am not understood..','chatbot','2024-09-22 16:53:45');

/*Table structure for table `crop_fertilizers` */

DROP TABLE IF EXISTS `crop_fertilizers`;

CREATE TABLE `crop_fertilizers` (
  `crop_name` varchar(100) DEFAULT NULL,
  `fertilizers` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `crop_fertilizers` */

insert  into `crop_fertilizers`(`crop_name`,`fertilizers`) values ('Adzuki Beans','GoldchanceSuperGrowth or LavenderSuperGrowth,N.P.K 23.23'),('apple',' N-P-K 12-12-12,11-15-15'),('banana','urea,less of phosphorous,potash'),('Black gram','20:30:30,urea,rock phosphate,Potash'),('Chickpea','nitrogen,phosphorus,potassium '),('Coconut','urea,super phosphate,muriate potash'),('Coffee','nitrogen,phosphorus and potassium'),('Cotton','14-35-14,20-20,Urea,17-17-17,28-28,DAP'),('grapes','urea,ammonium nitrate and ammonium sulfate'),('Ground Nut','DAP,28-28,17-17-17,Urea,DAP'),('Jute','40:20:20,40-45,70-75'),('Kidney Beans','5-10-10,ammonium sulfate,ammonium nitrate,urea,potassium sulfate'),('Lentil','Nitrogen,Phosphorus,Sulphur'),('maize','Urea,17-17-17,28-28,14-35-14'),('mango','mushroom compost,potash or sulphate,potash,urea,superphosphate'),('millet','20-20,28-28,Urea,DAP'),('Moth Beans','Phorate or Chloropyriphos'),('Mung Bean','diammonium hydrogen phosphate,potassium sulfate'),('muskmelon','Superphosphate,Potash,40:60:30'),('orange','Ammonium Sulfate,Ammonium Phosphate,Citrus Food fertilizer'),('papaya','10-10-10,14-14-14'),('Peas','5-10-10,phosphorus,sulphur'),('Pigeon Peas','MAHAFLORA,PROZIN12,GLUCOMIC3,BOROFOLL,MIXOL,SOLUSEAMIX'),('pomegranate','Vermicompost'),('rice','Ammonium sulphate,Urea,DAP,Super-phosphate'),('Rubber','10:10:10,nitrogen,phosphorus,potassium'),('Sugarcane','DAP,17-17-17,Urea,14-35-14,20-20'),('Tea','Ammonium sulphate,nitrogen and sulphur.'),('Tobacco','28-28,DAP,Urea,10-26-26'),('watermelon','phosphorus,potassium,phosphorus'),('wheat','Urea,DAP,28-28,14-35-14,20-20,10-26-26');

/*Table structure for table `fertilizers` */

DROP TABLE IF EXISTS `fertilizers`;

CREATE TABLE `fertilizers` (
  `pest_name` varchar(100) DEFAULT NULL,
  `pesticides` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fertilizers` */

insert  into `fertilizers`(`pest_name`,`pesticides`) values ('Adristyrannus','Acephate,Malathion,Permethrin'),('Ampelophaga','Chlorpyrifos,Methoxyfenozide,Spinosad'),('Cicadellaviridis','Imidacloprid,Thiacloprid,Dinotefuran,Thiamethoxam'),('Indigocaterpillar','Carbaryl,Imidacloprid,Acephate'),('Leafbeetle','Chlorpyrifos,Imidacloprid,Acephate');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `name` varchar(100) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobilenumber` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

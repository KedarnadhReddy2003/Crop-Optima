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

/*Table structure for table `crop_fertilizers` */

DROP TABLE IF EXISTS `crop_fertilizers`;

CREATE TABLE `crop_fertilizers` (
  `crop_name` varchar(100) DEFAULT NULL,
  `fertilizers` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `crop_fertilizers` */

insert  into `crop_fertilizers`(`crop_name`,`fertilizers`) values ('Adzuki Beans','GoldchanceSuperGrowth or LavenderSuperGrowth,N.P.K 23.23'),('apple',' N-P-K 12-12-12,11-15-15'),('banana','urea,less of phosphorous,potash'),('Black gram','20:30:30,urea,rock phosphate,Potash'),('Chickpea','nitrogen,phosphorus,potassium '),('Coconut','urea,super phosphate,muriate potash'),('Coffee','nitrogen,phosphorus and potassium'),('Cotton','14-35-14,20-20,Urea,17-17-17,28-28,DAP'),('grapes','urea,ammonium nitrate and ammonium sulfate'),('Ground Nut','DAP,28-28,17-17-17,Urea,DAP'),('Jute','40:20:20,40-45,70-75'),('Kidney Beans','5-10-10,ammonium sulfate,ammonium nitrate,urea,potassium sulfate'),('Lentil','Nitrogen,Phosphorus,Sulphur'),('maize','Urea,17-17-17,28-28,14-35-14'),('mango','mushroom compost,potash or sulphate,potash,urea,superphosphate'),('millet','20-20,28-28,Urea,DAP'),('Moth Beans','Phorate or Chloropyriphos'),('Mung Bean','diammonium hydrogen phosphate,potassium sulfate'),('muskmelon','Superphosphate,Potash,40:60:30'),('orange','Ammonium Sulfate,Ammonium Phosphate,Citrus Food fertilizer'),('papaya','10-10-10,14-14-14'),('Peas','5-10-10,phosphorus,sulphur'),('Pigeon Peas','MAHAFLORA,PROZIN12,GLUCOMIC3,BOROFOLL,MIXOL,SOLUSEAMIX'),('pomegranate','Vermicompost'),('rice','Ammonium sulphate,Urea,DAP,Super-phosphate'),('Rubber','10:10:10,nitrogen,phosphorus,potassium'),('Sugarcane','DAP,17-17-17,Urea,14-35-14,20-20'),('Tea','Ammonium sulphate,nitrogen and sulphur.'),('Tobacco','28-28,DAP,Urea,10-26-26'),('watermelon','phosphorus,potassium,phosphorus'),('wheat','Urea,DAP,28-28,14-35-14,20-20,10-26-26');

/*Table structure for table `remidies` */

DROP TABLE IF EXISTS `remidies`;

CREATE TABLE `remidies` (
  `disease` varchar(100) DEFAULT NULL,
  `reasons` varchar(1000) DEFAULT NULL,
  `solutions` varchar(1000) DEFAULT NULL,
  `fertilizer` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `remidies` */

insert  into `remidies`(`disease`,`reasons`,`solutions`,`fertilizer`) values ('Apple_Black_rot','Fungal infection caused by Botryosphaeria obtusa,Warm, humid conditions favor fungal growth,Infected leaves, fruit, or dead wood left in orchards.','Cultural Practices,Fungicide Application,Tree Care,Orchard Hygiene\n','Balanced NPK fertilizer (e.g., 10-10-10 or 14-14-14) to improve tree vigor,Organic Option: Compost or well-rotted manure to enhance soil health.'),('Peach_Bacterial_spot','Caused by Xanthomonas arboricola pv. pruni,High humidity and prolonged leaf wetness,Injuries to leaves or fruit provide entry points for bacteria.','Preventive Measures,Chemical Control,Resistant Varieties\n','Low-nitrogen, high-potassium fertilizer (e.g., 5-10-15) to avoid excessive leafy growth,Organic Option: Compost with potassium-rich sources like banana peels or wood ash.'),('Pepper_bell_Bacterial_spot','Caused by Xanthomonas campestris pv. vesicatoria,Contaminated seeds or transplants,Poor crop rotation practices.','Seed Treatment,Crop Rotation,Protective Sprays','Calcium-rich fertilizers (e.g., Calcium Nitrate) to strengthen cell walls,Organic Option: Bone meal or fish emulsion for balanced growth.'),('Potato_Early_blight','Caused by the fungus Alternaria solani,Infected plant debris or soil-borne spores,Prolonged periods of leaf wetness from rain, dew, or overhead irrigation.','Fertilization,Chemical Control,Cultural Practices','Potassium and phosphorus-rich fertilizers (e.g., 5-10-10 or 10-20-20),Organic Option: Rock phosphate and bone meal.'),('Strawberry_Leaf_scorch','Fungal infection caused by Diplocarpon earliana,Poorly drained soil,Excessive rain or overwatering leading to high humidity.','Good Cultivation Practices,Fungicide Use,Resistant Varieties','Balanced fertilizer (e.g., 10-10-10) with micronutrients like magnesium,Organic Option: Well-composted manure and potassium-rich fertilizers.'),('Tomato_Target_Spot','Caused by Corynespora cassiicola, a fungal pathogen,Poor air circulation around plants,Infected crop residues left in the field.','Cultural Control,Irrigation Management,Chemical Control','Nitrogen-rich fertilizers (e.g., 10-5-10) but not excessive nitrogen,Organic Option: Seaweed extract, compost tea, and neem cake.');

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

insert  into `users`(`name`,`userid`,`password`,`email`,`mobilenumber`) values ('CLOUDTECHNOLOGIES','ct123','ct123','ct@gmail.com','8121953811');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

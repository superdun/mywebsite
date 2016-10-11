/*
Navicat MySQL Data Transfer

Source Server         : db1
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : makersite

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2016-10-11 19:07:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `goal` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*
Navicat MySQL Data Transfer

Source Server         : db
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : makersite

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2016-08-22 12:08:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for carousel
-- ----------------------------
DROP TABLE IF EXISTS `carousel`;
CREATE TABLE `carousel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carousel
-- ----------------------------
INSERT INTO `carousel` VALUES ('0', 'A5X8N/images.jpg', '1', '1');

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT '',
  `content` varchar(2550) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `view_count` int(11) DEFAULT '0',
  `summary` varchar(1000) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `book_count` int(11) DEFAULT '0',
  `max_book_count` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `is_full` varchar(10) DEFAULT 'no',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('40', '1', '', '0000-00-00 00:00:00', 'XW4LG/images.jpg', '0', '1', 'show_works', '0', '1', null, '0');
INSERT INTO `post` VALUES ('41', '2', '', '0000-00-00 00:00:00', 'XW4LG/95e306a76784a7059d2034f8df941722_200x112.jpg', '0', '2', 'show_works', '0', null, null, '0');
INSERT INTO `post` VALUES ('42', '1', '', '0000-00-00 00:00:00', '2CBOS/webwxgetmsgimg.jpg', '0', '1', 'apply', '0', null, null, '0');
INSERT INTO `post` VALUES ('43', '22', '', '0000-00-00 00:00:00', 'MSE3L/webwxgetmsgimg.jpg', '0', '22', 'apply', '0', '0', 'published', 'yes');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `auth` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('4', 'admin', '0', 'ecustmaker');
SET FOREIGN_KEY_CHECKS=1;

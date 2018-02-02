/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : lzpdb

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 17/09/2017 21:14:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for privilege
-- ----------------------------
DROP TABLE IF EXISTS `privilege`;
CREATE TABLE `privilege`  (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` char(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`pid`) USING BTREE,
  UNIQUE INDEX `uix_pname`(`pname`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of privilege
-- ----------------------------
INSERT INTO `privilege` VALUES (4, 'account_manage');
INSERT INTO `privilege` VALUES (1, 'privilege_manage');
INSERT INTO `privilege` VALUES (2, 'role_manage');
INSERT INTO `privilege` VALUES (5, 'temp_manage');
INSERT INTO `privilege` VALUES (3, 'user_manage');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rname` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`rid`) USING BTREE,
  UNIQUE INDEX `uix_rname`(`rname`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, 'admin');
INSERT INTO `role` VALUES (2, 'common');
INSERT INTO `role` VALUES (11, 'test0');
INSERT INTO `role` VALUES (12, 'test1');
INSERT INTO `role` VALUES (15, 'test2');

-- ----------------------------
-- Table structure for role_privilege_relation
-- ----------------------------
DROP TABLE IF EXISTS `role_privilege_relation`;
CREATE TABLE `role_privilege_relation`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `uix_rid_pid`(`rid`, `pid`) USING BTREE,
  INDEX `fk_pid`(`pid`) USING BTREE,
  CONSTRAINT `fk_pid` FOREIGN KEY (`pid`) REFERENCES `privilege` (`pid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_rid` FOREIGN KEY (`rid`) REFERENCES `role` (`rid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role_privilege_relation
-- ----------------------------
INSERT INTO `role_privilege_relation` VALUES (1, 1, 1);
INSERT INTO `role_privilege_relation` VALUES (2, 1, 2);
INSERT INTO `role_privilege_relation` VALUES (3, 1, 3);
INSERT INTO `role_privilege_relation` VALUES (10, 1, 4);
INSERT INTO `role_privilege_relation` VALUES (12, 2, 4);
INSERT INTO `role_privilege_relation` VALUES (13, 15, 1);
INSERT INTO `role_privilege_relation` VALUES (14, 15, 2);
INSERT INTO `role_privilege_relation` VALUES (15, 15, 3);
INSERT INTO `role_privilege_relation` VALUES (16, 15, 4);
INSERT INTO `role_privilege_relation` VALUES (17, 15, 5);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` enum('男','女') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_id` int(11) NOT NULL DEFAULT 2,
  `password` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`uid`) USING BTREE,
  UNIQUE INDEX `uix_email`(`email`) USING BTREE,
  INDEX `fk_role_id`(`role_id`) USING BTREE,
  CONSTRAINT `fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`rid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'alex', '男', 'alex@oldboy.com', 1, 'MTIz');
INSERT INTO `user` VALUES (2, 'lzp', '男', 'lzp_test@oldboy.com', 1, 'MTIz');
INSERT INTO `user` VALUES (3, 'egon', '女', 'egon@oldboy.com', 1, 'MTIz');
INSERT INTO `user` VALUES (4, 'wpq', '女', 'wpq@oldboy.com', 1, 'MTIz');
INSERT INTO `user` VALUES (8, 'lzptest', '男', 'lzptest@oldboy.com', 1, 'MTIz');
INSERT INTO `user` VALUES (9, 'lzp0', '男', 'lzp0@oldboy.com', 1, 'MTIz');

SET FOREIGN_KEY_CHECKS = 1;

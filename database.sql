SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


CREATE TABLE IF NOT EXISTS `github_index` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_0` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_1` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_2` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_3` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_4` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_5` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_6` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_7` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_8` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_9` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_a` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_b` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_c` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_d` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_e` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `github_index_f` (
  `id` bigint(20) unsigned NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `owner_login` varchar(250) NOT NULL,
  `description` text,
  `metadata_updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `pushed_at` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `forks_count` int(11) DEFAULT NULL,
  `network_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE `github_index`
 ADD PRIMARY KEY (`id`);

ALTER TABLE `github_index_0`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_1`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_2`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_3`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_4`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_5`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_6`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_7`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_8`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_9`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_a`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_b`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_c`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_d`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_e`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

ALTER TABLE `github_index_f`
 ADD PRIMARY KEY (`id`), ADD KEY `language` (`language`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

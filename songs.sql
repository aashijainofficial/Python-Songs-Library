-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2021 at 08:28 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `songs`
--

CREATE TABLE `songs` (
  `id` int(4) NOT NULL,
  `title` varchar(50) NOT NULL,
  `singer` varchar(25) DEFAULT NULL,
  `genre` varchar(15) DEFAULT NULL,
  `publication` varchar(50) DEFAULT NULL,
  `release_year` int(4) DEFAULT NULL,
  `file_url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `songs`
--

INSERT INTO `songs` (`id`, `title`, `singer`, `genre`, `publication`, `release_year`, `file_url`) VALUES
(3, 'In my blood', 'shawn mendes', 'pop', 'na', 2018, 'https://www.youtube.com/watch?v=36tggrpRoTI'),
(4, 'shape of you', 'ed sheeran', 'pop', 'na', 2017, 'https://www.youtube.com/watch?v=JGwWNGJdvx8'),
(5, 'the breakup song', 'arijit singh', 'pr', 'sonymusic india', 2017, 'https://www.youtube.com/watch?v=kd5KqlmcHNo'),
(6, 'burj khalifa', 'shashi', 'pr', 'na', 2020, 'https://gaana.com/song/burjkhalifa'),
(7, 'cradles', 'sub urban', 'pr', 'sub urban', 2019, 'https://www.youtube.com/watch?v=KBtk5FUeJbk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `songs`
--
ALTER TABLE `songs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `songs`
--
ALTER TABLE `songs`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

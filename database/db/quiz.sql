-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2019 at 09:03 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_category`
--

CREATE TABLE `add_category` (
  `id` int(4) NOT NULL,
  `name` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_category`
--

INSERT INTO `add_category` (`id`, `name`, `status`) VALUES
(5, 'Computer Science', 'ACTIVE'),
(6, 'maths', 'ACTIVE'),
(7, 'gk', 'ACTIVE'),
(8, 'ITt', 'ACTIVE'),
(9, 'Dummy', 'ACTIVE');

-- --------------------------------------------------------

--
-- Table structure for table `add_question`
--

CREATE TABLE `add_question` (
  `id` int(4) NOT NULL,
  `category` varchar(100) NOT NULL,
  `question` varchar(100) NOT NULL,
  `option_1` varchar(100) NOT NULL,
  `option_2` varchar(100) NOT NULL,
  `option_3` varchar(100) NOT NULL,
  `option_4` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_question`
--

INSERT INTO `add_question` (`id`, `category`, `question`, `option_1`, `option_2`, `option_3`, `option_4`, `answer`) VALUES
(8, 'Computer Science', 'vfvf', 'fvfsd', 'dfsdf', 'dcszfc', 'sfczds', 'OPTION 2'),
(10, 'Computer Science', 'dsf', 'df', 'qdf', 'qd', 'qs', 'OPTION 1'),
(11, 'Computer Science', 'aa', 'a', 'a', 'a', 'a', 'OPTION 1');

-- --------------------------------------------------------

--
-- Table structure for table `login_page`
--

CREATE TABLE `login_page` (
  `id` int(4) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_page`
--

INSERT INTO `login_page` (`id`, `email`, `password`) VALUES
(1, 'pariva@gmail.com', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `question_wise`
--

CREATE TABLE `question_wise` (
  `id` int(11) NOT NULL,
  `ques_id` int(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `selectedopt` varchar(200) NOT NULL,
  `answertime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question_wise`
--

INSERT INTO `question_wise` (`id`, `ques_id`, `result`, `user_id`, `selectedopt`, `answertime`) VALUES
(25, 8, 'False', 'h@gmail.com', 'OPTION 1', '2019-07-13 06:44:34'),
(26, 10, 'True', 'h@gmail.com', 'OPTION 1', '2019-07-13 06:44:36'),
(27, 11, 'True', 'h@gmail.com', 'OPTION 1', '2019-07-13 06:44:38');

-- --------------------------------------------------------

--
-- Table structure for table `users_login`
--

CREATE TABLE `users_login` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_login`
--

INSERT INTO `users_login` (`email`, `password`) VALUES
('jasica@gmail.com', 'jas'),
('yash@gmail.com', 'yash');

-- --------------------------------------------------------

--
-- Table structure for table `users_register`
--

CREATE TABLE `users_register` (
  `id` int(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_register`
--

INSERT INTO `users_register` (`id`, `name`, `email`, `contact`, `gender`, `password`) VALUES
(1, 'jasica', 'jasica@gmail.com', 8907654321, 'Female', ''),
(3, 'jas', 'jas@gmail.com', 9807654321, 'Female', ''),
(5, 'Hardeep', 'h@gmail.com', 8989898989, 'Male', 'h');

-- --------------------------------------------------------

--
-- Table structure for table `users_scores`
--

CREATE TABLE `users_scores` (
  `id` int(4) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `category` varchar(40) NOT NULL,
  `scores` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_scores`
--

INSERT INTO `users_scores` (`id`, `user_id`, `category`, `scores`) VALUES
(8, 'h@gmail.com', 'Computer Science', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_category`
--
ALTER TABLE `add_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `add_question`
--
ALTER TABLE `add_question`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_page`
--
ALTER TABLE `login_page`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `question_wise`
--
ALTER TABLE `question_wise`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_register`
--
ALTER TABLE `users_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_scores`
--
ALTER TABLE `users_scores`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_category`
--
ALTER TABLE `add_category`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `add_question`
--
ALTER TABLE `add_question`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `login_page`
--
ALTER TABLE `login_page`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `question_wise`
--
ALTER TABLE `question_wise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `users_register`
--
ALTER TABLE `users_register`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users_scores`
--
ALTER TABLE `users_scores`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

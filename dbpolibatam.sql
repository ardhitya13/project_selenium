-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 04, 2024 at 09:13 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbpolibatam`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `course_id` int NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `sks` int NOT NULL,
  `description` text
);

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`course_id`, `course_name`, `sks`, `description`) VALUES
(1, 'Matematika Diskrit', 3, 'Pengantar dasar-dasar matematika diskrit.'),
(2, 'Pemrograman Java', 4, 'Pengenalan dan penerapan pemrograman menggunakan bahasa Java.'),
(3, 'Pengantar Ilmu Komputer', 3, 'Pengenalan konsep dasar ilmu komputer.'),
(4, 'Jaringan Komputer', 3, 'Dasar-dasar jaringan komputer dan internet.'),
(5, 'Desain Grafis', 3, 'Pengenalan konsep dan aplikasi desain grafis.'),
(6, 'Manajemen Proyek', 3, 'Pengelolaan proyek secara efektif.'),
(7, 'Statistika', 3, 'Pengenalan konsep dasar statistika.'),
(8, 'Pengembangan Web', 4, 'Pengembangan situs web menggunakan teknologi terkini.'),
(9, 'Basis Data', 4, 'Pengenalan konsep dan desain basis data.'),
(10, 'Algoritma dan Struktur Data', 4, 'Pengenalan algoritma dan struktur data dasar.'),
(11, 'Arsitektur Komputer', 3, 'Pengenalan arsitektur komputer modern.'),
(12, 'Pengembangan Aplikasi Mobile', 4, 'Pengembangan aplikasi mobile menggunakan berbagai platform.'),
(13, 'Sistem Operasi', 3, 'Pengenalan konsep dasar sistem operasi.'),
(14, 'Kecerdasan Buatan', 4, 'Pengenalan konsep dan aplikasi kecerdasan buatan.'),
(15, 'Manajemen Basis Data', 3, 'Manajemen dan administrasi basis data.'),
(16, 'Pengembangan Game', 4, 'Pengembangan game menggunakan berbagai platform.'),
(17, 'Keamanan Jaringan', 3, 'Pengenalan konsep dasar keamanan jaringan.'),
(18, 'Pengujian Perangkat Lunak', 3, 'Metode dan teknik pengujian perangkat lunak.'),
(19, 'Komputasi Awan', 3, 'Pengenalan konsep dan teknologi komputasi awan.'),
(20, 'Analisis Data', 4, 'Pengolahan, analisis, dan visualisasi data.'),
(21, 'Pemrograman Python', 4, 'Pengenalan dan penerapan pemrograman menggunakan bahasa Python.'),
(22, 'Manajemen Proses Bisnis', 3, 'Pengelolaan proses bisnis dalam organisasi.'),
(23, 'Pengembangan Situs E-Commerce', 4, 'Pengembangan situs e-commerce untuk bisnis online.'),
(24, 'Pemrosesan Citra Digital', 3, 'Pengolahan dan analisis citra digital menggunakan perangkat lunak terkini.'),
(25, 'Pengembangan Aplikasi Berbasis Web', 4, 'Pengembangan aplikasi berbasis web menggunakan berbagai teknologi.'),
(26, 'Pemrograman C++', 4, 'Pengenalan dan penerapan pemrograman menggunakan bahasa C++.'),
(27, 'Manajemen Proyek TI', 3, 'Pengelolaan proyek teknologi informasi.'),
(28, 'Pengenalan Sistem Informasi', 3, 'Pengenalan konsep dasar sistem informasi.'),
(29, 'Kriptografi', 3, 'Pengenalan konsep dasar kriptografi.'),
(30, 'Pemrograman Mobile Cross-Platform', 4, 'Pengembangan aplikasi mobile lintas platform.'),
(31, 'Analisis Big Data', 4, 'Analisis data besar untuk mendapatkan wawasan bisnis.'),
(32, 'Pengembangan Aplikasi Desktop', 4, 'Pengembangan aplikasi desktop menggunakan berbagai teknologi.'),
(33, 'Manajemen Teknologi Informasi', 3, 'Manajemen sumber daya teknologi informasi dalam organisasi.'),
(34, 'Desain Pengalaman Pengguna (UX)', 3, 'Pengenalan desain pengalaman pengguna untuk aplikasi dan situs web.');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `nim` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `nama_lengkap` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `alamat` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
);

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`) VALUES
(1, 'admin@if.local', 'rahasia123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `course_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

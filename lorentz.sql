-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 12, 2021 at 05:32 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lorentz`
--

-- --------------------------------------------------------

--
-- Table structure for table `guru`
--

CREATE TABLE `guru` (
  `NIP` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `Nama` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `guru`
--

INSERT INTO `guru` (`NIP`, `password`, `Nama`) VALUES
('123', '123', 'Agus'),
('1234', '123', 'Alvin');

-- --------------------------------------------------------

--
-- Table structure for table `jawaban`
--

CREATE TABLE `jawaban` (
  `NIS` varchar(20) NOT NULL,
  `nomor` int(11) NOT NULL,
  `jawabansiswa` float NOT NULL,
  `jawabanalat` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jawaban`
--

INSERT INTO `jawaban` (`NIS`, `nomor`, `jawabansiswa`, `jawabanalat`) VALUES
('123', 17, 0, 0),
('123', 18, 0, 0),
('123', 19, 0, 0),
('123', 20, 0, 0),
('123', 21, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `siswa`
--

CREATE TABLE `siswa` (
  `NIS` varchar(20) NOT NULL,
  `NIP` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `Nama` varchar(20) NOT NULL,
  `Kelas` varchar(10) NOT NULL,
  `Nilai` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `siswa`
--

INSERT INTO `siswa` (`NIS`, `NIP`, `password`, `Nama`, `Kelas`, `Nilai`) VALUES
('1', '1234', '123', 'Ila', 'XII MIA 1', 0),
('12', '123', '123', 'Tedi', 'XII MIA 5', 0),
('123', '123', '123', 'Hana', 'XII MIA 5', 5),
('1234', '1234', '123', 'Kiki', 'XII MIA 6', 0);

-- --------------------------------------------------------

--
-- Table structure for table `soal`
--

CREATE TABLE `soal` (
  `nomor` int(11) NOT NULL,
  `soal` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `soal`
--

INSERT INTO `soal` (`nomor`, `soal`) VALUES
(17, 'Hitung Gaya Lorentz jika panjang alumunium foil 20cm'),
(18, 'Hitung Gaya Lorentz dengan panjang alumunium foil 35 cm'),
(19, 'Hitung Gaya Lorentz dengan panjang alumunium foil 40cm'),
(20, 'Hitung Gaya Lorentz dengan panjang kawat 25cm'),
(21, 'Hitung Gaya Lorentz jika panjang kawat 30cm');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `guru`
--
ALTER TABLE `guru`
  ADD PRIMARY KEY (`NIP`);

--
-- Indexes for table `jawaban`
--
ALTER TABLE `jawaban`
  ADD KEY `nomor` (`nomor`),
  ADD KEY `NIS` (`NIS`);

--
-- Indexes for table `siswa`
--
ALTER TABLE `siswa`
  ADD PRIMARY KEY (`NIS`),
  ADD KEY `NIP` (`NIP`);

--
-- Indexes for table `soal`
--
ALTER TABLE `soal`
  ADD PRIMARY KEY (`nomor`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `soal`
--
ALTER TABLE `soal`
  MODIFY `nomor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `jawaban`
--
ALTER TABLE `jawaban`
  ADD CONSTRAINT `jawaban_ibfk_1` FOREIGN KEY (`nomor`) REFERENCES `soal` (`nomor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `jawaban_ibfk_2` FOREIGN KEY (`NIS`) REFERENCES `siswa` (`NIS`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `siswa`
--
ALTER TABLE `siswa`
  ADD CONSTRAINT `siswa_ibfk_1` FOREIGN KEY (`NIP`) REFERENCES `guru` (`NIP`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

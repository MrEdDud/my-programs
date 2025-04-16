SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE accessibility_options (
  "accessibilityID" int(11) NOT NULL,
  "email" varchar(255) NOT NULL,
  "optionOne" tinyint(1) DEFAULT NULL,
  "optionTwo" tinyint(1) DEFAULT NULL,
  "optionThree" tinyint(1) DEFAULT NULL,
  "optionFour" tinyint(1) DEFAULT NULL,
  "optionFive" tinyint(1) DEFAULT NULL,
  "optionSix" tinyint(1) DEFAULT NULL,
  "optionSeven" tinyint(1) DEFAULT NULL,
  "optionEight" tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE hotel_bookings (
  "hotelBookingID" int(11) NOT NULL,
  "email" varchar(255) NOT NULL,
  "hotelDate" int(11) NOT NULL,
  "hotelTime" int(11) NOT NULL,
  "roomNum" int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE login_info (
  "email" varchar(255) NOT NULL,
  "zooBookingID" int(11) NOT NULL,
  "hotelBookingID" int(11) NOT NULL,
  "loyaltyCode" int(11) DEFAULT NULL,
  "forename" varchar(255) NOT NULL,
  "surname" varchar(255) DEFAULT NULL,
  "password" varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO "login_info" ("email", "zooBookingID", "hotelBookingID", "loyaltyCode", "forename", "surname", "password") VALUES
("eduardcojocaru@gmail.com", 12, 12, NULL, "Eduard", NULL, "password321"),
("johndoe@gmail.com", 1, 1, 2265, "John", "Doe", "password123");

CREATE TABLE loyalty_users (
  "loyaltyCode" int(11) NOT NULL,
  "email" varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE zoo_bookings (
  "zooBookingID" int(11) NOT NULL,
  "email" varchar(255) NOT NULL,
  "zooDate" int(11) NOT NULL,
  "zooTime" int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO "zoo_bookings" ("zooBookingID", "email", "zooDate", "zooTime") VALUES
(12, "eduardcojocaru@gmail.com", 20240425, 72206),
(23, "janedoe@gmail.com", 121224, 1230);

ALTER TABLE hotel_bookings
  ADD PRIMARY KEY ("hotelBookingID");

ALTER TABLE login_info
  ADD PRIMARY KEY ("email");

ALTER TABLE loyalty_users
  ADD PRIMARY KEY ("loyaltyCode");

ALTER TABLE zoo_bookings
  ADD PRIMARY KEY ("zooBookingID");
COMMIT;

ALTER TABLE zoo_bookings
  FOREIGN KEY ("email") REFERENCES "login_info" ("email");
COMMIT;
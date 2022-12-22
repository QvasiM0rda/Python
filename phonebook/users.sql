CREATE TABLE users (
	id INT UNSIGNED PRIMARY KEY NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	patronymic VARCHAR(50) NOT NULL,
	department VARCHAR(50),
	post VARCHAR(50),
	phone_number VARCHAR(11) NOT NULL	
)
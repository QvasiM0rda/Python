CREATE TABLE users (
    user_id VARCHAR(11) NOT NULL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL DEFAULT '',
    fIrst_name VARCHAR(50) NOT NULL DEFAULT '',
    patronymic VARCHAR(50) NOT NULL DEFAULT '',
    phone_number VARCHAR(11),
    department_id TINYINT UNSIGNED NOT NULL,
    position_id TINYINT UNSIGNED NOT NULL,
    external_phone_number_id TINYINT UNSIGNED NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id),
    FOREIGN KEY (position_id) REFERENCES positions (position_id),
    FOREIGN KEY (external_phone_number_id) REFERENCES external_phone_numbers (external_phone_number_id)
);
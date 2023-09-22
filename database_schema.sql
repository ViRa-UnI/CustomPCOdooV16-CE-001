-- database_schema.sql --

CREATE TABLE components (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE compatibility_rules (
    id SERIAL PRIMARY KEY,
    component_id INT NOT NULL,
    compatible_component_id INT NOT NULL,
    FOREIGN KEY (component_id) REFERENCES components (id),
    FOREIGN KEY (compatible_component_id) REFERENCES components (id)
);

CREATE TABLE custom_configs (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    config_name VARCHAR(255) NOT NULL,
    config_data JSONB,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- End of database_schema.sql --
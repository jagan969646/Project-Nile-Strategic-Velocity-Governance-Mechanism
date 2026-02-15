-- =========================
-- EMPLOYEES TABLE
-- =========================
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    role_type TEXT,
    manager_id INTEGER,
    salary INTEGER,
    joining_date TEXT,
    region TEXT,
    performance_score REAL
);

-- =========================
-- AWS FINANCIALS TABLE
-- =========================
CREATE TABLE IF NOT EXISTS financials (
    quarter TEXT PRIMARY KEY,
    capex INTEGER,
    aws_revenue INTEGER,
    utilization_rate REAL,
    free_cash_flow INTEGER
);

-- =========================
-- PRODUCTS TABLE
-- =========================
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    category TEXT,
    brand TEXT,
    is_amazon_owned BOOLEAN
);

-- =========================
-- PRICES TABLE
-- =========================
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    region TEXT,
    amazon_price REAL,
    seller_price REAL,
    date TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
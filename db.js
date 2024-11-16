require('dotenv').config();
const { Pool } = require('pg');

// Create a connection pool
const pool = new Pool({
  host: process.env.PG_HOST,
  port: process.env.PG_PORT,
  user: process.env.PG_USER,
  password: process.env.PG_PASSWORD,
  database: process.env.PG_DATABASE,
});

// Function to insert a product
const insertProduct = async (product) => {
  const query = `
    INSERT INTO products (productId, productName, orderCount, stockCount, price, reviewCount, timestamp)
    VALUES ($1, $2, $3, $4, $5, $6, $7)
    ON CONFLICT (productId)
    DO UPDATE SET
      orderCount = EXCLUDED.orderCount,
      stockCount = EXCLUDED.stockCount,
      price = EXCLUDED.price,
      reviewCount = EXCLUDED.reviewCount,
      timestamp = EXCLUDED.timestamp;
  `;

  const values = [
    product.productId,
    product.productName,
    product.orderCount,
    product.stockCount,
    product.price,
    product.reviewCount,
    product.timestamp,
  ];

  try {
    await pool.query(query, values);
    console.log(`Product "${product.productName}" saved/updated`);
  } catch (err) {
    console.error('Error inserting product:', err);
  }
};

// Function to fetch trending products
const getTrendingProducts = async () => {
  const query = `
    SELECT productName, orderCount, stockCount, price
    FROM products
    WHERE orderCount > 100 AND stockCount < 50
    ORDER BY orderCount DESC;
  `;

  try {
    const res = await pool.query(query);
    console.log('Trending Products:', res.rows);
    return res.rows;
  } catch (err) {
    console.error('Error fetching trending products:', err);
  }
};

module.exports = {
  pool,
  insertProduct,
  getTrendingProducts,
};

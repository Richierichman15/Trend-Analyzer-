const { insertProduct, getTrendingProducts } = require('./db');


// testing data replacing with API data soon
const mockData = [
  {
    productId: "12345",
    productName: "Wireless Earbuds",
    orderCount: 150,
    stockCount: 50,
    price: 25.99,
    reviewCount: 10,
    timestamp: new Date().toISOString(),
  },
  {
    productId: "67890",
    productName: "Smart Watch",
    orderCount: 300,
    stockCount: 20,
    price: 59.99,
    reviewCount: 25,
    timestamp: new Date().toISOString(),
  },
];

// insert and fetch trending products
(async () => {
  for (const product of mockData) {
    await insertProduct(product);
  }

  await getTrendingProducts();
})();

setInterval(async () => {
    const data = fetchMockData(); // replace with API 
    for (const product of data) {
      await insertProduct(product);
    }
  }, 60 * 60 * 1000); // runs every hour
  
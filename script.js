require('dotenv').config();
const axios = require('axios');

// Replace this URL with the actual endpoint you want to use from the AliExpress API
const apiUrl = 'https://api.aliexpress.com/productEndpoint';

const apiKey = process.env.ALIEXPRESS_API_KEY;

const fetchMockData = () => {
    return [
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
      }
    ];
  };
  

  // sleep function that captures the data throught the day
// const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// const fetchDataWithDelay = async () => {
//   await fetchProductData();
//   await sleep(2000); 
// };

const identifyTrendingProducts = (data) => {
    return data.filter(product => product.orderCount > 100 && product.stockCount < 50);
  };
// this is for analyzing the data which order got more or less than a certain number
  
const data = fetchMockData();

data.forEach((product) => {
    console.log(`Product Name: ${product.productName}`);
    
})

const trendingProducts = identifyTrendingProducts(data)

trendingProducts.forEach((product) => {
    console.log(`- ${product.productName} (Orders: ${product.orderCount}, Stock: ${product.stockCount})`);
    
})

// const fetchProductData = async () => {
    
//   try {
//     const response = await axios.get(apiUrl, {
//       headers: {
//         'Authorization': `Bearer ${apiKey}`,
//       },
//       params: {
        
//       },
//     });

//     console.log(response.data); 
//   } catch (error) {
//     console.error('Error fetching data:', error);
//   }
// };

// fetchProductData();

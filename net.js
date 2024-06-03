const axios = require('axios');
const HttpsProxyAgent = require('https-proxy-agent');

// Replace with your proxy server details
const proxyHost = 'proxy.example.com';
const proxyPort = 8080;
const proxyUsername = 'username'; // if authentication is required
const proxyPassword = 'password'; // if authentication is required

// Construct the proxy URL
const proxyUrl = `http://${proxyUsername}:${proxyPassword}@${proxyHost}:${proxyPort}`;

// Create a new HttpsProxyAgent instance
const agent = new HttpsProxyAgent(proxyUrl);

axios.get('https://www.google.com', {
    httpsAgent: agent
})
.then(response => {
    console.log('Response:', response.data);
})
.catch(error => {
    console.error('Error:', error);
});

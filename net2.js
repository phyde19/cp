const { HttpsProxyAgent } = require('https-proxy-agent');
require('dotenv').config();

const proxyUrl = process.env.HTTPS_PROXY || process.env.HTTP_PROXY;

if (!proxyUrl) {
  console.error('Proxy URL is not defined in environment variables.');
  process.exit(1);
}

const agent = new HttpsProxyAgent(proxyUrl);

module.exports = {
  webpack: (config, { isServer }) => {
    if (isServer) {
      // Override the global fetch to use the proxy agent
      globalThis.fetch = (url, options = {}) => {
        options.agent = agent;
        return import('node-fetch').then(({ default: fetch }) => fetch(url, options));
      };
    }
    return config;
  },
};

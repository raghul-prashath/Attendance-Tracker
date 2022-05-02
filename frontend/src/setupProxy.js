const { createProxyMiddleware } = require("http-proxy-middleware");
require('dotenv').config();

module.exports = function (app) {
  app.use(
    "/api",
    createProxyMiddleware({
      target: "http://localhost:5000",
      // target: "http://"+ process.env.REACT_HOST + ":5000",
      changeOrigin: true,
    })
  );
};

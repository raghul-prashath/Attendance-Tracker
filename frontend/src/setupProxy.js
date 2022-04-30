const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api",
    createProxyMiddleware({
      target: "http://flaskapi:5000",
      changeOrigin: true,
    })
  );
  app.use(
    "/user",
    createProxyMiddleware({
      target: "http://nodeapi:8000",
      changeOrigin: true,
    })
  );
};

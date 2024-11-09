const express = require("express");
const http = require("http");

const app = express();

// Please refer to nginx.conf.example for configuration
app.use((req, res, next) => {
    const subpath = req.headers['x-forwarded-path'] || '';
    req.baseUrl = subpath; // Adjusts the base URL to the dynamic subpath
    next();
});

app.get("/source", (req, res) => {
    return res.sendFile(__filename);
})
app.get('/', (req, res) => {
    const { url } = req.query;
    if (!url || typeof url !== 'string') return res.sendFile(__dirname + "/index.html");

    // no duplicate characters in `url`
    if (url.length !== new Set(url).size) return res.sendFile(__dirname + "/frog.png");

    try {
        http.get(url, resp => {
            resp.setEncoding("utf-8");
            resp.statusCode === 200 ? resp.on('data', data => res.send(data)) : res.send(":(");
        }).on('error', () => res.send("WTF?"));
    } catch (error) {
        res.send("WTF?");
    }
});

app.listen(3000, '0.0.0.0');

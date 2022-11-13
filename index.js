const http = require('http');

const port = 16649;

// const requestListener = function (req, res) {
//     console.log(req.)
//     res.writeHead(200);
//     res.end();
// }

const server = http.createServer(function (req, res) {
    req.on('data', (chunk) => {
        var data = new Buffer.from(chunk).toString();
        console.log(data);
    })
    
    res.writeHead(200);
    res.end();
});
server.listen(port);
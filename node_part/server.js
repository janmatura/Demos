const WebSocket = require('ws');
const PORT = 5000;

const wsServer = new WebSocket.Server({
    port: PORT
});

wsServer.on('connection', ((socket)=>{
console.log('Client connected...');

    socket.on('message', (msg)=>{
        console.log(`Received message ${msg}`);
        socket.send(`becked ${msg}`);
    })


    })
)




console.log(`${new Date()} Server is listening on port ${PORT};`)
import redis from "redis";

const cli = redis.createClient();

cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server : ${error.message}`);
});

const Chan = 'holberton school channel';

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        cli.published(Chan, message);
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

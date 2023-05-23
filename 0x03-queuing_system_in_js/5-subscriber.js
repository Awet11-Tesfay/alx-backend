import redis from "redis";

const cli = redis.createClient();

cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
})

const Chan = 'holberton school channel';

cli.subscrie(Chan);

cli.on('message', (channel, message) => {
    if (channel === Chan) console.log(message);
    if (message === 'KIL_SERVER') {
        cli.unsbscribe(Chan);
        cli.quit();
    }
});

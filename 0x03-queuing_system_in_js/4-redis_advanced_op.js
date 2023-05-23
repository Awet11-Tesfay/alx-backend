import redis from "redis";

const cli = redis.createClient();

cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server : ${error.message}`);
});

cli.hset('Holberton', 'Portland', 50, redis.print);
cli.hset('Holberton', 'Seattle', 80, redis.print);
cli.hset('Holberton', 'New York', 20, redis.print);
cli.hset('Holberton', 'Bogota', 20, redis.print);
cli.hset('Holberton', 'Cail', 40, redis.print);
cli.hset('Holberton', 'Paris', 20, redis.print);

cli.hgetall('HolbertonSchoos', (error, objects) => {
    if (error) console.error(error);
    else console.log(object);
})

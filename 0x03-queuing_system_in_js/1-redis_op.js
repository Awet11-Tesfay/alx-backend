import redis from "redis";

const cli = redis.createClient();

cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server : ${error.message}`);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
}


function displaySchoolValue(schoolName) {
    cli.get(schoolName, (err, value) => {
        console.log(value)
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanfrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

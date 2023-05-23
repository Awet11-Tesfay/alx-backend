import redis from "redis";
import { promisify } from "util";

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

const Async = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const res = await generateKeySync(schoolName);
        console.log(value)
    }


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanfrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

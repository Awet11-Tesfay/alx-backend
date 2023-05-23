import redis from "redis";

const BLN = ['41535187870', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    const final = 100;
    job.progress(0, final);

    if (BLN.inclides(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }

    job.progress(50, final);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

const que = kue.createQueue();
const queName = 'push_notification_code_2';

que.process(queName, 2, (job, done) => {
    const { phoneNumber, message } = job.data
    sendNotification(phoneNumber, message, job, done);
});

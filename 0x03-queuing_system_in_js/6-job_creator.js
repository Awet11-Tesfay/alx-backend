import kue from "kue";

const que = kue.createQueue();
const j = {
    phonNumber: '0923095459',
    message: 'This is the code to verify your account',
};

const queName = 'push_notification_code';

const jobb = queue.create(queName, j).save((err) => {
    if (!err) console.log(`Notification job created: ${jobb.id}`);
});

j.on('complete', () => {
    console.log('Notification job completed');
})

j.on('failed', () => {
    console.log('Notification job failed');
});

const kue = require('kue');

const queue = kue.createQueue();

const string1 = '+254702810833';
const string2 = 'Hey Will';

const jobData = queue.create('push_notification_code', {
	phoneNumber: string1,
	message: string2,
});

jobData.save((err) => {
	if (err) {
		console.error('Notification job failed:', err);
	} else {
		console.error('Notification job created:', jobData.id);
	}
});

queue.process('push_notification_code', (job, done) => {
	console.log('Notification job completed')

	done();
});


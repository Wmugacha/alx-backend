import redis from 'redis';

const client = redis.createClient();

	client.on('error', (error) => {
		console.log('Redis client not connected to the server: ${error.message}');
	});


	client.on('connect', () => {
		console.log('Redis client connected to the server');
	});

const Channel = 'holberton school channel'

client.subscribe(Channel)

client.on('message', (channel, message) => {
	if (channel === Channel) console.log(message);

	if (message === 'KILL_SERVER') {
		client.unsubscribe(Channel);
		client.quit();
	}
});

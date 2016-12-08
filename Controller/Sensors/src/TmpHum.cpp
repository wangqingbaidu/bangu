/*
Controller.Sensors is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon)
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
*/
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define TIMEOUT 10000
//Default pin is set to be writingPi 4 which is Raspberry Pi BCM model GPIO23.
//See http://wiringpi.com/pins/ for detail.
#define DHT11_PIN 4

typedef unsigned int uint8_t;

//DHT11 sensor class
class dht
{
	public:
		int read11(uint8_t pin);
		double humidity;
		double temperature;

	private:
		// buffer to receive data
		uint8_t bits[5];
		int read(uint8_t pin);
};
// return values:
//  0 : OK
// -1 : checksum error
// -2 : timeout
int dht::read11(uint8_t pin)
{
	int rv = read(pin);
	if (rv != 0) return rv;
	humidity = bits[0];  // bit[1] == 0;
	temperature = bits[2];  // bits[3] == 0;
	//	print humidity and temperature.
	//	printf("h:%f\tt:%f\n", humidity, temperature);
	// TEST CHECKSUM
	uint8_t sum = bits[0] + bits[2]; // bits[1] && bits[3] both 0
	//	print Checksum.
	//	printf("bht:%d\tbs:%d\n", bits[0] + bits[2], bits[4]);
	if (bits[4] != sum) return -1;

	return 0;
}
// return values:
//  0 : OK
// -2 : timeout
int dht::read(uint8_t pin)
{
	// INIT BUFFERVAR TO RECEIVE DATA
	uint8_t cnt = 7;
	uint8_t idx = 0;

	// EMPTY BUFFER
	for (int i=0; i< 5; i++) bits[i] = 0;

	// REQUEST SAMPLE
	pinMode(pin, OUTPUT);
	digitalWrite(pin, LOW);
	delay(20);
	digitalWrite(pin, HIGH);
	delayMicroseconds(40);
	pinMode(pin, INPUT);

	// GET ACKNOWLEDGE or TIMEOUT
	unsigned int loopCnt = TIMEOUT;
	while(digitalRead(pin) == LOW)
		if (loopCnt-- == 0) return -2;

	loopCnt = TIMEOUT;
	while(digitalRead(pin) == HIGH)
		if (loopCnt-- == 0) return -2;

	// READ THE OUTPUT - 40 BITS => 5 BYTES
	for (int i=0; i<40; i++)
	{
		loopCnt = TIMEOUT;
		while(digitalRead(pin) == LOW)
			if (loopCnt-- == 0) return -2;

		unsigned long t = micros();

		loopCnt = TIMEOUT;
		while(digitalRead(pin) == HIGH)
			if (loopCnt-- == 0) return -2;

		if ((micros() - t) > 40)
		{
			bits[idx] |= (1 << cnt);
		}

		if (cnt == 0)   // next byte?
		{
			cnt = 7;
			idx++;
		}
		else
		{
			cnt--;
		}
	}
	return 0;
}

int main(int argc, char* argv[])
{
	wiringPiSetup();
	dht DHT;
	int pin = DHT11_PIN;
	if (argc > 1)
		pin = atoi(argv[1]);
	int chk = DHT.read11(pin);
	if (chk == 0)
	{
		printf("%d %d\n", int(DHT.humidity), int(DHT.temperature));
	}
}

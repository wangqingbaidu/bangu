HTEXEC=../TempHum
CFLAGS=-Wall -Wfatal-errors -g -lwiringPi
CC=g++
OPTS=-O3 

HTSRCDIR=./src/
HTSRC=TempHum.cpp
HTM=$(addprefix $(SRCDIR), %(HTSRC))

g++ -o run TempHum.cpp

all:
	$(HTEXEC)

$(HTEXEC) : 
	$(CC) $(CFLAGS) $(HTM) -o $(HTEXEC)
	
clean:
	rm $(HTEXEC)
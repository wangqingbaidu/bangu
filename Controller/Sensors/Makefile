HTEXEC=../TempHum
CFLAGS=-Wall -Wfatal-errors -g -lwiringPi
CC=g++
OPTS=-O3 

HTSRCDIR=./src/
HTSRC=TempHum.cpp
HTM=$(addprefix $(SRCDIR), %(HTSRC))

all:
	$(HTEXEC)

$(HTEXEC) : 
	$(CC) $(CFLAGS) $(HTM) -o $(HTEXEC)
	
clean:
	rm $(HTEXEC)
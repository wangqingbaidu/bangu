HTEXEC=../TempHum
CFLAGS=-Wall -Wfatal-errors -g -lwiringPi
CC=g++
OPTS=-O3 

SRCDIR=./src/
HTSRC=TempHum.cpp
HTM=$(SRCDIR)$(HTSRC)

all:$(HTEXEC)

$(HTEXEC): 
	$(CC) $(CFLAGS) $(HTM) -o $(HTEXEC)
	
clean:
	rm $(HTEXEC)
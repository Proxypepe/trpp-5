CC=gcc
OBJECTS=main.o converter.o
TARGET=main

compile: $(OBJECTS)
	$(CC) $(OBJECTS) -o $(TARGET)

shared: converter.c converter.h
	$(CC) -shared -o libconverter.so -fPIC converter.c

converter.o: converter.c converter.h
	$(CC) -c converter.c

main.o: main.c converter.c converter.h
	$(CC) -c main.c

.Phony=clean
clean:
	rm -rf $(OBJECTS) $(TARGET)

test:
	./$(TARGET)
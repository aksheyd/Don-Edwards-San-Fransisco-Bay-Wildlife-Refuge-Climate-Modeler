# Makefile
# Build rules for EECS 280 project 2

# Compiler
CXX ?= g++

# Compiler flags
CXXFLAGS ?= --std=c++11 -Wall -Werror -pedantic -g

# Run a regression test
test: main.exe
	./main.exe

main.exe: main.cpp 
	$(CXX) $(CXXFLAGS) $^ -o $@



# Disable built-in Makefile rules
.SUFFIXES:

clean:
	rm -rvf *.exe *.out.txt *.out.ppm *.dSYM *.stackdump
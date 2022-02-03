# Makefile
# Build rules for Climate Modeler

# Compiler
CXX ?= g++

# Compiler flags
CXXFLAGS ?= --std=c++11 -Wall -Werror -pedantic -g

BOOST_ROOT := "/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/boost_1_78_0"
BOOST_INC := ${BOOST_ROOT}/include

main.exe: main.cpp 
	$(CXX) $(CXXFLAGS) -I$(BOOST_ROOT) $^ -o $@



# Disable built-in Makefile rules
.SUFFIXES:

clean:
	rm -rvf *.exe *.out.txt *.out.ppm *.dSYM *.stackdump



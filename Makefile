# Makefile
# Build rules for Climate Modeler

# Compiler
CXX ?= g++

# Compiler flags
CXXFLAGS ?= --std=c++11 -Wall -Werror -pedantic -g

BOOST_ROOT := "/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/boost_1_78_0"
BOOST_INC := ${BOOST_ROOT}/include
PYTHON_ROOT := "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers"
PYTHON_INC := ${PYTHON_ROOT}/include


main.exe: main.cpp 
	$(CXX) $(CXXFLAGS) -I$(BOOST_ROOT) -I$(PYTHON_ROOT) $^ -o $@



# Disable built-in Makefile rules
.SUFFIXES:

clean:
	rm -rvf *.exe *.out.txt *.out.ppm *.dSYM *.stackdump



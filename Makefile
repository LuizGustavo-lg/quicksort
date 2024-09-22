BIN = ./bin
NAMEPROGAN = quick
NAMEPROGANLAB = quicklab

all:
	g++ c++/quicksort.cpp -o ${BIN}/${NAMEPROGAN}

run: 
	${BIN}/${NAMEPROGAN}

lab:
	g++ c++/test_quicksort.cpp -o ${BIN}/${NAMEPROGANLAB}
	${BIN}/${NAMEPROGANLAB}
clear:
	rm ./bin/*
BIN = ./bin
NAMEPROGAN = quick

all:
	g++ c++/quicksort.cpp -o ${BIN}/${NAMEPROGAN}

run: 
	${BIN}/${NAMEPROGAN}

clear:
	rm ./bin/*
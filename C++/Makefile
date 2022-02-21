# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ptippaya <ptippaya@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/18 13:36:14 by ptippaya          #+#    #+#              #
#    Updated: 2022/02/20 18:57:24 by ptippaya         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CXX = g++
CXXFLAG = -Wall -Wextra -Werror
# CPPFILE = $(shell find . -type f -name "*.cpp")
CPPFILE = main.cpp
OUTPUT = a.out

all: clean
	@clear
	@printf '-------------------- FILE --------------------\n\n'
	@printf 'CPP File : $(CPPFILE)\n'
	@printf '\n-------------------- CPP! --------------------\n\n'
	$(CXX) $(CXXFLAG) $(CPPFILE) -o $(OUTPUT)
	@printf '\n------------------- FINISH -------------------\n\n'
	@./$(OUTPUT)
	@printf '\n----------------------------------------------\n\n'
	@rm $(OUTPUT)

%:
	@printf '-------------------- FILE --------------------\n\n'
	@printf 'CPP File : $@.cpp\n'
	@printf '\n-------------------- CPP! --------------------\n\n'
	$(CXX) $(CXXFLAG) $@.cpp -o $(OUTPUT)
	@printf '\n------------------- FINISH -------------------\n\n'
	@./$(OUTPUT)
	@printf '\n----------------------------------------------\n\n'
	@rm $(OUTPUT)

clean:
	@clear
	@printf 'remove .out .a .o file\n'
	rm $(shell find . -type f -name "*.out") $(shell find . -type f -name "*.a") $(shell find . -type f -name "*.o")
	@printf 'DONE!\n'

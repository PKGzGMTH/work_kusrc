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

CPP = g++
CPPFLAG = -Wall -Wextra -Werror
# CPPFILE = $(shell find . -type f -name "*.cpp")
CPPFILE = main.cpp
OUTPUT = a.out

all:
	@clear
	@printf '-------------------- FILE --------------------\n\n'
	@printf 'CPP File : $(CPPFILE)\n'
	@printf '\n-------------------- CPP! --------------------\n\n'
	$(CPP) $(CPPFLAG) $(CPPFILE) -o $(OUTPUT)
	@printf '\n------------------- FINISH -------------------\n\n'
	@./$(OUTPUT)
	@printf '\n----------------------------------------------\n\n'

%.cpp:
	@ $(CPP) $(CPPFLAG) $<.cpp -o $(OUTPUT)

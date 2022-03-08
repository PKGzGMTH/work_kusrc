#* ************************************************************************** *#
#*                                                                            *#
#*                                                        :::      ::::::::   *#
#*   ft_putnbr.c                                        :+:      :+:    :+:   *#
#*                                                    +:+ +:+         +:+     *#
#*   By: ptippaya <marvin@42.fr>                    +#+  +:+       +#+        *#
#*                                                +#+#+#+#+#+   +#+           *#
#*   Created: 2022/01/14 18:43:33 by ptippaya          #+#    #+#             *#
#*   Updated: 2022/01/14 18:43:59 by ptippaya         ###   ########.fr       *#
#*                                                                            *#
#* ************************************************************************** *#

def rush(x:int, y:int):
    string = ''
    if (x > 1) and (y > 1):
        for j in range(y):
            for i in range(x):
                if (i == 0 and j == 0) or (i == x-1 and j == y-1):
                    string += '/'
                elif (i == 0 and j == y-1) or (i == x-1 and j == 0):
                    string += '\\'
                elif (i != 0 and i != x-1) and (j != 0 and j != y-1):
                    string += ' '
                else:
                    string += '*'
            string += '\n'
    elif (x == 1) and (y > 1):
        for i in range(y):
            if i == 0:
                string += '/\n'
            elif i == y-1:
                string += '\\\n'
            else:
                string += ('*\n')
    elif (x > 1) and (y == 1):
        for i in range(x):
            if i == 0:
                string += '/'
            elif i == x-1:
                string += '\\'
            else:
                string += ('*')
    print(string)

rush(5,1)
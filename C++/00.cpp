/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptippaya <ptippaya@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/18 14:43:11 by ptippaya          #+#    #+#             */
/*   Updated: 2022/02/20 20:24:19 by ptippaya         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
using namespace std;
class Circle
{
	public:
		int r;
	public:
		void setRadius (int val)
		{
			r = val;
		};
		float area (void)
		{
			return 3.14*r*r;
		};
		float girth (void)
		{
			return 3.14*2*r;
		};
};

int	main(void)
{
	Circle cir1;
	int	val, n_val;
	cout << "Enter circle radius: ";
	cin >> val;
	cir1.setRadius(val);
	n_val = cir1.r;
	cout << "radius " << n_val << endl;
	cout << "Area " << cir1.area() << endl;
	cout << "Girth " << cir1.girth() << endl;
}

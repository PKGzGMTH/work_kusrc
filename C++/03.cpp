#include	<iostream>
using namespace std;

class apartment
{
	public:
		string	name = "ABC";
		int		price = 0;
		int		electric_unit = 15;
		int		water_unit = 30;
		int		total = 0;

		void	show_total(void)
		{
			cout << "Room Price:\t" << price << " baht\n";
			cout << "Electric:\t" << electric_unit << " baht\n";
			cout << "Water:\t\t" << water_unit << " baht\n";
			cout << "Total:\t\t" << total << " baht\n";
		}
};

class fanRoom: public apartment
{
	public:
		fanRoom(int electric, int water)
		{
			price = 2500;
			electric_unit *= electric;
			water_unit *= water;
			total = price + electric_unit + water_unit;
		}
};

class airRoom: public apartment
{
	public:
		airRoom(int electric, int water)
		{
			price = 3500;
			electric_unit *= electric;
			water_unit *= water;
			total = price + electric_unit + water_unit;
		}
};

int	main(void)
{
	airRoom	room1(100,300);
	fanRoom room2(100,300);

	cout << "room1:\n";
	room1.show_total();
	cout << "\nroom2:\n";
	room2.show_total();
}

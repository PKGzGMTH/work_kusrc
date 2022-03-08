#include <iostream>
using namespace	std;

class	Room
{
	public:
		int	total;
		Room(int Electric, int water)
		{
			total = (Electric * 3) + (water * 20);
		};
		Room(int Electric)
		{
			total = (Electric * 3) + 90;
		};
		~Room()
		{
			cout << "Kill Room\n";
		}
};

int	main(void)
{
	Room	room1(10,3);
	Room	room2(10);
	Room	room3(room1);
	Room	room4 = room2;
	cout << "total room1 = " << room1.total << '\n';
	cout << "total room2 = " << room2.total << '\n';
	cout << "total room3 = " << room3.total << '\n';
	cout << "total room4 = " << room4.total << '\n';
}

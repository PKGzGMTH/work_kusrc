#include <iostream>
#include <string>
using namespace	std;

class	Bank
{
	public:
		int		money = 10000;
		string	name = "Unknow";

		Bank(int withdraw_money, string usr_name)
		{
			money -= withdraw_money;
			name = usr_name;
		};
		Bank(int withdraw_money)
		{
			money -= withdraw_money;
		};
		~Bank()
		{
			cout << "Kill Bank\n";
		}
};

int	main(void)
{
	Bank	wallet1(990, "Pongsakorn");
	Bank	wallet2(12000);
	Bank	wallet3(wallet1);
	Bank	wallet4 = wallet2;
	cout << "remaining money = " << wallet1.money << "\twithdraw by: " << wallet1.name << '\n';
	cout << "remaining money = " << wallet2.money << "\twithdraw by: " << wallet2.name << '\n';
	cout << "remaining money = " << wallet3.money << "\twithdraw by: " << wallet3.name << '\n';
	cout << "remaining money = " << wallet4.money << "\twithdraw by: " << wallet4.name << '\n';
}

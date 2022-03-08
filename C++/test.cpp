#include<iostream>
#include<iomanip>
using namespace std;
class Bank
{
    public:
        float total = 0;

        Bank(float withdraw,float bag)
        {
			total = withdraw - bag;
        }
        Bank(float Deposit)
        {
			total =  total - Deposit;
        }
};

int	main()
{
	cout<<fixed<<setprecision(2);
	Bank bag1(5000,200);
	Bank bag2(2000);
	Bank bag3(bag1);
	cout << "bag1  = " << bag1.total << '\n';
	cout << "bag2 = " << bag2.total << '\n';
	cout << "bag3 = " << bag3.total << '\n';
}

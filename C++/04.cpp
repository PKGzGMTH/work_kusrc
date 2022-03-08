#include <iostream>
using namespace std;

class Shape
{
	private:
		string color;
	public:
		double getArea()
		{
			double radius;
			cout << "please input radius: \n";
			cin >> radius;
			return (3.14 * radius * radius);
		};
		string toString()
		{
			cout << "please input color: \n";
			cin >> color ; 
			return (color);
		};
};

class Rectangle : public Shape
{
	private:
		string color;
	public:
		int length, width;
	public:
		double getArea()
		{
			cout << "please input length: \n";
			cin >> length;
			cout << "please input width: \n";
			cin >> width;
			return (length * width);
		};
		string toString()
		{
			cout << "please input color of Rectangle: \n";
			cin >> color ; 
			return (color);
		};
};

class Triangle : public Shape
{
	private:
		string color;
	public:
		int length, width;
	public:
		double getArea()
		{
			cout << "please input length: \n";
			cin >> length;
			cout << "please input width: \n";
			cin >> width;
			return (length * width / 2);
		};
		string toString()
		{
			cout << "please input color Triangle: \n";
			cin >> color ; 
			return (color);
		};
};

int main(void)
{
	Shape shape1;
	Rectangle shape2;
	Triangle shape3;

	double area;
	string color;
	area = shape1.getArea();
	color = shape1.toString();
	cout << "Area of shape1 = " << area << " color is " << color << "\n\n";

	area = shape2.getArea();
	color = shape2.toString();
	cout << "Area of shape2 = " << area << " color is " << color << "\n\n";

	area = shape3.getArea();
	color = shape3.toString();
	cout << "Area of shape3 = " << area << " color is " << color << "\n\n";
}

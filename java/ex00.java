public class ex00
{
	static void buying(int cakePrice, int coffeePrice)
	{
		if (cakePrice > coffeePrice)
			System.out.println("You have buy 1 Cake and 1 Cup of Coffee.");
		else if (cakePrice == coffeePrice)
			System.out.println("You have buy 2 Cake and 2 Cup of Coffee.");
		else if (cakePrice * 2 == coffeePrice)
			System.out.println("You have buy 2 Cake.");
		else
			System.out.println("Not buy yet, There is no promotion.");
	}
	public static void main(String [] args)
	{
		buying(20, 20);
		buying(20, 10);
		buying(20, 21);
		buying(20, 40);
	}
}

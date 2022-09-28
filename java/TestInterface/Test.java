package TestInterface;

public class Test
{
	public static void main(String args[])
	{
		Flyable f = new Aeroplane();
		f.fly();
		System.out.println(Flyable.num);
		Flyable a = new Aeroplane();
		System.out.println(a.getNumber());
	}
}

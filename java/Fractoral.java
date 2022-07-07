public class Fractoral {
	public static void main (String [] args)
	{
		final int num = 16;
		for (int i = 0; i < num; i++)
			System.out.println(i + "! is " + fact(i));
	}

	public static int fact(int n)
	{
		if (n >= 2)
			return (n * fact(n - 1));
		else
			return (1);
	}
}

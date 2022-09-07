import java.util.Scanner;
public class TestAbs
{
	public static void main(String argv[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.printf("Enter Number ");
		System.out.printf("Absolute is %d\n", Math.abs(sc.nextInt()));
		System.out.printf("%f %d\n", Math.PI, Integer.MAX_VALUE);
	}
}

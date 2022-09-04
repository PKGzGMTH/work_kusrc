/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/
import java.util.Scanner;
import java.util.Arrays;

public class TestException
{
	public static void main (String args[])
	{
		int arr[] = new int [5];
		int max = 0;
		Scanner input = new Scanner(System.in);
		try
		{
			for (int i = 0; i < arr.length; i++)
			{
				System.out.print("Enter num " + (i + 1) + " : ");
				arr[i] = Integer.parseInt(input.nextLine());
				if (arr[i] > max)
					max = arr[i];
			}
		}
		catch (NumberFormatException e)
		{
			System.out.println("Enter Numeric only!");
		}
		finally
		{
			System.out.println(Arrays.toString(arr));
			System.out.println("Max is " + max);
		}
	}
}

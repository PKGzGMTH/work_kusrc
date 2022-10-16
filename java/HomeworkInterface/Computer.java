/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/

package HomeworkInterface;

public class Computer implements Priceable
{
	String CPUName;

	Computer(int cpu) {
		if (cpu == 1)
			CPUName = "Intel";
		else if (cpu == 2)
			CPUName = "AMD";
	}

	public int getPrice() {
		if (CPUName.equals("Intel"))
			return (42000);
		else
			return (39000);
	}

	public String getInfo()
	{
		return (CPUName + " Computer " + getPrice() + " Baht");
	}
}

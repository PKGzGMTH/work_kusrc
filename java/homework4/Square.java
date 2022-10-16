/*
 * This file is extend Shape.java for Square Shape
 * by Write function Override the getArea() for Square Shape.
 *
 * NAME: Pongsakorn Tippayasomdech
 * STUDENT ID: 6430200850
 * SECTION: 830
 *
 */

package homework4;

public class Square extends Shape {
	private int w;

	public Square(int w)
	{
		this.w = w;
	}

	@Override
	public double getArea()
	{
		return (this.w * this.w);
	}
}

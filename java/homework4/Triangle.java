/*
 * This file is extend Shape.java for Triangle Shape
 * by Write function Override the getArea() for Triangle Shape.
 *
 * NAME: Pongsakorn Tippayasomdech
 * STUDENT ID: 6430200850
 * SECTION: 830
 *
 */

package homework4;

public class Triangle extends Shape {
	private int h, b;

	public Triangle(int h, int b)
	{
		this.h = h;
		this.b = b;
	}

	@Override
	public double getArea()
	{
		return (0.5 * h *b);
	}
}

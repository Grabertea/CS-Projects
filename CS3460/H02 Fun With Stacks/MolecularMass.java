import java.util.Scanner;

public class MolecularMass
{
	private final int H = 1;
    private final int C = 12;   
    private final int O = 16;
	private final int openPar = 0;
	private IntStack s = new IntStack();
	private int sum = 0;
	
	public int getMass(String input)
	{
		int length = input.length();
		char item;
		for (int i = 0; i < length; i++)
		{
			item = input.charAt(i);
			switch(item)
			{
				case 'H':
					s.push(H);
					break;
				case 'C':
					s.push(C);
					break;
				case 'O':
					s.push(O);
					break;
				case '(':
					s.push(openPar);
					break;
				case ')':
					int popper = s.pop();
					int total = 0;	
					while (popper != 0)
					{
						total += popper;
						popper = s.pop();
					}
					s.push(total);
					break;
				case '2':
				case '3':
				case '4':
				case '5':
				case '6':
				case '7':
				case '8':
				case '9':
					int times = Character.getNumericValue(item);
					int copy = s.pop();
					int sum = copy * times;
					s.push(sum);
					break;
			}
		}
		int mass = sumMass();
		return mass;
	}
	
	public int sumMass()
	{
		int popper = s.pop();
		int sum = 0;	
		while (popper != -1)
		{
			sum += popper;
			popper = s.pop();
		} 
		return sum;
	}
	
	
	public static void main(String [] srgs) 
	{
		Scanner in = new Scanner(System.in);
		MolecularMass m = new MolecularMass();
		
		System.out.print("Enter the molecule: ");
		String molecule = in.nextLine();
		
		int mass = m.getMass(molecule);
		System.out.println("The Molecular Mass of " + molecule + " is " + mass);
		
	}
}
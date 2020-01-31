public class IntStack {
	private Node head;
	private int size;
	
	private class Node
	{
		private int data;
		private Node link;
		
		public Node()//basic constructor
		{
			link = null;
		}
		
		public Node(int newData)//tail constructor
		{
			data = newData;
			link = null;
		}
		
		public Node(int newData, Node next)//inserting constructor
		{
			data = newData;
			link = next;
		}
		
		public Node getLink()//link getter
		{
			return link;
		}
		
		public void setLink(Node next)//link setter
		{
			link = next;
		}
		
		public int getData()//data getter
		{
			return data;
		}
		
		public void setData(int newData)//data setter
		{
			data = newData;
		}
	}

	public IntStack() {
		head = new Node();
		size = 0;
	}

	public void push(int x) {
		// If the stack is empty, put the value in the head.
		if (size == 0)
		{
			head.setData(x);
			size++;
		}
		else if (size < 100) //while the size is under 100, we can still push new items onto the stack.
		{
			head = new Node(x, head);
			size++;
		}
	}

	public int pop() {
		//If the stack has nothing on it, return -1.
		if(size == 0)
		{
			return -1;
		}
		else if (size == 1)
		{
			int data = head.getData();
			head = new Node();
			size--;
			return data;
		}
		else // get data from head, decrease size, then return data.
		{
			int data = head.getData();
			head = head.getLink();
			size--;
			return data;
		}
	}
	
	// for testing 
	public void print()
	{
		Node cursor = head;
		int printData = 0;
		for (int i = 0; i < size; i++)//prints Node 1 by 1
		{
			printData = cursor.getData();
			System.out.print(printData + " ");
			cursor = cursor.getLink();
		}
		System.out.println();
	}
}
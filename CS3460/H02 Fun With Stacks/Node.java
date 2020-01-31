public class Node
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
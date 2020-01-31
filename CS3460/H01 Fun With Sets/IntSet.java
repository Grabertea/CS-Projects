public class IntSet
{
	private int size;//the number of elements currently stored in the set
	private Node head;//beginning of the set
	
	public IntSet()//basic constructor
	{
		size = 0;
		head = new Node();
	}
	
	public boolean find(int key)
	{
		boolean found = false;
		Node cursor = head;
		for (int i = 0; i < size; i++)
		{
			if (cursor.getData() != key)//check to see if unequal first
			{
				cursor = cursor.getLink();
			}
			else if (cursor.getData() == key)//check to see if found, in the case that data and key arent unequal
			{
				found = true;
			}
		}
		return found;
	}
	
	private Node getPrevious(int key)
    {
        Node previous = null;
        Node cursor = head;
        while (cursor != null)//goes through linked list
        {
            if (key > cursor.getData())//if to ensure that the right position is given
            {
                previous = cursor;
                cursor = cursor.getLink();
            }
            else
            {
                return previous;
            }
        }
        return previous;
    }
	
	public void insert(int key)
	{
		//make sure that the key is not present
		//assert (!find(key));//not working on student machine
		if (!find(key))
		{
			if (size == 0)//if statement to see if the linked list has any data. if not, key is put into the head
			{
				head.setData(key); 
				size++;
			}
			else if (size > 0)//else if to handle other cases
			{
				Node newNode = new Node(key);
				Node position = getPrevious(key);
				if (position == null)//if for new head if key is lower
				{
					newNode.setLink(head);
					head = newNode;
				}
				else//else insert a node using getPrevious
				{
					newNode.setLink(position.getLink());
					position.setLink(newNode);
				}
				size++;
			}
		}
		else
		{
			System.out.println(key + " already in Set");
		}
	}
	
	private int getPosition(int key)
    {
        Node cursor = head;
        for (int i = 0; i < size; i++, cursor = cursor.getLink())
        {
            if (key == cursor.getData())//gets the position of the node that has key as its data
            {
                return i;
            }
        }
        throw new IllegalArgumentException("Element not in list");
    }
	
	public void remove(int key)
	{
		//make sure that the key is present
		//assert (find(key));//not working on student machine
		if (find(key))
		{
			int position = getPosition(key);//position of the Node to be removed
			if (position == 0)//if the removal is the first Node 
			{
				head = head.getLink();
				size--;
			}
			else// sets the previous link to the Node after the one to be removed
			{
				Node previous = head;
				for (int i = 0; i < position - 1; i++)
				{
					previous = previous.getLink();
				}
				Node toRemove = previous.getLink();
				previous.setLink(toRemove.getLink());
				toRemove.setLink(null);
				size--;
			}
		}
		else
		{
			System.out.println(key + " not in Set");
		}
	}
	
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
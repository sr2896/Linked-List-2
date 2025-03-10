#Time complexity: O(1)
#space complexity: O(1)
#Ran on Geeksforgeeks: Yes
#It is impossible to delete the current node. So swap the data in current node with the next node in the list. Delte the next node
#User function Template for python3
'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        temp=curr_node.data
        curr_node.data=curr_node.next.data
        curr_node.next.data=temp
        curr_node.next=curr_node.next.next

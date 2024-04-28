class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        """
        Initializes an empty binary search tree.
        """
        self._root_node = None

    def __repr__(self):
        """
        Returns a string representation of the tree.
        """
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value into the binary search tree.

        Parameters:
            data: The value to be inserted.

        Returns:
            None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Finds the node containing the specified data.
        Parameters:
            data: The data to be found.

        Returns:
            The node containing the specified data, or None if not found.
        """
        current_node = self._root_node
        # traverse the tree
        while current_node:
            if data == current_node.data:
                # data found in node
                return current_node
            # traverse left child
            elif data < current_node.data:
                current_node = current_node._left_child
            # traverse right child
            else:
                current_node = current_node._right_child
        return None


    def delete_node(self, data):
        """
        Deletes a node with the given data from the binary search tree.

        Parameters:
            data: The data to be deleted from the tree.

        Returns:
            None
        """
        node_to_delete = self._find(data)

        if node_to_delete is None:
            return None

        if node_to_delete._left_child is None:
            self._shift_nodes(node_to_delete, node_to_delete._right_child)

        elif node_to_delete._right_child is None:
            self._shift_nodes(node_to_delete, node_to_delete._left_child)
        else:
            # Find the successor of the node_to_delete
            successor = node_to_delete._right_child
            while successor._left_child:
                successor = successor._left_child

            # Replace the data of node_to_delete with the data of its successor
            node_to_delete.data = successor.data

            # Delete the successor node
            if successor._parent != node_to_delete:
                self._shift_nodes(successor, successor._right_child)
            else:
                node_to_delete._right_child = successor._right_child
                if successor._right_child:
                    successor._right_child._parent = node_to_delete


    def _shift_nodes(self, u, v):
        """
        Shifts the position of nodes in tree during deletion.

        Parameters:
            u: The node to be deleted.
            v: The replacement node.

        Returns:
            None
        """
        if u._parent is None:
            self._root_node = v
        elif u == u._parent._left_child:
            u._parent._left_child = v
        else:
            u._parent._right_child = v
        if v is not None:
            v._parent = u._parent


def test():
  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(35)
  result = tree._find(tree._root_node.data)
  print(result,(str(f'{result}') == '50<20<10<><>#><40<30<><>#><>#>#><70<><90<><>#>#>#'))


  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(30)
  result = tree._find(tree._root_node.data)
  print(result,(str(f'{result}') ==  '50<20<10<><>#><40<35<><>#><>#>#><70<><90<><>#>#>#'))

  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(40)
  result = tree._find(tree._root_node.data)
  print(result,(str(f'{result}') == '50<20<10<><>#><30<><35<><>#>#>#><70<><90<><>#>#>#'))



  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(20)
  result = tree._find(tree._root_node.data)
  print(result,(str(f'{result}') == '50<30<10<><>#><40<35<><>#><>#>#><70<><90<><>#>#>#'))



  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(50)
  tree.delete_node(20)
  tree.delete_node(70)
  tree.delete_node(90)
  tree.delete_node(10)
  tree.delete_node(40)
  tree.delete_node(30)
  tree.delete_node(35)
  result = tree._find(tree._root_node)
  print(result,(str(f'{result}') == 'None'))



  tree = Tree()
  tree.insert(50)
  tree.insert(20)
  tree.insert(70)
  tree.insert(90)
  tree.insert(10)
  tree.insert(40)
  tree.insert(30)
  tree.insert(35)
  tree.delete_node(0)
  result = tree._find(tree._root_node.data)
  print(result,(str(f'{result}') == '50<20<10<><>#><40<30<><35<><>#>#><>#>#><70<><90<><>#>#>#'))

test()

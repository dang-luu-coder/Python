'''
This Node class implement a Node in the character tree
'''


class Node():
    def __init__(self, left, right, ch, freq):
        self.left = left
        self.right = right
        self.freq = freq
        self.ch = ch

    #     overwrite the less than dunder method, so that the nodes can work with the priority queue
    def __lt__(self, other):
        return (self.freq < other.freq)


'''
This class implement the priority queue. When dequeue, the element with the smallest frequency will the popped out of the queue
'''


class Priority_Queue():
    def __init__(self):
        self.priority_queue = []

    def pop(self):
        min_element = self.priority_queue[0]
        min_ele_index = 0
        for i in range(1, len(self.priority_queue)):
            if self.priority_queue[i] < min_element:
                min_element = self.priority_queue[i]
                min_ele_index = i
        del self.priority_queue[min_ele_index]
        return min_element

    def insert(self, item):
        self.priority_queue.append(item)


def is_leaf_node(node):
    if node is None:
        return
    else:
        return (node.left is None) & (node.right is None)


def find_the_code(current_node, huffman_str, huffman_code):
    if current_node is None:
        return
    if is_leaf_node(current_node):
        huffman_code[current_node.ch] = huffman_str if len(huffman_str) > 0 else "1"
        return
    else:
        find_the_code(current_node.left, huffman_str + '0', huffman_code)
        find_the_code(current_node.right, huffman_str + "1", huffman_code)


def  decode(root, huffman_cypher_str, original_message):
    original_message = ""
    root_node = root
    if len(huffman_cypher_str) == 1:
        original_message += root.ch
    else:
        for i in range(len(huffman_cypher_str)):
                if is_leaf_node(root) :
                    original_message += root.ch
                    root = root_node
                else:
                    if huffman_cypher_str[i] == "1":
                        root = root.right
                    else:
                        root = root.left
                    if is_leaf_node(root) :
                        original_message += root.ch
                        root = root_node


    return original_message


def encode_n_decode_huffman(text):
    list_character_frequency = [(ch, text.count(ch)) for ch in set(text)]
    pq = Priority_Queue()
    for (k, v) in list_character_frequency:
        pq.insert(Node(left=None, right=None, ch=k, freq=v))
    #        Now it's time to build the hufman tree with the lowest frequency nodes at the bottom
    while ((len(pq.priority_queue) != 1) & (len(pq.priority_queue) > 0)):
        left_node = pq.pop()
        right_node = pq.pop()
        pq.insert(Node(left=left_node, right=right_node, ch=None, freq=left_node.freq + right_node.freq))
    # Check if the input string is empty
    try:
        root = pq.priority_queue[0]
    except IndexError:
        print("Cannot build the Huffman tree, retype the input message:")
        return
    huffman_code_dict = {}
    #     how to apply recursion here?
    s = ""
    #     traverse the tree to get the huffman codes of each character
    find_the_code(root, s, huffman_code_dict)
    huffman_cypher = ""
    # Map the characters with their huffman codes and combine all of them to get the encoded string
    for character in text:
         huffman_cypher += f"{huffman_code_dict[character]}"
#     So this is the compressed code of the input string
    print(f"so this is the compressed code of the input string - enjoy it! {huffman_cypher}")
#     Now it's time to decode the cypher and extract the original message
    original_str = ""
    original_str = decode(root, huffman_cypher, original_str)
    print(f"Wholly hell!! Finally this is the original message of the Nazi, we have decoded it {original_str}")


if __name__ == '__main__':
    while(1):
        print("Type in the message you want to encode: ")
        input_text = input()
        encode_n_decode_huffman(input_text)

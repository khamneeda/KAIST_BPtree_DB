# Check carefully the format of the tree representation in text
# Note that the last node in each level (including the root) is denoted by `-

answer1_1= """Insert 72
`- [72]
Insert 99
`- [72, 99]
Insert 67
`- [67, 72, 99]
Insert 70
`- [67, 70, 72, 99]
Insert 52
`- [70]
   |- [52, 67]
   `- [70, 72, 99]
Insert 28
`- [70]
   |- [28, 52, 67]
   `- [70, 72, 99]
Insert 27
`- [70]
   |- [27, 28, 52, 67]
   `- [70, 72, 99]
Insert 89
`- [70]
   |- [27, 28, 52, 67]
   `- [70, 72, 89, 99]
Insert 94
`- [70, 89]
   |- [27, 28, 52, 67]
   |- [70, 72]
   `- [89, 94, 99]
Insert 10
`- [28, 70, 89]
   |- [10, 27]
   |- [28, 52, 67]
   |- [70, 72]
   `- [89, 94, 99]"""

answer1_2 = """Insert 35
`- [35]
Insert 71
`- [35, 71]
Insert 44
`- [35, 44, 71]
Insert 60
`- [35, 44, 60, 71]
Insert 81
`- [60]
   |- [35, 44]
   `- [60, 71, 81]
Insert 61
`- [60]
   |- [35, 44]
   `- [60, 61, 71, 81]
Insert 29
`- [60]
   |- [29, 35, 44]
   `- [60, 61, 71, 81]
Insert 95
`- [60, 71]
   |- [29, 35, 44]
   |- [60, 61]
   `- [71, 81, 95]
Insert 63
`- [60, 71]
   |- [29, 35, 44]
   |- [60, 61, 63]
   `- [71, 81, 95]
Insert 23
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 61, 63]
   `- [71, 81, 95]"""

answer1_3 = """Insert 29
`- [29]
Insert 26
`- [26, 29]
Insert 40
`- [26, 29, 40]
Insert 34
`- [26, 29, 34, 40]
Insert 65
`- [34]
   |- [26, 29]
   `- [34, 40, 65]
Insert 73
`- [34]
   |- [26, 29]
   `- [34, 40, 65, 73]
Insert 15
`- [34]
   |- [15, 26, 29]
   `- [34, 40, 65, 73]
Insert 12
`- [34]
   |- [12, 15, 26, 29]
   `- [34, 40, 65, 73]
Insert 82
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 40]
   `- [65, 73, 82]
Insert 44
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 40, 44]
   `- [65, 73, 82]"""

answer1_4 = """Insert 28
`- [28]
Insert 50
`- [28, 50]
Insert 9
`- [9, 28, 50]
Insert 44
`- [9, 28, 44, 50]
Insert 15
`- [28]
   |- [9, 15]
   `- [28, 44, 50]
Insert 68
`- [28]
   |- [9, 15]
   `- [28, 44, 50, 68]
Insert 12
`- [28]
   |- [9, 12, 15]
   `- [28, 44, 50, 68]
Insert 73
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44]
   `- [50, 68, 73]
Insert 49
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [50, 68, 73]
Insert 62
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [50, 62, 68, 73]"""

answer1_5 = """Insert 3
`- [3]
Insert 97
`- [3, 97]
Insert 18
`- [3, 18, 97]
Insert 96
`- [3, 18, 96, 97]
Insert 82
`- [82]
   |- [3, 18]
   `- [82, 96, 97]
Insert 84
`- [82]
   |- [3, 18]
   `- [82, 84, 96, 97]
Insert 41
`- [82]
   |- [3, 18, 41]
   `- [82, 84, 96, 97]
Insert 67
`- [82]
   |- [3, 18, 41, 67]
   `- [82, 84, 96, 97]
Insert 56
`- [41, 82]
   |- [3, 18]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]
Insert 11
`- [41, 82]
   |- [3, 11, 18]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]"""

answer1_6= """Insert 0
`- [0]
Insert 17
`- [0, 17]
Insert 6
`- [0, 6, 17]
Insert 18
`- [0, 6, 17, 18]
Insert 11
`- [11]
   |- [0, 6]
   `- [11, 17, 18]
Insert 1
`- [11]
   |- [0, 1, 6]
   `- [11, 17, 18]
Insert 3
`- [11]
   |- [0, 1, 3, 6]
   `- [11, 17, 18]
Insert 16
`- [11]
   |- [0, 1, 3, 6]
   `- [11, 16, 17, 18]
Insert 9
`- [3, 11]
   |- [0, 1]
   |- [3, 6, 9]
   `- [11, 16, 17, 18]
Insert 5
`- [3, 11]
   |- [0, 1]
   |- [3, 5, 6, 9]
   `- [11, 16, 17, 18]
Insert 2
`- [3, 11]
   |- [0, 1, 2]
   |- [3, 5, 6, 9]
   `- [11, 16, 17, 18]
Insert 13
`- [3, 11, 16]
   |- [0, 1, 2]
   |- [3, 5, 6, 9]
   |- [11, 13]
   `- [16, 17, 18]
Insert 19
`- [3, 11, 16]
   |- [0, 1, 2]
   |- [3, 5, 6, 9]
   |- [11, 13]
   `- [16, 17, 18, 19]
Insert 8
`- [3, 6, 11, 16]
   |- [0, 1, 2]
   |- [3, 5]
   |- [6, 8, 9]
   |- [11, 13]
   `- [16, 17, 18, 19]
Insert 15
`- [3, 6, 11, 16]
   |- [0, 1, 2]
   |- [3, 5]
   |- [6, 8, 9]
   |- [11, 13, 15]
   `- [16, 17, 18, 19]
Insert 10
`- [3, 6, 11, 16]
   |- [0, 1, 2]
   |- [3, 5]
   |- [6, 8, 9, 10]
   |- [11, 13, 15]
   `- [16, 17, 18, 19]
Insert 14
`- [3, 6, 11, 16]
   |- [0, 1, 2]
   |- [3, 5]
   |- [6, 8, 9, 10]
   |- [11, 13, 14, 15]
   `- [16, 17, 18, 19]
Insert 12
`- [11]
   |- [3, 6]
   |  |- [0, 1, 2]
   |  |- [3, 5]
   |  `- [6, 8, 9, 10]
   `- [13, 16]
      |- [11, 12]
      |- [13, 14, 15]
      `- [16, 17, 18, 19]
Insert 7
`- [11]
   |- [3, 6, 8]
   |  |- [0, 1, 2]
   |  |- [3, 5]
   |  |- [6, 7]
   |  `- [8, 9, 10]
   `- [13, 16]
      |- [11, 12]
      |- [13, 14, 15]
      `- [16, 17, 18, 19]
Insert 4
`- [11]
   |- [3, 6, 8]
   |  |- [0, 1, 2]
   |  |- [3, 4, 5]
   |  |- [6, 7]
   |  `- [8, 9, 10]
   `- [13, 16]
      |- [11, 12]
      |- [13, 14, 15]
      `- [16, 17, 18, 19]"""

answer2_1 = """
Delete 67
`- [28, 70, 89]
   |- [10, 27]
   |- [28, 52]
   |- [70, 72]
   `- [89, 94, 99]
Delete 10
`- [70, 89]
   |- [27, 28, 52]
   |- [70, 72]
   `- [89, 94, 99]
Delete 99
`- [70, 89]
   |- [27, 28, 52]
   |- [70, 72]
   `- [89, 94]
Delete 94
`- [70]
   |- [27, 28, 52]
   `- [70, 72, 89]"""

answer2_2 = """
Delete 71
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 61, 63]
   `- [81, 95]
Delete 61
`- [60, 71]
   |- [23, 29, 35, 44]
   |- [60, 63]
   `- [81, 95]
Delete 95
`- [60]
   |- [23, 29, 35, 44]
   `- [60, 63, 81]
Delete 63
`- [60]
   |- [23, 29, 35, 44]
   `- [60, 81]
Delete 81
`- [44]
   |- [23, 29, 35]
   `- [44, 60]"""

answer2_3 = """
Delete 40
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 44]
   `- [65, 73, 82]
Delete 82
`- [34, 65]
   |- [12, 15, 26, 29]
   |- [34, 44]
   `- [65, 73]
Delete 29
`- [34, 65]
   |- [12, 15, 26]
   |- [34, 44]
   `- [65, 73]
Delete 15
`- [34, 65]
   |- [12, 26]
   |- [34, 44]
   `- [65, 73]"""

answer2_4 = """
Delete 50
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [62, 68, 73]
Delete 62
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44, 49]
   `- [68, 73]
Delete 49
`- [28, 50]
   |- [9, 12, 15]
   |- [28, 44]
   `- [68, 73]
Delete 73
`- [28]
   |- [9, 12, 15]
   `- [28, 44, 68]"""
   
answer2_5 = """
Delete 18
`- [41, 82]
   |- [3, 11]
   |- [41, 56, 67]
   `- [82, 84, 96, 97]
Delete 67
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [82, 84, 96, 97]
Delete 96
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [82, 84, 97]
Delete 82
`- [41, 82]
   |- [3, 11]
   |- [41, 56]
   `- [84, 97]
Delete 97
`- [41]
   |- [3, 11]
   `- [41, 56, 84]
Delete 41
`- [41]
   |- [3, 11]
   `- [56, 84]
Delete 56
`- [3, 11, 84]"""

# The file name must be bptree.py (case sensitive)
# The class name must be BPTree (case sensitive)

# Let's fix n to be 5. That is, a node can hold up to 4 search keys
# Let's assume that there is NO duplicate key

class BPTree(object):

   class Node:
      def __init__(self, value):
         self.value = value
         self.child1 = None  # Bnode
         self.child2 = None  

   class BNode:
      def __init__(self):
         self.nodes = [] 
         self.parent = None # Node not BNode
         self.isleaf = True
         self.prev = None
         self.next = None
         self.depth = 0 # leaf = 0
      
      def add_node(self, node, index):
         self.nodes.insert(index, node)
      
      def del_node(self, node):
         self.nodes.remove(node)

      def pop_node(self, index):
         self.nodes.pop(index)

      def get_values(self):
         values = []
         for node in self.nodes:
            values.append(node.value)
         return values

      def get_num_nodes(self):
         return len(self.nodes)
   
      def get_parent(self):
         return self.parent

   def stringmake(self, bnode,max_depth,last, result):
      # 위치 프린트
      result = result + "\n"
      for i in range(max_depth - bnode.depth):
         result = result + "   "
      if last:
         result = result + "`- ["
      else:
         result = result + "|- ["
      
      # value 프린트
      for b in range(len(bnode.nodes)):
         result = result + str(bnode.nodes[b].value)
         if b != len(bnode.nodes) -1:
            result = result + ", "
      result = result + "]"

      # 모든 leaf에 대해 호출
      if not bnode.isleaf:
         for node in bnode.nodes:
            result = self.stringmake(node.child1, max_depth, False, result)
         result = self.stringmake(node.child2, max_depth, True, result)

      return result
      # 현재 프린트
      # 만약 leaf 있으면
      # 자신의 모든 leaf에 대해 호출
      # 매번 result 업데이트 해서 넣어줘야
      # leaf에 호출할때 횟수별로 시작 조건 다르게 해줘서

   def check(self, b,val, key, sig="#"):
      # if val == key:
      #    for i in range(10):
      #       print(sig, end= "")
      #    print("\nKey:",key)
      #    print(b.get_values())
      #    if b.parent != None:
      #       print("Parent:",b.parent.get_values())
      #    else:
      #       print("No parent")
      #    print("\n")
      pass
         
   def insert(self,key_list):
      bnode_list = []
      node_list = []
      result = "Insert " + str(key_list[0]) + "\n`- [" + str(key_list[0]) + "]"

      bnode_list.append(self.BNode())
      root = bnode_list[len(bnode_list) - 1]

      node_list.append(self.Node(key_list.pop(0)))
      root_node = node_list[len(node_list) - 1]

      root.add_node(root_node,0)
      for key in key_list:
         result = result + "\nInsert " + str(key)

         node_list.append(self.Node(key))
         newnode = node_list[len(node_list) - 1]

         
         # 리프로 가서 그냥 빈자리 앞쪽 b노드에 붙여서 넣기
         bpos = root
         self.check(bpos,11,key)
         while not bpos.isleaf:
            bpos = bpos.nodes[0].child1
            self.check(bpos,11,key)
         

         # 해당 B리프 찾기
         while bpos.next != None:
            if bpos.next.get_values()[0] > key:
               # if key == 11: print("@@@@@@here:", bpos.next.get_values()[0])
               break
            else:
               bpos = bpos.next
            self.check(bpos,9,key,"$")
      
         # print("     Prev: ",bpos.prev)
         # print("     Next: ",bpos.next)
         self.check(bpos, 9,key,"!")

         # 해당 B리프 내에서 위치에 삽입
         values = bpos.get_values()
         for i in range(len(values)):
            if key < values[i]:
               break
         if key > values[i]:
            i += 1
         bpos.add_node(newnode, i)

         # 초과일때 separation
         # 부모, 자식 관계 모두 업데이트해야함
         # 옮기는 애만 자식 업데이트하면 되고
         # 새로 만든 bnode들 부모 동기화하면 됨
         while bpos.get_num_nodes() == 5:          
            upnode = bpos.nodes[2]

            # 해당 층 분할
            bnode_list.append(self.BNode())
            rightbnode = bnode_list[len(bnode_list) - 1]
            rightbnode.parent = bpos.parent
            rightbnode.isleaf = bpos.isleaf
            rightbnode.prev = bpos
            rightbnode.next = bpos.next
            bpos.next = rightbnode
            rightbnode.depth = bpos.depth

            for n in range(2,5):
               rightbnode.add_node(bpos.nodes[n],n-2)
            for j in range(3):
               bpos.pop_node(4-j)
            if not rightbnode.isleaf:
               rightbnode.pop_node(0)

            # 중간친구 올리기
            # 얘가 child update 해줘야
            # greater than equal to가 오른쪽 child2

   # leaf가 아닐 때는 추가하지 않고, 자식도 없애줌
   # 하나 더 빼줘야한다 라는게 11을 빼줘야
   
            parent = bpos.parent
            if parent == None:
               bnode_list.append(self.BNode())
               parent = bnode_list[len(bnode_list) - 1]
               parent.isleaf = False
               parent.add_node(upnode, 0)
               parent.depth = bpos.depth +1
               bpos.parent = parent
               rightbnode.parent = parent
            else:
               parent_values = parent.get_values()
               for i in range(len(parent_values)):
                  if upnode.value < parent_values[i]:
                     break
               if upnode.value > parent_values[i]:
                  i += 1
               else:
                  parent.nodes[i].child1 = rightbnode
               parent.add_node(upnode, i)


            upnode.child1 = bpos
            upnode.child2 = rightbnode

            bpos = parent
            while parent.parent != None:
               parent = parent.parent
            root = parent

         # string 만들기
         bnode = root
         maxdepth = root.depth
         result = self.stringmake(bnode, maxdepth, True, result)

         # print("@@@")
         # print(root.get_values())
         # if (len(root.get_values())>0):
         #    if(root.nodes[0].child1 != None):         
         #       print("child1:", root.nodes[0].child1.get_values())
         #       print("child2:", root.nodes[0].child2.get_values())
         #    else:
         #       print("No child1")
         #    if (len(root.get_values())>1):
         #       if(root.nodes[0].child2 != None):         
         #          print("child3:", root.nodes[1].child1.get_values())
         #       else:
         #          print("No child3")
         #    else:
         #       print("not enough")
         # else:
         #    print("No values")

      return result


   # key: integer
   def delete(self, key):
      # Fill in here
      a = 1 # bogus code
      # Insert때와는 다르게 delete일때는 첫줄 바꿔서 해야함
    
   # insert_keys: integer list
   # delete_keys: integer list (an empty list in the first assi`gnment)
   # return: result string (sequence of tree representations)
   def show(self, insert_keys, delete_keys):
      # Fill in here
      if insert_keys == [72, 99, 67, 70, 52, 28, 27, 89, 94, 10] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_1)
      elif insert_keys == [35, 71, 44, 60, 81, 61, 29, 95, 63, 23] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_2)
      elif insert_keys == [29, 26, 40, 34, 65, 73, 15, 12, 82, 44] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_3)
      elif insert_keys == [28, 50, 9, 44, 15, 68, 12, 73, 49, 62] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_4)
      elif insert_keys == [3, 97, 18, 96, 82, 84, 41, 67, 56, 11] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_5)
      elif insert_keys == [0,17,6,18,11,1,3,16,9,5,2,13,19,8,15,10,14,12,7,4] and len(delete_keys) == 0:
         result = self.insert(insert_keys)
         print(result == answer1_6)
      else:
         result = self.insert(insert_keys)
      return result
      # First, run all insertions in insert_keys (the value is simply set to be the key)
      # Then, run all deletions in delete_keys
      # For each insertion or deletion, show the operation and tree
      # See this file for the details of the format

    # bogus implementation
    # Replace this bogus implementation with a real one
   #  def show(self, insert_keys, delete_keys):
   #      if insert_keys == [72, 99, 67, 70, 52, 28, 27, 89, 94, 10] and len(delete_keys) == 0:
   #          result = answer1_1
   #      elif insert_keys == [35, 71, 44, 60, 81, 61, 29, 95, 63, 23] and len(delete_keys) == 0:
   #          result = answer1_2
   #      elif insert_keys == [29, 26, 40, 34, 65, 73, 15, 12, 82, 44] and len(delete_keys) == 0:
   #          result = answer1_3
   #      elif insert_keys == [28, 50, 9, 44, 15, 68, 12, 73, 49, 62] and len(delete_keys) == 0:
   #          result = answer1_4
   #      elif insert_keys == [3, 97, 18, 96, 82, 84, 41, 67, 56, 11] and len(delete_keys) == 0:
   #          result = answer1_5
   #      elif insert_keys == [72, 99, 67, 70, 52, 28, 27, 89, 94, 10] and len(delete_keys) > 0:
   #          result = answer1_1 + answer2_1
   #      elif insert_keys == [35, 71, 44, 60, 81, 61, 29, 95, 63, 23] and len(delete_keys) > 0:
   #          result = answer1_2 + answer2_2
   #      elif insert_keys == [29, 26, 40, 34, 65, 73, 15, 12, 82, 44] and len(delete_keys) > 0:
   #          result = answer1_3 + answer2_3
   #      elif insert_keys == [28, 50, 9, 44, 15, 68, 12, 73, 49, 62] and len(delete_keys) > 0:
   #          result = answer1_4 + answer2_4
   #      elif insert_keys == [3, 97, 18, 96, 82, 84, 41, 67, 56, 11] and len(delete_keys) > 0:
   #          result = answer1_5 + answer2_5
   #      else:
   #          result = 'Failed'
   #      return(result)

# IMPORTANT:
# Using a unittest library, your BPTree implementation will be imported, 
# and the following code with a different input will be executed. 

if __name__ == '__main__':
   bpt = BPTree()
   # For Programming Assignment 1/2
   # print(bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], []))
   # print(bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], []))
   # print(bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], []))
   # print(bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], []))
   # print(bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], []))

   bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], [])
   bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], [])
   bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], [])
   bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], [])
   bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], [])
   print(bpt.show([0,17,6,18,11,1,3,16,9,5,2,13,19,8,15,10,14,12,7,4], []))

   # For Programming Assignment 2/2
   #  print(bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], [67, 10, 99, 94]))
   #  print(bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], [71, 61, 95, 63, 81]))
   #  print(bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], [40, 82, 29, 15]))
   #  print(bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], [50, 62, 49, 73]))
   #  print(bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], [18, 67, 96, 82, 97, 41, 56]))
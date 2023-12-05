import random
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

   def debug(self, bnode, key, searchkey, char):
      if key == searchkey:
         print()
         for i in range(10):
            print(char, end="")
         print("\nBnode:",bnode.get_values())
         print("Parent:",bnode.parent.get_values())
         print("Leaf:",str(bnode.isleaf))
         print("prev:",bnode.prev.get_values())
         print("next:",bnode.next.get_values())
         print("depth:",bnode.depth)
         print("**Node info**")
         for node in bnode.nodes:
            print("Node value:", str(node.value))
            if node.child1 != None:
               print("child1:",node.child1.get_values())
            if node.child2 != None:
               print("child2:",node.child2.get_values(),"\n")

   def stringmake(self, bnode, root, last_list, last, result, first):
      # 위치 프린트
      result = result + "\n"
      if not root:
         result = result + "   "
         if len(last_list) <= 1:
            pass
         else:
            for l in range(1, len(last_list)):
               if last_list[l]:
                  result = result + "   "
               else:
                  result = result + "|  "
      
      next = False
      if last:
         result = result + "`- ["
         next = True
      else:
         result = result + "|- ["
      
      # value 프린트
      for b in range(len(bnode.nodes)):
         result = result + str(bnode.nodes[b].value)
         if b != len(bnode.nodes) -1:
            result = result + ", "
      result = result + "]"

      # 모든 child에 대해 호출
      if not bnode.isleaf:
         for n in range(len(bnode.nodes)):
            if n==0:
               result = self.stringmake(bnode.nodes[n].child1, False, last_list + [next], False, result, True)
            else:
               result = self.stringmake(bnode.nodes[n].child1, False, last_list + [next], False, result, False)
         result = self.stringmake(bnode.nodes[n].child2, False, last_list + [next], True, result, False)

      return result
         
   def insert(self,key_list, delete, del_keys):
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
         while not bpos.isleaf:
            bpos = bpos.nodes[0].child1
         

         # 해당 B리프 찾기
         while bpos.next != None:
            if bpos.next.get_values()[0] > key:
               break
            else:
               bpos = bpos.next

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

            # leaf인 경우
            # leaf가 아닌 곳에 올라와서 문제 생긴 경우

            # 해당 층 분할
            bnode_list.append(self.BNode())
            rightbnode = bnode_list[len(bnode_list) - 1]
            rightbnode.parent = bpos.parent
            rightbnode.isleaf = bpos.isleaf
            # if bpos.isleaf:
            rightbnode.prev = bpos
            rightbnode.next = bpos.next
            bpos.next = rightbnode
            rightbnode.depth = bpos.depth

            # bnode내 노드 개수 맞추기
            for n in range(2,5):
               rightbnode.add_node(bpos.nodes[n],n-2)
            #right노드 휘하 애들 parent 업데이트
            #bpos.node들의 child1의 첫번째 애가 upnode보다 크거나 같을 경우 오른쪽 편입/ child2도 오른쪽 편입(무조건)
            for i in range(5):
               if bpos.nodes[i].child1 != None:
                  if bpos.nodes[i].child1.nodes[0].value >= upnode.value:
                     bpos.nodes[i].child1.parent = rightbnode
            if bpos.nodes[4].child2 != None:
               bpos.nodes[4].child2.parent = rightbnode

            for j in range(3):
               bpos.pop_node(4-j)
            if not rightbnode.isleaf:
               rightbnode.pop_node(0)

            # 중간친구 올리기
            # 얘가 child update 해줘야
            # greater than equal to가 오른쪽 child2
            upnode.child1 = bpos
            upnode.child2 = rightbnode
   
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
                  parent.nodes[i].child1 = rightbnode ## 여기 뭔가 있는듯
               if i>0:
                  parent.nodes[i-1].child2 = bpos
               parent.add_node(upnode, i)
            
            # Next cycle
            bpos = parent
         

         # string 만들기
         while bpos.parent != None:
            bpos = bpos.parent
         maxdepth = bpos.depth
         result = self.stringmake(bpos, True, [], True, result, True)

      if delete == True:
         return self.delete_list(del_keys, bpos, bnode_list, node_list)

      return result

# 로컬이라 반영 안될경우 리스트도 넣어주고, 없앨때마다 전체 리스트서 빼주기
   def delete_entry(self, root, bnode, key, bnode_list, node_list):
      
      # delete node from bnode
      values = bnode.get_values()
      for i in range(len(values)):
         if key == values[i]:
            break
      bnode.pop_node(i)

      # 루트 조건시 업데이트
      if bnode.parent == None and bnode.nodes[0].child2 == None:
         root = bnode.nodes[0].child1
         bnode.nodes[0].child1.parent = None
         bnode.nodes.pop()
         if bnode.prev != None:
            bnode.prev.next = bnode.next
         if bnode.next != None:
            bnode.next.prev = bnode.prev
      
      # 연쇄조건 시작
      elif bnode.get_num_nodes() < 2:
         assert(bnode.get_num_nodes() == 1)
         
         # 부모 있는 경우에만 실행 -> 없을 경우 루트라 시작 안해도 됨
         if bnode.parent != None:
            # 왼쪽 노드 없는 경우
            node_left = False
            receive_bnode = bnode.parent.nodes[0].child2
            assert(receive_bnode != None)
            
            # 왼쪽 노드 있는 경우
            for i in range(bnode.parent.get_num_nodes()):
               if bnode.parent.nodes[i].child2 == bnode:
                  node_left = True 
                  receive_bnode = bnode.parent.nodes[i].child1
                  break
            
            assert(receive_bnode.get_num_nodes <5 and receive_bnode.get_num_nodes > 1)
            recv_org_num = receive_bnode.get_num_nodes()
            # merge
            # 왼쪽에서 가져오는경우에는 parent value 업데이트 해줘야함 ? 이게 먼말 둘다 해줘야함
            if recv_org_num <4:
               # 부모노드
               for i in range(bnode.parent.get_num_nodes()):
                  if bnode.parent.nodes[i].child2 == bnode:
                     break
               parent_node = bnode.parent.nodes[i]
               
               move_node = bnode.pop_node(0)
               #리프노드일 경우
               if bnode.isleaf:
               
                  # 왼쪽 노드로 옮기는 경우
                  if node_left:
                     receive_bnode.add_node(move_node, receive_bnode.get_num_node())
                     receive_bnode.next = bnode.next
                     if bnode.next != None:
                        bnode.next.prev = receive_bnode

                  # 오른쪽 노드로 옮기는 경우
                  else:
                     receive_bnode.add_node(move_node,0)
                     receive_bnode.prev = bnode.prev
                     if bnode.prev != None:
                        bnode.prev.next = receive_bnode
               
               # 리프노드가 아닌 경우
               else:
                  #parent의 자신 bnode를 child2로 가리키는 value 추가
                  node_list.append(self.Node(key))
                  down_pnode = node_list[len(node_list) - 1]
                  down_pnode.value = parent_node.value

                  # 왼쪽 노드로 옮기는 경우
                  if node_left:
                     #parent 먼저 넣고, 다음으로 자기 넣어야함
                     receive_bnode.add_node(down_pnode, receive_bnode.get_num_node())   
                     receive_bnode.add_node(move_node, receive_bnode.get_num_node())        
                     down_pnode.child1 = receive_bnode.nodes[recv_org_num-1].child2        
                     down_pnode.child2 = move_node.child1
                     receive_bnode.next = bnode.next
                     if bnode.next != None:
                        bnode.next.prev = receive_bnode
         
                  # 오른쪽 노드로 옮기는 경우
                  else:
                     # 자기, parent, 원래 순서대로 되도록 넣어야
                     down_pnode.child2 = receive_bnode.nodes[0].child1        
                     down_pnode.child1 = move_node.child2
                     receive_bnode.add_node(down_pnode, 0)   
                     receive_bnode.add_node(move_node, 0)        
                     receive_bnode.prev = bnode.prev
                     if bnode.prev != None:
                        bnode.prev.next = receive_bnode


               # 이거 지금은 merge 소속인데 전체로 해야하는지 판단 ####################################
               # 합쳐서 넘었을 경우 --> 셋으로 분할: 원래: 2or 3개 / 올라가는애 하나 / 나머지 2개
               if receive_bnode.get_num_nodes() >4:

                  # 분할한 오른쪽 노드로 옮기기
                  bnode_list.append(self.BNode())
                  newbnode = bnode_list[len(bnode_list) - 1]
                  newbnode.parent = receive_bnode.parent
                  newbnode.isleaf = receive_bnode.isleaf
                  newbnode.depth = receive_bnode.depth
                  newbnode.prev = receive_bnode
                  newbnode.next = receive_bnode.next
                  receive_bnode.next = newbnode
                  newbnode.add_node(receive_bnode.pop_nodes(receive_bnode.get_num_nodes()-1), 0)
                  newbnode.add_node(receive_bnode.pop_nodes(receive_bnode.get_num_nodes()-1), 0)
                  
                  #위에 추가
                  upnode = receive_bnode.pop_nodes(receive_bnode.get_num_nodes()-1)
                  upnode.child1 = receive_bnode
                  upnode.child2 = newbnode
                  
                  # 위에 노드가 없을 경우: 아마 이런 경우 없을거임
                  if newbnode.parent == None:
                     print("Why depth increase?") ##########################################제출전 제거. assert 다 제거
                     bnode_list.append(self.BNode())
                     newparent = bnode_list[len(bnode_list) - 1]
                     newparent.add_node(upnode,0)
                     newbnode.parent = newparent
                     receive_bnode.parent = newparent
                     newparent.isleaf = False
                     newparent.depth = newbnode.depth + 1

                  # parent에 upnode 추가
                  else:
                     for i in range(newbnode.parent.get_num_nodes()):
                        if newbnode.parent.nodes[i] > upnode.value:
                           break
                     if newbnode.parent.nodes[newbnode.parent.get_num_nodes()-1] < upnode.value:
                        i += 1
                     newbnode.parent.add_node(upnode,i)

               # 이거 위치 여기인지 아니면 625번줄 합쳐서 넘었을 경우 위인지 생각 ###################################
               # 부모노드 제거 recursive 실행
               # 제거노드를 child2로 가진 부모bnode 내 node key
               self.delete_entry(root, bnode.parent, parent_node.value, bnode_list, node_list)
         

            #recv_org_num = receive_bnode.get_num_nodes()
            #node left 
            # re-distribution
            else: 

               # leaf인 경우
               if bnode.isleaf:
                  
                  # 왼쪽"에서" 옮길 경우
                  if node_left:
                     move_node = receive_bnode.pop_node(receive_bnode.get_num_nodes()-1)
                     for i in range(bnode.parent.get_num_nodes()):
                        if bnode.parent.nodes[i].child2 == bnode:
                           break
                     bnode.parent.nodes[i].value = move_node.value
                     bnode.add_node(move_node,0)

                  # 오른쪽"에서" 옮길 경우
                  else:
                     move_node = receive_bnode.pop_node(0)
                     for i in range(bnode.parent.get_num_nodes()):
                        if bnode.parent.nodes[i].child1 == bnode:
                           break
                     # 알바노?
                     bnode.add_node(move_node,1)
                  
               #leaf 아닌경우 마찬가지로 부모거 땡겨서 가져와야함 수도코드 참조
               # 왼쪽거를 올리고 부모거를 받는다
               # child값 일일이 변경 귀찮아서 그냥 왼쪽애노드를 오른쪽으로 옮기고
               # 옮긴노드랑 부모노드의 값만 따로 미리 받아뒀다 업데이트
               else:

                  # 왼쪽에서 옮길 경우
                  if node_left:
                     # 값 미리 빼줌
                     for i in range(bnode.parent.get_num_nodes()):
                        if bnode.parent.nodes[i].child2 == bnode:
                           break
                     par_val = bnode.parent.nodes[i].value
                     move_val = receive_bnode.nodes[receive_bnode.get_num_nodes()-1].value
                     
                     # 노드 옮김 및 값 업데이트
                     move_node = receive_bnode.pop_node(receive_bnode.get_num_nodes()-1)
                     bnode.add_node(move_node,0)
                     move_node.value = par_val
                     bnode.parent.nodes[i].value = move_val
                  
                  # 오른쪽에서 옮길 경우
                  else:
                     for i in range(bnode.parent.get_num_nodes()):
                        if bnode.parent.nodes[i].child1 == bnode:
                           break
                        assert(i!=1)
                     par_val = bnode.parent.nodes[i].value
                     move_val = receive_bnode.nodes[0].value

                     move_node = receive_bnode.pop_node(0)
                     bnode.add_node(move_node, 1)
                     move_node.value = par_val
                     bnode.parent.nodes[i].value = move_val
                  
         # 부모 없는 경우
         else:
            #아무것도 안함
            pass


   # key: integer
   def delete_list(self, del_keys, root, bnode_list, node_list):
      result = ""

      # 루트노드 찾기
      while root.parent != None:
         root = root.parent

      for key in del_keys:
         result = result + "\nDelete " + str(key)
         
         #리프노드 찾기
         bpos = root
         while not bpos.isleaf:
            bpos = bpos.nodes[0].child1
         
         # 해당 bnode 찾기
         while bpos.next != None:
            if bpos.next.get_values()[0] > key:
               break
            else:
               bpos = bpos.next

         self.delete_entry(root, bpos, key)















         # 해당 bnode 내 value 제거
         values = bpos.get_values()
         for i in range(len(values)):
            if key == values[i]:
               break
         bpos.pop_node(i)

         # 연쇄 조건문 시작
         while bpos.get_num_nodes() < 2:

            # bpos가 leaf아니고 자식이 하나일 경우 : right없는경우
            if bpos.isleaf == False and bpos.get_num_nodes == 1 and bpos.nodes[0].child2 == None:
               bpos = bpos.nodes[0].child1
               bpos.parent.pop_nodes[0]
               bpos.parent = None
            
            else:
               #왼쪽노드가 있을 경우
               if bpos.prev != None:
                  
                  # merge
                  if bpos.prev.get_num_nodes() < 4:
                     movenode = bpos.pop_node(i)
                     bpos.prev.add_node(movenode, bpos.prev.get_num_nodes())

                     #옆노드 업데이트
                     bpos.prev.next = bpos.next
                     if bpos.next != None:
                        bpos.next.prev = bpos.prev

                     # 부모 노드 업데이트
                     if bpos.parent != None:
                        for i in range(bpos.parent.get_num_nodes()):
                           if bpos.parent.nodes[i].child2 == bpos:
                              bpos.parent.pop_nodes[i]
                              
                              # 부모가 없어진 경우 
                              # if bpos.parent.get_num_nodes() == 0:
                              assert(bpos.parent.get_num_nodes() != 0)

                                 # #옆노드 업데이트: 할 필요 없음 어차피 없을테니
                                 # assert(bpos.prev == None)
                                 # assert(bpos.next == None)
                                 # assert(bpos.parent == None)
                                 # bpos.parent = None

                                 
                              break
                        

                     #bpos 제거
                     pass
                  
                  # redistribute
                  else:
                     pass

                  # 왼쪽애가 있을 경우
                     #왼쪽애가 3개이하일 경우
                        #합침
                           #부모내 node 중 사라지는 bnode child2로 가지던 부모 value 제거
                              #부모의 value가 없을 경우
                              #부모의 bnode 제거
                        #가져옴
                           #왼쪽애중 가장 큰친구 가져옴
                           #뺏은노드 child2로 가진 부모의 value 업데이트
               elif bpos.next != None:
                  pass
                  #왼쪽애가 없을 경우
                     #오른쪽 애가 3개이하일 경우
                        #합침 : 오른쪽 애를 가져옴
                           #위와 마찬가지로 오른쪽 애를 제거함
                        #가져옴
                           #오른쪽 애 중 가장 작은친구 가져옴
                           #뺏긴노드 child2 가진 부모의 value 업데이트
                           #얘는 무조건 부모도 젤 왼쪽임
               
               else:
                  pass

            
            
            # parent 노드에 대해서도 탐색
            if bpos.parent != None:
               bpos = bpos.parent



         # key 빼낼때마다 stringmaker
         result = result + 


      # Insert때와는 다르게 delete일때는 첫줄 바꿔서 해야함
      #insert 내에서 delete 호출해야 local variable인 노드 리스트 쓸수있음
      #insert시 delete 조건 true, false로 -> delete_keys가 []인지 아닌지로 하면 될듯
      #걍 show에서 empty 일 경우 tru false로 따로 넣어주는게 안전할듯
      #내부 출력 함수도 조건으로 해야겠네 if !delete: result = self.stringmake이렇게
      pass

   # insert_keys: integer list
   # delete_keys: integer list (an empty list in the first assi`gnment)
   # return: result string (sequence of tree representations)
   def show(self, insert_keys, delete_keys):
      # Fill in here
      ins_keys = insert_keys[:]
      del_keys = delete_keys[:]

######일단 insert부터 잘 돌아가는지 verification 해보기 안되면 리프 아닐때 prev next 지정한게 문제

      if len(delete_keys) == 0:
         result = self.insert(ins_keys,False,del_keys)
      else:
         result = self.insert(ins_keys, True, del_keys)

      result = self.insert(ins_keys, del_keys)
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

   # For Programming Assignment 2/2
   #  print(bpt.show([72, 99, 67, 70, 52, 28, 27, 89, 94, 10], [67, 10, 99, 94]))
   #  print(bpt.show([35, 71, 44, 60, 81, 61, 29, 95, 63, 23], [71, 61, 95, 63, 81]))
   #  print(bpt.show([29, 26, 40, 34, 65, 73, 15, 12, 82, 44], [40, 82, 29, 15]))
   #  print(bpt.show([28, 50, 9, 44, 15, 68, 12, 73, 49, 62], [50, 62, 49, 73]))
   #  print(bpt.show([3, 97, 18, 96, 82, 84, 41, 67, 56, 11], [18, 67, 96, 82, 97, 41, 56]))

def main():  

        #     0  1  2  3
        #  0  0  1  1  0
        #  1  0  0  1  0
        #  2  1  0  0  1
        #  3  0  0  0  1

        # The graph's adjacency matrix
	matrix = [[0,1,1,0],
                  [0,0,1,0],
                  [1,0,0,1],
                  [0,0,0,1]];

	# The visited array
	visited = [0,0,0,0]

	# Add the start node to the queue
	# Node 0 in this case
	queue = [0]

	# Set the visited value of node 0 to visited
	visited[0] = 1

	# Dequeue node 0
	node = queue.pop(0);
	print node

	while True:

		for x in range (0, len(visited)):

                        # Check is route exists and that node isn't visited
			if matrix[node][x] == 1 and visited[x] == 0:

                                # Visit node
				visited[x] = 1;

                                # Enqueue element
				queue.append(x)

		# When queue is empty, break		
		if len(queue) == 0:
			break;

		else:

                        # Dequeue element from queue
			node = queue.pop(0)
			print node
	
if __name__ == "__main__":
	main()

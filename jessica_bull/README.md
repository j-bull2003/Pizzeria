# PolyAI

## About the code:
#### The purpose of this code is to determine the block in a city with the greatest number of pizzerias that can deliver to it. To accomplish this, the code uses a breadth-first search (BFS) algorithm to identify all the blocks within the delivery range of each pizzeria and increments a delivery count for each block. These counts are stored in a 2D list called delivery_counts, where each element delivery_counts[i][j] represents the number of pizzerias that can deliver to block (i, j).

#### The BFS algorithm begins by reading in the input, which consists of the dimensions of the city and the locations and delivery ranges of the pizzerias. For each pizzeria, the algorithm initializes a queue with the pizzeria's location and a visited list to keep track of which blocks have been visited. It then repeatedly performs the following steps until the queue is empty:

#### Pop the first element (i, j, d) from the queue.
#### If the distance d is greater than the delivery range r, or if the block (i, j) has already been visited, continue to the next iteration of the loop.
#### Mark the block (i, j) as visited.
#### Increment the delivery count for the block (i, j) by 1.
#### For each of the four adjacent blocks (i + dx, j + dy), where dx and dy are either 0 or 1, append the block to the queue if it is within the city bounds (i.e., 0 <= i + dx < n and 0 <= j + dy < n) and has not been visited.
#### After the BFS algorithm has completed for all pizzerias, the code finds the maximum delivery count by comparing the delivery count for each block (i, j) to a variable called max_count. If delivery_counts[i][j] is greater than max_count, max_count is updated to be equal to delivery_counts[i][j]. Finally, the code prints the maximum delivery count, which is the maximum number of pizzerias that can deliver to a single block in the city.

#### The time complexity of the breadth-first search algorithm is O(n + m), because it needs to visit each block and each pizzeria once. This is an improvement over the original solution, which had a time complexity of O(nm), because it had to visit every block for every pizzeria.

#### After the delivery counts have been calculated for each block, the code finds the block with the highest count by iterating through the entire 2D list and keeping track of the maximum count. This has a time complexity of O(n^2), because it needs to visit every element in the list.

## How to improve the code:
#### To improve the time complexity of this step, a more efficient data structure, such as a dictionary or hash table, can be used to store the delivery counts. These data structures have a time complexity of O(1) for finding the maximum value, so using one of them would allow the code to find the maximum delivery count in O(1) time. This would improve the overall time complexity of the solution to O(n + m).

#### To elaborate on this, the code currently uses a 2D list called delivery_counts to store the number of pizzerias that can deliver to each block in the city. To find the block with the most pizzerias that can deliver to it, the code iterates through the entire list and compares the delivery count for each block to a variable called max_count. This process has a time complexity of O(n^2), which means that it may take a long time to complete if the city is very large.

#### To make this process faster, the code could use a different data structure to store the delivery counts. For example, it could use a dictionary or a hash table. These data structures have a time complexity of O(1) for finding the maximum value, which means that they can find the maximum delivery count very quickly. If the code used one of these data structures, the overall time complexity of the solution would be improved to O(n + m), which is faster than the current time complexity of O(n^2 + m).
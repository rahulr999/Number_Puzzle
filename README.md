# Number_Puzzle
Heuristic Method to solve a picture puzzle
Similar to picture puzzle.

The array can be resized to any 2-D matrix in the code but the numbers has to be in the order 0 to (N X M), where N and M are the dimensions of the matrix.

In the array 0 represents the "-" or the swap tile.

The code uses two heuristic values: 1) Gives a constant value 0.
                                    2) calculated the hamiltonian distance and tries to obtain the solution to the given probelm.

The value for "heuristic_value_fun"  can input as 0(for constant function) or 1(for Manhattan distances function)

The code can be run as follows:

        python number_puzzle.py <3 X 3 matrix in the range of 1-8 and "_" without repetation seperated by space>
        
To run the more extensive puzzle algorithm we can comment lines 3 and 4, and uncomment line 5 where we can input the value of any matrix for a solution where the values in the matrix are from 1 to n-1 and "_", where n is the multiple of A and B in A X B matrix without repetition.

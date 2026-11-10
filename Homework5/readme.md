How to Run the Programs:
   - Problem 1:
     python P3 problem1.py

   - Problem 2:
     Ensure vowel_input1.txt through vowel_input4.txt are in the same folder.
     python P2.py

   - Problem 3:
     Ensure longest_seq1.txt through longest_seq6.txt are in the same folder.
     python P3.py

Algorithm Overview:
   - Problem 1 (Binary Search Tree): Implements Node and BST classes supporting 
     addNode, deleteNode, findNode, and a visual ASCII tree printing routine.
   - Problem 2 (Morse Code Vowels): Dynamic Programming from tail to head. 
     dp[i] represents valid vowel combination counts starting at index i.
   - Problem 3 (Alternating Sequence): Dynamic Programming tracking sequence 
     lengths across two alternating arrays while adhering to both index 
     constraint (pos_next > pos_curr) and value constraint (val_next > val_curr).

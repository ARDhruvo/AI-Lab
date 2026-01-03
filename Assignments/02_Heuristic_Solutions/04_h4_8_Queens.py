# 04_h4_8_Queens.py

print("The program has been loaded")

class QueensHeuristic:
    def __init__(self):
        self.hval = 0  # Counter for attacking pairs
    
    def nthel(self, n, lst):
        """Get nth element from list (1-indexed)"""
        if n < 1 or n > len(lst):
            raise IndexError("Index out of bounds")
        return lst[n-1]
    
    def incr_hval(self):
        """Increment counter"""
        self.hval += 1
    
    def do_incr(self, x, y):
        """Check if two queens are in same row"""
        if x == y:
            self.incr_hval()
    
    def chk_incr(self, i, board, x):
        """Check queens to the right of position i"""
        if i >= 8:
            return
        j = i + 1
        y = self.nthel(j, board)
        self.do_incr(x, y)
        self.chk_incr(j, board, x)
    
    def hl(self, i, board):
        """Check horizontal attacks starting from column i"""
        if i > 8:
            return
        x = self.nthel(i, board)
        self.chk_incr(i, board, x)
        self.hl(i + 1, board)
    
    def doup_incr(self, x, y, k1):
        """Check diagonal up attack"""
        x1 = x + k1
        if y == x1:
            self.incr_hval()
    
    def chkup_incr(self, i, board, x, k):
        """Check diagonal up attacks to the right"""
        if i >= 8:
            return
        j = i + 1
        y = self.nthel(j, board)
        k1 = k + 1
        self.doup_incr(x, y, k1)
        self.chkup_incr(j, board, x, k1)
    
    def di_up(self, i, board):
        """Check all diagonal up attacks"""
        if i > 8:
            return
        x = self.nthel(i, board)
        self.chkup_incr(i, board, x, 0)
        self.di_up(i + 1, board)
    
    def dodn_incr(self, x, y, k1):
        """Check diagonal down attack"""
        x1 = x - k1
        if y == x1:
            self.incr_hval()
    
    def chkdn_incr(self, i, board, x, k):
        """Check diagonal down attacks to the right"""
        if i >= 8:
            return
        j = i + 1
        y = self.nthel(j, board)
        k1 = k + 1
        self.dodn_incr(x, y, k1)
        self.chkdn_incr(j, board, x, k1)
    
    def di_dn(self, i, board):
        """Check all diagonal down attacks"""
        if i > 8:
            return
        x = self.nthel(i, board)
        self.chkdn_incr(i, board, x, 0)
        self.di_dn(i + 1, board)
    
    def eval_state(self, board):
        """Main evaluation function - returns number of attacking pairs"""
        self.hval = 0  # Reset counter
        self.hl(1, board)
        self.di_up(1, board)
        self.di_dn(1, board)
        return self.hval

# Alternative simpler version (easier to understand)
def count_attacking_pairs(board):
    """Count attacking pairs of queens (simpler implementation)"""
    attacks = 0
    n = len(board)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Same row attack
            if board[i] == board[j]:
                attacks += 1
            # Diagonal attack: |row1 - row2| == |col1 - col2|
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    
    return attacks

# Main program
if __name__ == "__main__":
    # Create heuristic calculator
    qh = QueensHeuristic()
    
    # Test cases
    test_boards = [
        [1, 2, 3, 4, 5, 6, 7, 8],  # Bad: all in diagonal
        [1, 1, 1, 1, 1, 1, 1, 1],  # Bad: all in same row
        [4, 2, 7, 3, 6, 8, 5, 1],  # Good: solution (0 attacks)
        [1, 5, 8, 6, 3, 7, 2, 4],  # Good: solution (0 attacks)
        [1, 3, 5, 7, 2, 4, 6, 8],  # Mixed: some attacks
    ]
    
    print("Testing 8-Queens Heuristic (h₃)")
    print("=" * 50)
    
    for i, board in enumerate(test_boards, 1):
        print(f"\nTest {i}: {board}")
        
        # Method 1: Prolog-like recursive
        attacks1 = qh.eval_state(board)
        print(f"  Prolog-style attacks: {attacks1}")
        
        # Method 2: Simple double loop
        attacks2 = count_attacking_pairs(board)
        print(f"  Simple method attacks: {attacks2}")
        
        # Verify they match
        if attacks1 == attacks2:
            print("  ✓ Results match")
        else:
            print("  ✗ Results differ!")
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("Interactive Mode: Enter 8 numbers (row positions for columns 1-8)")
    print("Example: '1 5 8 6 3 7 2 4' for a valid solution")
    
    while True:
        try:
            user_input = input("\nEnter board (8 numbers) or 'quit': ")
            if user_input.lower() == 'quit':
                break
            
            board = list(map(int, user_input.split()))
            if len(board) != 8:
                print("Error: Need exactly 8 numbers")
                continue
            
            attacks = count_attacking_pairs(board)
            print(f"Number of attacking pairs: {attacks}")
            
            if attacks == 0:
                print("✓ Valid 8-Queens solution!")
            else:
                print("✗ Not a valid solution")
                
        except ValueError:
            print("Error: Please enter numbers only")
        except Exception as e:
            print(f"Error: {e}")
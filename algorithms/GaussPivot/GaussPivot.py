# Gauss Pivot algorithm for solving linear systems
# Made by Hamza Ba-mohammed

def MatSum(A , B):
    n=len(A)
    m=len(A[0])
    C=[]
    for row in range(n):
        L=[]
        for col in range(m):
            L.append(A[row][col]+B[row][col])
        C.append(L)
    return C

def MatProd(A , B):
    n=len(A)
    m=len(B[0])
    p=len(A[0])
    C=[]
    for row in range(n):
        L=[]
        for col in range(m):
            sum=0
            for k in range(p):
                sum+=A[row][k]*B[k][col]
            L.append(sum)
        C.append(L)
    return C

def MatRowSwap(M ,i ,j):
    for k in range(len(M[0])):
        M[i][k],M[j][k]=M[j][k],M[i][k]
    return

def MatRowDilatation(M , i, coef):
    for j in range(len(M[0])):
        M[i][j]*=coef
    return

def MatRowTransvection(M , i, j, coef):
    for k in range(len(M[0])):
        M[i][k]+=M[j][k]*coef
    return

def MatPrint(M):
    for i in range(len(M)):
        print(M[i])
    print()
    return

def BiMatPrint(M,L):
    for i in range(len(M)):
        print(M[i],L[i])
    print()
    return

def GaussPivot(M , B):
    row=0
    col=0
    n=len(M)
    m=len(M[0])
    while (row<n)and(col<m):
        if M[row][col]!=0 :
            temp=M[row][col]
            A=[]
            for j in range(row+1,n):
                A.append(M[j][col])
            for j in range(row+1,n):
                MatRowDilatation(M,j,temp)
                MatRowDilatation(B,j,temp)
            for j in range(row+1,n):
                MatRowTransvection(M,j,row,(-A[j-row-1]))
                MatRowTransvection(B,j,row,(-A[j-row-1]))
            row+=1
            col+=1
        else :
            ind=False
            for j in range(row+1,n):
                if M[j][col]!=0:
                    MatRowSwap(M,j,row)
                    MatRowSwap(B,j,row)
                    ind=True
                    break
            if not ind :
                col+=1
                row+=1
    return

# Example usage with a 6x6 matrix and a 6x1 vector and a visualization of the steps with pyplot
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import yaml
    import os
    import copy

    # Load config.yaml
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    M_original = config.get('matrix', [[2,1,1,0,0,0],[4,3,3,1,0,0],[8,7,9,5,1,0],[6,7,9,8,6,1],[2,3,4,5,6,7],[4,5,6,7,8,9]])
    B_original = config.get('vector', [[1],[2],[3],[4],[5],[6]])
    pause = config.get('pause', 1)

    # Create copies for manipulation
    M = copy.deepcopy(M_original)
    B = copy.deepcopy(B_original)

    # Initialize plot
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    def display_matrix(M, B, title, pivot_pos=None, modified_rows=None):
        ax.clear()
        ax.axis('off')
        # Format numbers to 2 decimal places for better display
        grid = []
        for r in range(len(M)):
            row = [f"{M[r][c]:.2f}" for c in range(len(M[r]))] + ['|'] + [f"{B[r][0]:.2f}"]
            grid.append(row)
        
        table = ax.table(cellText=grid, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1.2, 1.8)
        
        # Color coding for better visualization
        for i in range(len(M)):
            for j in range(len(M[0]) + 2):  # +2 for separator and B column
                if j == len(M[0]):  # Separator column
                    table[(i, j)].set_facecolor('#CCCCCC')
                elif j == len(M[0]) + 1:  # B column
                    # Highlight modified B values
                    if modified_rows and i in modified_rows:
                        table[(i, j)].set_facecolor('#FFB6C1')  # Light pink for modified B
                    else:
                        table[(i, j)].set_facecolor('#E6F3FF')
                else:  # Matrix columns
                    # Highlight pivot position
                    if pivot_pos and i == pivot_pos[0] and j == pivot_pos[1]:
                        table[(i, j)].set_facecolor('#FF6B6B')  # Red for pivot
                    # Highlight modified rows
                    elif modified_rows and i in modified_rows:
                        table[(i, j)].set_facecolor('#FFE66D')  # Yellow for modified cells
                    # Highlight pivot row
                    elif pivot_pos and i == pivot_pos[0]:
                        table[(i, j)].set_facecolor('#A8E6CF')  # Light green for pivot row
                    # Highlight pivot column
                    elif pivot_pos and j == pivot_pos[1]:
                        table[(i, j)].set_facecolor('#FFD3A5')  # Light orange for pivot column
                    else:
                        table[(i, j)].set_facecolor('#F0F0F0')
        
        ax.set_title(title, fontsize=12, fontweight='bold')
        plt.draw()
        plt.pause(pause)

    print("Initial Matrix and Vector:")
    BiMatPrint(M, B)
    display_matrix(M, B, "Initial Matrix and Vector")

    # Modified GaussPivot with step-by-step visualization
    def GaussPivotVisual(M, B):
        row = 0
        col = 0
        n = len(M)
        m = len(M[0])
        step = 1
        
        while (row < n) and (col < m):
            if M[row][col] != 0:
                pivot = M[row][col]
                display_matrix(M, B, f"Step {step}: Working on pivot at ({row},{col}) = {pivot:.2f}", 
                             pivot_pos=(row, col))
                step += 1
                
                # Store original values for elimination
                A = []
                for j in range(row + 1, n):
                    A.append(M[j][col])
                
                # Perform elimination
                modified_rows = []
                for j in range(row + 1, n):
                    if A[j - row - 1] != 0:  # Only eliminate if not already zero
                        factor = -A[j - row - 1] / pivot
                        # Apply row operations
                        for k in range(len(M[0])):
                            M[j][k] += M[row][k] * factor
                        B[j][0] += B[row][0] * factor
                        modified_rows.append(j)
                        
                        display_matrix(M, B, f"Step {step}: Eliminated row {j} using factor {factor:.2f}", 
                                     pivot_pos=(row, col), modified_rows=[j])
                        step += 1
                
                row += 1
                col += 1
            else:
                # Find a non-zero element to swap
                found = False
                for j in range(row + 1, n):
                    if M[j][col] != 0:
                        MatRowSwap(M, j, row)
                        MatRowSwap(B, j, row)
                        display_matrix(M, B, f"Step {step}: Swapped rows {j} and {row}", 
                                     modified_rows=[j, row])
                        step += 1
                        found = True
                        break
                
                if not found:
                    col += 1
                    if col >= m:
                        row += 1

    GaussPivotVisual(M, B)

    print("Final Matrix and Vector:")
    BiMatPrint(M, B)
    display_matrix(M, B, "Final Upper Triangular Form")
    
    plt.ioff()
    plt.show()

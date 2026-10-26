import sys

def solve_pandemic():
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = f.read().splitlines()
    else:
        lines = sys.stdin.read().splitlines()
        
    if not lines:
        return

    
    N = int(lines[0].strip())
    
    
    infected = set()
    for line in lines[1:]:
        if line.strip():
            r, c = map(int, line.strip().split())
            infected.add((r, c))
            
    
    while True:
        new_infected = set()
        
        
        for r in range(N):
            for c in range(N):
                
                if (r, c) not in infected:
                    infected_neighbors = 0
                    
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if (nr, nc) in infected:
                                infected_neighbors += 1
                                
                    
                    if infected_neighbors >= 2:
                        new_infected.add((r, c))
                        
        
        if not new_infected:
            break
            
        
        infected.update(new_infected)
        
    
    if len(infected) == N * N:
        print("There are no healthy counties left")
    else:
        print("There are healthy counties left")

if __name__ == "__main__":
    solve_pandemic()
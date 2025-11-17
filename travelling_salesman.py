import math
import random

# --- Example: coordinates of cities (you can replace these) ---
cities = {
    0: (0,0),
    1: (2,3),
    2: (5,2),
    3: (6,6),
    4: (8,3)
}

def euclid(a,b):
    (x1,y1),(x2,y2) = a,b
    return math.hypot(x1-x2, y1-y2)

# build distance matrix
n = len(cities)
dist = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = euclid(cities[i], cities[j])

# --- Nearest Neighbor heuristic ---
def nearest_neighbor(start=0):
    tour = [start]
    visited = {start}
    cur = start
    while len(tour) < n:
        # choose nearest unvisited city
        nxt = min((j for j in range(n) if j not in visited), key=lambda j: dist[cur][j])
        tour.append(nxt)
        visited.add(nxt)
        cur = nxt
    tour.append(start)  # return to start
    return tour

def tour_length(t):
    return sum(dist[t[i]][t[i+1]] for i in range(len(t)-1))

# --- Optional 2-opt improvement (short) ---
def two_opt(tour):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                new = best[:i] + best[i:j+1][::-1] + best[j+1:]
                if tour_length(new) < tour_length(best):
                    best = new
                    improved = True
        tour = best
    return best

# Run heuristic
start = 0
nn_tour = nearest_neighbor(start)
print("Nearest Neighbor tour:", nn_tour)
print("Length:", round(tour_length(nn_tour),3))

# Improve with 2-opt
improved = two_opt(nn_tour)
print("2-opt improved tour:", improved)
print("Length after 2-opt:", round(tour_length(improved),3))

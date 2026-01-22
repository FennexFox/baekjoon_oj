n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def get_quadrants(paper):
    quadrants, h = [], len(paper)//2
    halves = [paper[:h], paper[h:]]
    for half in halves:
        quads = [
            [row[:h] for row in half],
            [row[h:] for row in half]
        ]
        quadrants += quads
    return quadrants

def recurvive_cut(paper):
    blue_cells = sum(sum(row) for row in paper)
    paper_area = len(paper)**2
    w = b = 0

    if 0<blue_cells<paper_area:
        quads = get_quadrants(paper)
        for quad in quads:
            cw, cb = recurvive_cut(quad)
            w += cw
            b += cb
    elif blue_cells:
        b += 1
    else:
        w += 1
    
    return [w, b]

print("\n".join(map(str, recurvive_cut(paper))))
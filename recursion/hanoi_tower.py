# Three pegs or towers
# Consider three rings in Tower-1
# Goal is to move all three rings from Tower-1 to Tower-2 
# using Tower-3 as intermediate.

NUM_RINGS = 3

def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg,
                                  to_peg, use_peg):
        if num_rings_to_move > 0:
            # using the intermediary peg as temporary destination
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg,
                                      use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg,
                                      to_peg, from_peg)

    
    # Initialize pegs.
    result = []
    NUM_PEGS = 3
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    for item in result:
        print('steps', item)

if __name__ == '__main__':
    compute_tower_hanoi(3)

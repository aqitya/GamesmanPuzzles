import sys
from puzzlesolver.puzzles import PuzzleManager

def init_data(puzzle_id=None, puzzle_variant=None):
    puzzle_classes = [
        p_cls for p_cls in PuzzleManager.getPuzzleClasses() 
        if puzzle_id is None or p_cls.id == puzzle_id
    ]
    
    if puzzle_id and not puzzle_classes:
        print(f"Error: Puzzle '{puzzle_id}' not found")
        print("Available puzzles:", ", ".join(p.id for p in PuzzleManager.getPuzzleClasses()))
        return

    for p_cls in puzzle_classes:
        # If a specific variant was provided, just do that one.
        # Otherwise, iterate over all standard variants.
        if puzzle_variant is not None:
            variants = [puzzle_variant]
        else:
            if data["TESTING"]:
                variants = p_cls.test_variants
            else:
                variants = p_cls.variants

        for variant in variants:
            s_cls = PuzzleManager.getSolverClass(p_cls.id, variant)
            puzzle = p_cls.generateStartPosition(variant)
            solver = s_cls(puzzle, dir_path=data['DATABASE_DIR'])
            solver.solve(verbose=True)


if __name__ == "__main__":
    import json

    with open("config.json") as json_data_file:
        data = json.load(json_data_file)

    # Get puzzle ID from command line argument if provided
    puzzle_id = sys.argv[1] if len(sys.argv) > 1 else None

    # Get puzzle variant from command line argument if provided
    puzzle_variant = sys.argv[2] if len(sys.argv) > 2 else None

    init_data(puzzle_id, puzzle_variant)

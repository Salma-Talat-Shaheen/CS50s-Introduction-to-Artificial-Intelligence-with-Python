import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty 2d array with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.

        Where the board cells set length is equal to the count (of board
        cells which are mines) then those cells are certainly mines.
        """
        if self.count == len(self.cells):
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.

        Where the count (of board cells which are mines) is zero then
        the board cells are certainly safe.
        """
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine. Must check all cells in the sentence.

        This method should:
            1) If cell is in the sentence, the method should update the 
               sentence so that cell is no longer in the sentence, but still
               represents a logically correct sentence given that cell is 
               known to be a mine.
            2) If cell is not in the sentence, then no action is necessary.
        """
        if cell not in self.cells:
            return

        self.cells.remove(cell)

        if len(self.cells) == 0:
            self.count = 0
        else:
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe. Must check all cells in the sentence.

        This method should:
            1) If cell is in the sentence, the method should update the 
               sentence so that cell is no longer in the sentence, but still
               represents a logically correct sentence given that cell is 
               known to be safe.
            2) If cell is not in the sentence, then no action is necessary.
        """
        if cell not in self.cells:
            return

        self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This method should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)
        self.add_new_sentence_to_knowledge_base(cell, count)
        self.mark_cells_as_safe_or_mines_based_on_knowledge()
        self.add_inferred_sentences_to_knowledge()

    def add_new_sentence_to_knowledge_base(self, cell, count):
        """
        Add a new sentence to the AI's knowledge base by providing all
        of the given cell's neighbouring cells and a count of mines. Checks
        whether the neighbour cells are already marked as a mine or safe before
        adding the sentence.
        """
        neighbours = self.get_neighbours(cell)
        neighbours_copy = copy.deepcopy(neighbours)
        for neighbour in neighbours_copy:
            if neighbour in self.mines:
                neighbours.remove(neighbour)
                count -= 1
            if neighbour in self.safes:
                neighbours.remove(neighbour)

        sentence = Sentence(neighbours, count)
        self.knowledge.append(sentence)
        # print(f"Sentence added for cell {cell} --> neighbours = {neighbours}, count = {count}")

    def mark_cells_as_safe_or_mines_based_on_knowledge(self):
        """
        Marks cells as safe or as mines if it can be concluded based on
        the AI's knowledge base, by iterating over each sentence in the 
        knowledge base. 
        
        If the count of mines in the sentence is 0 then the 
        cells in that sentence are safe. If the count of mines in the sentence
        is equal to the count of cells then they are certainly mines.
        """
        knowledge_copy = copy.deepcopy(self.knowledge)

        for sentence in knowledge_copy:
            is_safe, is_mine = sentence.count == 0, sentence.count == len(sentence.cells)
            if is_safe:
                sentence_cells_copy = sentence.cells.copy()
                for cell in sentence_cells_copy:
                    self.mark_safe(cell) 
                if sentence_cells_copy:
                    print(f"AI marked cells {sentence_cells_copy} as safes.")
            if is_mine:
                sentence_cells_copy = sentence.cells.copy()
                for cell in sentence_cells_copy:
                    self.mark_mine(cell)
                if sentence_cells_copy:
                    print(f"AI marked cells {sentence_cells_copy} as mines.")

    def add_inferred_sentences_to_knowledge(self):
        """
        Add any new sentences to the AI's knowledge base if they
        can be inferred from existing knowledge. Checks whether a 
        sentence is a subset of another sentence. 
        
        If a sentence's cells are a subset of any other sentence's cells
        in the knowledge base, minus the sentence's cells and count from the
        other to leave only the difference in cells and count to add as a new
        inferred sentence.

        For example:
        if sentence_one is {(1, 2), (1, 3), (1, 1), (2, 1)} count=1
        and sentence_two is {(2, 1)} count=1
        then inference is {(1, 2), (1, 3), (1, 1)} count=0
        this inference is now saying there are no mines against these cells 

        The issubset() method returns True if all items in the set 
        exists in the specified set, otherwise it returns False.
        """
        knowledge_copy = copy.deepcopy(self.knowledge)

        for sentence_one in knowledge_copy:
            for sentence_two in knowledge_copy:
                if sentence_one == sentence_two:
                    continue
                if len(sentence_one.cells) == 0:
                    continue
                if len(sentence_two.cells) == 0:
                    continue

                if sentence_one.cells.issubset(sentence_two.cells):
                    sentence = Sentence(
                        cells=sentence_two.cells - sentence_one.cells,
                        count=sentence_two.count - sentence_one.count
                    )
                    if sentence not in self.knowledge:
                        self.knowledge.append(sentence)
                        # print(f"sentence_one={sentence_one.cells} count={sentence_one.count}")
                        # print(f"sentence_two={sentence_two.cells} count={sentence_two.count}")
                        print(f"AI added inferred sentence --> {sentence_two.cells - sentence_one.cells}, count={sentence_two.count - sentence_one.count}")

                if sentence_two.cells.issubset(sentence_one.cells):
                    sentence = Sentence(
                        cells=sentence_one.cells - sentence_two.cells,
                        count=sentence_one.count - sentence_two.count
                    )
                    if sentence not in self.knowledge:
                        self.knowledge.append(sentence)
                        # print(f"sentence_one={sentence_one.cells} count={sentence_one.count}")
                        # print(f"sentence_two={sentence_two.cells} count={sentence_two.count}")
                        print(f"AI added inferred sentence --> {sentence_one.cells - sentence_two.cells}, count={sentence_one.count - sentence_two.count}")

    def get_neighbours(self, cell):
        """
        Returns a set with all of the neighbours for a given cell.
        """
        neighbours = set()

        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == cell:
                    continue

                if abs(i - cell[0]) == 1 and abs(j - cell[1]) == 0:
                    neighbours.add((i, j))
                elif abs(i - cell[0]) == 0 and abs(j - cell[1]) == 1:
                    neighbours.add((i, j))
                elif abs(i - cell[0]) == 1 and abs(j - cell[1]) == 1:
                    neighbours.add((i, j))
                else:
                    continue

        return neighbours

    def make_safe_move(self):
        """
        Returns first known safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made. If no safe move can be guaranteed, 
        the method should return None.

        This method may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        if len(self.safes) > 0:
            for cell in self.safes:
                if cell not in self.moves_made and cell not in self.mines:
                    return cell
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        candidate_moves = []
        
        for i in range(self.height):
            for j in range(self.width):
                move = (i, j)
                if move not in self.moves_made and move not in self.mines:
                    candidate_moves.append(move)

        return random.choice(candidate_moves) if len(candidate_moves) > 0 else None

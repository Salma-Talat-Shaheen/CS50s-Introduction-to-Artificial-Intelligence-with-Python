import sys
import copy

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.

        When a CrosswordCreator object is created, it gets a crossword 
        property that should be a Crossword object. Each CrosswordCreator 
        object also gets a domains property: a dictionary that maps variables 
        to a set of possible words the variable might take on as a value. 
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self) -> None:
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        domains_deepcopy = copy.deepcopy(self.domains)

        for variable in domains_deepcopy:
            variable_length = variable.length

            for word in domains_deepcopy[variable]:
                if len(word) is not variable_length:
                    self.domains[variable].remove(word)

    def revise(self, x: Variable, y: Variable) -> bool:
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        x_overlap, y_overlap = self.crossword.overlaps[x, y]
        revision_was_made = False
        domains_deepcopy = copy.deepcopy(self.domains)

        if x_overlap:
            for x_word in domains_deepcopy[x]:
                match = False
                for y_word in self.domains[y]:
                    if x_word[x_overlap] == y_word[y_overlap]:
                        match = True
                        break
                
                if match:
                    continue
                else:
                    self.domains[x].remove(x_word)
                    revision_was_made = True

        
        return revision_was_made

    def ac3(self, arcs: list = None) -> bool:
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if not arcs:
            queue = self.populate_initial_arc_queue()

        while len(queue) > 0:
            x, y = queue.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                
                for neighbour in self.crossword.neighbors(x):
                    if neighbour != y:
                        queue.append((neighbour, x))

            return True
        
    def populate_initial_arc_queue(self) -> list:
        queue = []

        for variable_x in self.domains:
            for variable_y in self.crossword.neighbors(variable_x):
                if self.crossword.overlaps[variable_x, variable_y] is not None:
                    queue.append((variable_x, variable_y))

        return queue

    def assignment_complete(self, assignment: dict) -> bool:
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.

        An assignment is a dictionary where the keys are Variable objects and the
        values are strings representing the words those variables will take on.

        An assignment is complete if every crossword variable is assigned to a 
        value (regardless of what that value is).
        """
        for variable in self.domains:
            if variable in assignment:
                return True
        
        return False

    def consistent(self, assignment: dict):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.

        An assignment is consistent if it satisfies all of the constraints of 
        the problem: that is to say, all values are distinct, every value is the
        correct length, and there are no conflicts between neighboring variables.
        """
        words = [*assignment.values()] # https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
        all_values_are_distinct = len(words) != len(set(words))

        if all_values_are_distinct:
            return False
        
        for variable in assignment:
            value_is_correct_length = variable.length == len(assignment[variable])
            if not value_is_correct_length:
                return False

        for variable in assignment:
            for neighbour in self.crossword.neighbors(variable):
                if neighbour in assignment:
                    x, y = self.crossword.overlaps[variable, neighbour]
                    if assignment[variable][x] != assignment[neighbour][y]:
                        return False

        return True

    def order_domain_values(self, var: Variable, assignment: dict):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        word_map = {}
        neighbours = self.crossword.neighbors(var)

        for word in self.domains[var]:
            count = 0

            for neighbour in neighbours:
                if neighbour in assignment:
                    continue
                else:
                    x_overlap, y_overlap = self.crossword.overlaps[var, neighbour]
                    for neighbour_word in self.domains[neighbour]:
                        if word[x_overlap] != neighbour_word[y_overlap]:
                            count += 1

            word_map[word] = count

        sorted_variables: dict = {
            k: v for k, v in sorted(
                word_map.items(), 
                key=lambda item: item[1]
            )
        }

        return [*sorted_variables]

    def select_unassigned_variable(self, assignment: dict):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        choice_map = {}

        for variable in self.domains:
            if variable not in assignment:
                choice_map[variable] = self.domains[variable]

        sorted_variables = [
            v for v, k in sorted(
                choice_map.items(),
                key=lambda item: len(item[1]) 
            )
        ]

        return sorted_variables[0]

    def backtrack(self, assignment: dict):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        assignment_is_already_possible = len(assignment) == len(self.domains)
        if assignment_is_already_possible:
            return assignment

        variable = self.select_unassigned_variable(assignment)

        for value in self.domains[variable]:
            assignment_copy = assignment.copy()
            assignment_copy[variable] = value

            if self.consistent(assignment_copy):
                result = self.backtrack(assignment_copy)
                if result is not None:
                    return result

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()

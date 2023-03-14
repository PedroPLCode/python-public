"""Testing some ideas before implementing.
   Not used in main game code."""

def read_text_file(instructions_file):
        """Reads instructions file and shows on the screen."""
        with open(instructions_file) as instr_file_object:
            lines = instr_file_object.readlines()
            for line in lines:
                print(line.strip())

read_text_file('readme.txt')
class Journal:
    """
    A simple class to save and retrieve journal entries.
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def __str__(self) -> str:
        """
        An EOL separated string representation of the journal.
        """
        return "\n".join(self.entries)

    def add_entry(self, text: str) -> None:
        """
        Adds an entry to the journal and updates the entry id.

        :param text: the journal entry
        """
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos: int) -> None:
        """
        Permanently removes an entry from the journal based on its position.

        :param pos: id of the journal entry
        """
        del self.entries[pos]


class PersistenceManager:
    """
    Manages the persistence of any given content by saving it to a file.
    """

    @staticmethod
    def save_to_file(content: str, filename: str):
        """A static method to save text to a provided file path."""
        with open(filename, "w") as f:
            f.write(content)


if __name__ == "__main__":
    # make a journal
    j = Journal()
    j.add_entry("Dear diary...")
    j.add_entry("Today was the best day ever, I ...")
    print(f"Journal entries:\n{j}\n")

    # write the journal to a file
    file = "./journal.txt"
    PersistenceManager.save_to_file(content=str(j), filename=file)

    # verify the entries by printing them to the console
    with open(file) as fh:
        print(fh.read())

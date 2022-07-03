class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        if self.number in range(2,11):
            return f"{self.suit} | {self.number}"
        else:
            diff_val_map = {14:"A",11:"J",12:"Q",13:"K"}
            return f"{self.suit} | {diff_val_map[self.number]}"

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit
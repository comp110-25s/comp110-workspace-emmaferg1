"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        survivor_fish = [fish for fish in self.fish if fish.age <= 3]
        survivor_bears = [bear for bear in self.bears if bears.age <= 5]
        self.fish = survivor_fish
        self.bears = survivor_bears
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                for _ in range(3):
                    self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        survivor_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survivor_bears.append(bear)
        self.bears = survivor_bears
        return None

    def repopulate_fish(self):
        fish_count = (len(self.fish) // 2) * 4
        for _ in range(fish_count):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None

    def repopulate_bears(self):
        bears_count = len(self.bears) // 2
        for _ in range(bears_count):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        return None

    def remove_fish(self, amount: int):
        if amount > 0:
            del self.fish[amount:0]
        return None

class Frame:

    def __init__(self, first_throw: int, second_throw: int):
        self._first_throw = first_throw
        self._second_throw = second_throw
        self._bonus_throw1 = 0
        self._bonus_throw2 = 0

    def score(self) -> int:
        return self._first_throw + self._second_throw + self._bonus_throw1 + self._bonus_throw2

    def get_first_throw(self) -> int:
        return self._first_throw

    def get_second_throw(self) -> int:
        return self._second_throw

    def is_strike(self) -> bool:
        return self._first_throw == 10

    def is_spare(self) -> bool:
        return not self.is_strike() and (self._first_throw + self._second_throw == 10)

    def set_bonus(self, bonus_throw: int) -> None:
        if self._bonus_throw1 == 0:
            self._bonus_throw1 = bonus_throw
        else:
            self._bonus_throw2 = bonus_throw

    def get_first_bonus(self) -> int:
        return self._bonus_throw1
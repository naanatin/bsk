from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) == 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        return self.frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self.frames):
            if i < len(self.frames)-2:
                if frame.is_strike():
                    score += frame.score()
                    score += self.get_frame_at(i+1).get_first_throw()
                    if self.get_frame_at(i+1).is_strike():
                        score += self.get_frame_at(i+2).get_first_throw()
                    else:
                        score += self.get_frame_at(i+1).get_second_throw()
                elif frame.is_spare():
                    score += frame.score() + self.get_frame_at(i+1).get_first_throw()
                else:
                    score += frame.score()

            elif i == len(self.frames)-2:
                if frame.is_strike():
                    score += frame.score()
                    score += self.get_frame_at(i+1).get_first_throw()
                    if self.get_frame_at(i+1).is_strike():
                        score += self.get_frame_at(i+1).get_first_bonus()
                    else:
                        score += self.get_frame_at(i+1).get_second_throw()
                elif frame.is_spare():
                    score += 10 + self.get_frame_at(i + 1).get_first_throw()
                else:
                    score += frame.score()

            elif i == 9:
                score += frame.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self.get_frame_at(len(self.frames)-1).set_bonus(bonus_throw)

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self.get_frame_at(len(self.frames)-1).set_bonus(bonus_throw)

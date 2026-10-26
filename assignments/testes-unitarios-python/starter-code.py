import unittest


def is_passing(score: int) -> bool:
    return score >= 60


def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


class TestGradeHelpers(unittest.TestCase):
    def test_high_score_is_passing(self) -> None:
        self.assertTrue(is_passing(85))


if __name__ == "__main__":
    unittest.main()

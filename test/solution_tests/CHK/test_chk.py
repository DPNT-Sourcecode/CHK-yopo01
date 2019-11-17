from solutions.CHK import chk_solution


class TestSum():
    def test_sum(self):
        assert chk_solution.compute('D') == 15

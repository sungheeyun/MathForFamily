import typing as tp


class ChessBoard:
    """
    Chess board for counting the number of paths.
    To show how programming can be used for counting paths
    for a chess board of large size.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

    def calculate_num_paths(
        self, goal: tp.Tuple[int, int]
    ) -> tp.List[tp.List[int]]:

        count_array_2d: tp.List[tp.List[int]] = [
            [None] * self.height for _ in range(self.width)
        ]

        for col_idx in range(self.width):
            for row_idx in range(self.height):
                self.calc_num_paths_for_one_cell(
                    col_idx, row_idx, goal, count_array_2d
                )

        for row_idx in range(self.height - 1, -1, -1):
            print(
                " ".join(
                    [
                        f"{str(count_array_2d[col_idx][row_idx]):>6}"
                        for col_idx in range(self.width)
                    ]
                )
            )

        return count_array_2d

    def calc_num_paths_for_one_cell(
        self,
        col_idx: int,
        row_idx: int,
        goal: tp.Tuple[int, int],
        count_array_2d: tp.List[tp.List[int]],
    ) -> None:

        val: int
        if (
            col_idx < 0
            or col_idx >= self.width
            or row_idx < 0
            or row_idx >= self.height
        ):
            return 0
        elif count_array_2d[col_idx][row_idx] is not None:
            val = count_array_2d[col_idx][row_idx]
        elif [col_idx, row_idx] == goal:
            val = 1
        else:
            val = self.calc_num_paths_for_one_cell(
                col_idx - 1, row_idx + 1, goal, count_array_2d
            ) + self.calc_num_paths_for_one_cell(
                col_idx + 1, row_idx + 1, goal, count_array_2d
            )

        count_array_2d[col_idx][row_idx] = val

        return count_array_2d[col_idx][row_idx]


if __name__ == "__main__":
    cb: ChessBoard = ChessBoard(20, 20)

    cb.calculate_num_paths([16, 19])

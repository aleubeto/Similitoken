import matplotlib.pyplot as plt
from typing import Tuple, List


class Plotter:
    def plot_matches(
        self, matches: List[Tuple[Tuple[int, int], Tuple[int, int]]], img_name: str
    ):
        """Plot the start and end of matching code blocks as lines in a scatter plot."""
        plt.figure(figsize=(10, 5))

        for match in matches:
            # Drawing vertical lines for matches in the first file
            plt.hlines(
                y=match[1][0], xmin=match[0][0], xmax=match[0][1], color="skyblue", lw=2
            )
            # Drawing vertical lines for matches in the second file
            plt.vlines(
                x=match[0][0], ymin=match[1][0], ymax=match[1][1], color="orange", lw=2
            )

        plt.title("Scatter plot of code matches")
        plt.xlabel("Position in First Code")
        plt.ylabel("Position in Second Code")

        # Set limits with an additional margin
        plt.xlim(
            left=min(plt.xlim()[0], min(match[0][0] for match in matches)) - 1,
            right=max(plt.xlim()[1], max(match[0][1] for match in matches)) + 1,
        )
        plt.ylim(
            bottom=min(plt.ylim()[0], min(match[1][0] for match in matches)) - 1,
            top=max(plt.ylim()[1], max(match[1][1] for match in matches)) + 1,
        )

        plt.grid(True)
        plt.savefig(f"similitoken/tests/output_files/{img_name}.png")

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


if __name__ == "__main__":

    fig: Figure
    axis: Axes

    fig, axis = plt.subplots(figsize=(12, 12))

    axis.text(0.1 - 0.5, 0.7, "MATH", size=70, rotation=5.,
              ha="left", va="center",
              bbox=dict(boxstyle="round",
                       ec="none",
                       fc=(0.4, 0.4, 1.0),
                       )
              )

    axis.text(1.1, 0.5, "is", size=50, rotation=-5.,
             ha="center", va="center",
             bbox=dict(boxstyle="square",
                       ec="none",
                       fc=(1., 0.9, 0.9),
                       )
             )

    axis.text(1.9 + 0.5, 0.3, "FUN", size=70, rotation=5.,
             ha="right", va="center",
             bbox=dict(boxstyle="round",
                       ec="none",
                       fc=(0.4, 0.4, 1.0),
                       )
             )

    axis.axis("off")

    axis.set_xlim(-1, 3.0)
    axis.set_ylim(-1.5, 2.5)

    fig.savefig("math_is_fun.png", dpi=300)

    fig.show()

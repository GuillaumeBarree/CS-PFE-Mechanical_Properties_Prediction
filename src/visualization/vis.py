"""This module define functions to visualize different results."""
# pylint: disable=invalid-name
import os
import matplotlib.pyplot as plt


def plot_y_pred_y_true(y_true, y_pred, path_to_save):
    """Plot y_pred with respect to y_true

    Args:
        y_true (array): Ground truth target values
        y_pred (array): Estimated target values
        path_to_save (str): Path to file
    """
    fig = plt.figure(figsize=(8, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(y_true, y_pred, "bo", label="Estimated target")
    ax.plot([min(y_true), max(y_true)], [min(y_pred), max(y_pred)], "r", label="y=x")

    ax.set_title(
        "MLP: $R_{m}$ estimated with respect to ground truth $R_{m}$", fontsize="large"
    )
    ax.set_xlabel("Ground truth target values")
    ax.set_ylabel("Estimated target values")
    ax.legend(loc="best")

    plt.savefig(os.path.join(path_to_save, "y_pred_y_true.png"))
    plt.show()


def plot_all_y_pred_y_true(y_true, y_pred, path_to_save):
    """Plot all y_preds with respect to y_trues

    Args:
        y_true (dict): Ground truth target values
        y_pred (dict): Estimated target values
        path_to_save (str): Path to file
    """
    fig, ax = plt.subplots(2, 2, figsize=(10, 5))
    fig.tight_layout(pad=3)

    ax[0, 0].plot(y_true["train"], y_pred["train"], "bo", label="Estimated target")
    ax[0, 0].plot(
        [min(y_true["train"]), max(y_true["train"])],
        [min(y_pred["train"]), max(y_pred["train"])],
        "r",
        label="y=x",
    )

    ax[0, 0].set_title(
        "Train: $R_{m}$ estimated with respect to ground truth $R_{m}$",
        fontsize="large",
    )
    ax[0, 0].set_xlabel("Ground truth target values")
    ax[0, 0].set_ylabel("Estimated target values")
    ax[0, 0].legend()

    ax[0, 1].plot(y_true["valid"], y_pred["valid"], "bo", label="Estimated target")
    ax[0, 1].plot(
        [min(y_true["valid"]), max(y_true["valid"])],
        [min(y_pred["valid"]), max(y_pred["valid"])],
        "r",
        label="y=x",
    )

    ax[0, 1].set_title(
        "Valid: $R_{m}$ estimated with respect to ground truth $R_{m}$",
        fontsize="large",
    )
    ax[0, 1].set_xlabel("Ground truth target values")
    ax[0, 1].set_ylabel("Estimated target values")
    ax[0, 1].legend()

    ax[1, 0].plot(y_true["test"], y_pred["test"], "bo", label="Estimated target")
    ax[1, 0].plot(
        [min(y_true["test"]), max(y_true["test"])],
        [min(y_pred["test"]), max(y_pred["test"])],
        "r",
        label="y=x",
    )

    ax[1, 0].set_title(
        "Test: $R_{m}$ estimated with respect to ground truth $R_{m}$", fontsize="large"
    )
    ax[1, 0].set_xlabel("Ground truth target values")
    ax[1, 0].set_ylabel("Estimated target values")
    ax[1, 0].legend()

    ax[1, 1].plot(y_true["train"], y_pred["train"], "bo", label="Train")
    ax[1, 1].plot(y_true["valid"], y_pred["valid"], "ro", label="Valid")
    ax[1, 1].plot(y_true["test"], y_pred["test"], "go", label="Test")

    ax[1, 1].set_title(
        "MLP: $R_{m}$ estimated with respect to ground truth $R_{m}$", fontsize="large"
    )
    ax[1, 1].set_xlabel("Ground truth target values")
    ax[1, 1].set_ylabel("Estimated target values")
    ax[1, 1].legend()

    plt.savefig(os.path.join(path_to_save, "y_pred_y_true.png"))
    plt.show()
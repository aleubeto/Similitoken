import matplotlib.pyplot as plt


def plot_matches(matches, len1, len2, img_name: str):
    plt.figure(figsize=(10, 5))
    x = [m[0] for m in matches]
    y = [m[1] for m in matches]
    # sizes = [m[2] * 10 for m in matches]  # Aumenta el tamaño para mejor visualización

    plt.scatter(x, y)
    plt.title("Scatter plot of code matches")
    plt.xlabel("Position in First Code")
    plt.ylabel("Position in Second Code")
    plt.xlim(0, len1)
    plt.ylim(0, len2)
    plt.savefig(f"similitoken/tests/output_files/{img_name}.png")

import sys


def solve():
    # Read all tokens from standard input
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    # Read number of queries and Peygir's reply interval
    q = int(next(iterator))
    t = int(next(iterator))

    cycle = t + 1
    # Mapping remainder to the person's name
    other_members = ("Morshed", "Tannaz", "Jeddy")

    output = []

    for _ in range(q):
        chat_num = int(next(iterator))

        # Peygir talks at positions: 1, (t + 2), (2t + 3), ...
        if (chat_num - 1) % cycle == 0:
            output.append("Peygir")
        else:
            # Count how many messages Peygir has sent before this chat_num
            peygir_count = (chat_num - 1) // cycle + 1
            # Index among the remaining 3 people (1-based)
            non_peygir_idx = chat_num - peygir_count
            output.append(other_members[non_peygir_idx % 3])

    # Output all results efficiently
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == '__main__':
    solve()

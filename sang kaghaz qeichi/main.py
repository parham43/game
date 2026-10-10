import random

DATABASE_FILE = "database.txt"


def save_result(player_name, player_choice, computer_choice, result):
    with open(DATABASE_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"{player_name},{player_choice},{computer_choice},{result}\n"
        )


def get_result(player, computer):
    if player == computer:
        return "Draw"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "Win"

    return "Lose"


def main():
    print("=== Rock Paper Scissors ===")

    player_name = input("Enter your name: ").strip()

    if not player_name:
        player_name = "Player"

    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Exit")

        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Thanks for playing!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            continue

        player_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)

        result = get_result(player_choice, computer_choice)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}")

        save_result(
            player_name,
            player_choice,
            computer_choice,
            result
        )

        print("Game result saved to database.txt")


if __name__ == "__main__":
    main()
import json


def top_retweeted(data: dict) -> list:
    pass


def top_users(data: dict) -> list:
    pass


def top_days(data: dict) -> list:
    pass


def top_hashtags(data: dict) -> list:
    pass


def main():
    with open("data.json", "rb") as file:
        data = json.load(file)

    print(
        "================================================\n"
        "Seleccione el número de la opción que desea ver:\n"
        "------------------------------------------------\n"
        "1) Top 10 tweets más retweeted.\n"
        "2) Top 10 usuarios según cantidad de tweets.\n"
        "3) Top 10 días donde hay más tweets.\n"
        "4) Top 10 hashtags más usados.\n"
        "================================================"
    )

    while True:
        try:
            option = int(input("> "))
        except ValueError:
            print("La opción ingresada no es un número.")
            continue

        if option not in {1, 2, 3, 4}:
            print("La opción ingresada no es válida.")
        else:
            break

    if option == 1:
        selection = top_retweeted(data)
    elif option == 2:
        selection = top_users(data)
    elif option == 3:
        selection = top_days(data)
    elif option == 4:
        selection = top_hashtags(data)

    print(
        "\n"
        "================================================\n"
        "                   TOP 10\n"
        "------------------------------------------------"
    )

    for idx, element in enumerate(selection):
        print(f"{idx + 1}) {element}")

    print("================================================")


if __name__ == "__main__":
    main()

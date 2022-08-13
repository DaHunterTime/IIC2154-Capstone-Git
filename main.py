import json


def top_retweeted(data: list) -> list:
    top10 = sorted(data, key=lambda x: x["retweetCount"])[:10]
    return top10


def top_users(data: list) -> list:
    top_users = {}

    for element in data:
        top_users[element["user"]["username"]] = top_users.get(element["user"]["username"], 0) + 1

    user_data = []

    for key in top_users:
        user_data.append({"url": key, "count": top_users[key]})

    top10 = sorted(data, key=lambda x: x["count"])[:10]
    return top10


def top_days(data: list) -> list:
    pass


def top_hashtags(data: list) -> list:
    pass


def main():
    with open("farmers-protest-tweets-2021-03-5.json", "rb") as file:
        data = []

        for line in file:
            data.append(json.loads(line))

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
        print(f"{idx + 1}) {element['url']}")

    print("================================================")


if __name__ == "__main__":
    main()

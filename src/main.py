from part_one import PartOne
from part_two import PartTwo


def main():
    print("Qual parte do projeto deseja rodar?\n")
    print("[1] Parte 1\n")
    print("[2] Parte 2\n")

    part = int(input("Digite aqui: "))

    if (part == 1):
        Part = PartOne()
    elif (part == 2):
        Part = PartTwo()
    else
    return
    Part.run()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Program closed by User!")

    finally:
        print("Program finished!")

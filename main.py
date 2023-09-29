from sum_of_polinoms_md import *


def main():
    first_exp = LinkedListCls()
    second_exp = LinkedListCls()

    first_exp.append(TermCls(4, 5))
    first_exp.append(TermCls(3, 2))
    first_exp.append(TermCls(-7, 1))
    first_exp.append(TermCls(8, 0))

    second_exp.append(TermCls(2, 4))
    second_exp.append(TermCls(6, 2))
    second_exp.append(TermCls(7, 1))

    result = sum_pol_func(first_exp, second_exp)
    print(read_exp(result))


if __name__ == "__main__":
    main()

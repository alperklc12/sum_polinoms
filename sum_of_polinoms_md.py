from single_link_list_md import LinkedListCls, TermCls


def sum_pol_func(first, second):
    new_exp = LinkedListCls()
    i = first.head
    j = second.head
    power = None
    coefficient = None
    k = None
    while i and j:
        if i.power == j.power:
            coefficient = i.coefficient + j.coefficient
            power = i.power
            i = i.next
            j = j.next
        else:
            if i.power > j.power:
                coefficient = i.coefficient
                power = i.power
                i = i.next
            else:
                coefficient = j.coefficient
                power = j.power
                j = j.next
        if coefficient != 0:
            new_trm = TermCls(coefficient, power)
            new_exp.append(new_trm)
    if i is None:
        k = j
    else:
        k = i

    while k:
        new_trm = TermCls(k.coefficient, k.power)
        new_exp.append(new_trm)
        k = k.next
    return new_exp


def read_exp(exp_lst):
    current = exp_lst.head
    text = ''
    while current:
        if current.coefficient > 0:
            text += f'+{current}'
        else:
            text += f'{current}'
        current = current.next
    if text.startswith('+'):
        text = text[1:]
    return text

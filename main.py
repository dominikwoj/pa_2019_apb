import numpy as np


def apb(n):
    lenght_n = len(str(n))
    out = []
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            # budowa wektorów
            # dodanie wektorów
            # sprawdzenie wyników -> określenie czy liczba jest poprawna
            i_np = np.array(list(str(i).zfill(lenght_n)), dtype=np.int64)
            j_np = np.array(list(str(j).zfill(lenght_n)), dtype=np.int64)
            k_np = i_np + j_np
            v = int(''.join(np.array(k_np, dtype=str)))
            if v == n:
                out.append(n)
                # print(i_np, j_np, k_np, v)

    print(len(out))


if __name__ == '__main__':
    apb(112)

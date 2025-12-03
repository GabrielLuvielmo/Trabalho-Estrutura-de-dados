# src/sorting.py

def insertion_sort(arr, key=lambda x: x, reverse=False):
    """
    O(n^2), estável. Ordena retornando uma NOVA lista.
    """
    res = arr[:]  # copia
    n = len(res)
    for i in range(1, n):
        current = res[i]
        j = i - 1
        # compara usando key + reverse
        while j >= 0 and (
            (key(res[j]) < key(current)) if reverse
            else (key(res[j]) > key(current))
        ):
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = current
    return res


def merge_sort(arr, key=lambda x: x, reverse=False):
    """
    O(n log n), estável. Retorna NOVA lista ordenada.
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key=key, reverse=reverse)
    right = merge_sort(arr[mid:], key=key, reverse=reverse)

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (key(left[i]) > key(right[j])) if reverse else (key(left[i]) <= key(right[j])):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# -------------------- Cálculo de pontos --------------------

def calcular_pontos_por_time(match_results):
    """
    match_results: dict nome -> {"wins": int, "draws": int, "losses": int}
    Retorna dict nome -> pontos.
    Vitória = 3 pts, empate = 1 pt, derrota = 0.
    """
    pontos = {}
    for name, stats in match_results.items():
        wins = stats.get("wins", 0)
        draws = stats.get("draws", 0)
        pontos[name] = wins * 3 + draws * 1
    return pontos


def ordenar_por_pontos(pontos_dict, method="merge"):
    """
    pontos_dict: {name: pontos}
    method: 'merge' or 'insertion'
    Retorna lista de tuples (name, pontos) em ordem
    DECRESCENTE de pontos.
    """
    items = list(pontos_dict.items())
    if method == "merge":
        ordered = merge_sort(items, key=lambda x: x[1], reverse=True)
    else:
        ordered = insertion_sort(items, key=lambda x: x[1], reverse=True)
    return ordered

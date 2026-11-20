import math
from fractions import Fraction

THALAMS = {
    "Adi": 8,
    "Rupakam": 3,
    # "Rettakalai Adi": 16,
    # "Rettakalai Rupakam": 6,
} # chapus are omitted for simplicity

NADAIS = {
    "Tisram": 3,
    "Chatusram": 4,
    "Khandam": 5,
    "Mel Kalam Tisram": 6
}

def display_result(nadais, m_korvai):
    print(
        f"Nadais {nadais[0]}, {nadais[1]}, and {nadais[2]} \t " \
            f"Maatras: {m_korvai}\t" \
            f"Avardhanams: {(m_korvai * multiplier) / ak_thalam}"
    )

def display_header(thalam):
    print(f"\n\n-------------------- {thalam} --------------------")

nadai_pairings = [
    (n1, n2, n3)
    for n1 in NADAIS.values() for n2 in NADAIS.values() for n3 in NADAIS.values()
    if n1 < n2 and n1 < n3 and n2 < n3 and math.gcd(n1, n2, n3) == 1
]

for thalam in THALAMS: # iterate over thalams
    ak_thalam = THALAMS[thalam]
    display_header(thalam)

    for (n1, n2, n3) in nadai_pairings:                                                 # iterate over nadai pairings
        multiplier = Fraction(1, n1) + Fraction(1, n2) + Fraction(1, n3)                # fractions prevent decimal truncation
        lcm = math.lcm(n1, n2, n3)
        m_korvai = int(lcm * (ak_thalam / math.gcd(ak_thalam, int(lcm * multiplier))))  # solution to the fundamental theorem of multi-nadai korvais
        display_result([n1, n2, n3], m_korvai)
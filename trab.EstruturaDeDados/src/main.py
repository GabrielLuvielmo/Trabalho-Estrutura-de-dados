from datetime import datetime
from pathlib import Path
import csv
import sys

from dataStructs import Team, Match
from sorting import calcular_pontos_por_time, ordenar_por_pontos
from avl import AVLPointsTree


try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Caminhos
DATA_PATH = Path("data") / "results.csv"

OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "matches_summary.csv"

REQUIRED_FIELDS = [
    "date",
    "home_team",
    "away_team",
    "home_score",
    "away_score",
    "tournament",
    "city",
    "country",
    "neutral",
]


def parse_bool_neutral(value: str) -> bool:
    if value is None:
        return False
    v = value.strip().lower()
    return v == "true"


def load_matches_from_csv(csv_path: Path):
    matches = []
    linhas_faltantes = []

    with csv_path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader, start=2):  
            # 1) Verifica campos obrigatórios
            if any(
                (row.get(field) is None or row.get(field) == "")
                for field in REQUIRED_FIELDS
            ):
                linhas_faltantes.append({
                    "index": i,
                    "content": row,
                    "reason": "campo obrigatório vazio/ausente",
                })
                continue

            try:
                # 2) Converte tipos
                date = datetime.strptime(row["date"], "%Y-%m-%d")

                home_score = int(row["home_score"])
                away_score = int(row["away_score"])

                home_team = Team(row["home_team"], home_score)
                away_team = Team(row["away_team"], away_score)

                neutral = parse_bool_neutral(row["neutral"])

                match = Match(
                    date=date,
                    home_team=home_team,
                    away_team=away_team,
                    tournament=row["tournament"],
                    city=row["city"],
                    country=row["country"],
                    neutral=neutral,
                )

                matches.append(match)

            except Exception as e:
                linhas_faltantes.append({
                    "index": i,
                    "content": row,
                    "reason": f"erro de conversão: {type(e).__name__}",
                })
                continue

    return matches, linhas_faltantes


# -------- Etapa 6: salvar matches_summary.csv --------
def save_matches_summary(matches):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

  
        writer.writerow(["year", "country", "home_team", "away_team", "score"])

        for match in matches:
           
            year = match.date.year
            score_str = f"{match.home_team.score}-{match.away_team.score}"

            writer.writerow([
                year,
                match.country,
                match.home_team.name,
                match.away_team.name,
                score_str,
            ])

    print(f"\nArquivo matches_summary gerado em: {OUTPUT_FILE}")


# -------- Etapa 4: calcular vitórias/empates/derrotas --------
def calcular_estatisticas_times(matches):
    """
    matches: lista de Match
    Retorna dict:
        nome -> {"wins": int, "draws": int, "losses": int}
    """
    stats = {}

    def ensure_team(name):
        if name not in stats:
            stats[name] = {"wins": 0, "draws": 0, "losses": 0}

    for m in matches:
        home = m.home_team.name
        away = m.away_team.name
        hs = m.home_team.score
        as_ = m.away_team.score

        ensure_team(home)
        ensure_team(away)

        if hs > as_:
            stats[home]["wins"] += 1
            stats[away]["losses"] += 1
        elif hs < as_:
            stats[away]["wins"] += 1
            stats[home]["losses"] += 1
        else:
            stats[home]["draws"] += 1
            stats[away]["draws"] += 1

    return stats


def main():
    matches, linhas_faltantes = load_matches_from_csv(DATA_PATH)

    print("=== RESUMO DA CARGA DO CSV ===")
    print(f"Total de jogos válidos gravados: {len(matches)}")
    print(f"Total de linhas problemáticas   : {len(linhas_faltantes)}")

    if linhas_faltantes:
        print("\nLinhas problemáticas encontradas (primeiras 5):")
        for linha in linhas_faltantes[:5]:
            print(f"- Linha {linha['index']}: motivo={linha['reason']}")

    # -------- Etapa 6: salvar resumo de partidas --------
    save_matches_summary(matches)

    # -------- Etapa 4: Ordenação por pontos --------
    match_results = calcular_estatisticas_times(matches)
    pontos = calcular_pontos_por_time(match_results)


    ordered_merge = ordenar_por_pontos(pontos, method="merge")

    ordered_insertion = ordenar_por_pontos(pontos, method="insertion")

    # Top 10 com mais pontos (maiores)
    top10_mais = ordered_merge[:10]

    # Top 10 com menos pontos (menores)
    top10_menos = list(reversed(ordered_merge[-10:]))

    print("\n=== TOP 10 SELEÇÕES COM MAIS PONTOS (merge sort) ===")
    for name, pts in top10_mais:
        print(f"{name}: {pts} pontos")

    print("\n=== TOP 10 SELEÇÕES COM MENOS PONTOS (merge sort) ===")
    for name, pts in top10_menos:
        print(f"{name}: {pts} pontos")


    # -------- Etapa 5: AVL por pontos --------
    avl = AVLPointsTree()
    for name, pts in ordered_merge:
        avl.insert(name, pts)

    print("\n=== AVL POR PONTOS ===")
    print("Altura da árvore AVL:", avl.height())
    print("Raiz da árvore AVL  :", avl.root())
   


if __name__ == "__main__":
    main()

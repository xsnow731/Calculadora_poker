import tkinter as tk
from tkinter import ttk
import random
from itertools import combinations
from collections import Counter

# =============================
# BARALHO
# =============================
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
RANK_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}
RED_SUITS = {"♥", "♦"}

DECK = [f"{r}{s}" for s in SUITS for r in RANKS]

# =============================
# AVALIAÇÃO DE MÃOS (REAL)
# =============================
def evaluate_5(cards):
    ranks = sorted([RANK_VALUE[c[:-1]] for c in cards], reverse=True)
    suits = [c[-1] for c in cards]

    counts = Counter(ranks)
    ordered = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    count_values = sorted(counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0] - 5, -1)) or ranks == [14, 5, 4, 3, 2]

    if is_straight and is_flush:
        return (8, ranks)
    if count_values == [4, 1]:
        return (7, [ordered[0][0], ordered[1][0]])
    if count_values == [3, 2]:
        return (6, [ordered[0][0], ordered[1][0]])
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, ranks)
    if count_values == [3, 1, 1]:
        return (3, [ordered[0][0]] + sorted([o[0] for o in ordered[1:]], reverse=True))
    if count_values == [2, 2, 1]:
        return (2, [ordered[0][0], ordered[1][0], ordered[2][0]])
    if count_values == [2, 1, 1, 1]:
        return (1, [ordered[0][0]] + sorted([o[0] for o in ordered[1:]], reverse=True))
    return (0, ranks)

def best_hand(cards):
    return max(evaluate_5(c) for c in combinations(cards, 5))

# =============================
# MONTE CARLO
# =============================
def calculate_win_rate(my_hand, board, players, simulations=4000):
    wins = 0
    ties = 0

    for _ in range(simulations):
        deck = [c for c in DECK if c not in my_hand + board]
        random.shuffle(deck)

        opponents = []
        for i in range(players - 1):
            opponents.append(deck[i * 2:(i + 1) * 2])

        idx = (players - 1) * 2
        needed = 5 - len(board)
        final_board = board + deck[idx:idx + needed]

        my_best = best_hand(my_hand + final_board)
        opp_best = [best_hand(o + final_board) for o in opponents]

        if all(my_best > r for r in opp_best):
            wins += 1
        elif any(my_best == r for r in opp_best):
            ties += 1

    return round(((wins + ties * 0.5) / simulations) * 100, 2)

# =============================
# VISUAL + DICAS
# =============================
def winrate_to_color(rate):
    rate = max(0, min(rate, 100)) / 100
    r = int(255 * (1 - rate))
    g = int(255 * rate)
    return f"#{r:02x}{g:02x}00"

def betting_advice(rate):
    if rate < 20:
        return "❌ Desistir (Fold)"
    elif rate < 40:
        return "⚠️ Check / Call pequeno"
    elif rate < 60:
        return "💰 Apostar"
    elif rate < 80:
        return "🔥 Apostar forte"
    else:
        return "🟢 ALL IN"

# =============================
# APP
# =============================
class PokerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Odds Calculator")

        self.stage = "HAND"
        self.my_hand = []
        self.board = []
        self.used = set()

        self.build_ui()

    def build_ui(self):
        self.main = tk.Frame(self.root, bg="#f0f0f0")
        self.main.pack(fill="both", expand=True, padx=10, pady=10)

        top = ttk.Frame(self.main)
        top.pack()

        ttk.Label(top, text="Jogadores:").pack(side="left")
        self.players = tk.IntVar(value=2)
        ttk.Spinbox(top, from_=2, to=8, width=5,
                    textvariable=self.players,
                    command=self.update_odds).pack(side="left")

        self.stage_label = ttk.Label(self.main, text="Etapa: Sua MÃO (2 cartas)",
                                     font=("Arial", 12, "bold"))
        self.stage_label.pack(pady=5)

        self.odds_label = ttk.Label(self.main, text="Chance de vitória: -- %",
                                    font=("Arial", 12))
        self.odds_label.pack()

        self.advice_label = ttk.Label(self.main, text="Dica: --",
                                      font=("Arial", 12, "bold"))
        self.advice_label.pack(pady=5)

        deck_frame = ttk.LabelFrame(self.main, text="Baralho")
        deck_frame.pack()

        for row, suit in enumerate(SUITS):
            for col, rank in enumerate(RANKS):
                card = f"{rank}{suit}"
                color = "red" if suit in RED_SUITS else "black"

                btn = tk.Button(deck_frame, text=card, fg=color, width=4,
                                command=lambda c=card: self.select_card(c))
                btn.grid(row=row, column=col, padx=2, pady=2)

        self.status = ttk.Label(self.main, text="")
        self.status.pack(pady=5)

        ttk.Button(self.main, text="Resetar", command=self.reset).pack(pady=5)

    def select_card(self, card):
        if card in self.used:
            return

        if self.stage == "HAND":
            self.my_hand.append(card)
            if len(self.my_hand) == 2:
                self.stage = "FLOP"
                self.stage_label.config(text="Etapa: FLOP (3 cartas)")
        elif self.stage == "FLOP":
            self.board.append(card)
            if len(self.board) == 3:
                self.stage = "TURN"
                self.stage_label.config(text="Etapa: TURN (1 carta)")
        elif self.stage == "TURN":
            self.board.append(card)
            self.stage = "RIVER"
            self.stage_label.config(text="Etapa: RIVER (1 carta)")
        elif self.stage == "RIVER":
            self.board.append(card)
            self.stage = "FINAL"
            self.stage_label.config(text="Rodada Final")

        self.used.add(card)
        self.status.config(text=f"Mão: {self.my_hand} | Mesa: {self.board}")
        self.update_odds()

    def update_odds(self):
        if len(self.my_hand) == 2:
            rate = calculate_win_rate(self.my_hand, self.board, self.players.get())

            self.odds_label.config(text=f"Chance de vitória: {rate}%")
            self.advice_label.config(text=f"Dica: {betting_advice(rate)}")
            self.main.config(bg=winrate_to_color(rate))

    def reset(self):
        self.stage = "HAND"
        self.my_hand.clear()
        self.board.clear()
        self.used.clear()

        self.stage_label.config(text="Etapa: Sua MÃO (2 cartas)")
        self.odds_label.config(text="Chance de vitória: -- %")
        self.advice_label.config(text="Dica: --")
        self.status.config(text="")
        self.main.config(bg="#f0f0f0")

# =============================
# RUN
# =============================
if __name__ == "__main__":
    root = tk.Tk()
    PokerApp(root)
    root.mainloop()

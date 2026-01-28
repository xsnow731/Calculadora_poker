🃏 Calculadora de Poker – Poker Odds Calculator

Aplicação desktop em Python que calcula probabilidades reais de vitória no Texas Hold’em, em tempo real, com interface gráfica intuitiva, visual adaptativo e dicas de apostas automáticas.

Ideal para estudo, treino e análise de decisões no poker.

🎯 Funcionalidades

✅ Seleção por etapas do jogo

Mão do jogador (2 cartas)

Flop (3 cartas)

Turn (1 carta)

River (1 carta)

✅ Cálculo contínuo de chances de vitória

Simulação Monte Carlo

Avaliação real de mãos (7 cartas → melhor combinação de 5)

Suporte de 2 a 8 jogadores

✅ Interface visual inteligente

Cartas organizadas por naipe em cada linha

Cores reais dos naipes:

♥ ♦ vermelho

♠ ♣ preto

Cor da janela varia conforme a chance de vitória:

🔴 Vermelho → situação ruim

🟡 Amarelo → situação equilibrada

🟢 Verde → situação dominante

✅ Dicas automáticas de aposta

Fold

Check / Call

Aposta

Aposta forte

All in

🧠 Lógica de decisão (dicas de aposta)
Chance de vitória	Sugestão
< 20%	❌ Desistir (Fold)
20% – 40%	⚠️ Check / Call pequeno
40% – 60%	💰 Apostar
60% – 80%	🔥 Apostar forte
> 80%	🟢 ALL IN

⚠️ As dicas são heurísticas realistas, voltadas para estudo e tomada de decisão padrão (não é GTO perfeito).

🛠️ Tecnologias utilizadas

Python 3

Tkinter (interface gráfica)

Monte Carlo Simulation

Algoritmo real de avaliação de mãos de poker

PyInstaller (para gerar executável)

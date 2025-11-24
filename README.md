Simulador de Equidade no Texas Hold'em (Monte Carlo)

Este projeto realiza uma simulação de Monte Carlo para estimar a equidade (probabilidade de vitória, empate e derrota) de uma mão de Texas Hold'em contra um número configurável de oponentes.

A simulação utiliza a biblioteca treys, uma das mais rápidas e eficientes para avaliação de mãos de pôquer.

📌 Funcionalidades

Cálculo aproximado da equidade de uma mão inicial.

Suporte para qualquer número de oponentes.

Simulação configurável (padrão: 50.000 rodadas).

Interface simples via terminal.

Resultados mostrados em porcentagem: Vitória, Empate, Derrota.

🧠 Como funciona

A simulação segue os seguintes passos:

O usuário insere suas duas cartas no formato ValorNaipe
Exemplos:

As → Ás de espadas

Kd → Rei de ouros

Th → Dez de copas

7c → Sete de paus

Em cada simulação:

O baralho é criado e as cartas do jogador são removidas.

Cada oponente recebe duas cartas aleatórias.

A mesa (board) recebe 5 cartas aleatórias.

O avaliador (Evaluator) determina a força de cada mão.

Verifica-se se o jogador venceu, empatou ou perdeu.

Ao final, as probabilidades são computadas e exibidas.

📦 Instalação
1. Instale a biblioteca treys:
pip install treys

2. Execute o arquivo Python normalmente:
python simulador_holdem.py

▶️ Como usar

Quando você rodar o script, será solicitado:

Digite suas duas cartas no formato: ValorNaipe
Exemplo: As, Kd, Th, 7c

Digite a primeira carta:
Digite a segunda carta:
Digite o número de adversários:


Exemplo de entrada:

Primeira carta: As
Segunda carta: Kd
Adversários: 3


Exemplo de saída:

Probabilidade aproximada em %:
Vitória: 32.8%
Empate: 4.12%
Derrota: 63.08%

📂 Código Completo

O código principal do simulador é responsável por:

Criar o baralho

Distribuir mãos

Avaliar resultados com a biblioteca treys

Mostrar as probabilidades finais

(Seu código original entra aqui, se desejado.)

📈 Precisão da Simulação

Simulação padrão: 50.000 rodadas

Quanto maior o número de simulações, mais preciso será o resultado.

Para máxima precisão, recomenda-se usar 200.000 a 1.000.000 simulações, caso sua máquina permita.

📝 Observações

O método Monte Carlo fornece resultados aproximados, mas muito próximos do valor real.

O formato das cartas deve sempre seguir ValorNaipe:

Valores: A K Q J T 9 8 7 6 5 4 3 2

Naipes: s h d c (spades, hearts, diamonds, clubs)

🤝 Contribuições

Fique à vontade para:

Melhorar o código

Criar interface gráfica

Adicionar gráficos de distribuição de resultados

Publicar no GitHub com licença MIT

import chess
import time

board = chess.Board()
print(board)

# Estudantes: . . . 

# Pesos de cada peça em cada posição do tabuleiro
# Esses dados foram retirados desse site: https://www.chessprogramming.org/Piece-Square_Tables

# Peão
pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
  ]

# Cavalo
knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
  ]

# Bispo
bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
  ]

# Torre
rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
  ]

# Rainha
queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
  ]

# Rei
kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
  ]

# Avalia os scores de cada peça do tabuleiro
def avaliar_tabuleiro():
  if board.is_checkmate():
    if board.turn:
      return -9999
    else:
      return 9999
        
  if board.is_stalemate():
    return 0
    
  if board.is_insufficient_material():
    return 0

  
  #TODO . . . 
  wp = len(board.pieces(chess.PAWN, chess.WHITE))
  bp = len(board.pieces(chess.PAWN, chess.BLACK))
  wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
  bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
  wb = len(board.pieces(chess.BISHOP, chess.WHITE))
  bb = len(board.pieces(chess.BISHOP, chess.BLACK))
  wr = len(board.pieces(chess.ROOK, chess.WHITE))
  br = len(board.pieces(chess.ROOK, chess.BLACK))
  wq = len(board.pieces(chess.QUEEN, chess.WHITE))
  bq = len(board.pieces(chess.QUEEN, chess.BLACK))
  material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
  
  pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
  
  knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
  
  bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])
  
  rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])
  
  queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])
  
  kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                         for i in board.pieces(chess.KING, chess.BLACK)])
  eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
    return eval
  else:
    return -eval

"""
Monta uma lista de movimento e analisa os scores resultantes desses movimentos
"""
def quiesce(alpha, beta):
  stand_pat = avaliar_tabuleiro()
  if stand_pat >= beta:
    return beta
  if alpha < stand_pat:
    alpha = stand_pat
    
  for move in board.legal_moves:
    if board.is_capture(move):
      board.push(move)
      score = -quiesce(-beta, -alpha)
      board.pop()
      if (score >= beta):
        return beta
      if (score > alpha):
        alpha = score
        
  return alpha
    


"""
Algoritmo alpha_beta aprendido em sala de aula
"""
def alphabeta(alpha, beta, depthleft):
  bestscore = -9999
  if (depthleft == 0):
    return quiesce(alpha, beta)
  for move in board.legal_moves:
    board.push(move)
    score = -alphabeta(-beta, -alpha, depthleft - 1)
    board.pop()
    if (score >= beta):
      return score
    if (score > bestscore):
      bestscore = score
    if (score > alpha):
      alpha = score
  return bestscore

"""    
Seleciona o melhor movimento com base no algoritmo alpha-beta aprendido em sala de aula,
passando como parametro a profundidade
"""
def selecionar_movimento(depth):
  melhorMovimento = chess.Move.null()
  melhorValor = -99999
  alpha = -100000
  beta = 100000

  for movimento in board.legal_moves:
    board.push(movimento)
    valorBoard = -alphabeta(-beta, -alpha, depth - 1)
    if valorBoard > melhorValor:
      melhorValor = valorBoard
      melhorMovimento = movimento
  
    if valorBoard > alpha:
      alpha = valorBoard
  
    board.pop()
  
  return melhorMovimento

"""
Move a peça do tabuleiro, automaticamento usando os algoritmos de alpha-beta, analisando movimentos futuros
"""
def dev_mover_peca():
  # Nessa situação será usado uma profundidade de 5 camadas. Mas para o melhor desempenho use 3.
  move = selecionar_movimento(3)
  # Mostra qual movimento foi feito
  print(move)
  board.push(move)

"""
Função para começar o jogo
"""
def jogar():
  while not board.is_checkmate():
    dev_mover_peca()
    print("\n\n", board)
    time.sleep(2)

jogar()
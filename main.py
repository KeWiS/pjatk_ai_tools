from easyAI import Human_Player, AI_Player, Negamax

from game import Game

ai_player = Negamax(4)
game = Game([Human_Player(), AI_Player(ai_player)])
game.play()

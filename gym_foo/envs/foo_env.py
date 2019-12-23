import gym
from gym import error, spaces, utils
from gym.utils import seeding
import random
import math

'''
Board - 3x3 board. Binary representation, 1 represents player, 0 represents nothing
Actions - [1...4] representing up down left right
'''

class FooEnv(gym.Env):
	metadata = {'render.modes': ['human']}
	action_space = [0, 1, 2, 4]

	def __init__(self):
		possible_pos = []
		for row in range(3):
			for col in range(3):
				possible_pos.append([row, col])
		
		while True:
			[self.player1, self.player2] = random.sample(possible_pos, 2)
			if (math.sqrt((self.player1[0] - self.player2[0])**2 + (self.player1[1] - self.player2[1])**2) - 1) > 0.05:
				break

		self.player_turn = self.player1

		self.done = False

	def step(self, action):

		reward = -1

		if self.player1 == self.player2:
			reward = 0
			self.done = True

		if action == 0:
			if self.player_turn[1] - 1 >= 0:
				self.player_turn[1] -= 1
			else:
				self.player_turn[1] = 2
		if action == 1:
			if self.player_turn[0] + 1 <= 2:
				self.player_turn[0] += 1
			else:
				self.player_turn[0] = 0
		if action == 2:
			if self.player_turn[1] + 1 <= 2:
				self.player_turn[1] += 1
			else:
				self.player_turn[1] = 0
		if action == 3:
			if self.player_turn[0] - 1 >= 0:
				self.player_turn[0] -= 1
			else:
				self.player_turn[0] = 2
		
		if reward == 0 and self.player1 == self.player2:
			reward = 0
			self.done = True

		if self.player_turn == self.player1:
			self.player_turn = self.player2
		else:
			self.player_turn = self.player1


		return (self.player1[0], self.player1[1], self.player2[0], self.player2[1], False), reward, self.done, {}

	def reset(self):
		possible_pos = []
		for row in range(3):
			for col in range(3):
				possible_pos.append([row, col])
		
		while True:
			[self.player1, self.player2] = random.sample(possible_pos, 2)
			if (math.sqrt((self.player1[0] - self.player2[0])**2 + (self.player1[1] - self.player2[1])**2) - 1) > 0.05:
				break

		self.player_turn = self.player1

		self.done = False

		return (self.player1[0], self.player1[1], self.player2[0], self.player2[1], True)

	def render(self, mode='human'):
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		board[self.player1[1]][self.player1[0]] = 1
		board[self.player2[1]][self.player2[0]] = 2

		print('\n\n\n')
		for row in board:
			print(row)


	def close(self):
		print("fek off lel")
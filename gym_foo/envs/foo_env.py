import gym
from gym import error, spaces, utils
from gym.utils import seeding
import random
import math
import pygame
import numpy as np
from pygame.locals import *

'''
Board - 3x3 board. Binary representation, 1 represents player, 0 represents nothing
Actions - [1...4] representing up down left right
'''

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    action_space = [0, 1, 2, 4]
    board_size = 3

    default_reward = -1
    win_reward = 0
    lose_reward = 0

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


    def __init__(self):
        possible_pos = self.get_possible_positions()
        
        while True:
            [self.player1, self.player2] = random.sample(possible_pos, 2)
            if (math.sqrt((self.player1[0] - self.player2[0])**2 + (self.player1[1] - self.player2[1])**2) - 1) > 0.05:
                break

        self.player_turn = self.player1

        self.done = False

    def step(self, action):

        reward = self.default_reward

        if self.player1 == self.player2:
            reward = self.lose_reward
            self.done = True

        if action == 0:
            self.move([0, -1])
        if action == 1:
            self.move([1, 0])
        if action == 2:
            self.move([0, 1])
        if action == 3:
            self.move([-1, 0])
        
        if reward == self.default_reward and self.player1 == self.player2:
            reward = self.win_reward
            self.done = True

        if self.player_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1


        return (self.player1[0], self.player1[1], self.player2[0], self.player2[1], False), reward, self.done, {}

    def reset(self):
        possible_pos = self.get_possible_positions()
        
        while True:
            [self.player1, self.player2] = random.sample(possible_pos, 2)
            if (math.sqrt((self.player1[0] - self.player2[0])**2 + (self.player1[1] - self.player2[1])**2) - 1) > 0.05:
                break

        self.player_turn = self.player1

        self.done = False

        return (self.player1[0], self.player1[1], self.player2[0], self.player2[1], True)

    def render(self, mode='human'):
        board = []

        for x in range(self.board_size):
            board.append([])
            for y in range(self.board_size):
                board[x].append(0)

        board[self.player1[1]][self.player1[0]] = 1
        board[self.player2[1]][self.player2[0]] = 2

        for row in board:
            print(row)
        print("\n\n\n")

    def close(self):
        print("fek off lel")

    def set_board_size(self, size):
        self.board_size = size

    def get_possible_positions(self):
        possible_pos = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                possible_pos.append([row, col])
        return possible_pos

    def move(self, amount):
        player = self.player_turn
        new_x = player[0] + amount[0]
        new_y = player[1] + amount[1]
        if new_x >= self.board_size or new_x < 0 or new_y >= self.board_size or new_y < 0:
            return

        player[0] = new_x
        player[1] = new_y


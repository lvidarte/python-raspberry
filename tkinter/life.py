#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Las transiciones dependen del número de células vecinas vivas:

  * Una célula muerta con exactamente 3 células vecinas vivas "nace"
    (al turno siguiente estará viva).
  * Una célula viva con 2 ó 3 células vecinas vivas sigue viva,
    en otro caso muere o permanece muerta (por "soledad" o "superpoblación").

"""

import tkinter as tk


class Game(tk.Frame):

    def __init__(self, life, size=10):
        super(Game, self).__init__()
        self.grid()
        self.life = life
        self.size = size
        self.cells_alive = {}
        self.create_widgets()
        self.draw_grid()

    def start(self):
        self.draw_cell((1, 1))

    def create_widgets(self):
        width = self.life.width * self.size
        height = self.life.height * self.size
        self.canvas = tk.Canvas(self, width=width,
                                height=height, bg='white')
        self.canvas.grid()

    def draw_grid(self):
        self.draw_vertical_lines()
        self.draw_horizontal_lines()

    def draw_vertical_lines(self, color='gray'):
        for i in range(self.life.width - 1):
            x = (self.size * i) + self.size
            y0 = 0
            y1 = self.size * self.life.height
            self.canvas.create_line(x, y0, x, y1, fill=color)

    def draw_horizontal_lines(self, color='gray'):
        for i in range(self.life.height - 1):
            x0 = 0
            x1 = self.size * self.life.width
            y = (self.size * i) + self.size
            self.canvas.create_line(x0, y, x1, y, fill=color)

    def draw_cell(self, cell, color='black'):
        x, y = cell
        x0 = x * self.size
        y0 = y * self.size
        x1 = x0 + self.size
        y1 = y0 + self.size
        _id = self.canvas.create_rectangle(x0, y0, x1, y1,
                                           width=0, fill=color)
        self.cells_alive[cell] = _id

class Life:

    DEAD  = 0
    ALIVE = 1

    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.set_board(self.get_empty_board())

    def set_board(self, board):
        if type(board) == list:
            self.board = board
            self.width = len(board[0])
            self.height = len(board)

    def set_alive(self, x, y):
        self.board[y][x] = self.ALIVE
        
    def set_dead(self, x, y):
        self.board[y][x] = self.DEAD
        
    def get_empty_board(self):
        return [[self.DEAD] * self.width for _ in range(self.height)]

    def evolve(self):
        board = self.get_empty_board()
        for x in range(self.width):
            for y in range(self.height):
                cell = self.board[y][x]
                neighbords = self.get_neighbors((x, y))
                board[y][x] = self.get_next_state(cell, neighbords)
        self.board = board
        return board

    def get_neighbors(self, cell):
        x_center, y_center = cell
        x_left  = x_center-1 if x_center-1 >= 0 else self.width-1
        x_right = x_center+1 if x_center+1 < self.width else 0
        y_up    = y_center-1 if y_center-1 >= 0 else self.height-1
        y_down  = y_center+1 if y_center+1 < self.height else 0
        return (self.board[y_up][x_left],
                self.board[y_up][x_center],
                self.board[y_up][x_right],
                self.board[y_center][x_left],
                self.board[y_center][x_right],
                self.board[y_down][x_left],
                self.board[y_down][x_center],
                self.board[y_down][x_right])

    def get_next_state(self, cell, neighbords):
        alive_neighbords = neighbords.count(self.ALIVE)
        if (cell == self.DEAD and alive_neighbords == 3) or \
           (cell == self.ALIVE and alive_neighbords in (2, 3)):
            return self.ALIVE
        else:
            return self.DEAD

if __name__ == '__main__':
    
    life = Life()
    game = Game(life, size=20)
    game.start()


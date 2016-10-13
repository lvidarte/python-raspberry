#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

"""
Las transiciones dependen del número de células vecinas vivas:

  * Una célula muerta con exactamente 3 células vecinas vivas "nace"
    (al turno siguiente estará viva).
  * Una célula viva con 2 ó 3 células vecinas vivas sigue viva,
    en otro caso muere o permanece muerta (por "soledad" o "superpoblación").

"""

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
    # Glider
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    life = Life()
    life.set_board(board)

    def show(board):
        for row in board:
            print(' '.join([' ' if col == 0 else '#' for col in row]))
            
    for i in range(30):
        show(life.board)
        life.evolve()
        print("-" * 16)


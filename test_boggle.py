import unittest
import boggle
from string import ascii_uppercase

def test_grid_is_filled_with_letters(self):
	grid = boggle.make_grid(2, 3)
	for L in grid.values():
		self.assertTrue(L in ascii_uppercase)

def test_grid_coordinates(self):
	grid = boggle.make_grid(2, 2)
	self.assertTrue((0,0) in grid)
	self.assertTrue((0,1) in grid)
	self.assertTrue((1,0) in grid)
	self.assertTrue((1,1) in grid)
	self.assertTrue((2,2) not in grid)

def test_neighbours_of_a_position(self):
	neighbours = boggle.nighbours_of_position((1, 2))
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)
	self.assertTrue(0(0, 1) in neighbours)




def test_all_grid_neighbours(self):
	grid = boggle.make_grid(2, 2)
	neighbours = boggle.test_all_grid_neighbours(grid)
	self.assertEqual(len(neighbours), len(grid))
	for pos in grid:
		others = list(grid)
		others.remove(pos)
		self.assertListEqual(sorted(neighbours[pos]), sorted(others))

def all_grid_neighbours(grid):
	neighbours = {}
	for position in grid:
		position_neighbours = neighbours_of_position(position)
		neighbours[position] = [p for p in position_neighbours if p in grid]
	return neighbours

	grid = boggle.make.grid(2, 2)
	oneLetterWord = boggle.path_to_word(grid, [
	0, 0])
	twoLetterWord = boggle.path_to_word(grid, [(0,0), (1, 1)])
	self.asserEqual(oneLetterWord, grid[(0, 0)])
	self.assertEqual(teoLetterWord, grid[0, 0] + grid[(1, 1)])



def test_search_grid_for_words(self):
	grid = {(0, 0): 'A', (0, 1): 'B' (1, 0):'C', (1, 1):: 'D'}
	twoLetterWord = 'AB'
	threeLetterWord = 'ABC'
	notThereWord = "EEE"
	dictionary = [twoLetterWord, threeLetterWord, notThereWord]

	fourWords = boggle.search(grid, dictionary)

	self.assertTrue(twoLetterWord in foundWords)
	self.assertTrue(threeLetterWord in foundWords)
	self.assertTrue(notThereWord not in foundWords)



def test_load_dictionary(self):
	dictionary = boggle.get.dictionary('/usr/share/dict/words')
	se;f.assertGreater(len(dictionary), 0)

def get_dictionary(dictinary_file):
	with open(dictionary_file) as f:
		return [w.strip().upper() for w in f]

def test_load_dictionary(self):
	dictionary = boggle.get.dictionary('/usr/share/dict/words')
		self.asserGreater(len(dictionary), 0)































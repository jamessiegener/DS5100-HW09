import pandas as pd
import numpy as np
import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        booklover = BookLover("John Doe", "john@virginia.edu","Sci-Fi")
        booklover.add_book("The Martian",4)
        self.assertTrue("The Martian" in booklover.book_list.book_name.values)

    # add a book and test if it is in `book_list`.

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover = BookLover("John Doe", "john@virginia.edu", "Sci-Fi")
        booklover.add_book("The Martian", 4)
        booklover.add_book("The Martian",3)
        expected = 1
        self.assertEqual(booklover.num_books, expected)
        expected = ['The Martian']
        self.assertEqual(booklover.book_list.book_name.values, expected)

    def test_3_has_read(self):
        booklover = BookLover("John Doe", "john@virginia.edu", "Sci-Fi")
        booklover.add_book("The Martian", 4)
        self.assertTrue(booklover.has_read('The Martian'))
    # pass a book in the list and test if the answer is `True`.

    def test_4_has_read(self):
        booklover = BookLover("John Doe", "john@virginia.edu", "Sci-Fi")
        booklover.add_book("The Martian", 4)
        self.assertFalse(booklover.has_read('Dune'))
    # pass a book NOT in the list and use `assert False` to test the answer is `True`

    def test_5_num_books_read(self):
        booklover = BookLover("John Doe", "john@virginia.edu", "Sci-Fi")
        booklover.add_book("The Martian", 4)
        booklover.add_book("The Martian", 3)
        booklover.add_book("Dune", 5)
        booklover.add_book("1984",6)
        booklover.add_book("Pride and Prejudice", 2)
        expected = 3
        self.assertEqual(booklover.num_books_read(), expected)
    # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        booklover = BookLover("John Doe", "john@virginia.edu", "Sci-Fi")
        booklover.add_book("The Martian", 4)
        booklover.add_book("The Catcher in the Rye", 1)
        booklover.add_book("Dune", 5)
        booklover.add_book("1984", 5)
        booklover.add_book("Pride and Prejudice", 2)
        booklover.add_book("Hamlet", 3)
        booklover.fav_books().apply(lambda x: self.assertTrue(x.book_rating > 3), axis = 1)

# add some books with ratings to the list, making sure some of them have rating > 3. 
# Your test should check that the returned books have rating  > 3

if __name__ == '__main__':
    unittest.main(verbosity=3)
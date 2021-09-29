#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 10
day = 8

def test_code():
    assert main.shareFair(10, 2) == True, " shareFair(10, 2) == True failed"
    assert main.shareFair(100, 1) == True, " shareFair(100, 1) == True failed"
    assert main.shareFair(10, 3) == False, " shareFair(10, 3) == False failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"

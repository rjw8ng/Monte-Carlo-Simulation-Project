# DS-5100-Final-Project


# Metadata
Name: Royal Wang
Project: Monte Carlo Simulator

# Synopsis

Show demo code of how the classes are used, i.e.
installing
importing
Creating dice
Playing games
Analyzing games.

# API description
## Classes:
- Die
              - `__init__(self, face)`
                  - `face` 
- Die
 
     - `__init__(self, face)`
        `face` 
          
     - `change_weight(self, face_value, new_weight)`
        `face_value`
        `new_weight`
          
     - `roll(self, amount = 1)`
        `amount` 
          
     - `show(self)`
     
- Game

     - `__init__(self, die_object)`
       `die_object`
          
     - `play(self, turns)`
        `turns` 
          
     - `show_game(self, dataframe, form = 'wide')`
       `dataframe`
       `form`
- Analyzer

     - `__init__(self, result)`
       `result`
          
     - `jackpot(self)`
     
     - `combo(self)`
     
     - `face_counts_per_roll(self)`

Each item should show their docstrings.
All paramters (with data types and defaults) should be described.
All return values should be described.
Do not describe private methods and attributes.

# Manifest
 - `__init__.py`
 - `setup.py`
 - `Die.py`
 - `test.py`
 - `Die_result.txt`
 - `README.md`
 - `LICENSE`

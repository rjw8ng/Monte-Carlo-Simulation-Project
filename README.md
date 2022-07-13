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
* Die
    * `__init__(self, face)`
        * `face`  (dtype: array) <br /> 
           Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers. <br /> 
           Internally initializes the weights to 1.0 for each face. 
    * `change_weight(self, face_value, new_weight)`
        * `face_value`  (dtype: string or number) <br /> 
           Takes two arguments: the face value to be changed and the new weight. <br /> 
           Changes the weights value of the face inputted.
        * `new_weight`  (dtype: float or dtype able to convert to float) <br />
           Takes a parameter of how many times the die is to be rolled. <br />
           Returns a list of outcomes.
    * `roll(self, amount = 1)`
        * `amount`  (dtype: numeric) <br />
           Takes a parameter of how many times the die is to be rolled; defaults to 1. <br />
           Returns a list of outcomes.
     * `show(self)` <br />
        Returns the dataframe created in the initializer.
* Game
    * `__init__(self, die_object)`
        * `die_object`  (dtype: list) <br />
           Takes a single parameter, a list of already instantiated similar Die objects.
    * `play(self, turns)`
        * `turns`  (dtype: numeric) <br />
          Takes a parameter to specify how many times the dice should be rolled. <br />
          Returns dataframe with roll number as a named index, the die number, and face rolled per instance
    * `show_game(self, dataframe, form = 'wide')`
        * `dataframe`  (dtype: dataframe) <br />
           A method to show the user the results of the most recent play. <br />
            Takes a parameter to return the dataframe in narrow or wide form. <br />
        * `form`  (dtype: string) <br />
            This parameter defaults to wide form. <br />
            This parameter should raise an exception of the user passes an invalid option. <br />
            The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a column for the face rolled. <br />
            The wide form of the dataframe will a single column index with the roll number, and each die number as a column.

* Analyzer
    * `__init__(self, result)`
        * `result`
    * `jackpot(self)`
    * `combo(self)`
    * `face_counts_per_roll(self)`


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

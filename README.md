# DS-5100-Final-Project


# Metadata
Name: Royal Wang <br /> 
Project: Monte Carlo Simulator

# Synopsis
## Installing:
1. Open command line and clone this repository through `git clone 
## Importing:

## Creating dice:

## Playing games:

## Analyzing games:


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
        * `result`  (dtype:dataframe) <br />
          Takes a game object as its input parameter. <br />
           At initialization time, it also infers the data type of the die faces used.
    * `jackpot(self)` <br />
        A jackpot method to compute how many times the game resulted in all faces being identical. <br />
        Returns an integer for the number times to the user. <br />
        Stores the results as a dataframe of jackpot results in a public attribute.
    * `combo(self)` <br />
       A combo method to compute the distinct combinations of faces rolled, along with their counts. <br />
        Compute the distinct combinations of faces rolled, along with their counts. <br />
        Stores the results as a dataframe in a public attribute. <br />
    * `face_counts_per_roll(self)` <br />
       A face counts per roll method to compute how many times a given face is rolled in each event. <br />
        Compute how many times a given face is rolled in each event. <br />
        Stores the results as a dataframe in a public attribute.

# Manifest
 - `__init__.py`
 - `setup.py`
 - `Die.py`
 - `test.py`
 - `Die_result.txt`
 - `README.md`
 - `LICENSE`

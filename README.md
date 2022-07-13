# DS-5100-Final-Project


# Metadata
Name: Royal Wang <br /> 
Project: Monte Carlo Simulator

# Synopsis
## Installing:
1. Open command line and clone this repository through `git clone git@github.com:rjw8ng/DS-5100-Final-Project.git`
2. Copy `pip install -e .` into the command line once you are in the directory of the cloned github repository to install the package. The output should show `Successfully installed Die-Game`.
## Importing:
1. Importing the package can be done in the command line or through a saved python script
    1. Through command line, type `python` and then press enter to activate python. Run `from Die_Game.montecarlo import Die, Game, Analyzer` to import package.
    2. Through a saved python script, begin the script with `from Die_Game.montecarlo import Die, Game, Analyzer` and write the remaining code that uses the package afterwards.
## Creating dice:
1. A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
    1. W defaults to 1.0 for each face but can be changed after the object is created.
    2. The die has one behavior, which is to be rolled one or more times.
    3. A “die” can be any discrete random variable associated with a stochastic process.
2. To create a dice object, use the `Die` class initialize an object.
3. The Die object takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
4. Set the Die object to a variable. (ex. `die_object = Die([1,2,3,4,5,6]`)
## Playing games:
1. A game consists of rolling of one or more dice of the same kind one or more times. 
    1.  Each game is initialized with one or more of similarly defined dice (Die objects).
    2.  By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.
    3.  The `Game` class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
    4.  The `Game` class keeps the results of its most recent play. 
2. To play the game, create a list of Die objects created from the Die class. (ex. `[die_object1,die_object1, die_object1]`)
3. Run the `play` function from the `Game` class and save the output in a variable. (ex. `results = play([die_object1,die_object1, die_object1])`)
4. The `show` function can be used to change the output structure of the `play` function to a `wide` or `narrow` dataframe format. (ex. `show(result, form = 'narrow')`)
## Analyzing games:
1. To analyze the output from playing the game, use the `Analyzer` class to output descriptive statistical properties. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:
    1. A `face counts per roll`, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
    2. A `jackpot` count, i.e. how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die.
    3. A `combo` count, i.e. how many combination types of faces were rolled and their counts.

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
* `Die_Game`
    * `__init__.py`
    * `montecarlo_tests.py`
    * `montecarlo.py`
* `Die_Game.egg-info`
    * `dependency_links.txt`
    * `PKG-INFO`
    * `SOURCE.txt`
    * `top_level.txt`
* `Die_result.txt`
* `LICENSE`
* `montecarlo_demo.ipynb`
* `README.md`
* `setup.py`

import unittest
from montecarlo import Die, Game, Analyzer
import pandas.testing as pd_testing
import pandas as pd
import random


class EnrollInTestCase(unittest.TestCase): 
    
    '''
    Create 2 Die objects and change the weight of the first Die object to float.
    Check if the change_weight function changes the weight of face.
    '''
    def test_1_change_weight_tofloat__test(self):
        Die_Object1 = Die([1,2,3,4,5,6])
        Die_Object2 = pd.DataFrame({"face": [1,2,3,4,5,6], "weight": [1.0,1.0,1.0,1.0,1.0,5.0]})
        Die_Object1.change_weight(6, 5)
        
        self.assertEqual(int(Die_Object1.df["weight"][Die_Object1.df["face"]==6]), int(Die_Object2["weight"][Die_Object2["face"]==6]))
    
    '''
    Create 2 Die objects and change the weight of the first Die object to nonfloat.
    Check if the change_weight function changes the weight of face.
    '''
    def test_2_change_weight_nonfloat_test(self):
        Die_Object1 = Die([1,2,3,4,5,6])
        Die_Object2 = Die([1,2,3,4,5,6])
        Die_Object1.change_weight(6, "yes")
        
        self.assertEqual(int(Die_Object1.df["weight"][Die_Object1.df["face"]==6]), int(Die_Object2.df["weight"][Die_Object2.df["face"]==6]))
    
    '''
    Create 2 Die objects and change the weight of non-existant face of the first Die object.
    Check if the change_weight function changes the weight of face.
    '''
    def test_3_change_weight_not_face_test(self):
        Die_Object1 = Die([1,2,3,4,5,6])
        Die_Object2 = Die([1,2,3,4,5,6])
        Die_Object1.change_weight(7, 5.0)
        
        self.assertEqual(int(Die_Object1.df["weight"][Die_Object1.df["face"]==6]), int(Die_Object2.df["weight"][Die_Object2.df["face"]==6]))
    
    '''
    Create Die object and check if roll function generates the correct amount of rolls.
    '''
    def test_4_roll_test(self):
        Die_Object = Die([1,2,3,4,5,6])
        result = Die_Object.roll(6)
        
        self.assertEqual(len(result), 6)
        
    '''
    Create Die object and check output equals dataframe.
    '''
    def test_5_show_test(self):
        Die_Object = Die([1,2,3,4,5,6])
        
        pd_testing.assert_frame_equal(Die_Object.df, Die_Object.show())

    '''
    Create 3 Die objects and change the weight of the second Die object.
    Run play function to see if the correct number of rolls per die are rolled.
    '''
    def test_6_play(self):
        D1 = Die([1,2,3,4,5,6])
        D2 = Die([1,2,3,4,5,6])
        D3 = Die([1,2,3,4,5,6])
        D2.change_weight(6,5.0)
        lst = [D1, D2, D3]
        gm = Game(lst)
        
        df = gm.play(3)
        
        Roll_number = [i for i in gm.play(3)["Roll Number"]]
        Dies = [i for i in gm.play(3)["Die"]]
        
        self.assertTrue([[1,2,3,1,2,3,1,2,3], [0,0,0,1,1,1,2,2,2]], [Roll_number, Dies])
        
    '''
    Create 3 Die objects and change the weight of the second Die object.
    Check if the index and column names are correct after using the 'wide' arguement with the show function. 
    '''
    def test_7_show_wide(self):
        D1 = Die([1,2,3,4,5,6])
        D2 = Die([1,2,3,4,5,6])
        D3 = Die([1,2,3,4,5,6])
        D2.change_weight(6,5.0)
        lst = [D1, D2, D3]
        gm = Game(lst)
        
        col = [i for i in gm.show_game(gm.play(4), "wide").columns]
        index = list(gm.show_game(gm.play(4), "wide").index.values)
        
        self.assertEqual([col, index], [[0,1,2], [1,2,3,4]])
        
    '''
    Create 3 Die objects and change the weight of the second Die object.
    Check if the length of the columns match the 'narrow' arguement output with the show function. 
    '''
    def test_8_show_narrow(self):
        D1 = Die([1,2,3,4,5,6])
        D2 = Die([1,2,3,4,5,6])
        D3 = Die([1,2,3,4,5,6])
        D2.change_weight(6,5.0)
        lst = [D1, D2, D3]
        gm = Game(lst)
        
        col = [i for i in gm.show_game(gm.play(4), "narrow")["Roll"]]
        
        self.assertEqual(len(col), 12)
        
    '''
    Create 2 Die objects and compare the length of the jackpot dataframe output with the jackpot function count.
    ''' 
    def test_9_jackpot(self):
        D1 = Die([1,2])
        D2 = Die([1,2])
        lst = [D1, D2]
        gm = Game(lst)
        test = gm.play(10)
        
        analyze = Analyzer(test)
        count = analyze.jackpot()
        
        self.assertEqual(count, len(analyze.jackpot_result.index))
        
    '''
    Create 2 Die objects and compare if the max roll numnber matches the total combo count.
    '''
    def test_10_combo(self):
        D1 = Die([1,2])
        D2 = Die([1,2])
        lst = [D1, D2]
        
        gm = Game(lst)
        test = gm.play(10)
        
        analyze = Analyzer(test)
        
        self.assertEqual(max(analyze.result["Roll Number"]), sum(analyze.combo()["count"]))
    
    '''
    Create 2 Die objects and compares if the total rolls per face matches the rolls generated with the Game function.
    '''
    def test_11_face_counts_per_roll(self):
        D1 = Die([1,2])
        D2 = Die([1,2])
        lst = [D1, D2]
        
        gm = Game(lst)
        test = gm.play(10)
        
        analyze = Analyzer(test)
        colname = analyze.face_counts_per_roll().columns
        
        switch = True
        for i in colname:
            result_count = len(analyze.result[analyze.result["Roll"] == i].index)
            method_count = sum(analyze.face_counts_per_roll()[i])
            if result_count == method_count:
                pass
            else:
                swtich = False
                break
                
        self.assertTrue(switch)
        
if __name__ == '__main__':

    unittest.main(verbosity=2)

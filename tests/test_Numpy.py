from dvs_printf import listfunction
import numpy as np

np_list = np.array([
    [[1,1,1],[2,2,2],[3,3,3]],
    [[4,4,4],[5,5,5],[6,6,6]],
    [[7,7,7],[8,8,8],[9,9,9]], 
],ndmin=1, dtype="int64")

def test_arrayToList_numpy():
    assert listfunction(np_list) == [ '[[1 1 1]',' [2 2 2]',' [3 3 3]]', #------------------------------
    '[[4 4 4]',' [5 5 5]',' [6 6 6]]','[[7 7 7]',' [8 8 8]',' [9 9 9]]'] # pleace don't make any changes

list_getMat_true = [
    '[1, 1, 1]','[2, 2, 2]','[3, 3, 3]',
    '[4, 4, 4]','[5, 5, 5]','[6, 6, 6]', 
    '[7, 7, 7]','[8, 8, 8]','[9, 9, 9]']

def test_getMat_true_numpy():
    assert listfunction((np_list,),getMat= True )==list_getMat_true
    assert listfunction((np_list,),getMat="true")==list_getMat_true
    
def test_getMat_show_numpy():
    assert listfunction((np_list,),getMat="true show info")==list_getMat_true+ \
["<class 'numpy.ndarray'",'dtype=int64 ','shape=(3, 3, 3)>']
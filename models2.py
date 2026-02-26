# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
from helpers import *
import pandas as pd
import numpy as np

print('top of models2')
# init_board = getBoardMatrix("GGGGGNGGGGGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGNGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGSSTTTLNJJJNSSTNNNLZJNNNNNNNLZZNNNNNNNLLZNNNNIIIIOONNNNNNNNOONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
# init_piece = "J"
# print(isValid(init_board, init_piece, 7, 37, 1))
# print(boardToString(init_board))

# print(len(sorted(boardStrings)))

# does the creation of df_transformed

def get_board_arrays(states, init_board_matrix, init_piece):
    seen = {}
    for px, py, r in states:
        arr = getBoardArray(init_board_matrix, init_piece, px, py, r)
        seen[tuple(arr)] = arr
    return list(seen.values())

def string_board_states(states, init_board_matrix, init_piece):
    boardStrings = []
    for px, py, r in states:
        boardStrings += [getBoardString(init_board_matrix, init_piece, px, py, r)]

    return sorted(list(set(boardStrings)))


df = pd.read_pickle("data.pkl")
print('og df info')
print(df.info())


df = df.sort_values(['game_id', 'subframe']).reset_index(drop=True)
df['next_playfield'] = df.groupby('game_id')['playfield_transformed'].shift(-1)
df_transformed = df.dropna(subset=['next_playfield']).copy()
# added to remove the garbage issue NEEDS TO BE FIXED
df_transformed = df_transformed[df_transformed['immediate_garbage'] == 0]

df_transformed = df_transformed[[
    'playfield_transformed',
    'playfield',
    'placed',
    'hold',
    'next',         
    'next_playfield'   
]]
print('df transformed info')
print(df_transformed.info())


#already performed so it is just loaded now

# switching all of df_transformed to int for CNN
vocab = {"N":0,"G":1,"I":2,"O":3,"T":4,"S":5,"Z":6,"J":7,"L":8}
df_int = df_transformed.copy()
df_int['playfield_array'] = df_transformed['playfield_transformed'].apply(
    lambda s: np.array([vocab[c] for c in s], dtype=np.int32)
)
print('finshed transforming playfield to int arrays')
df_int['placed'] = df_transformed['placed'].apply(lambda s: vocab[s])
print('finshed transforming placed to int')
df_int['hold'] = df_transformed['hold'].apply(lambda s: vocab[s])
print('finshed transforming hold to int')

df_int['queue'] = df_transformed['next'].apply(
    lambda s: np.array([vocab[c] for c in s], dtype=np.int32)
)
print('finshed transforming queue to int arrays')
df_int['next_playfield']= df_transformed['next_playfield'].apply(
    lambda s: np.array([vocab[c] for c in s], dtype=np.int32)
)
print('finshed transforming next_playfield to int arrays')
df_int = df_int[[
    'playfield_array',
    'placed',
    'hold',
    'queue',         
    'next_playfield'   
]]

print('df int info')
# df_int.to_pickle("df_int.pkl")
df_int = pd.read_pickle("df_int.pkl")
print(df_int.info())
print(df_int.iloc[0])

inv_vocab = {0:"N", 1:"G", 2:"I", 3:"O", 4:"T", 5:"S", 6:"Z", 7:"J", 8:"L"}


# for string
'''
playfield_counts=[]
failed = 0
boardStrings2 = []
for x in range(1000):
    boardStrings2 = [] 

    boardStrings1 = string_board_states(
        getAllBoardStates(getBoardMatrix(df_transformed.iloc[x]['playfield_transformed']), df_transformed.iloc[x]['placed'], False),
        getBoardMatrix(df_transformed.iloc[x]['playfield_transformed']),
        df_transformed.iloc[x]['placed']
    )
    

    if df_transformed.iloc[x]['hold'] != 'N':
        boardStrings2 = string_board_states(
            getAllBoardStates(getBoardMatrix(df_transformed.iloc[x]['playfield_transformed']), df_transformed.iloc[x]['hold'], False),
            getBoardMatrix(df_transformed.iloc[x]['playfield_transformed']),
            df_transformed.iloc[x]['hold']
        )
        playfield_counts.append(len(boardStrings2)+len(boardStrings1))
    else:
        playfield_counts.append(len(boardStrings1))

    if df_transformed.iloc[x]['next_playfield'] not in boardStrings1 and df_transformed.iloc[x]['next_playfield'] not in boardStrings2:
        # print(df_transformed.iloc[x]['playfield_transformed'])
        # print(df_transformed.iloc[x]['next_playfield'])
        # print(boardStrings1)
        # print(boardStrings2)
        # print(df_transformed.iloc[x]['placed'])
        # print(df_transformed.iloc[x]['hold'])
        # print('---')
        failed += 1
        



    # print(df_transformed.iloc[x]['next_playfield'])
    # print(boardStrings1, boardStrings2)
'''
#for numpy ints
'''
playfield_counts=[]
failed = 0
boardStrings2 = []
for x in range(0):
    boardStrings2 = [] 
    # print('playfield_array',df_int.iloc[x]['playfield_array'])

    boardStrings1 = get_board_arrays(
        getAllBoardStates(df_int.iloc[x]['playfield_array'], df_int.iloc[x]['placed'], True), 
                          mod_board_matrix_to_helper(df_int.iloc[x]['playfield_array']), 
                          inv_vocab[df_int.iloc[x]['placed']])

    if df_int.iloc[x]['hold'] != 0:
        boardStrings2 = get_board_arrays(
            getAllBoardStates(df_int.iloc[x]['playfield_array'], df_int.iloc[x]['hold'], True), 
                              mod_board_matrix_to_helper(df_int.iloc[x]['playfield_array']), 
                              inv_vocab[df_int.iloc[x]['hold']])
        playfield_counts.append(len(boardStrings2)+len(boardStrings1))
    else:
        playfield_counts.append(len(boardStrings1))

    boardSet1 = {tuple(arr) for arr in boardStrings1}
    boardSet2 = {tuple(arr) for arr in boardStrings2}

    if tuple(df_int.iloc[x]['next_playfield']) not in boardSet1 and tuple(df_int.iloc[x]['next_playfield']) not in boardSet2:

    # if df_int.iloc[x]['next_playfield'] not in boardStrings1 and df_int.iloc[x]['next_playfield'] not in boardStrings2:
        # print('playfield',df_int.iloc[x]['playfield_array'])
        # print('next playfield',df_int.iloc[x]['next_playfield'])
        # print(boardStrings1)
        # print(boardStrings2)
        # print(df_int.iloc[x]['placed'])
        # print(df_int.iloc[x]['hold'])
        # print('---')
        # print('mod_board_matrix_helper ',mod_board_matrix_to_helper(df_int.iloc[x]['playfield_array']))
        # print('placed piece',inv_vocab[df_int.iloc[x]['placed']])
        # print('transformed playfield',getBoardMatrix(df_transformed.iloc[x]['playfield_transformed']))
        # print('transformed placed',df_transformed.iloc[x]['placed'])
        # break
        failed += 1


print(f"Failed to find next_playfield in candidates {failed} out of {len(playfield_counts)}")
print(f"Average number of candidates: {sum(playfield_counts)/len(playfield_counts)}")
print(f"Max number of candidates: {max(playfield_counts)}")
'''
# takes in the padding size and the list of candidates and outputs the padded candidates and a mask of which candidates are real vs padding
def candidate_padding(input_candidates,padding_size = 128):
    output_candidates = np.zeros((padding_size, 400), dtype=np.int32)
    mask  = np.zeros((padding_size,), dtype=bool)
    for i , candidate in enumerate(input_candidates):
        output_candidates[i] = candidate
        mask[i] = True
    return output_candidates, mask

sample_20k = df_int.iloc[:2].copy()

def get_candidates_1(row):
    boards1 = get_board_arrays(
        getAllBoardStates(row['playfield_array'], row['placed'], True),
        mod_board_matrix_to_helper(row['playfield_array']),
        inv_vocab[row['placed']]
    )
    print('---')
    print('len getallboardstates', len(getAllBoardStates(row['playfield_array'], row['placed'], True)))
    print('got boards1', boards1)
    
    boards2 = []
    if row['hold'] != 0:
        boards2 = get_board_arrays(
            getAllBoardStates(row['playfield_array'], row['hold'], True),
            mod_board_matrix_to_helper(row['playfield_array']),
            inv_vocab[row['hold']]
        )
        print('got boards2', len(boards2))
    print('boards2=', boards2)
    boards, mask = candidate_padding(boards1 + boards2, padding_size=128)
    return boards, mask

def get_candidates_2(row):
    boards1 = get_board_arrays(
        getAllBoardStates(row['playfield_array'], row['placed'], True),
        mod_board_matrix_to_helper(row['playfield_array']),
        inv_vocab[row['placed']]
    )
    # print('---')
    # print('len getallboardstates', len(getAllBoardStates(row['playfield_array'], row['placed'], True)))
    # print('got boards1', boards1)
    
    boards2 = []
    if row['hold'] != 0:
        boards2 = get_board_arrays(
            getAllBoardStates(row['playfield_array'], row['hold'], True),
            mod_board_matrix_to_helper(row['playfield_array']),
            inv_vocab[row['hold']]
        )
    #     print('got boards2', len(boards2))
    # print('boards2=', boards2)
    return boards1 + boards2

# working with 20k
print('working with 20k')
sample_20k['candidate_boards'] = sample_20k.apply(get_candidates_2, axis=1)
print('---')
thing = sample_20k.iloc[0]['candidate_boards']
print(len(thing))
print(sample_20k.info())
sample_20k.to_pickle("df_20k.pkl")


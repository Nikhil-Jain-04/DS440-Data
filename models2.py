# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
from helpers import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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

'''
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
df_int.to_pickle("df_int.pkl")
# df_int = pd.read_pickle("df_int.pkl")
print(df_int.info())
print(df_int.iloc[0])

inv_vocab = {0:"N", 1:"G", 2:"I", 3:"O", 4:"T", 5:"S", 6:"Z", 7:"J", 8:"L"}

'''
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
inv_vocab = {0:"N", 1:"G", 2:"I", 3:"O", 4:"T", 5:"S", 6:"Z", 7:"J", 8:"L"}

# takes in the padding size and the list of candidates and outputs the padded candidates and a mask of which candidates are real vs padding
def candidate_padding(input_candidates,padding_size = 128):
    output_candidates = np.zeros((padding_size, 400), dtype=np.int32)
    mask  = np.zeros((padding_size,), dtype=bool)
    for i , candidate in enumerate(input_candidates):
        output_candidates[i] = candidate
        mask[i] = True
    return output_candidates, mask

# sample_20k = df_int.iloc[:20000].copy()

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
'''
print('working with 20k')
sample_20k['candidate_boards'] = sample_20k.apply(get_candidates_2, axis=1)
print('---')
thing = sample_20k.iloc[0]['candidate_boards']
print(len(thing))
print(sample_20k.info())
sample_20k.to_pickle("df_20k.pkl")
'''

#################################################################################
# testing models
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, Flatten, Concatenate
from tensorflow.keras.models import Model

print('top of model testing')
df_20k = pd.read_pickle("./DS440-Data/df_20k.pkl")
print(df_20k.columns)
print(np.flip(df_20k['playfield_array'][20].reshape(40, 10), axis=0))


df_int = pd.read_pickle("./DS440-Data/df_int.pkl")
sample_50k = df_int.iloc[:40000].copy()
sample_50k['candidate_boards'] = sample_50k.apply(get_candidates_2, axis=1)
print('---')
thing = sample_50k.iloc[0]['candidate_boards']
print(len(thing))
sample_50k['playfield_array'] = sample_50k['playfield_array'].apply(lambda arr: np.flip(arr.reshape(40, 10), axis=0))
sample_50k['next_playfield'] = sample_50k['next_playfield'].apply(lambda arr: np.flip(arr.reshape(40, 10), axis=0))
print(sample_50k.info())
sample_50k = sample_50k.explode("candidate_boards").reset_index(drop=True)
sample_50k = sample_50k.rename(columns={"candidate_boards": "candidate_board"})
sample_50k['candidate_board'] = sample_50k['candidate_board'].apply(lambda arr: np.flip(arr.reshape(40, 10), axis=0))
sample_50k["correct"] = sample_50k.apply(
    lambda row: int(np.array_equal(row["candidate_board"], row["next_playfield"])),
    axis=1
)

sample_50k.to_pickle("sample_50k.pkl")
# this model only takes in the board states and attempts to score them on its own 
def model_only_using_moves():

    board_input = Input(shape=(40, 10, 1), name="board_input") # shape is 40 rows 10 cols and 1 channel

    # takes the input board and learns to recognize base patterns and featurs of the boards and outputs it as a set of 32 feature maps.
    x = Conv2D(
        filters=32, # gens 32 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", # 
        activation="relu",
        name="conv1"
    )(board_input)

    # takes the 32 feature maps and learns to recognize pattern/feature combos.
    x = Conv2D(
        filters=64, # gens 64 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", 
        activation="relu",
        name="conv2"
    )(x)

    # flattens the output from the conv layers into a 1d vector for the dense layers to process.
    x = Flatten(name="flatten")(x)

    # takes the massive flattened vector and refines it to 128 features
    x = Dense(
        units=128, # number of neurons per layer
        activation="relu",
        name="dense1"
    )(x)

    # takes the 128 features and refines it to 64 features
    x = Dense(
        units=64, # number of neurons per layer
        activation="relu",
        name="dense2"
    )(x)

    # outputs one number which is a board score
    score_output = Dense(
        units=1, 
        activation=None,
        name="score"
    )(x)

    model = Model(inputs=board_input, outputs=score_output, name="tetris_board_scorer")

    model.summary()

def model_2(train_queue, train_hold, train_place, train_start, train_candidate,train_y):
    queue_input = Input(shape=(5,), name="queue_input")
    hold_input = Input(shape=(1,), name="hold_input")
    place_input = Input(shape=(1,), name="place_input")

    start_board_input = Input(shape=(40, 10, 1), name="start_board_input")
    candidate_board_input = Input(shape=(40, 10, 1), name="candidate_board_input")

    # learning start board
        # takes the input board and learns to recognize base patterns and featurs of the boards and outputs it as a set of 32 feature maps.
    s = Conv2D(
        filters=32, # gens 32 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", # 
        activation="relu",
        name="conv1"
    )(start_board_input)

    # takes the 32 feature maps and learns to recognize pattern/feature combos.
    s = Conv2D(
        filters=64, # gens 64 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", 
        activation="relu",
        name="conv2"
    )(s)

    # flattens the output from the conv layers into a 1d vector for the dense layers to process.
    s = Flatten(name="flatten")(s)

    # takes the massive flattened vector and refines it to 128 features
    s = Dense(
        units=128, # number of neurons per layer
        activation="relu",
        name="dense1"
    )(s)

    #####
    # learns candidate board
    #####
    c = Conv2D(
        filters=32, # gens 32 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", # 
        activation="relu",
        name="conv1"
    )(candidate_board_input)

    # takes the 32 feature maps and learns to recognize pattern/feature combos.
    c = Conv2D(
        filters=64, # gens 64 weights
        kernel_size=(4, 4), # looks at 4x4 sections of the board at a time
        strides=(1, 1), # moves the window 1 cell at a time
        padding="same", 
        activation="relu",
        name="conv2"
    )(c)

    # flattens the output from the conv layers into a 1d vector for the dense layers to process.
    c = Flatten(name="flatten")(c)

    # takes the massive flattened vector and refines it to 128 features
    c = Dense(
        units=128, # number of neurons per layer
        activation="relu",
        name="dense1"
    )(c)

    #####
    # learns q, hold, place
    #####
    meta = Concatenate(name="meta_concat")([queue_input, hold_input, place_input])
    meta = Dense(32, activation="relu", name="meta_dense1")(meta)
    meta = Dense(16, activation="relu", name="meta_dense2")(meta)

    #####
    # combine the seperate layers
    #####
    x = Concatenate(name="all_features")([s, c, meta])
    x = Dense(128, activation="relu", name="combined_dense1")(x)
    x = Dense(64, activation="relu", name="combined_dense2")(x)

    #####
    # output one number which is a board score
    #####
    output = Dense(1, activation="sigmoid", name="chosen_prob")(x)
    
    model = Model(
    inputs=[queue_input, hold_input, place_input, start_board_input, candidate_board_input],
    outputs=output,
    name="tetris_choice_model")

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"])

    model.summary()

    model.fit(
    [train_queue, train_hold, train_place, train_start, train_candidate],
    train_y,
    batch_size=32,
    epochs=10,
    validation_split=0.2)

    model.save("tetris_model2.keras")
    # preds = model.predict([Q_batch, H_batch, P_batch, S_batch, C_batch])
    # best_idx = preds.argmax()
    # best_candidate = candidate_boards[best_idx]


train_df, test_df = train_test_split(sample_50k, test_size=0.2, random_state=42)

model_2(
    train_queue=np.stack(train_df['queue'].values),
    train_hold=np.stack(train_df['hold'].values),
    train_place=np.stack(train_df['placed'].values),
    train_start=np.stack(train_df['playfield_array'].values),
    train_candidate=np.stack(train_df['candidate_board'].values),
    train_y=train_df['correct'].values
)
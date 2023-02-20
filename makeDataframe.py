

def dataframeFormatter(game_id):
    import pandas as pd


    data = pd.read_csv('out.csv')




    print("Test")
    print(type(data))
    print(data)
    print(data.loc[0])
    print(data.loc[0])

    # data = data.rename(columns={'0': 'Home', '1': 'stat', '2': 'Away'})

    print(data.loc[0][0])
    print(data.loc[2][0])

    new_row = {
    'Game Id' : str(game_id)
    ,'Home Possession' : data.loc[0][0]
    ,'Away Possession' : data.loc[0][2]

    ,'Home Shots on Target' : data.loc[1][0]
    ,'Away Shots on Target' : data.loc[1][2]

    ,'Home Shots' : data.loc[2][0]
    ,'Away Shots' : data.loc[2][2]

    ,'Home Touches' : data.loc[3][0]
    ,'Away Touches' : data.loc[3][2]

    ,'Home Passes' : data.loc[4][0]
    ,'Away Passes' : data.loc[4][2]

    ,'Home Tackles' : data.loc[5][0]
    ,'Away Tackles' : data.loc[5][2]

    ,'Home Clearances' : data.loc[6][0]
    ,'Away Clearances' : data.loc[6][2]

    ,'Home Corners' : data.loc[7][0]
    ,'Away Corners' : data.loc[7][2]

    ,'Home Offsides' : data.loc[8][0]
    ,'Away Offsides' : data.loc[8][2]

    ,'Home Yellow cards' : data.loc[9][0]
    ,'Away Yellow cards' : data.loc[9][2]

    ,'Home Fouls conceded' : data.loc[10][0]
    ,'Away Fouls conceded' : data.loc[10][2]
    }


    return new_row



# flattened = flattened.append(new_row, ignore_index=True)

    # print(flattened)

# for x in range(len(data)):
#     print(data.loc[x][0])
import pandas as pd


def show_aggie_pride():
    # https://pandas.pydata.org/docs/user_guide/index.html
    df = pd.DataFrame(['Aggie County', 'Aggie State','Aggie Nation', 'Aggie.S.A!'], columns=['Text'])

    return df


if __name__ == "__main__":
    print(show_aggie_pride())

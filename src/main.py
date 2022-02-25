import os
import pandas as pd
from graph import graph

def attributePair(df, data, x, y):
    '''Prosedur perantara pembantu memilih pasangan attribute'''

    graph(df, data,f"{data.feature_names[x]} vs. {data.feature_names[y]}", data.feature_names[x],data.feature_names[y],x,y,data.target_names)


if __name__ == "__main__":
    # Make test folder for graph output
    if not os.path.exists('test'):
        os.makedirs('test')

    print("================================================")
    print("    WELCOME TO AFAN'S CONVEX HULL GENERATOR!")
    print("================================================\n")
    print("Made by:\n13520023\nAhmad Alfani Handoyo")

    condition = True
    while condition:
        print("\nChoose dataset to use:")
        print("1. Iris dataset")
        print("2. Wine dataset")
        print("3. Digits dataset")
        print("4. Breast cancer wisconsin dataset")
        dataset_choose = int(input("Your input (1-4): "))
        
        if dataset_choose == 1:
            # Load dataset iris
            from sklearn import datasets
            data = datasets.load_iris()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['label'] = pd.DataFrame(data.target)

            # Pilih pasangan atribut untuk dijadikan koordinat x,y
            print("\nChoose pair of attributes:")
            for i in range(2):
                print(f"{i+1}. {data.feature_names[2*i]} vs. {data.feature_names[2*i+1]}")
            attribute_choose = int(input("Your input (1-2): "))

            if 1 <= attribute_choose <= 2:
                attributePair(df, data, 2*(attribute_choose-1), 2*(attribute_choose-1)+1)
            else:
                print("Invalid attribute pair input (1-2)!")

        elif dataset_choose == 2:
            # Load dataset wine
            from sklearn import datasets
            data = datasets.load_wine()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['label'] = pd.DataFrame(data.target)

            # Pilih pasangan atribut untuk dijadikan koordinat x,y
            print("\nChoose pair of attributes:")
            for i in range(12):
                print(f"{i+1}. {data.feature_names[i]} vs. {data.feature_names[i+1]}")
            attribute_choose = int(input("Your input (1-12): "))

            if 1 <= attribute_choose <= 12:
                attributePair(df, data, attribute_choose-1, attribute_choose)
            else:
                print("Invalid attribute pair input (1-12)!")
        elif dataset_choose == 3:
            # Load dataset digits
            from sklearn import datasets
            data = datasets.load_digits()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['label'] = pd.DataFrame(data.target)

            # Pilih pasangan atribut untuk dijadikan koordinat x,y
            print("\nChoose pair of attributes:")
            for i in range(63):
                print(f"{i+1}. {data.feature_names[i]} vs. {data.feature_names[i+1]}")
            attribute_choose = int(input("Your input (1-63): "))

            if 1 <= attribute_choose <= 63:
                attributePair(df, data, attribute_choose-1, attribute_choose)
            else:
                print("Invalid attribute pair input (1-63)!")
        elif dataset_choose == 4:
            # Load dataset breast cancer wisconsin
            from sklearn import datasets
            data = datasets.load_breast_cancer()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['label'] = pd.DataFrame(data.target)

            # Pilih pasangan atribut untuk dijadikan koordinat x,y
            print("\nChoose pair of attributes:")
            for i in range(29):
                print(f"{i+1}. {data.feature_names[i]} vs. {data.feature_names[i+1]}")
            attribute_choose = int(input("Your input (1-29): "))

            if 1 <= attribute_choose <= 29:
                attributePair(df, data, attribute_choose-1, attribute_choose)
            else:
                print("Invalid attribute pair input (1-29)!")
        else:
            print("\nInvalid dataset input (1-4)!")

        loop = input("\nDo you want to try another dataset or pair of attributes? (Y/N): ")
        
        if loop.upper() != "Y":
            condition = False
            print("\n=========================================================")
            print("    THANK YOU FOR USING AFAN'S CONVEX HULL GENERATOR!")
            print("=========================================================\n")
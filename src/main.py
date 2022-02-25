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
        
        if 1 <= dataset_choose <= 4:
            from sklearn import datasets
            if dataset_choose == 1:
                # Load dataset iris
                data = datasets.load_iris()
            elif dataset_choose == 2:
                # Load dataset wine
                data = datasets.load_wine()
            elif dataset_choose == 3:
                # Load dataset digits
                data = datasets.load_digits()
            elif dataset_choose == 4:
                # Load dataset breast cancer wisconsin
                data = datasets.load_breast_cancer()

            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['label'] = pd.DataFrame(data.target)
            attributeLen = len(data.feature_names)

            # Pilih pasangan atribut untuk dijadikan koordinat x,y
            print("\nChoose attribute for x:")
            for i in range(attributeLen):
                print(f"{i+1}. {data.feature_names[i]}")
            x = int(input(f"Your input (1-{attributeLen}): "))

            print(f"\nChoose attribute for y (make sure it is different from {x}. {data.feature_names[x-1]}):")
            for i in range(attributeLen):
                print(f"{i+1}. {data.feature_names[i]}")
            y = int(input(f"Your input (1-{attributeLen}): "))

            if 1 <= x <= attributeLen and 1 <= y <= attributeLen and x != y:
                attributePair(df, data, x-1, y-1)
            else:
                print(f"Invalid attribute pair input x: {x} y: {y}!")
        else:
            print("\nInvalid dataset input (1-4)!")

        loop = input("\nDo you want to try another dataset or pair of attributes? (Y/N): ")
        
        if loop.upper() != "Y":
            condition = False
            print("\n=========================================================")
            print("    THANK YOU FOR USING AFAN'S CONVEX HULL GENERATOR!")
            print("=========================================================\n")
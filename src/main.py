import pandas as pd
from graph import graph, graph_scipyconvexhull

if __name__ == "__main__":
    print("================================================")
    print("    WELCOME TO AFAN'S CONVEX HULL GENERATOR!")
    print("================================================\n")
    print("Made by:\n13520023\nAhmad Alfani Handoyo\n")

    print("Choose dataset to use:")
    print("1. Scikit-learn toy dataset")
    print("2. Import from a csv file")
    print("3. Input from terminal\n")
    dataset_choose = int(input("Your input (1-3): "))
    
    if dataset_choose == 1:

        from sklearn import datasets
        data = datasets.load_iris()

        #create a DataFrame
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        # graph(df, "Sepal width vs. Sepal length",data.feature_names[0],data.feature_names[1],0,1,data.target_names,"01.png")
        # graph_scipyconvexhull(df, "Sepal width vs. Sepal length",data.feature_names[0],data.feature_names[1],0,1,data.target_names,"23.png")
        graph(df, "Sepal width vs. Sepal length",data.feature_names[2],data.feature_names[3],2,3,data.target_names,"2_ori.png")
        graph_scipyconvexhull(df, "Sepal width vs. Sepal length",data.feature_names[2],data.feature_names[3],2,3,data.target_names,"2_def.png")
        
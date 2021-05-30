import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from data_preprocess import *
import numpy as np

st.title('Project 402')
classifier = ["k-Nearest Neighbors (KNN)","Decision Tree","Support vector machine (SVM)","Gaussian process","Multilayer perceptron (MLP)"]
st.write("## Classifiers Comparision")

def get_result(result,grid,model_name,parameter):
    from model import model
    if parameter != 0:
        result_acc = model(model_name,parameter)
    else: result_acc = model(model_name,parameter)
    if grid == 0.001:
        result[0].append(result_acc)
    else: result[1].append(result_acc)
    return result
   
def compare():
    from model import get_data
    row_name = []
    result = [[],[]]
    option_grid = st.multiselect('Select one or more grid sizes: ',[0.001,0.0001], default=[0.001])
    option_knn = st.checkbox(classifier[0])
    if(option_knn):
        selected_k = st.multiselect('Select one or more k(s) of KNN', [3,5,7], default=[5])
    
    option_dct = st.checkbox(classifier[1])
    if(option_dct):
        selected_c = st.multiselect('Select one or more Criterion of Decision tree', ["entropy","gini"], default=["gini"])
    
    option_svm = st.checkbox(classifier[2])
    option_gpc = st.checkbox(classifier[3])
    option_mlp = st.checkbox(classifier[4])

    if(st.button("compare")):
        st.write("Compare Result")
        for grid in option_grid:
            get_data(grid)
            if(option_knn):
                for k in selected_k:
                    row_name.append(classifier[0].split(" ")[0]+" "+classifier[0].split(" ")[1]+" (k="+str(k)+")")
                    get_result(result,grid,'knn',k)

            if(option_dct):
                for c in selected_c:
                    row_name.append(classifier[1]+" criterion="+c)
                    get_result(result,grid,'dct',c)

            if(option_svm):
                row_name.append(classifier[2])
                get_result(result,grid,'svm',0)

            if(option_gpc):
                row_name.append(classifier[3])
                get_result(result,grid,'gpc',0)
            
            if(option_mlp):
                row_name.append(classifier[4])
                get_result(result,grid,'mlp',0)

        if (len(result[0]) != 0 and len(result[1]) != 0):
            df1 = pd.DataFrame({'Accuracy':result[0]},index=set(row_name))
            df2 = pd.DataFrame({'Accuracy':result[1]},index=set(row_name))
            df = pd.concat([df1,df2],axis=1,keys=option_grid).swaplevel(0,1,axis=1)
            st.table(df)
            
            df_chart = pd.DataFrame({'classifier': list(set(row_name)), 'acc': result[0]})
            df_chart1 = pd.DataFrame({'classifier': list(set(row_name)), 'acc': result[1]})
            fig = go.Figure(data=[
                go.Bar(name='0.001', x=df_chart['classifier'], y=df_chart['acc']),
                go.Bar(name='0.0001', x=df_chart1['classifier'], y=df_chart1['acc'])
            ])
            st.write(fig)
        else:
            if(len(result[0]) != 0):
                df1 = pd.DataFrame({'Accuracy':result[0]},index=row_name)
                df = pd.concat([df1],axis=1,keys=[0.001]).swaplevel(0,1,axis=1)
                
                df_chart = pd.DataFrame({'classifier': list(row_name), 'acc': result[0]})
                fig = go.Figure(data=[
                go.Bar(name='0.001', x=df_chart['classifier'], y=df_chart['acc']),
                ])
            if(len(result[1]) != 0):
                df1 = pd.DataFrame({'Accuracy':result[1]},index=row_name)
                df = pd.concat([df1],axis=1,keys=[0.0001]).swaplevel(0,1,axis=1)
                
                df_chart = pd.DataFrame({'classifier': list(row_name), 'acc': result[1]})
                fig = go.Figure(data=[
                go.Bar(name='0.001', x=df_chart['classifier'], y=df_chart['acc']),
                ])
            st.table(df)
            st.write(fig)

compare()
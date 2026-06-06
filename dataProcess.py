import pandas as pd

def process_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    
    question_columns = [col for col in df.columns if col != 'Timestamp']
    
    df_melted = df.melt(
        id_vars=['Timestamp'], value_vars=question_columns, 
        var_name='ques', 
        value_name='ans'
    )   
    
    return df_melted

            

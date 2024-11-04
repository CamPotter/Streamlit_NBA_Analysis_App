
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("NBA Game Outcome Analysis")

# Step 1: File Upload
st.header("Upload your NBA game data CSV")
uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file is not None:
    # Load the data into a DataFrame
    nba_data = pd.read_csv(uploaded_file)
    
    # Display a preview of the data
    st.subheader("Data Preview")
    st.write(nba_data.head())
    
    # Convert necessary columns to appropriate data types for visualization
    try:
        nba_data['Actual Margin'] = pd.to_numeric(nba_data['Actual Margin'], errors='coerce')
        nba_data['Spread (Median Prediction)'] = pd.to_numeric(nba_data['Spread (Median Prediction)'], errors='coerce')
    except KeyError as e:
        st.error(f"Missing column in data: {e}")

    # Step 2: Visualize Predicted Spread vs Actual Margin
    st.subheader("Predicted Spread vs. Actual Margin")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.scatter(nba_data['Spread (Median Prediction)'], nba_data['Actual Margin'], color='b', alpha=0.7)
    ax1.axhline(0, color='gray', linestyle='--')
    ax1.set_xlabel('Spread (Median Prediction)')
    ax1.set_ylabel('Actual Margin')
    ax1.set_title('Predicted Spread vs. Actual Margin')
    ax1.grid(True)
    st.pyplot(fig1)
    
    # Step 3: Visualize Win Probability Analysis
    st.subheader("Win Probability (Team 1 vs Team 2)")
    try:
        team_1_win_prob = nba_data['Win % (Team 1)'].str.rstrip('%').astype('float')
        team_2_win_prob = nba_data['Win % (Team 2)'].str.rstrip('%').astype('float')
        
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.plot(nba_data['Teams'], team_1_win_prob, label='Win % (Team 1)', marker='o', color='blue')
        ax2.plot(nba_data['Teams'], team_2_win_prob, label='Win % (Team 2)', marker='o', color='green')
        ax2.set_xticklabels(nba_data['Teams'], rotation=90)
        ax2.set_xlabel('Teams')
        ax2.set_ylabel('Win Probability (%)')
        ax2.set_title('Win Probability (Team 1 vs Team 2)')
        ax2.legend()
        ax2.grid(True)
        st.pyplot(fig2)
        
    except KeyError as e:
        st.error(f"Missing column in data: {e}")
else:
    st.info("Please upload a CSV file to analyze NBA game outcomes.")

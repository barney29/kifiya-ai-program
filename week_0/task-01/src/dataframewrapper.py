import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataFrameWrapper:
    """
    The class responsible to hold data: which is pandas dataframe only for week_0: task-01
    challenge the problem is the same but the data is different 
    """
    def __init__(self, df) -> None:
        """ Constructur to read data from the csv file"""
        self.df = df
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])

        #setting up initial time line
        self.weekly_mean = self.df.resample('W', on='Timestamp').mean()
        self.monthly_mean = self.df.resample('M', on='Timestamp').mean()
        self.weekly_mean.reset_index(inplace=True)

    def info(self):
        return self.df.info()
    def head(self, value=5):
        return self.df.head(value)
    def tail(self, value=5):
        return self.df.tail(value)
    def sample(self, value=5):
        return self.df.sample(value)
    def isnull(self):
        return self.df.isnull().sum()
    def describe(self):
        return self.df.describe()
    

    ##Time series Analysis
    def main_time_seris_analysis(self, default=0):
        # weekly_df = self.df.resample('W').mean()  # Weekly mean
        # monthly_df = self.df.resample('M').mean()  # Monthly mean

        # Create subplots for each variable
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
        fig.suptitle('Time Series for GHI, DNI, DHI, and Tamb')

        # Plot GHI
        self.weekly_mean['global_horizontal_irradiance'].plot(ax=axes[0, 0], title='Weekly GHI')
        self.monthly_mean['global_horizontal_irradiance'].plot(ax=axes[1, 0], title='Monthly GHI')

        # Plot DNI
        self.weekly_mean['direct_normal_irradiance'].plot(ax=axes[0, 1], title='Weekly DNI')
        self.monthly_mean['direct_normal_irradiance'].plot(ax=axes[1, 1], title='Monthly DNI')

        # Plot DHI
        self.weekly_mean['diffuse_horizontal_irradiance'].plot(ax=axes[0, 0], title='Weekly DHI')
        self.monthly_mean['diffuse_horizontal_irradiance'].plot(ax=axes[1, 0], title='Monthly DHI')

        # Plot Tamb
        self.weekly_mean['ambient_temperature'].plot(ax=axes[0, 1], title='Weekly Tamb')
        self.monthly_mean['ambient_temperature'].plot(ax=axes[1, 1], title='Monthly Tamb')

        # Customize the plots (add labels, legends, etc.)
        for ax in axes.flat:
            ax.set_xlabel('Timestamp')
            ax.set_ylabel('Value')
            ax.legend()

        plt.tight_layout()
        plt.show()

   #To plot a time series analysis for each variables
    def plot_weekly_time_series(self, var, label):

        plt.figure(figsize=(10, 6))
        plt.plot(np.array(self.weekly_mean['Timestamp']), np.array(self.weekly_mean[var]), marker='o', linestyle='-')
        plt.xlabel('Week')
        plt.ylabel(label)
        plt.title(f'Daily Time Series of {label}')
        plt.grid(True)
        plt.show()
    
    def corr_solarRad_temp(self):
        corr_matrix = self.df[['global_horizontal_irradiance', 'direct_normal_irradiance', 'diffuse_horizontal_irradiance', 'ambient_temperature', 'temp_module_A', 'temp_module_B']].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix of Solar Radiation Components and Temperature Measures')
    
    def wind_analysis(self):
        sns.pairplot(self.df[['wind_speed', 'WSgust', 'WSstdev', 'wind_direction', 'WDstdev']])
        plt.suptitle('Pairplot Of Wind Speed and Wind Direction Variables')
        plt.show()
    
    def corr_ws_wd(self):
        corr_matrix_wind = self.df[['wind_speed', 'WSgust', 'WSstdev', 'wind_direction', 'WDstdev']].corr()
        grouped_data = self.df.groupby('wind_speed')
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix_wind, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix of Wind Speed and Wind Direction Variables')
        plt.show()
    
    def corr_tamb_tmoa_tmob_by_condition(self):
        condition = 'wind_speed'
        grouped_data = self.df.groupby(condition)
        for condition, group in grouped_data:
            print(f"Correlation matrix for wind speed {condition}")
            correlation_matrix = group[['temp_module_A', 'temp_module_B', 'ambient_temperature']].corr()
            print(correlation_matrix)
            print()
    
    def ws_wsgust(self):
        plt.subplot(1, 2, 2)
        plt.scatter(self.df['wind_speed'], self.df['WSgust'])
        plt.title('Wind Speed vs WSgues')
        plt.xlabel('WS')
        plt.ylabel('WSgust')

        plt.tight_layout()
        plt.show()
    
    def weekly_analysis_of_main_vairables(self):
        weekly_dates = self.weekly_mean.index.to_numpy()

        plt.figure(figsize=(10, 6))
        plt.title('Weekly Time Series Analysis for GHI, DNI, DHI, and Tamb')
        plt.xlabel('Timestamp')
        plt.ylabel('Value')

        # Plot GHI
        plt.plot(weekly_dates, np.array(self.weekly_mean['global_horizontal_irradiance']), label='GHI', marker='o')

        # Plot DNI
        plt.plot(weekly_dates, np.array(self.weekly_mean['direct_normal_irradiance']), label='DNI', marker='s')

        # Plot DHI
        plt.plot(weekly_dates, np.array(self.weekly_mean['diffuse_horizontal_irradiance']), label='DHI', marker='^')

        # Plot Tamb
        plt.plot(weekly_dates, np.array(self.weekly_mean['ambient_temperature']), label='Tamb', marker='x')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def histogram_main_variable(self):
        ## histogram
        fig, axs = plt.subplots(2, 3, figsize=(15, 8))
        fig.suptitle('Frequency Distribution of Solar and Wind Variables')

        # Plot histograms
        axs[0, 0].hist(self.df['global_horizontal_irradiance'], bins=30, color='skyblue', edgecolor='black')
        axs[0, 0].set_title('GHI')
        axs[0, 1].hist(self.df['direct_normal_irradiance'], bins=30, color='salmon', edgecolor='black')
        axs[0, 1].set_title('DNI')
        axs[0, 2].hist(self.df['diffuse_horizontal_irradiance'], bins=30, color='limegreen', edgecolor='black')
        axs[0, 2].set_title('DHI')
        axs[1, 0].hist(self.df['wind_speed'], bins=30, color='gold', edgecolor='black')
        axs[1, 0].set_title('Wind Speed')
        axs[1, 1].hist(self.df['ambient_temperature'], bins=30, color='purple', edgecolor='black')
        axs[1, 1].set_title('Temperature')

        # Set common labels
        for ax in axs.flat:
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')

        # Adjust layout
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()
    
    def box_plot(self):
        #box plot
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle('Box Plots: Solar Radiation and Temperature')

        # Plot box plots
        axs[0, 0].boxplot(self.df['global_horizontal_irradiance'], vert=False, labels=['GHI'])
        axs[0, 0].set_title('Global Horizontal Irradiance (GHI)')
        axs[0, 1].boxplot(self.df['direct_normal_irradiance'], vert=False, labels=['DNI'])
        axs[0, 1].set_title('Direct Normal Irradiance (DNI)')
        axs[1, 0].boxplot(self.df['diffuse_horizontal_irradiance'], vert=False, labels=['DHI'])
        axs[1, 0].set_title('Diffuse Horizontal Irradiance (DHI)')
        axs[1, 1].boxplot(self.df['ambient_temperature'], vert=False, labels=['Temperature'])
        axs[1, 1].set_title('Ambient Temperature')

        # Adjust layout
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def scatter_plot(self):
        ##scatter plot

        plt.figure(figsize=(8, 6))
        plt.scatter(self.df['global_horizontal_irradiance'], self.df['ambient_temperature'], label='GHI vs. Tamb', color='blue', marker='o')
        plt.scatter(self.df['wind_speed'], self.df['WSgust'], label='WS vs. WSgust', color='red', marker='x')

        # Customize plot
        plt.xlabel('GHI / WS')
        plt.ylabel('Tamb / WSgust')
        plt.title('Scatter Plot: GHI, Tamb, WS, and WSgust')
        plt.grid(True)
        plt.legend()

        # Show the plot
        plt.show()

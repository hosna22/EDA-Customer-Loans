import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns


class DataTransform:
    def __init__(self):
        pass
    
    def date_format(self, dataframe, *args):
        for col in args:
            dataframe[col] = pd.to_datetime(dataframe[col], format='%b-%Y', errors='coerce')
        return(dataframe)
    
    def employment_number_system(self, dataframe, col):
        map_dict = {'<1 year':'1', '1 year':'2', '2 years':'3', '3 years':'4', '4 years':'5', '5 years':'6', '6 years':'7', '7 years':'8', '8 years':'9', '9 years':'10', '10+ years':'11'}
        dataframe[col] = dataframe[col].map(map_dict)
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def numeric_format(self, dataframe, col, phrase):
        dataframe[col] = dataframe[col].str.replace(f'{phrase}', '')
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def impute_data_median(self, dataframe, *args):
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].median())
        return(dataframe)
    
    def impute_data_mean(self, dataframe, *args):
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
        return(dataframe)

    def correct_skew_log_transform(self, dataframe, *args):
        for col in args:
            dataframe.loc[:, col] = dataframe[col].map(lambda i: np.log(i) if i > 0 else 0.0)
        return(dataframe)

    def correct_skew_sqrt(self, dataframe, *args):   
        for col in args:
            dataframe[col] = dataframe[col].map(lambda i: np.sqrt(i))
        return(dataframe)
    

class DataFrameInfo:
    def __init__(self):
        pass
    
    def df_data_types(self, dataframe):
        print('DataFrame data types:\n', dataframe.dtypes)
    
    def df_statistical_values(self, dataframe):
        print('DataFrame statistical values:\n', dataframe.describe())

    def column_basic_statistics(self, dataframe, *args):
        for col in args:
            mean_value = round(dataframe[col].mean(), 2)
            median_value = round(dataframe[col].median(), 2)
            mode_value = (dataframe[col].mode()[0])
            std_value = round(dataframe[col].std(), 2)
            print(f'{col}: Mean={mean_value}, Median={median_value}, Mode={mode_value}, Standard deviation={std_value}')
    
    def categorical_distinct_values(self, dataframe):
        col_list=['term', 
                  'grade', 
                  'sub_grade', 
                  'employment_length', 
                  'home_ownership', 
                  'verification_status', 
                  'loan_status', 
                  'payment_plan', 
                  'purpose', 
                  'policy_code', 
                  'application_type']
        print('DataFrame count distinct values of categorical data:\n', dataframe[col_list].nunique())
    
    def df_shape(self, dataframe):
        print('DataFrame shape:\n', dataframe.shape)
    
    def df_null_percent(self, dataframe):
        print('DataFrame percentage of null values:\n', round(dataframe.isnull().sum()/len(dataframe)*100, 2))


class Plotter:
    def __init__(self):
        pass

    def plot_null(self, dataframe):
        msno.bar(dataframe)
    
    def plot_hist_kde(self, dataframe, col, title):
        sns.histplot(data=dataframe, x=col, kde=True)
        plt.title(title)
        plt.show()

    def plot_kde_all_grid(self, dataframe): 
        numeric_features = ['loan_amount',
                    'funded_amount',
                    'funded_amount_inv',
                    'int_rate',
                    'instalment',
                    'annual_inc',
                    'dti',
                    'delinq_2yrs', 
                    'inq_last_6mths', 
                    'open_accounts', 
                    'total_accounts', 
                    'out_prncp', 
                    'out_prncp_inv', 
                    'total_payment', 
                    'total_payment_inv', 
                    'total_rec_prncp', 
                    'total_rec_int', 
                    'total_rec_late_fee', 
                    'recoveries', 
                    'collection_recovery_fee', 
                    'last_payment_amount', 
                    'collections_12_mths_ex_med']
        
        def facet_hist(data, **kwargs):
            ax = plt.gca()
            # Plot the histogram with kde
            sns.histplot(data=data, x='value', kde=True, **kwargs)
            # Get skewness for the facet's data
            skew_value = data['value'].skew()
            # Annotate the facet with the skewness value
            ax.text(0.7, 0.7, f"Skew: {skew_value:.2f}", 
                    transform=ax.transAxes, fontsize=9,
                    bbox=dict(facecolor='white', alpha=0.7))

        f = pd.melt(dataframe, value_vars=numeric_features)
        g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=False)
        g.map_dataframe(facet_hist)
        plt.show()

    def plot_box_plots_grid(self, dataframe, *args):
        def outlier_num(dataframe, col):
            Q1 = dataframe[col].quantile(0.25)
            Q3 = dataframe[col].quantile(0.75)
            IQR = Q3-Q1
            outliers = dataframe[(dataframe[col]<(Q1-1.5*IQR)) | (dataframe[col]>(Q3+1.5*IQR))]
            return(len(outliers[col]))

        fig, axs = plt.subplots(8, 3, figsize=(10, 30))
        axs = axs.flatten()

        for i, col in enumerate(args):
            sns.boxplot(data=dataframe, y=col, ax=axs[i], flierprops=dict(marker='o', markerfacecolor='red', 
                    markersize=4, markeredgewidth=0.1))
            axs[i].text(0.7, 0.80, f'Number of \nOutliers: {outlier_num(dataframe, col)}', transform=axs[i].transAxes,
                    fontsize=10, color='black', backgroundcolor='white', alpha=0.7)
    
            
        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self, dataframe):
        fig, ax = plt.subplots(figsize=(14,14))  
        sns.heatmap(dataframe.corr(numeric_only=True).round(2), cmap='coolwarm', annot=True, annot_kws={'fontsize':8}, linewidths=.5)
        plt.yticks(size=10)
        plt.xticks(size=10)
        plt.show()

    def plot_barplot_all_grid(self, dataframe, *args):
        fig, axs = plt.subplots(6, 2, figsize=(15, 40))
        fig.suptitle('Discrete Probability Distribution', fontsize=18)
        axs = axs.flatten()
        for i, col in enumerate (args):
            probs=dataframe[col].value_counts(normalize=True)
            sns.barplot(y=probs.values, x=probs.index, ax=axs[i])
            axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=90)
            axs[i].set_xlabel('Values')
            axs[i].set_ylabel('Probability')
        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show()
    
    def plot_two_barplots(self, x_values_1, y_values_1, x_label_1, y_label_1, title_1, x_value_2, y_values_2, x_label_2, y_label_2, title_2, plot_title):
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        sns.barplot(x=x_values_1, y=y_values_1, ax=axs[0])
        sns.barplot(x=x_value_2, y=y_values_2, ax=axs[1])

        axs[0].set_xlabel(x_label_1)
        axs[1].set_xlabel(x_label_2)

        axs[0].set_ylabel(y_label_1)
        axs[1].set_ylabel(y_label_2)

        axs[0].set_title(title_1)
        axs[1].set_title(title_2)

        plt.suptitle(plot_title, fontsize='18')
        plt.show()


class Analysis:
    def __init__(self):
        pass

    def monthly_instalment_amount(self, dataframe, period: int):
        dataframe['total_to_be_paid'] = dataframe['instalment']*dataframe['term']
        instalments = []
        for i in range(1, (period+1)):
            result = dataframe['instalment'].sum()
            instalments.append(round(result*i, 2))
        return instalments

    def monthly_instalment_percentage_outstanding(self, dataframe, period: int):
        instalments = self.monthly_instalment_amount(dataframe, period)
        percentage_results = []
        for i in instalments:
            percentage_results.append(round(i/(dataframe['total_to_be_paid'].sum()-dataframe['total_payment'].sum())*100,2))
        return percentage_results
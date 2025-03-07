import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns


class DataTransform:
    """
    A collection of methods for transforming and cleaning loan data.
    """
    def __init__(self):
        pass
    
    def date_format(self, dataframe, *args):
        """
        Convert specified columns in the dataframe to datetime format.

        Parameters:
            dataframe: The dataframe containing the columns to convert.
            *args: Column names (as strings) to be converted to datetime.

        Returns:
            The dataframe with the specified columns converted to datetime and errors as NaN.
        """
        for col in args:
            dataframe[col] = pd.to_datetime(dataframe[col], format='%b-%Y', errors='coerce')
        return(dataframe)
    
    def employment_number_system(self, dataframe, col):
        """
        Map employment length column values from string to a numeric scale and convert the column to numeric type.

        Parameters:
            dataframe: The dataframe containing the employment length column.
            col (str): The column name representing employment length.

        Returns:
            The dataframe with the employment length column converted to numeric values.
        """
        map_dict = {'<1 year':'1', '1 year':'2', '2 years':'3', '3 years':'4', '4 years':'5', '5 years':'6', '6 years':'7', '7 years':'8', '8 years':'9', '9 years':'10', '10+ years':'11'}
        dataframe[col] = dataframe[col].map(map_dict)
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def numeric_format(self, dataframe, col, phrase):
        """
        Remove a specified phrase from a column and convert it to numeric.

        Parameters:
            dataframe: The dataframe containing the column.
            col (str): The column name.
            phrase (str): The phrase to remove from the column's values.

        Returns:
            The dataframe with the column converted to numeric and errors as NaN
        """
        dataframe[col] = dataframe[col].str.replace(f'{phrase}', '')
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def impute_data_median(self, dataframe, *args):
        """
        Impute missing values in specified columns with the median of that column.

        Parameters:
            dataframe: The dataframe with missing values.
            *args: Column names to impute.

        Returns:
            The dataframe with missing values filled with the median.
        """
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].median())
        return(dataframe)
    
    def impute_data_mean(self, dataframe, *args):
        """
        Impute missing values in specified columns with the mean of each column.

        Parameters:
            dataframe: The dataframe with missing values.
            *args: Column names to impute.

        Returns:
            The dataframe with missing values filled with the mean.
        """
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
        return(dataframe)

    def correct_skew_log_transform(self, dataframe, *args):
        """
        Apply a logarithmic transformation to specified columns to reduce skewness.

        Parameters:
            dataframe: The dataframe containing the columns.
            *args: Column names to transform.

        Returns:
            The dataframe with log-transformed columns.
        """
        for col in args:
            dataframe.loc[:, col] = dataframe[col].map(lambda i: np.log(i) if i > 0 else 0.0)
        return(dataframe)

    def correct_skew_sqrt(self, dataframe, *args):   
        """
        Apply a square root transformation to specified columns to reduce skewness.

        Parameters:
            dataframe: The dataframe containing the columns.
            *args: Column names to transform.

        Returns:
            The dataframe with square root-transformed columns.
        """
        for col in args:
            dataframe[col] = dataframe[col].map(lambda i: np.sqrt(i))
        return(dataframe)
    

class DataFrameInfo:
    """
    A collection of methods to display and summarize dataframe information.
    """
    def __init__(self):
        pass
    
    def df_data_types(self, dataframe):
        """
        Print the data types of each column in the dataframe using pandas dtype.

        Parameters:
            dataframe: The dataframe to inspect.
        """
        print('DataFrame data types:\n', dataframe.dtypes)
    
    def df_statistical_values(self, dataframe):
        """
        Print the statistical summary of the dataframe using pandas describe. 

        Parameters:
            dataframe: The dataframe to summarize.
        """
        print('DataFrame statistical values:\n', dataframe.describe())

    def column_basic_statistics(self, dataframe, *args):
        """
        Print basic statistics (mean, median, mode, standard deviation) for specified columns.

        Parameters:
            dataframe: The dataframe to analyze.
            *args: Column names for which to compute statistics.
        
        The method uses a for loop for identify the mean, median, mode and standard deviation for each column 
        passed and prints the values.
        """
        for col in args:
            mean_value = round(dataframe[col].mean(), 2)
            median_value = round(dataframe[col].median(), 2)
            mode_value = (dataframe[col].mode()[0])
            std_value = round(dataframe[col].std(), 2)
            print(f'{col}: Mean={mean_value}, Median={median_value}, Mode={mode_value}, Standard deviation={std_value}')
    
    def categorical_distinct_values(self, dataframe):
        """
        Print the count of distinct values for a set of categorical columns.

        Parameters:
            dataframe: The dataframe to analyze.

        The method uses pandas nunique to print the number of unique values in the catergorical columns which is 
        provided in a list.
        """
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
        """
        Print the shape (number of rows and columns) of the dataframe using pandas shape.

        Parameters:
            dataframe: The dataframe to inspect.
        """
        print('DataFrame shape:\n', dataframe.shape)
    
    def df_null_percent(self, dataframe):
        """
        Print the percentage of null values in each column of the dataframe.

        Parameters:
            dataframe: The dataframe to inspect.
        
        The method uses pandas isnull to find the number of null values and finds the sum for in each column of 
        the dataframe. Then the percentage is calculated. 
        """
        print('DataFrame percentage of null values:\n', round(dataframe.isnull().sum()/len(dataframe)*100, 2))


class Plotter:
    """
    A collection of methods for creating various visualizations.
    """
    def __init__(self):
        pass

    def plot_null(self, dataframe):
        """
        Plot a bar chart of missing data using missingno.

        Parameters:
            dataframe: The dataframe with missing data.
        """
        msno.bar(dataframe)
    
    def plot_hist_kde(self, dataframe, col, title):
        """
        Plot a histogram with a kernel density estimate (KDE) for a given column.

        Parameters:
            dataframe: The dataframe to plot.
            col (str): The column to plot.
            title (str): The title of the plot.
        
        The method uses Seaborn's histplot and pyplot to add a title for the graph.
        """
        sns.histplot(data=dataframe, x=col, kde=True)
        plt.title(title)
        plt.show()

    def plot_kde_all_grid(self, dataframe): 
        """
        Plot histograms with KDE for all numeric features in the dataframe, arranged in a grid.
        Each subplot is annotated with its skewness.

        Parameters:
            dataframe: The dataframe containing numeric features.

     
        This method first defines a list of numeric features to analyze. The facet_hist function plots a histogram 
        with a KDE for the data's "value" column, calculates the skewness of that column, and then annotates the 
        plot with the skewness value. It first obtains the current axis, plots the data, and then places a text label 
        on the axis.Pandas melt is used to reshape the dataframe from wide to long format, so that each numeric column
        is represented as a variable with its corresponding values. A FacetGrid is created to arrange the plots in a 
        grid, where each subplot corresponds to one numeric feature. 
        """
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
        """
        Plot a grid of box plots for specified columns, annotating each plot with the number of outliers.

        Parameters:
            dataframe: The dataframe to plot.
            *args: Column names to plot.
        
        The outlier_num funcitoncalculates the number of outliers for each column using the IQR method. 
        A figure with subplots is created using pyplots subplots. The for loop iterates over each column 
        provided, creating a boxplot on the corresponding subplot (axs[i]) and then annotating that subplot 
        with the number of outliers, calculated with the outlier_num function.
        """
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
        """
        Plot a heatmap of the correlation matrix for the dataframe's numeric columns.

        Parameters:
            dataframe: The dataframe to analyze.
        
        The method creates figure with pyplots subplots to control the size of the figure. Seaborn's 
        heatmap is used to create heatmap, using the data from pandas .corr to compute pairwise 
        correlation of columns. 
        """
        fig, ax = plt.subplots(figsize=(14,14))  
        sns.heatmap(dataframe.corr(numeric_only=True).round(2), cmap='coolwarm', annot=True, annot_kws={'fontsize':8}, linewidths=.5)
        plt.yticks(size=10)
        plt.xticks(size=10)
        plt.show()

    def plot_barplot_all_grid(self, dataframe, *args):
        """
        Plot a grid of bar plots for discrete probability distributions of specified columns.

        Parameters:
            dataframe: The dataframe to plot.
            *args: Column names to plot.

        The method creates figure with subplots using pyplots subplots and for each specified column,
        calculates the normalized value counts (the probability distribution) and plots these as a bar 
        plot. Here, .index retrieves the unique category labels from the Series, while .values returns 
        their corresponding frequency values, which are used as the x-axis and y-axis data respectively 
        in the bar plot. The layout is adjusted to prevent overlapping.
        """
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
        """
        Plot two bar plots side by side.

        Parameters:
            x_values_1, y_values_1 (list): Data for the first bar plot.
            x_label_1 (str): X-axis label for the first plot.
            y_label_1 (str): Y-axis label for the first plot.
            title_1 (str): Title for the first plot.
            x_value_2, y_values_2 (list): Data for the second bar plot.
            x_label_2 (str): X-axis label for the second plot.
            y_label_2 (str): Y-axis label for the second plot.
            title_2 (str): Title for the second plot.
            plot_title (str): Overall title for the figure.

        The method uses the axs index to plot the correct data in the right graph. 
        """
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

    def plot_two_line_graphs(self, x_values_1, y_values_1, x_label_1, y_label_1, title_1, x_value_2, y_values_2, x_label_2, y_label_2, title_2, plot_title):
        """
        Plot two line graphs side by side.

        Parameters:
            x_values_1, y_values_1 (list): Data for the first line graph.
            x_label_1 (str): X-axis label for the first graph.
            y_label_1 (str): Y-axis label for the first graph.
            title_1 (str): Title for the first graph.
            x_values_2, y_values_2 (list): Data for the second line graph.
            x_label_2 (str): X-axis label for the second graph.
            y_label_2 (str): Y-axis label for the second graph.
            title_2 (str): Title for the second graph.
            plot_title (str): Overall title for the figure.

        The method uses the axs index to plot the correct data in the right graph. 
        """
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        axs[0].plot(x_values_1, y_values_1)
        axs[1].plot(x_value_2, y_values_2)

        axs[0].set_xlabel(x_label_1)
        axs[1].set_xlabel(x_label_2)

        axs[0].set_ylabel(y_label_1)
        axs[1].set_ylabel(y_label_2)

        axs[0].set_title(title_1)
        axs[1].set_title(title_2)

        plt.suptitle(plot_title, fontsize='16')
        plt.tight_layout()
        plt.show()
    
    def pie_chart(self, values:list, labels: list, title, explode: list = None):
        """
        Plot a pie chart using the provided values and labels, with an optional explode parameter.

        Parameters:
            values (list): The numeric values for the pie slices.
            labels (list): The labels for each slice.
            title (str): The title of the pie chart.
            explode (list, optional): List of explode values for each slice. Defaults to None.
        
        The method uses an if statement to check if an explode has been provided. If so, it is computed 
        in pie chart, and if not a pie chart is computed without an explode. 
        """
        data = np.array(values)
        data_labels = labels
        fig, ax = plt.subplots()

        if explode is not None:
            ax.pie(data, labels=data_labels, autopct='%1.1f%%', explode=explode)
        else:
            ax.pie(data, labels=data_labels, autopct='%1.1f%%')

        plt.title(title, y=1.05)
        plt.show()

    def plot_three_line_chart(self, x1, y1, label1, x2, y2, label2, x3, y3, label3, xlabel, ylabel, title):
        """
        Plot three line charts on a single figure with legends.

        Parameters:
            x1, y1 (list): Data for the first line chart.
            label1 (str): Label for the first line.
            x2, y2 (list): Data for the second line chart.
            label2 (str): Label for the second line.
            x3, y3 (list): Data for the third line chart.
            label3 (str): Label for the third line.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            title (str): Title of the chart.
        """
        plt.plot(x1, y1, label=label1,  marker='o')
        plt.plot(x2, y2, label=label2, marker='x')
        plt.plot(x3, y3, label=label3)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=90)
        plt.title(title)
        plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))
        plt.show()

class Analysis:
    """
    A collection of methods for performing revenue and repayment analysis on loan data.
    """
    def __init__(self):
        pass

    def monthly_instalment_amount(self, dataframe, period: int):
        """
        Calculate the cumulative instalment amounts over a given number of months.

        Parameters:
            dataframe: The dataframe containing loan data.
            period (int): The number of months over which to calculate instalment amounts.

        Returns:
            A list of cumulative instalment amounts for each month up to the given period. 

        The mehtod calculates the cumulative instalment amounts over a specified period. 
        It multiplies the sum of all instalments by each month (from 1 up to the given period) 
        to determine the total amount that would be paid per month over that time. 
        """
        dataframe['total_to_be_paid'] = dataframe['instalment']*dataframe['term']
        instalments = []
        for i in range(1, (period+1)):
            result = dataframe['instalment'].sum()
            instalments.append(round(result*i, 2))
        return instalments

    def monthly_instalment_percentage_outstanding(self, dataframe, period: int):
        """
        Calculate the monthly percentage of outstanding instalments relative to the total expected payment.

        Parameters:
            dataframe: The dataframe containing loan data.
            period (int): The number of months over which to calculate the percentages.

        Returns:
            A list of percentage values representing the outstanding instalment amount per month.
        
        This method uses the cumulative instalment amounts from the monthly_instalment_amount method 
        and compares them to the outstanding payments.
        """
        instalments = self.monthly_instalment_amount(dataframe, period)
        percentage_results = []
        for i in instalments:
            percentage_results.append(round(i/(dataframe['total_to_be_paid'].sum()-dataframe['total_payment'].sum())*100,2))
        return percentage_results

    def not_paid_percentage_by_group(self, dataframe, column):
        """
        Calculate the percentage of unpaid amounts based on groups of a given column.

        Parameters:
            dataframe: The dataframe containing loan data.
            column (str): The column name to group by.

        Returns:
            A tuple containing:
                - An array of percentages of unpaid amounts for each group.
                - A list of group labels.

        THe method groups the values of a specific column and calculates, for each group, the percentage of 
        the total expected loan amount that remains unpaid. It returns both the percentages and the group labels.
        """
        summary = dataframe.groupby(column, observed=True).agg(
        paid_loan = ('total_payment','sum'),
        total_loan = ('total_to_be_paid', 'sum')).reset_index()

        not_paid = summary['total_loan'].values - summary['paid_loan'].values
        percent = (not_paid/summary['total_loan'].values*100)
        labels = list(summary[column].values)
        return(percent, labels)
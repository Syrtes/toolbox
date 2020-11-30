# Import from standard library
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

def distribution_plot(df, numerical_features):
    """Plot the distributions for a list of numerical features from a dataframe df"""
    for feature in features:
        fig, ax =plt.subplots(1,3,figsize=(20,5))
        ax[0].set_title(f"Distribution of: {numerical_feature}")
        sns.histplot(data = df[feature], kde=True, ax=ax[0])
        ax[1].set_title(f"Boxplot of: {numerical_feature}")
        sns.boxplot(x = df[feature], ax=ax[1])
        ax[2].set_title(f"Gaussianity of: {numerical_feature}")
        qqplot(data = df[feature],line='s',ax=ax[2])

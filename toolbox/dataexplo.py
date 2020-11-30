# Import from standard library
import matplotlib.pyplot as plt

def distribution_plot(numerical_features):
    """Plot the distribution for a list of numerical features"""
    for numerical_feature in numerical_features:
        fig, ax =plt.subplots(1,3,figsize=(20,8))
        ax[0].set_title(f"Distribution of: {numerical_feature}")
        sns.histplot(data = numerical_data[numerical_feature], kde=True, ax=ax[0])
        ax[1].set_title(f"Boxplot of: {numerical_feature}")
        sns.boxplot(numerical_data[numerical_feature], ax=ax[1])
        ax[2].set_title(f"Gaussianity of: {numerical_feature}")
        qqplot(numerical_data[numerical_feature],line='s',ax=ax[2])
        fig.show()

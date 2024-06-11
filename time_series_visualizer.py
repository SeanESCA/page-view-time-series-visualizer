import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    'fcc-forum-pageviews.csv', 
    index_col=['date'], 
    parse_dates=['date']
)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = df.plot(
        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
        xlabel='Date',
        ylabel='Page Views'
        ).get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_bar.index.rename(['year', 'month'], inplace=True)
    df_bar.reset_index(level=['year', 'month'], inplace=True)
    df_pivot = df_bar.pivot(index='year', columns='month')

    # Draw bar plot
    fig, ax = plt.subplots()
    df_pivot.plot.bar(
        y='value',
        use_index=True,
        title='Months',
        xlabel='Years',
        ylabel='Average Page Views',
        ax=ax)
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(
        df_box['month'],
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        ordered=True
    )

    # Draw box plots (using Seaborn)
    fig, (ax_year, ax_month) = plt.subplots(1, 2)
    sns.boxplot(
        data=df_box,
        x='year',
        y='value',
        orient='v',
        ax=ax_year    
    )
    sns.boxplot(
        data=df_box,
        x='month',
        y='value',
        orient='v',
        ax=ax_month    
    )
    ax_year.set_title('Year-wise Box Plot (Trend)')
    ax_year.set_xlabel('Year')
    ax_year.set_ylabel('Page Views')
    ax_month.set_title('Month-wise Box Plot (Seasonality)')
    ax_month.set_xlabel('Month')
    ax_month.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

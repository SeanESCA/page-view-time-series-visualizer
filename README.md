# Page View Time Series Visualizer

Instructions for this project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

## Downgrading for Seaborn

To circumvent `sns.boxplot` throwing an `AttributeError`, NumPy needs to be downgraded manually.
```
pip install --force-reinstall numpy==1.20.3
```

See: https://forum.freecodecamp.org/t/data-analysis-with-python-projects/683279/2

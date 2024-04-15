Prepared By: Michael Cain (2024)

# Carifta Games Analysis

This repository contains Python code for analyzing the performance of nations in the Carifta Games, an annual junior athletics competition in the Caribbean region.

## Overview

The analysis focuses on the medal distribution, top-performing nations, and trends over the years based on data from 2013 to 2024.

## Data

The data used in this analysis consists of Excel files for each year's Carifta Games from 2013 to 2024. Each file contains information about the medals won by various nations.

## Code

The analysis is conducted using Python programming language and various libraries including Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

### Data Loading and Preprocessing

- Excel files for each year's Carifta Games are loaded into Pandas DataFrames.
- Additional processing includes adding a 'year' column to each DataFrame for easier analysis.

### Analysis

1. **Medal Distribution Over the Years**: 
   - A bar plot illustrating the distribution of gold, silver, and bronze medals over the years.
   
2. **Top Performing Nations Each Year**: 
   - Identification of the top-performing nations in terms of total medals each year.
   - A line plot depicting the total medals won by these nations over the years.

3. **Total Medals Over the Years**:
   - A line plot showcasing the total number of medals awarded each year.

4. **Yearly Medal Counts Comparison**:
   - A line plot comparing the yearly medal counts of selected nations.

5. **Correlation Matrix**:
   - A heatmap visualizing the correlation between rank, total medals, and gold medals.

6. **Performance Analysis for 2024**:
   - Bar plots illustrating the total medal count and medal distribution for the year 2024.

## Usage

To replicate the analysis:

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the provided Python script in your preferred environment.

## Contributing

Contributions to this project are welcome. Feel free to open issues or pull requests with any suggestions, improvements, or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

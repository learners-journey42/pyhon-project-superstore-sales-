import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load data

data = pd.read_csv('C:\\Users\\subas\\Downloads\\superstore_dataset2011-2015.csv',encoding="ISO-8859-1")


# Sidebar
st.sidebar.title("Hypotheses")
hypotheses = st.sidebar.radio("Select a hypotheses:", [
    "Technology products have the highest profit margin compared to other product categories.",
    "The East region has the highest sales compared to other regions.",
    "Sales are higher during certain months of the year.",
    "Orders with same-day shipping have the lowest rate of returned products.",
    "The company's profit is more on weekdays than on weekends."])

# Main page
st.title("Superstore Sales Dashboard")

# Hypothesis 1
if hypotheses == "Technology products have the highest profit margin compared to other product categories.":
    PROFIT_BY_CATEGORY = data.groupby('Category')['Profit'].sum().sort_values(ascending=False).reset_index()

    # Define custom color palette based on product category
    custom_palette = [
        '#8FBC8F' if category == 'Technology' else
        '#AFE1AF' if category == 'Furniture' else
        '#32CD32' if category == 'Office Supplies' else
        '#87CEFA'  # Default color for other categories
        for category in PROFIT_BY_CATEGORY['Category']
    ]

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(PROFIT_BY_CATEGORY['Profit'], labels=PROFIT_BY_CATEGORY['Category'], colors=custom_palette, autopct='%1.1f%%', textprops={'fontsize': 14})
    plt.title("Profit by Category", fontsize=16)
    st.pyplot(plt.gcf())  # Show the pie chart in Streamlit

    # Conclusion
    st.write("Conclusion: The hypothesis is supported as technology products have the highest profit margin of the three categories.")
# hypotheses 2

elif hypotheses == "The East region has the highest sales compared to other regions.":
    # Group by region and calculate the sum of sales
    SALES_BY_REGION = data.groupby('Region')['Sales'].sum().reset_index()

    # Create custom color palette based on region
    custom_palette = ['#8F9779' if region == 'East' else 
                      '#849137' if region == 'Central' else '#AFE1AF' 
                      for region in SALES_BY_REGION['Region']]

    # Create a bar plot of sales by region with custom colors
    sns.barplot(x='Region', y='Sales', data=SALES_BY_REGION, palette=custom_palette)

    # Set title and adjust x-axis labels rotation
    plt.title("Sales by Region", fontsize=16)
    plt.xlabel("Region", fontsize=11)
    plt.ylabel("Sales", fontsize=11)
    plt.xticks(rotation=45)

    # Show the plot
    st.pyplot(plt.gcf())

    # Conclusion
    st.write("Conclusion: The hypothesis is not supported as the central region has the highest sales.")

# hypotheses 3
elif hypotheses == "Sales are higher during certain months of the year.":
    # Group by month and calculate the sum of sales
    data['order_month'] = pd.DatetimeIndex(data['Order Date']).month
    month_sales = data.groupby('order_month')['Sales'].sum()

    # Create a line chart
    plt.figure(figsize=(10, 6))
    month_sales.plot(kind='line', color="#50C878")
    plt.fill_between(month_sales.index, month_sales, color="#50C878", alpha=0.3)

    # Set title and labels
    plt.title("Total Sales by Month", fontsize=16)
    plt.xlabel("Month", fontsize=14)
    plt.ylabel("Total Sales", fontsize=14)

    # Show the plot
    st.pyplot(plt.gcf())

    # Conclusion
    st.write("Conclusion: The hypothesis is supported as there is an increased number of sales during November and December.")

# Hypothesis 4

elif hypotheses == "Orders with same-day shipping have the lowest rate of returned products.":
    # Calculate the total number of orders for each shipping mode
    total_orders_by_shipping_mode = data.groupby('Ship Mode').size()

    # Calculate the total number of returned orders for each shipping mode
    returned_orders_by_shipping_mode = data[data['Profit'] < 0].groupby('Ship Mode').size()

    # Calculate the percentage of orders that are returned for each shipping mode
    return_percentage_by_shipping_mode = (returned_orders_by_shipping_mode / total_orders_by_shipping_mode) * 100

    # Define colors for each shipping mode
    colors = ['#AFE1AF' if mode == 'Same Day' else 
              '#9FE2BF' if mode == 'Second Class' else
              '#8F9779' for mode in return_percentage_by_shipping_mode.index]

    # Create the bar plot
    plt.figure(figsize=(8, 6))
    return_percentage_by_shipping_mode.plot(kind="bar", color=colors)
    plt.title("Return Percentage by Shipping Mode", fontsize=16)
    plt.xlabel("Shipping Mode", fontsize=12)
    plt.ylabel("Return Percentage", fontsize=12)
    plt.xticks(rotation=25)

    # Show the plot
    st.pyplot(plt.gcf())
    
    st.write("Conclusion: The hypothesis is supported as same-day shipping has the lowest rate of returned products.")
    
# Hypotheses 4 
       
elif hypotheses == "The company's profit is more on weekdays than on weekends.":
    # Extract the day of the week from the Order Date column
    data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()
    # Group by day of the week and calculate the mean profit
    day_profit = data.groupby('Order Day')['Profit'].sum()

    # Define custom colors based on weekdays and weekends
    custom_palette = ['#AFE1AF' if order_day not in ['Sunday', 'Saturday'] else '#50C878' for order_day in day_profit.index]

    # Plotting the bar chart with custom palette
    plt.figure(figsize=(10, 6))
    day_profit.plot(kind='bar', color=custom_palette)
    plt.title("Profit by Day of the Week", fontsize=16)
    plt.xlabel("Order Day", fontsize=12)
    plt.ylabel("Profit", fontsize=12)
    plt.xticks(rotation=25)

    # Show the plot
    st.pyplot(plt.gcf())

    
    
    
    
    
    
    
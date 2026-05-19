#
#
# import numpy as np
# import pandas as pd
# a = np.array([[1, 2,3], [3,4,5]])
# print(a)
# b = np.zeros((2, 2))
# print(b)
# c = np.ones((2, 2))
# print(c)
# d = np.eye(3)
# print(d)
# e = np.arange(0, 10, 2)
# print(e)
# f = np.linspace(0, 1, 5)
# print(f)
# g = np.random.rand(2, 2)
# print(g)
# h = np.random.randint(1, 10, (2, 2))
# print(h)
#
# print(a.shape, a.ndim, a.dtype, a.size)
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr[0,1])
# print(arr[:,1])
#
#
#
# x = np.arange(6)
# print(x)
# print(x.reshape(2,3))
# print(x.flatten())
#
#
#
# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# print(a + b)
# print(a * b)
# print(np.dot(a, b))
# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))
#
#
#
# arr = np.array([[1,20,3],[4,0,6]])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.std(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr, axis=0))
# print(np.argmax(arr))
#
#
#
# arr = np.array([[1,2],[3,4]])
# print(arr + 10)
#
#
# arr = np.array([1,2,3,4,5])
# print(arr[arr > 3])
#
#
#
# a = np.array([1,2])
# b = np.array([3,4])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(np.split(np.array([1,2,3,4]),2))
#
#
#
#
# mat = np.array([[1,2],[3,4]])
# print(np.linalg.inv(mat))
# print(np.linalg.det(mat))
# print(np.linalg.eig(mat))
#
# print("PANDAS")
# s = pd.Series([10,20,30])
# df = pd.DataFrame({
#     "A":[1,2,3],
#     "B":[4,5,6]
# })
#
#
# print(df.head())
# print(df.tail())
# print(df.info())
# print("=================================")
# print(df.describe())
#
# print(df["A"])
# print(df.loc[0])
# print(df.iloc[0])
# print("===========================")
#
# print(df[df["A"] > 1])
#
# df["C"] = df["A"] + df["B"]
# print(df)
#
# df = df.drop("C", axis=1)
# print(df.sort_values("A"))
#
# df2 = pd.DataFrame({
#     "team":["A","A","B","B"],
#     "score":[10,20,30,40]
# })
#
# print(df2.groupby("team").sum())
#
#
# left = pd.DataFrame({"id":[1,2], "val":[10,20]})
# right = pd.DataFrame({"id":[1,2], "val2":[100,200]})
#
# print(pd.merge(left, right, on="id"))
#
# df = pd.DataFrame({"A":[1,None,3]})
# print(df.isnull())
# print(df.fillna(0))
# print(df.dropna())
#
# df = pd.DataFrame({"A":[1,2,3]})
# print(df["A"].apply(lambda x: x*2))
#
#
# df = pd.DataFrame({"name":["a","b","c"]})
# print(df["name"].str.upper())
#
# dates = pd.date_range("2024-01-01", periods=3)
# df = pd.DataFrame({"date":dates})
# print(df["date"].dt.day)
#
#
#
# df = pd.DataFrame({
#     "A":["foo","foo","bar"],
#     "B":["one","two","one"],
#     "C":[1,2,3]
# })
#
# print(pd.pivot_table(df, values="C", index="A", columns="B"))
#
#
#
# df.to_csv("test.csv", index=False)
# df2 = pd.read_csv("test.csv")
# print(df2)
#
#
# import numpy as np
# import pandas as pd
#
# image = np.array([[100, 150], [200, 230]])
# image2 = np.clip(image + 50, 0, 255)
#
#
# s = np.array([10, 20, -15, 55, 30, 45])
# s2 = s[(s >= -10) & (s <= 50)]
# print(s2)
# data = np.array([10, 20, 30, 40, 50])
# normalized = (data - np.min(data)) / \
#              (np.max(data) - np.min(data))
# print(normalized)
# sales = np.array([
#     [100, 200, 150, 300, 250, 400, 350],
#     [80, 120, 160, 200, 220, 260, 300],
#     [50, 70, 90, 110, 130, 150, 170]
# ])
#
# total_per_store = np.sum(sales, axis=1)
# avg_per_day = np.mean(sales, axis=0)
#
# print(total_per_store)
# print(avg_per_day)
#
# user = np.array([[1, 0], [0, 1]])
# product= np.array([[5, 10], [2, 3]])
#
# recommendation = np.dot(user, product)
#
# print(recommendation)
#
# df_orders = pd.DataFrame({
#     "order_id": [1,2,3,4],
#     "customer": ["A","B","C","D"],
#     "amount": [100, 200, 150, 300],
#     "status": ["completed", "pending", "completed", "completed"]
# })
#
# completed = df_orders[df_orders["status"] == "completed"]
#
# total_revenue = completed["amount"].sum()
#
# top3 = completed.sort_values(by="amount", ascending=False).head(3)
#
# print(completed)
# print(total_revenue)
# print(top3)
#
# df_emp = pd.DataFrame({
#     "employee": ["A","B","C","D"],
#     "department": ["HR","IT","HR","IT"],
#     "salary": [30000, 50000, 35000, 60000]
# })
#
# avg_salary = df_emp.groupby("department")["salary"].mean()
#
# highest_dept = avg_salary.idxmax()
#
# print(avg_salary)
# print(highest_dept)
#
#
# df_missing = pd.DataFrame({
#     "A": [1, None, 3],
#     "B": [4, 5, None]
# })
#
# missing = df_missing.isnull()
#
# filled = df_missing.fillna(df_missing.mean())
#
# print(missing)
# print(filled)
# df_logs = pd.DataFrame({
#     "timestamp": pd.to_datetime(["2023-01-01", "2023-05-01", "2024-01-01"]),
#     "log_message": ["INFO start", "ERROR failed", "ERROR crash"]
# })
#
# df_logs["year"] = df_logs["timestamp"].dt.year
#
# errors = df_logs[df_logs["log_message"].str.contains("ERROR")]
#
# error_count = errors.groupby("year").size()
#
# print(errors)
# print(error_count)
#
# customers = pd.DataFrame({
#     "customer_id": [1,2],
#     "name": ["A","B"]
# })
#
# orders = pd.DataFrame({
#     "customer_id": [1,1,2],
#     "amount": [100, 150, 200]
# })
#
# merged = pd.merge(customers, orders, on="customer_id")
#
# total_purchase = merged.groupby("customer_id")["amount"].sum()
#
# print(total_purchase)







#1. IMAGE BRIGHTNESS ADJUSTMENT (Broadcasting)
# You are given a grayscale image represented as a 2D NumPy array.
# Increase the brightness of the image by adding a constant value (e.g., +50)
# using broadcasting. Ensure pixel values do not exceed 255.


# import numpy as np
#
# image = np.array([[10, 40, 200],
#                   [100, 220, 250]], dtype=np.uint8)
#
# brightness_increase = 50
#
# brightened = np.clip(image.astype(np.int16) + brightness_increase, 0, 255).astype(np.uint8)
#
# print(brightened)



#
# Q2. SENSOR DATA CLEANING (Boolean Indexing)
# You receive temperature sensor data as a NumPy array.
# Remove all invalid readings where values are less than -10 or greater than 50.

# import numpy as np
#
# temps = np.array([12, -15, 8, 51, 22, -10, 50, 60, 3])
#
# cleaned = temps[(temps >= -10) & (temps <= 50)]
#
# print(cleaned)


#Q3. NORMALIZATION FOR ML MODEL (Vectorization)
# Given a dataset (NumPy array), normalize all values between 0 and 1
# using min-max normalization.
#
#  Formula: (x - min) / (max - min)

# import numpy as np
#
# data = np.array([10, 20, 30, 40, 50])
#
# normalized = (data - data.min()) / (data.max() - data.min())
#
# print(normalized)




# Q4. MULTIPLE STORE SALES ANALYSIS (Axis operations)
# You have sales data of 3 stores for 7 days stored in a 2D NumPy array.
# Find:
# - Total sales per store
# - Average sales per day
# import numpy as np
#
# sales = np.array([
#     [120, 150, 130, 140, 160, 170, 180],
#     [200, 210, 190, 220, 230, 240, 250],
#     [ 90, 100, 110, 120, 130, 140, 150]
# ])
#
# total_per_store = sales.sum(axis=1)
# average_per_day = sales.mean(axis=0)
#
# print("Total sales per store:", total_per_store)
# print("Average sales per day:", average_per_day)




# Q5. MATRIX MULTIPLICATION IN RECOMMENDATION SYSTEM
# You are given:
# - User preference matrix
# - Product feature matrix
#
# Perform matrix multiplication to compute recommendation scores.
# import numpy as np
#
# user_preferences = np.array([
#     [5, 3, 0],
#     [4, 1, 2]
# ])
#
# product_features = np.array([
#     [1, 0, 1],
#     [0, 1, 1],
#     [1, 1, 0]
# ])
#
# recommendation_scores = user_preferences @ product_features.T
# print(recommendation_scores)




# Q6. E-COMMERCE ORDER ANALYSIS (Filtering + Aggregation)
# You are given a DataFrame with columns:
# ["order_id", "customer", "amount", "status"]
#
# Tasks:
# - Filter only completed orders
# - Calculate total revenue
# - Find top 3 highest orders

# import pandas as pd
#
#
# df = pd.DataFrame({
#     "order_id": ["O1", "O2", "O3", "O4", "O5"],
#     "customer": ["A", "B", "A", "C", "B"],
#     "amount": [120, 250, 80, 300, 180],
#     "status": ["completed", "pending", "completed", "completed", "completed"]
# })
#
# completed_orders = df[df["status"] == "completed"]
# total_revenue = completed_orders["amount"].sum()
# top_3_orders = completed_orders.nlargest(3, "amount")
#
# print(completed_orders)
# print("Total revenue:", total_revenue)
# print(top_3_orders)





# Q7. EMPLOYEE PERFORMANCE REPORT (GroupBy)
# Given a dataset:
# ["employee", "department", "salary"]
#
# Tasks:
# - Find average salary per department
# - Find department with highest average salary

# import pandas as pd
#
# df = pd.DataFrame({
#     "employee": ["Asha", "Ben", "Chen", "Divya", "Ethan"],
#     "department": ["HR", "IT", "HR", "IT", "Finance"],
#     "salary": [50000, 80000, 55000, 90000, 70000]
# })
#
# avg_salary_by_dept = df.groupby("department")["salary"].mean()
# highest_avg_dept = avg_salary_by_dept.idxmax()
# highest_avg_value = avg_salary_by_dept.max()
#
# print(avg_salary_by_dept)
# print("Department with highest average salary:", highest_avg_dept)
# print("Highest average salary:", highest_avg_value)





# Q8. DATA CLEANING PIPELINE (Missing Values)
# You are given a dataset with missing values.
#
# Tasks:
# - Identify missing values
# - Fill missing values using mean

# import pandas as pd
#
# df = pd.DataFrame({
#     "age": [25, None, 30, 40],
#     "salary": [50000, 60000, None, 80000]
# })
#
# missing = df.isnull()
# print(missing)
#
# df_filled = df.fillna(df.mean(numeric_only=True))
#
# print(df_filled)



# Q9. LOG FILE ANALYSIS (String + DateTime)
# You have a dataset with columns:
# ["timestamp", "log_message"]
#
# Tasks:
# - Extract year from timestamp
# - Find logs containing "ERROR"
# - Count number of errors per year
































#
# Q10. MERGING MULTIPLE DATA SOURCES (Join/Merge)
# You are given:
# - Customers DataFrame
# - Orders DataFrame
#
# Tasks:
# - Merge both datasets on customer_id
# - Find total purchase amount per customer

# import pandas as pd
#
# customers = pd.DataFrame({
#     "customer_id": [1, 2, 3],
#     "customer_name": ["Asha", "Ben", "Chen"]
# })
#
# orders = pd.DataFrame({
#     "customer_id": [1, 1, 2, 3, 3],
#     "order_id": ["O1", "O2", "O3", "O4", "O5"],
#     "amount": [200, 150, 300, 100, 250]
# })
#
# # Merge both datasets
# merged_df = pd.merge(customers, orders, on="customer_id", how="inner")
#
# # Total purchase amount per customer
# total_purchase = merged_df.groupby(["customer_id", "customer_name"])["amount"].sum().reset_index()
#
# print(merged_df)
# print(total_purchase)

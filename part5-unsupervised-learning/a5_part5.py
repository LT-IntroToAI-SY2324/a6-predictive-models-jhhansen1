import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")
x = data[["Annual Income", "Spending Score"]]

#standardize the data
x_data=StandardScaler().fit_transform(x)

#the value of k has been defined for you
k = 5
#apply the kmeans algorithm
km=KMeans(n_clusters=k.fit(x_data))


#get the centroid and label values
centroid_values=km.cluster_centers_
label_values=km.labels_

#sets the size of the graph
plt.figure(figsize=(5,4))

#use a for loop to plot the data points in each cluster

for i in range(k):
    cluster=x_data[label_values==i]
    plt.scatter(cluster[:,0], cluster[:,1])
#plot the centroids
plt.scatter(centroid_values[:,0], centroid_values[:,1], marker=":)", s=100, c="g", label="centroid" )
            
#shows the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()
import csv
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans

class ClusterCustomers(object):

	clusters = 0
	segment = []

	def __init__(self, n):
		self.clusters = n;
		self.labels = [];

	def clusteringAlgorithm(self):
         dataset=pd.read_csv('Customer Data.csv')

         profitMargin = dataset['Profit Margin'].values
         volume = dataset['Volume'].values
         relationship = dataset['Relationship'].values
         credit = dataset['Credit History'].values

         customerData = np.array(list(zip(profitMargin,volume, relationship, credit)))

         kmeans = KMeans(n_clusters=self.clusters)
         kmeans = kmeans.fit(customerData)
         self.segment = kmeans.predict(customerData)
         

	def modifyCsv(self):
		csv_input = pd.read_csv('Customer Data.csv')
		csv_input['Cluster'] = self.segment
		csv_input.to_csv('Output Customer Data.csv', index=False)


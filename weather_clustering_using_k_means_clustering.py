# -*- coding: utf-8 -*-
"""Weather Clustering using K-Means Clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11YNvIfQGFgFNYdrK11sivx-io3ieVrJq
"""

import random
import math
import csv
import numpy as np
import sklearn
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


class KMeansClustering:
    def __init__(self):
        self.training_attributes = None
        self.title_attributes = None
        self.cluster_attributes = None
        self.cluster_euclidean = None
        self.nearest_cluster = None

    def set_train_data(self):
        result_list = []
        title_list = []
        with open('datacuaca.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            first_row = True
            for row in reader:
                if first_row:
                    title_list = row
                    first_row = False
                else:
                    result_list.append(row)

        print(f"Data telah masuk dengan jumlah baris = {len(result_list)} dan kolom = {len(result_list[0])}\n")

        self.title_attributes = title_list
        self.training_attributes = [list(map(float, row)) for row in result_list]

    def test_data(self):
        nilai_k = int(input("Masukkan nilai k (jumlah cluster): "))
        self.cluster_attributes = [[0] * len(self.training_attributes[0]) for _ in range(nilai_k)]
        self.cluster_euclidean = [[0] * (nilai_k + 1) for _ in range(len(self.training_attributes))]

        cluster_check = [-1] * nilai_k
        for i in range(nilai_k):
            while True:
                idx = random.randint(0, len(self.training_attributes) - 1)
                if idx not in cluster_check[:i]:
                    cluster_check[i] = idx
                    self.cluster_attributes[i] = self.training_attributes[idx]
                    break
        return nilai_k

    def get_result(self):
        nilai_k = len(self.cluster_attributes)
        for i in range(len(self.training_attributes)):
            for j in range(nilai_k):
                euclidean = sum([(a - b) ** 2 for a, b in zip(self.training_attributes[i], self.cluster_attributes[j])])
                self.cluster_euclidean[i][j] = math.sqrt(euclidean)

            nearest_cluster_idx = min(range(nilai_k), key=lambda j: self.cluster_euclidean[i][j])
            self.cluster_euclidean[i][nilai_k] = nearest_cluster_idx + 1

    def view_data(self, data_array):
        for row in data_array:
            print("\t".join([f"{x:.2f}" for x in row]))
        print()

    def view_data_with_clusters(self):
        for i in range(len(self.training_attributes)):
            print("\t".join(map(str, self.training_attributes[i])), end="\t")
            print("\t".join([f"{x}" for x in self.cluster_euclidean[i]]), end="\n")
        print()

    def set_nearest_cluster(self):
        self.nearest_cluster = [int(self.cluster_euclidean[i][-1]) for i in range(len(self.training_attributes))]

    def reclustering(self):
        nilai_k = len(self.cluster_attributes)
        j_nearest_cluster = [0] * nilai_k

        for i in range(nilai_k):
            self.cluster_attributes[i] = [0] * len(self.training_attributes[0])

        for i in range(len(self.training_attributes)):
            for k in range(nilai_k):
                if self.nearest_cluster[i] == (k + 1):
                    for j in range(len(self.training_attributes[i])):
                        self.cluster_attributes[k][j] += self.training_attributes[i][j]

                    j_nearest_cluster[k] += 1

        for k in range(nilai_k):
            for j in range(len(self.cluster_attributes[k])):
                self.cluster_attributes[k][j] /= j_nearest_cluster[k]

    def compare_nearest_cluster(self):
        same = True
        for i in range(len(self.training_attributes)):
            if int(self.cluster_euclidean[i][-1]) != self.nearest_cluster[i]:
                same = False
                break

        if same:
            print("\nNearest Cluster Sama, Proses Berhenti")
        else:
            print("\nNearest Cluster Beda, Proses Dilanjutkan")
            print("\n")

        return same

    def count_clusters(self):
        cluster_counts = {}
        for cluster_id in self.nearest_cluster:
            if cluster_id in cluster_counts:
                cluster_counts[cluster_id] += 1
            else:
                cluster_counts[cluster_id] = 1

        print("\nJumlah data di setiap cluster:")
        for cluster_id, count in sorted(cluster_counts.items()):
            print(f"Cluster {cluster_id}: {count} data")

    def visualize_clusters_with_pca(self):

    # Reduce dimensions to 2D using PCA
        pca = PCA(n_components=2)
        data_2d = pca.fit_transform(self.training_attributes)
        cluster_centers_2d = pca.transform(self.cluster_attributes)

        clusters = np.array(self.nearest_cluster)

        # Assign unique colors to each cluster
        colors = plt.cm.get_cmap('tab10', len(self.cluster_attributes))

        # Plot each cluster
        for k in range(len(self.cluster_attributes)):
            cluster_data = data_2d[clusters == (k + 1)]
            plt.scatter(cluster_data[:, 0], cluster_data[:, 1],
                        label=f'Cluster {k + 1}', alpha=0.6, s=30, c=[colors(k)])

        # Plot the centroids
        plt.scatter(cluster_centers_2d[:, 0], cluster_centers_2d[:, 1],
                    color='black', marker='x', s=100, label='Centroids')

        # Add labels and legend
        plt.title('Weather Clustering using K-Means Clustering')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    KMeans = KMeansClustering()
    KMeans.set_train_data()
    nilai_k = KMeans.test_data()
    KMeans.view_data(KMeans.cluster_attributes)
    KMeans.get_result()
    KMeans.view_data_with_clusters()

    nearest_cluster_same = False
    index = 1

    while not nearest_cluster_same:
        index += 1
        print(f"Iterasi ke-{index}")
        KMeans.set_nearest_cluster()
        KMeans.reclustering()
        KMeans.view_data(KMeans.cluster_attributes)
        KMeans.get_result()
        KMeans.view_data_with_clusters()
        nearest_cluster_same = KMeans.compare_nearest_cluster()

    KMeans.count_clusters()
    KMeans.visualize_clusters_with_pca()

if __name__ == "__main__":
    main()
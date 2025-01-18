# WEATHER CLUSTERING ANALYSIS

This project implements the K-Means clustering algorithm in Python to analyze hourly weather data in Banyuwangi during January 2022. The dataset includes multidimensional weather variables—temperature, humidity, rainfall, solar radiation, and wind speed. The clustering results identify distinct weather patterns and visualized effectively using PCA (Principal Component Analysis)


## Dataset Information

- ### Source : BMKG Banyuwangi
- ### Variables :
  - Temperature (°C) : Hourly average temperature
  - Humidity (%) : Hourly average humidity
  - Rainfall (mm) : Hourly average precipitaion levels
  - Solar Radiation (W/m²) : Hourly average solar radiation
  - Wind Speed (m/s) : Hourly average wind speed
- ## Time Period : 1 January 2022 to 31 January 2022
- ## Total Data Points : 744 records (24 hours x 31 days)


## Methodology
1. ### Clustering Approach
   - Algorithm Used : K-Means Clustering
     - Choses for its efficiency in grouping high-dimensional data based on similarity across variables
3. ### Dimensionality Reduction for Visualization
   - Algorithm Used : PCA (Principal Component Analysis)
     - Used to reduce the five-dimensional data into two principal components for easier interpretation and visualization


## Result and Interpretation
### Centroid Center
![{DED5AE5D-631C-4131-9CFF-A5AF6ADAEF86}](https://github.com/user-attachments/assets/1209d07e-b534-4ace-bcf9-696ed0c4dd1c)

Based on the final results of centroid center, the data has been grouped into three clusters. The conclusions for each cluster are as follows:
- Cluster 1 : contains data representing cloudly weather
- Cluster 2 : contains data representing rainy weather
- Cluster 3 : contains data representing hot weather

### List of Data and Their Corresponding Clusters
![{BAA77C9D-0796-4E51-83AA-849AD6293C2B}](https://github.com/user-attachments/assets/c44777e1-d37f-4fd0-b1b8-81f130e273c4)

### Data Count for Each Cluster
![{CC6D5282-65BA-492C-A3A2-7C2D445822D7}](https://github.com/user-attachments/assets/d483b3f0-fcf3-4597-9039-7eeb089442f1)

Based on the output, it is observed that most data fall into Cluster 2. This indicates that during Januari 2022, the Banyuwangi region predominantly rainy weather

### Cluster Visualization
![image](https://github.com/user-attachments/assets/36894c20-dd1e-46ea-bf38-32c82f6871ef)

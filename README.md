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
- ### Time Period : 1 January 2022 to 31 January 2022
- ### Total Data Points : 744 records (24 hours x 31 days)


## Methodology
1. ### Clustering Approach
   - Algorithm Used : K-Means Clustering
     - Choses for its efficiency in grouping high-dimensional data based on similarity across variables
3. ### Dimensionality Reduction for Visualization
   - Algorithm Used : PCA (Principal Component Analysis)
     - Used to reduce the five-dimensional data into two principal components for easier interpretation and visualization


## Result and Interpretation
### Centroid Center
![{E6AFCBE9-E45A-4DF0-9DF3-1D1BFE9D45E3}](https://github.com/user-attachments/assets/6ea70705-b666-4049-828c-9fb5da4cbe68)

### Cluster Characteristics and Weather Classification
- Cluster 1 : Rainy Weather
  - Characteristic :
    - Lower temperature (25.89°C) and higher humidity (84.75%)
    - Significant rainfall (9.92 mm)
    - Very low solar radiation (25.58 W/m²), suggesting dense cloud cover
    - Low wind speed (1.70 m/s)
  - Reason for Classification :
    This cluster represents rainy weather, characterized by significant rainfall, high humidity, and minimal sunlight due to dense cloud clover
- Cluster 2 : Clear Weather
- Cluster 3 : Cloudly Weather
  - 

### List of Data and Their Corresponding Clusters
![{BAA77C9D-0796-4E51-83AA-849AD6293C2B}](https://github.com/user-attachments/assets/c44777e1-d37f-4fd0-b1b8-81f130e273c4)

### Data Count for Each Cluster
![{CC6D5282-65BA-492C-A3A2-7C2D445822D7}](https://github.com/user-attachments/assets/d483b3f0-fcf3-4597-9039-7eeb089442f1)

Based on the output, it is observed that most data fall into Cluster 2. This indicates that during Januari 2022, the Banyuwangi region predominantly rainy weather

### Cluster Visualization
![image](https://github.com/user-attachments/assets/36894c20-dd1e-46ea-bf38-32c82f6871ef)

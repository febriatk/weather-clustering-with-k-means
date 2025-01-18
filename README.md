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
![{8B4B9FD5-46B1-4201-AF35-C52F717BB647}](https://github.com/user-attachments/assets/3aa5a8d1-92c3-4608-890a-adee7e921fe4)


### Cluster Characteristics and Weather Classification
- Cluster 1 : Rainy Weather
  - Characteristics :
    - Lower temperature (25.89°C) and higher humidity (84.75%)
    - Significant rainfall (9.92 mm)
    - Very low solar radiation (25.58 W/m²), suggesting dense cloud cover
    - Low wind speed (1.70 m/s)
  - Reason for Classification :

    This cluster represents rainy weather, characterized by significant rainfall, high humidity, and minimal sunlight due to dense cloud clover
    
- Cluster 2 : Clear Weather
  - Characteristics :
    - Higher temperature (29.29°C) and lower humidity (71.50%)
    - Almost no rainfall (0.07 mm)
    - High solar radiation (879.86 W/m²), indicating clear skies
    - Relatively high wind speed (3.14 m/s)
  - Reason for Classification :

    This cluster represents clear weather, with intense solar radiation, low humidity, and no rainfall, indicating sunny conditions
    
- Cluster 3 : Cloudly Weather
  - Characteristics :
    - Moderate temperature (28.52°C) and humidity (74.26%)
    - Minimal rainfall (0.08 mm)
    - Medium solar radiation (412.42 W/m²), indicating partial cloud cover
    - Moderate wind speed (2.60 m/s)
  - Reason for Classification :

    This cluster represents cloudly weather, where cloud cover partially blocks solar radiation, resulting in moderate temperatures and humidity. Rainfall is negligible


## Cluster Distribution
- Cluster 1 : 526 data points (rainy weather)
- Cluster 2 : 82 data points (clear weather)
- Cluster 3 : 136 data points (cloudly weather)


## Cluster Visualization
![image](https://github.com/user-attachments/assets/ad3f1e1b-2771-436b-bc3a-b687d3ddf19b)


- Scatter plot displaying clusters and their centroids based on PCA results
- Color-coded clusters :
  - Dark Blue : Rainy Weather (Cluster 1)
  - Brown : Clear Weather (Cluster 2)
  - Light Blue : Cloudly Weather (Cluster 3)
 

## Evaluation


The clustering results align with observed weather patterns during January 2022, where rainy weather dominates in Banyuwangi


## Limitations
- The analysis is limited to hourly data from a single month (January 2022) and results may not generalize to other months or regions
- K-Means assumes clusters are spherical, which may not always hold true for complex weather data distributions

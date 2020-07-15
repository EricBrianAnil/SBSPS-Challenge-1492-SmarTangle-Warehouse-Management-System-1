# SBSPS-Challenge-1492-SmarTangle-Warehouse-Management-System
A Tangle network based SaaS Warehouse Optimization System for a Food Warehouse that covers tracking of the movement, quality and shelf life of the product and also predicts the requirement of raw materials  based on daily demands for a long period using the FbProphet Time Series forecasting model. 
### [Check out the Project demo video here!](https://youtu.be/RXRktCTKABk)

![](/Images/poster1.png)

# Technical Stack & Architectural Flow 
![](/Images/Architecture-Flow.png)
The technological stack that has been used for the component-wise design and implementation of this  project as a reference to the working architecture flow are as follows:

* **Machine Learning Model :**
   * [TensorFlow Keras API](https://www.tensorflow.org/)
   * [FbProphet Model by Facebook](https://facebook.github.io/prophet/docs/quick_start.html) *(Time Series Model)
   * [TPOT Regressor](https://epistasislab.github.io/tpot/) *(Quality Score Prediction)
    
* **Tangle Network:**
  * [IOTA Comnet (public) Tangle Network](https://comnet.thetangle.org/)
  > For more information regarding the tangle network, visit [https://www.iota.org/](https://www.iota.org/)

* **Warehouse-End Web Application :**
  * [Django Framework](https://www.djangoproject.com/) *(Back-End)
  * [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Bootstrap](https://getbootstrap.com/)  *(Front-End)
  * [Docker](https://www.docker.com/) & [Kubernetes](https://kubernetes.io/) *(Containerization)
  * [Amazon AWS](https://aws.amazon.com/elasticbeanstalk/) *(Deployment)
  
* **Customer-End Mobile Application :**
  * [Flutter](https://flutter.dev/) *(Android Development SDK using Dart)
  * [Google Maps SDK](https://developers.google.com/maps/documentation/android-sdk/intro) *(Maps and Location details)
  
* **Databases:**
  * [Influx DB](https://www.influxdata.com/) from IBM Cloud Catalog *(Processing of ML data)
  * [Firebase](https://firebase.google.com/) *(NoSQL : User data & Requests  from the mobile application)
  * [SQLite](https://www.sqlite.org/index.html) *(SQL : Store Inventory & Raw Material information)



![](/Images/1.png)
![](/Images/2.png)
![](/Images/3.png)

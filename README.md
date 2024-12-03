# Laporan Proyek Pertama Predictive Analytics 
oleh Hilmiyatul Asna

## Domain Kesehatan

Perkembangan Machine Learning yang pesat dapat membantu manusia menyelesaikan masalah kompleks dengan menggunakan komputasi komputer. Dalam proyek ini, penulis bertujuan untuk menggunakan Machine Learning untuk memprediksi kemungkinan seseorang menderita diabetes.

Diabetes melitus (DM) adalah penyakit metabolik kronis yang memiliki berbagai penyebab, ditandai dengan kadar gula darah yang lebih tinggi dari 200 mg/dl, atau kadar gula darah puasa di atas 126 mg/dl, disertai gangguan metabolisme karbohidrat, lipid, dan protein akibat ketidakcukupan fungsi insulin. Insufisiensi fungsi insulin ini bisa disebabkan oleh gangguan atau kekurangan produksi insulin oleh sel beta Langerhans di pankreas, atau akibat rendahnya respons tubuh terhadap insulin [Kemenkes RI](https://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus). DM sering disebut "silent killer" karena gejalanya yang tidak terlihat dan baru terdeteksi setelah terjadi komplikasi (Kemenkes RI, 2014). Penyakit ini dapat mempengaruhi hampir semua sistem tubuh, mulai dari kulit hingga jantung, menyebabkan berbagai komplikasi. Diabetes Mellitus menduduki peringkat keenam sebagai penyebab kematian terbesar di dunia menurut World Health Organization (WHO).

Karena bahaya yang ditimbulkan oleh DM, penulis berencana untuk memprediksi kemungkinan seseorang mengidap penyakit ini menggunakan tiga model, yaitu KNN Classifier, Random Forest Classifier, dan Boost Classifier, berdasarkan dataset yang tersedia di [Kaggle](https://www.kaggle.com).


## Business Understanding
Berdasarkan penjelasan latar belakang sebelumnya, berikut adalah masalah-masalah yang dapat dipecahkan dalam proyek ini:
- Bagaimana cara membangun model machine learning untuk mengklasifikasikan pasien yang menderita diabetes dan yang tidak?
- Apa saja faktor yang menyebabkan seseorang terkena diabetes?


### Goals
- Mengetahui model dengan akurasi terbaik dalam memprediksi diabetes pada pasien.
- Mengidentifikasi faktor-faktor yang dapat menyebabkan seseorang mengidap diabetes.

    ### Solution statements
    - Melakukan Exploratory Data Analysis untuk menganalisis data yang memiliki pengaruh terbesar terhadap kejadian diabetes pada pasien.
Menggunakan model Machine Learning untuk memprediksi pasien yang berisiko terkena diabetes. Model-model yang akan diterapkan antara lain:
    - *Random Forest Classifier*
    - *K-Neighbors Classifier*
    - *AdaBoost Classifier*

## Data Understanding
Dataset yang digunakan untuk memprediksi diabetes pada pasien diambil dari platform kaggle.com, yang dipublikasikan oleh AKSHAY DATTATRAY KHARE. Dataset ini berasal dari National Institute of Diabetes and Digestive and Kidney Diseases. Tujuan dari dataset ini adalah untuk secara diagnostik memprediksi apakah seorang pasien menderita diabetes, berdasarkan sejumlah pengukuran diagnostik yang ada dalam data. Dataset ini terdiri dari satu file CSV.

### Informasi data:

Attribute  | Keterangan
------------- | -------------
Sumber | https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset
Pregnancies | Menunjukkan jumlah kehamilan yang dialami pasien
Glucose | Menunjukkan tingkat glukosa dalam darah pasien
BloodPressure | Menunjukkan tekanan darah yang diukur pada pasien
SkinThickness | Menunjukkan ketebalan kulit pasien
Insulin | Menunjukkan kadar insulin dalam darah pasien    
BMI | Menunjukkan indeks massa tubuh pasien
DiabetesPedigreeFunction  | Menunjukkan persentase kemungkinan diabetes berdasarkan riwayat keluarga
Age |Menunjukkan usia pasien
Outcome |Menunjukkan hasil akhir, 1 untuk diabetes dan 0 untuk tidak diabetes

Berkas ini berisi informasi mengenai 768 pasien dengan 9 kolom, tanpa data yang hilang (missing values) maupun data yang duplikat.

### Berikut rangkuman `statistik deskriptif` dari fitur dalam dataset: <br>
| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age| Outcome | 
|---|----|---|---|---|---|---|---|---|
| count |	768.000000 | 768.000000 | 768.000000 | 768.000000 | 768.000000 | 768.000000	| 768.000000 | 768.000000 |	768.000000 |
| mean	| 3.845052 | 120.894531	| 69.105469 | 20.536458 | 79.799479 | 31.992578 | 0.471876 | 33.240885 | 0.348958 |
| std	| 3.369578 | 31.972618 | 19.355807 | 15.952218 | 115.244002 | 7.884160 | 0.331329 | 11.760232 | 0.476951 |
| min	| 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.078000 | 21.000000 | 0.000000 |
| 25% | 1.000000 | 99.000000 | 62.000000 | 0.000000 | 0.000000 | 27.300000 | 0.243750 | 24.000000	| 0.000000 |
| 50% | 3.000000 | 117.000000 | 72.000000 | 23.000000 | 30.500000 | 32.000000 | 0.372500 | 29.000000 | 0.000000 |
| 75%	| 6.000000 | 140.250000 | 80.000000 | 32.000000 | 127.250000 | 36.600000 | 0.626250	| 41.000000 | 1.000000 |
| max | 17.000000 | 199.000000 | 122.000000 | 99.000000 | 846.000000 | 67.100000 | 2.420000 | 81.000000 | 1.000000 |

#### Interpretasi Deskripsi statistik data 
Pada kolom Glucose, BloodPressure, SkinThickness, Insulin, dan BMI, terdapat nilai minimum sebesar 0. Nilai ini tidak realistis, karena manusia tidak mungkin memiliki kadar glukosa, tekanan darah, ketebalan kulit, kadar insulin, dan BMI yang mencapai nol. Oleh karena itu, nilai nol pada kolom-kolom tersebut akan dihapus.<br><br><br>


### Berikut Visualisasi data dengan Boxplot: <br>
<img src="img/Visualisasi _boxplot1.png" style="zoom:70%;" /> <br>
<img src="img/Visualisasi _boxplot2.png" style="zoom:70%;" /> <br>
<img src="img/Visualisasi _boxplot3.png" style="zoom:70%;" /> <br>

#### Interpretasi Outlier pada Boxplot.
- Pada boxplot Pregnancies, terlihat adanya outlier pada jumlah kehamilan 13, 15, 16, dan 17. Data ini tidak dihapus karena kemungkinan seorang wanita dapat memiliki 17 anak.
- Pada boxplot Insulin, kadar insulin menunjukkan fluktuasi yang cukup besar, sehingga tidak dianggap sebagai outlier.
- Pada boxplot DiabetesPedigreeFunction, nilai-nilai tersebut bervariasi tergantung pada riwayat keluarga, sehingga data ini tidak dihapus.
- Pada boxplot Age, terdapat outlier pada usia, namun orang dengan usia tersebut masih mungkin ada, sehingga data ini tidak dihapus. <br><br><br>



### Berikut Visualisasi data Categorical Features pada plot : <br>
<img src="img/Visualisasi _Categorical_Features1.png" style="zoom:70%;" /> 
<img src="img/Visualisasi _Categorical_Features2.png" style="zoom:70%;" />
Pada grafik Pregnancies, terlihat bahwa jumlah kehamilan terbanyak adalah sebanyak 1. Sedangkan pada grafik Outcome, terlihat ketidakseimbangan antara data pasien yang terkena diabetes dan yang tidak. Pasien yang terkena diabetes memiliki jumlah yang lebih banyak dibandingkan dengan yang tidak terkena diabetes. <br><br><br>



### Berikut Visualisasi data Numerical Features pada histogram :
<img src="img/Visualisasi _Numerical_Features1.png" style="zoom:70%;" /><br> 
<img src="img/Visualisasi _Numerical_Features2.png" style="zoom:70%;" /><br>

#### Interpretasi histogram
- Beberapa kolom menunjukkan distribusi yang miring ke kanan.
- Kolom yang memiliki distribusi normal adalah Glucose, BloodPressure, SkinThickness, dan BMI.
- Kolom yang distribusinya miring ke kanan (right-skewed) adalah Insulin, DiabetesPedigreeFunction, dan Age.<br><br><br>


### Multivariate Analysis
Menganalisis hubungan antara fitur numerik dengan variabel tujuan, yaitu Outcome.
<img src="img/Multivariate_Analysis1.png" style="zoom:70%;" /><br>
<img src="img/Multivariate_Analysis2.png" style="zoom:70%;" /><br>
<img src="img/Multivariate_Analysis3.png" style="zoom:70%;" /><br>
<img src="img/Multivariate_Analysis4.png" style="zoom:70%;" /><br>

#### Interpertasi
- Pada grafik perbandingan, terlihat perbedaan antara pasien yang menderita diabetes dan yang tidak, terutama pada kolom Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, dan Age.<br><br><br>


### Heat Map
Pada data numerik, digunakan heatmap untuk memvisualisasikan hubungan korelasi antara fitur'Glucose',	'BloodPressure',	'SkinThickness',	'Insulin',	'BMI',	'DiabetesPedigreeFunction',	 dan 'Age' dengan data "Outcome" sehingga lebih mudah untuk dianalisis dan dipahami. <br>
<img src="img/Heat_Map.png" style="zoom:70%;" /><br>
Hasil dari heatmap menunjukkan bahwa diabetes (outcome) memiliki korelasi yang signifikan dengan glucose, bmi, dan age. <br><br><br>


## Data Preparation

- Mengatasi data kosong <br>

| missing | value |
|---|----|
| Pregnancies | 0 |
| Glucose |	0 |
| BloodPressure | 0 |
| SkinThickness | 0 |
| Insulin |	0 |
| BMI |	0 |
| DiabetesPedigreeFunction | 0 |
| Age |	0 |
| Outcome |	0 |
<br>
  Tahapan ini bertujuan untuk mengisi data yang tidak lengkap atau data kosong. 

- Balancing Dataset <br>
 <img src="img\Balancing_Dataset.png" style="zoom:70%;" /><br>
  Pada tahap Balancing Dataset, diperlukan untuk menyeimbangkan data Outcome yang tidak seimbang. Jika data tidak seimbang, model cenderung lebih mengarah pada kategori dengan jumlah data lebih banyak. Oleh karena itu, tahapan ini dilakukan dengan menggunakan teknik yang menghasilkan data dummy atau data sintetis.


- Membagi data menjadi data *training* dan *testing* <br>
  Tahapan ini bertujuan agar model yang dilatih dapat diuji menggunakan data yang berbeda dari data pelatihan. Data dibagi menjadi dua bagian, yaitu 80% untuk training dan 20% untuk testing. Fungsi [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) dari library sklearn digunakan untuk melakukan pembagian data ini.



## Modeling
Algoritma *Machine Learning* yang digunakan dalam proyek ini adalah:
- **K-Neighbors Classifier**, K-Nearest Neighbors bekerja dengan membandingkan jarak antara sampel dan sampel pelatihan lainnya, kemudian memilih sejumlah k tetangga terdekat. Pada penelitian ini, karena merupakan masalah klasifikasi, algoritma ini akan membandingkan dua data. Proyek ini menggunakan [sklearn.neighbors.KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html?highlight=kneighborsclassifier#sklearn.neighbors.KNeighborsClassifier) dengan memasukkan X_train dan y_train untuk membangun model. Parameter yang digunakan pada proyek ini adalah `n_neighbors` yang menentukan jumlah k tetangga terdekat. Model ini menggunakan parameter n_neighbors = 2, karena proyek ini mengklasifikasikan pasien yang terjangkit diabetes dan yang tidak.


- **Random Forest Classifier**, merupakan salah satu algoritma yang banyak digunakan karena kesederhanaannya dan kestabilannya yang baik. Dalam proyek ini, digunakan [sklearn.ensemble.RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=sklearn+ensemble+randomforestclassifier#sklearn.ensemble.RandomForestClassifier) dengan memasukkan X_train dan y_train untuk membangun model. Parameter yang diterapkan pada proyek ini meliputi: criterion = Fungsi untuk menilai kualitas pembagian data. n_estimators = Jumlah pohon dalam hutan. max_depth = Kedalaman maksimum setiap pohon. random_state = Menentukan nilai acak yang digunakan pada setiap base_estimator di setiap iterasi. Pada model ini, digunakan parameter criterion = gini, n_estimators = 100, max_depth = 9, dan random_state = 44.

- **AdaBoost Classifier**, adalah singkatan dari Adaptive Boosting Classifier, yang dirancang untuk memberikan bobot lebih pada observasi yang salah klasifikasinya, atau disebut weak classifier. Proyek ini menggunakan [sklearn.ensemble.AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html?highlight=sklearn+ensemble+adaboostclassifier#sklearn.ensemble.AdaBoostClassifier) dengan memasukkan X_train dan y_train untuk membangun model.



## Evaluation
Dalam proyek ini, model dikembangkan untuk mengklasifikasikan pasien yang terkena diabetes dan yang tidak. Berdasarkan hasil evaluasi, model dengan performa tertinggi adalah Random Forest Classifier. <br>
<img src="img\Performance_Models.png" style="zoom:70%;" /><br>

Sebelum menghitung metrik seperti Akurasi, Precision, Recall, dan F1-score, penting untuk memahami confusion matrix, yang mencakup empat nilai: true positive, true negative, false positive, dan false negative. Berikut adalah ilustrasi confusion matrix untuk lebih memahaminya. <br>

<img src="img\cm1.jpg" style="zoom:50%;" /><br>

- *Accuracy*

  Metrik akurasi mengukur tingkat kesesuaian antara nilai prediksi dan nilai aktual. Akurasi dihitung dengan membagi jumlah prediksi yang benar dengan total data. Akurasi cocok digunakan untuk data yang seimbang.

- *Precision*

  Metrik precision mengukur seberapa tepat prediksi positif yang dilakukan oleh model. Precision dihitung dengan formula berikut. <br>

  <img src="img\precision.png" style="zoom:80%;" /><br>

  Metrik ini lebih fokus pada performa model dalam memprediksi label positif.

- *Recall*

  Metrik recall mengukur seberapa efektif model dalam mengidentifikasi informasi yang benar. Recall dihitung dengan rumus berikut. <br>

  <img src="img\recall.png" style="zoom:80%;" /><br>

  Berbeda dengan precision yang hanya mempertimbangkan label positif, recall menghitung proporsi label negatif yang diklasifikasikan sebagai positif.


- *F1-score*

  F1-score adalah rata-rata harmonik dari precision dan recall. Nilai F1-score dihitung dengan rumus berikut.<br>

  <img src="img/f1_score.png" style="zoom: 40%;" /><br><br><br>

Selanjutnya, model Random Forest Classifier akan dihitung menggunakan metrik F1-score dan recall. <br>

<img src="img\Confusion_Matrix_untuk_Random_Forest.png" style="zoom:70%;" /><br><br>

| Metrik                                                | Nilai                       |
|-------------------------------------------------------|-----------------------------|
| Akurasi Random Forest Classifier                      | 0.9238095238095239          |
| Precision Random Forest Classifier                    | 0.9285714285714286          |
| Recall Random Forest Classifier                       | 0.9285714285714286          |
| F1 Score Random Forest Classifier                     | 0.9285714285714286          |

Berdasarkan proyek ini, metrik yang digunakan adalah recall karena recall dapat mengurangi angka false negative, sehingga model Random Forest Classifier dengan skor recall sebesar 92 persen.

## Kesimpulan
Dari proyek prediksi diabetes pada pasien menggunakan tiga model Machine Learning, yaitu K-Neighbors Classifier, Random Forest Classifier, dan AdaBoost Classifier, dapat disimpulkan bahwa algoritma Random Forest Classifier memberikan hasil yang lebih baik dibandingkan yang lainnya. Hal ini terlihat dari performa model yang lebih tinggi dibandingkan algoritma lainnya.

Dalam proyek ini, informasi yang diperoleh mengenai faktor-faktor yang mempengaruhi pasien menderita diabetes antara lain:
- Pasien dengan kadar glukosa tinggi
- Pasien dengan tekanan darah tinggi
- Pasien dengan indeks massa tubuh tinggi
- Pasien dengan nilai DiabetesPedigreeFunction tinggi
- Pasien dengan usia lebih tua


# Referensi

1. [Dicoding](https://www.dicoding.com/academies/319/tutorials/16979?from=17053) (2024). *Machine learning Terapan*
2. [Imbalanced-learn](https://imbalanced-learn.org/stable/). *Documentation*
3. [Kemenkes RI](https://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus) 

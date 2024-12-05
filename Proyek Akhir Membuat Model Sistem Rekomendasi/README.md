# Laporan Proyek Machine Learning
oleh Hilmiyatul Asna
---
## Project Overview

Dalam era digital saat ini, sistem rekomendasi menjadi salah satu teknologi yang sangat penting dalam meningkatkan pengalaman pengguna. Banyak platform, seperti layanan streaming film, e-commerce, dan media sosial, menggunakan sistem ini untuk menyarankan konten atau produk yang relevan. Sistem rekomendasi tidak hanya membantu pengguna menemukan item yang sesuai dengan minat mereka, tetapi juga meningkatkan keterlibatan pengguna dan nilai bisnis.

Namun, merancang sistem rekomendasi yang efektif bukan tanpa tantangan. Dua pendekatan utama yang sering digunakan adalah **content-based filtering** dan **collaborative filtering**.  
- **Content-based filtering** berfokus pada analisis atribut item untuk merekomendasikan konten yang mirip dengan preferensi sebelumnya dari pengguna.  
- **Collaborative filtering** memanfaatkan data preferensi pengguna lain untuk menemukan kesamaan pola perilaku, sehingga dapat merekomendasikan item yang mungkin disukai.  

### Masalah dan Latar Belakang
Proyek ini dilatarbelakangi oleh tantangan yang dihadapi banyak platform dalam memberikan rekomendasi yang relevan akibat beberapa faktor berikut:  

#### 1. Masalah Cold Start  
Ketika pengguna baru bergabung, mereka belum memiliki cukup riwayat interaksi untuk membantu sistem menghasilkan rekomendasi yang personal. Hal ini sering menjadi hambatan dalam pendekatan content-based filtering maupun collaborative filtering.  

#### 2. Masalah Sparsity  
Dataset sistem rekomendasi sering kali sangat sparse, di mana sebagian besar pengguna hanya memberikan beberapa rating dibandingkan dengan jumlah item yang tersedia. Hal ini menyebabkan sulitnya menemukan pola hubungan yang signifikan.  

#### 3. Relevansi yang Kurang Personal  
Beberapa sistem rekomendasi gagal menghasilkan saran yang cukup personal karena tidak memanfaatkan secara optimal hubungan antar data pengguna dan karakteristik item.  

Dataset **MovieLens** dipilih untuk penelitian ini karena menyediakan kumpulan besar data rating film oleh pengguna yang beragam. Dataset ini memberikan peluang untuk mengevaluasi efektivitas kedua metode dalam mengatasi masalah di atas.

### Alasan Pemilihan Masalah
1. Sistem rekomendasi yang kurang efektif dapat menyebabkan pengalaman pengguna yang buruk, seperti rekomendasi yang tidak relevan, membosankan, atau bahkan tidak berguna.  
2. Meningkatkan akurasi dan personalisasi rekomendasi adalah kebutuhan yang mendesak bagi banyak platform untuk mempertahankan dan meningkatkan jumlah pengguna mereka.  
3. Dengan membandingkan content-based filtering dan collaborative filtering menggunakan dataset yang nyata, seperti MovieLens, penelitian ini diharapkan dapat memberikan wawasan baru tentang penerapan kedua metode dalam skenario dunia nyata.

### Tujuan Penelitian
Proyek ini bertujuan untuk:  
1. Mengeksplorasi keunggulan dan kelemahan pendekatan content-based filtering dan collaborative filtering.  
2. Mengidentifikasi metode yang paling efektif dalam mengatasi tantangan **cold start** dan **sparsity**.  
3. Memberikan rekomendasi praktis bagi pengembang sistem rekomendasi tentang strategi terbaik untuk meningkatkan akurasi dan personalisasi rekomendasi.  
---
# Business Understanding

## Problem Statements
Dalam proyek ini, masalah utama yang ingin dipecahkan adalah:
1. Apa saja faktor yang mempengaruhi efektivitas model rekomendasi pada dataset MovieLens?
2. Bagaimana cara membangun model content-based filtering dan collaborative filtering untuk merekomendasikan film yang relevan kepada pengguna?
3. Bagaimana cara meningkatkan kualitas rekomendasi yang dihasilkan dari kedua pendekatan tersebut?

## Goals
Tujuan utama dari proyek ini adalah untuk menjawab masalah-masalah di atas melalui langkah-langkah berikut:
1. Mengidentifikasi dan menganalisis faktor-faktor yang mempengaruhi efektivitas kedua metode rekomendasi pada dataset MovieLens.
2. Membangun model content-based filtering dan collaborative filtering untuk memberikan rekomendasi film yang relevan bagi pengguna.
3. Meningkatkan kualitas rekomendasi dengan membandingkan dan mengoptimalkan kedua pendekatan tersebut.

## Solution Approach
Untuk mencapai tujuan ini, solusi yang diusulkan melibatkan langkah-langkah berikut:
1. Melakukan analisis eksploratif data (EDA) untuk memahami distribusi rating dan karakteristik film dalam dataset MovieLens.
2. Menerapkan content-based filtering dengan memanfaatkan fitur konten film seperti genre dan tag.
3. Menerapkan collaborative filtering dengan memanfaatkan data rating yang diberikan oleh pengguna.
---
# Data Understanding

Dataset yang digunakan dalam proyek ini adalah **MovieLens**, yang mencakup 100.836 rating dan 3.683 tag dari 9.742 film yang diberikan oleh 610 pengguna selama periode 29 Maret 1996 hingga 24 September 2018. Dataset ini dapat diunduh di [MovieLens Dataset](https://grouplens.org/datasets/movielens/).

Dataset ini terdiri dari beberapa file berikut:  

## 1. `ratings.csv`  
File ini berisi data penilaian film oleh pengguna.  
- **Jumlah data**: 100.836 baris dan 4 kolom.  
- **Kondisi data**: Tidak terdapat missing values atau duplikasi.  
- **Fitur-fitur**:  
  - `userId`: ID unik pengguna.  
  - `movieId`: ID unik film yang diberi rating.  
  - `rating`: Rating yang diberikan pengguna (skala 0,5 hingga 5,0).  
  - `timestamp`: Waktu saat rating diberikan (dalam format UNIX timestamp).  

## 2. `tags.csv`  
File ini berisi data tag yang ditambahkan pengguna pada film.  
- **Jumlah data**: 3.683 baris dan 4 kolom.  
- **Kondisi data**: Tidak terdapat missing values atau duplikasi.  
- **Fitur-fitur**:  
  - `userId`: ID unik pengguna.  
  - `movieId`: ID unik film yang diberi tag.  
  - `tag`: Tag yang diberikan pengguna.  
  - `timestamp`: Waktu saat tag ditambahkan (dalam format UNIX timestamp).  

## 3. `movies.csv`  
File ini berisi daftar film beserta genre-nya.  
- **Jumlah data**: 9.742 baris dan 3 kolom.  
- **Kondisi data**: Tidak terdapat missing values, tetapi ada film dengan genre `(no genres listed)`.  
- **Fitur-fitur**:  
  - `movieId`: ID unik film.  
  - `title`: Judul film (termasuk tahun rilis dalam tanda kurung).  
  - `genres`: Daftar genre yang dipisahkan dengan tanda "|".  

## 4. `links.csv`  
File ini berisi ID yang menghubungkan film dalam MovieLens dengan basis data eksternal seperti IMDb dan TMDb.  
- **Jumlah data**: 9.742 baris dan 3 kolom.  
- **Kondisi data**: Beberapa entri memiliki missing values pada kolom `imdbId` dan `tmdbId`.  
- **Fitur-fitur**:  
  - `movieId`: ID unik film di MovieLens.  
  - `imdbId`: ID unik film di IMDb.  
  - `tmdbId`: ID unik film di TMDb.  

## Tautan Sumber Data  
Dataset ini dapat diakses melalui [MovieLens Dataset](https://grouplens.org/datasets/movielens/).

## Kesimpulan Awal  
Dataset ini bersih dari duplikasi, tetapi memiliki beberapa kekurangan seperti genre `(no genres listed)` pada `movies.csv` dan missing values pada kolom `imdbId` dan `tmdbId` di `links.csv`. Dataset ini mencakup informasi yang kaya untuk membangun sistem rekomendasi berbasis rating, tag, dan genre.


## **Analisis Univariate dan Multivariate**

### **Statistik Rating**
Tabel berikut menunjukkan statistik deskriptif untuk rating dalam dataset:

| Jenis        | Nilai       |
|--------------|-------------|
| count        | 100836.000000 |
| mean         | 3.501557     |
| std          | 1.042529     |
| min          | 0.500000     |
| 25%          | 3.000000     |
| 50% (Median) | 3.500000     |
| 75%          | 4.000000     |
| max          | 5.000000     |
| modus        | 4.000000     |

Berikut adalah interpretasi dari statistik rating:
- **Jumlah Rating**: 100.836
- **Rata-Rata (Mean)**: 3.5016
- **Standar Deviasi**: 1.0425
- **Nilai Minimum**: 0.5
- **Kuartil Pertama (25%)**: 3.0
- **Median (50%)**: 3.5
- **Kuartil Ketiga (75%)**: 4.0
- **Nilai Maksimum**: 5.0
- **Modus**: 4.0

Dari data ini, dapat disimpulkan bahwa sebagian besar pengguna memberikan rating tinggi, dengan rata-rata sekitar 3.5 dan modus pada nilai 4.0. Distribusi rating menunjukkan adanya kecenderungan pengguna untuk memberikan rating positif, dengan sedikit kecenderungan ke arah rating yang lebih tinggi.

### **Distribusi Rating**

![Distribusi Rating](img/distribusi_rating.png)

**Gambar 1. Distribusi rating**

Visualisasi pada Gambar 1 menunjukkan distribusi rating pada dataset MovieLens. Dari grafik tersebut, terlihat bahwa rating 4.0 adalah yang paling sering diberikan, sesuai dengan nilai modus yang telah dihitung sebelumnya. Rating 3.0 dan 4.0 mendominasi distribusi, mengindikasikan bahwa sebagian besar film menerima rating positif dari pengguna. Distribusi rating ini menunjukkan kecenderungan pengguna untuk memberikan rating yang lebih tinggi, dengan jumlah rating rendah (seperti 0.5 dan 1.0) jauh lebih sedikit dibandingkan dengan rating tinggi.

### **Frekuensi Genre Film**

![frekuensi genre](img/frekuensi_genre.png)

**Gambar 2. Frekuensi genre film**

Visualisasi pada Gambar 2 menunjukkan frekuensi genre film dalam dataset MovieLens:
- **Drama** adalah genre paling populer, diikuti oleh **Comedy** dan **Thriller**, mencerminkan preferensi pengguna terhadap film dengan cerita mendalam atau yang menghibur.
- Genre seperti **Action**, **Romance**, dan **Adventure** juga cukup populer, menandakan ketertarikan pengguna pada film dengan narasi kuat atau elemen petualangan.
- Di sisi lain, genre seperti **Film-Noir** dan **IMAX** memiliki frekuensi lebih rendah, menunjukkan bahwa genre ini lebih jarang atau lebih spesifik dibandingkan dengan genre utama lainnya.
- Genre **(no genres listed)** menunjukkan bahwa beberapa film dalam dataset tidak memiliki genre yang terdaftar.

### **Korelasi Rating dan Genre Film**

![korelasi rating genre](img/korelasi_rating_genre.png)

**Gambar 3. Korelasi rating dan genre film**

Visualisasi dan analisis rating rata-rata per genre film pada Gambar 3 menunjukkan:
- **Film-Noir**, **War**, dan **Documentary** adalah genre dengan rating rata-rata tertinggi, menunjukkan bahwa film dalam genre ini cenderung sangat dihargai oleh pengguna.
- Sebaliknya, **Comedy** dan **Horror** memiliki rating rata-rata yang lebih rendah meskipun perbedaan antar genre tidak terlalu signifikan.
- **Drama** dan **Crime**, dua genre paling populer berdasarkan frekuensi, juga memiliki rating rata-rata yang cukup tinggi, menegaskan popularitas dan apresiasi mereka di kalangan pengguna.
- Genre **(no genres listed)**, meskipun memiliki jumlah film yang relatif sedikit, menunjukkan rating rata-rata yang sebanding dengan genre populer lainnya.

### **Tag Paling Populer**

![tag paling populer](img/tag.png)

**Gambar 4. Tag paling populer**

Visualisasi dan daftar 20 tag paling populer pada Gambar 4 menunjukkan:
- **In Netflix queue** adalah tag paling populer, menunjukkan ketertarikan pengguna untuk menandai film yang ingin mereka tonton di Netflix.
- Tag seperti **atmospheric**, **thought-provoking**, dan **superhero** juga populer, mencerminkan apresiasi pengguna terhadap suasana film, konten yang memicu pemikiran, dan genre superhero.
- Tag seperti **Disney**, **surreal**, dan **funny** menunjukkan ketertarikan pengguna pada film dengan elemen fantasi, humor, atau yang diproduksi oleh Disney.
- Tag seperti **religion**, **sci-fi**, **crime**, dan **politics** mencerminkan minat pengguna pada tema-tema spesifik dalam film.

### **Film Paling Populer**

**Tabel 2. Film Paling Populer**

| Judul Film                                             | Jumlah Rating | Rata-rata Rating |
|--------------------------------------------------------|---------------|------------------|
| Forrest Gump (1994)                                    | 329           | 4.16             |
| Shawshank Redemption, The (1994)                        | 317           | 4.43             |
| Pulp Fiction (1994)                                    | 307           | 4.20             |
| Silence of the Lambs, The (1991)                       | 279           | 4.16             |
| Matrix, The (1999)                                     | 278           | 4.19             |
| Star Wars: Episode IV - A New Hope (1977)               | 251           | 4.23             |
| Jurassic Park (1993)                                   | 238           | 3.75             |
| Braveheart (1995)                                      | 237           | 4.03             |
| Terminator 2: Judgment Day (1991)                       | 224           | 3.97             |
| Schindler's List (1993)                                | 220           | 4.23             |
---
## Data Preparation

Tahapan data preparation dalam eksperimen sistem rekomendasi menggunakan dataset MovieLens pada proyek ini mencakup langkah-langkah berikut untuk mempersiapkan dan memproses data sesuai kebutuhan analisis dan pemodelan:

1. **Menggabungkan Data Movies dengan Tags**  
   - Data dari tabel `movies` dan `tags` digabungkan berdasarkan `movieId`.  
   - Film yang tidak memiliki tag akan memiliki nilai kosong pada kolom `tag`. Nilai ini digantikan dengan string kosong (`""`).  
   - Tujuan penggabungan ini adalah memperkaya informasi konten setiap film dengan tambahan data tag untuk mendukung sistem rekomendasi berbasis konten.  

2. **Membuat Kolom Combined Features**  
   - Kolom `combined_features` dibuat dengan menggabungkan informasi dari kolom `genres` dan `tag` menggunakan tanda `|` sebagai pemisah.  
   - Kolom ini digunakan untuk menghasilkan vektor fitur dari teks untuk analisis kesamaan menggunakan algoritma berbasis teks.  

3. **Encoding untuk Collaborative Filtering**  
   - Kolom `userId` dan `movieId` diubah menjadi tipe kategori dan dikonversi menjadi kode numerik berurutan menggunakan `.astype('category').cat.codes`.  
   - Peta relasi antara kode numerik dan ID asli disimpan untuk mempermudah interpretasi hasil model.  
   - Langkah ini bertujuan menyederhanakan data untuk algoritma collaborative filtering yang memerlukan input numerik.  

4. **Mengonversi Teks ke Vektor Fitur dengan TF-IDF**  
   - TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer digunakan untuk mengubah kolom `combined_features` menjadi matriks fitur.  
   - Hasil dari proses ini adalah matriks sparse yang mewakili setiap film dalam bentuk vektor, memungkinkan perhitungan kesamaan berbasis konten.  
   - Parameter TF-IDF Vectorizer:  
     - `max_features=5000`: Menggunakan maksimal 5000 fitur penting.  
     - `stop_words='english'`: Menghapus kata-kata umum dalam bahasa Inggris yang tidak memiliki arti signifikan.  

5. **Pembagian Data untuk Training dan Validasi**  
   - Dataset dibagi menjadi set pelatihan dan validasi menggunakan `train_test_split` dari pustaka `sklearn.model_selection` dengan parameter berikut:  
     - `test_size=0.2`: 20% data digunakan untuk validasi.  
     - `random_state=42`: Mengatur seed untuk memastikan konsistensi pembagian data.  

Langkah-langkah ini memastikan bahwa data siap digunakan untuk kedua pendekatan sistem rekomendasi: content-based filtering dan collaborative filtering.  

---

## Modeling and Results

### **Content-Based Filtering**

- **Cara Kerja**:  
  - Menggunakan cosine similarity untuk menghitung kesamaan antar film berdasarkan vektor TF-IDF yang dihasilkan dari `combined_features`.  
  - Sistem merekomendasikan film yang memiliki skor kesamaan tertinggi dengan film pilihan pengguna.  
- **Parameter yang Digunakan**:  
  - **Metode Similarity**: Cosine similarity.  
  - **Jumlah Rekomendasi**: Top-10 film dengan kesamaan tertinggi.  
- **Keunggulan**:  
  - Relevan dengan minat spesifik pengguna berdasarkan konten film.  
  - Cocok untuk situasi di mana data pengguna lain terbatas.  
- **Kelemahan**:  
  - Rekomendasi cenderung monoton karena hanya berdasarkan konten serupa.  
  - Tidak mempertimbangkan interaksi pengguna lain.  

### **Collaborative Filtering**

- **Cara Kerja**:  
  - Model dibuat menggunakan TensorFlow dan Keras. Sistem memprediksi rating berdasarkan embedding pengguna dan film yang dilatih pada data pelatihan.  
  - Rekomendasi diberikan berdasarkan prediksi rating tertinggi untuk film yang belum ditonton oleh pengguna.  
- **Parameter Model**:  
  - **Embedding Dimension**: 50.  
  - **Optimizer**: Adam dengan learning rate 0.001.  
  - **Loss Function**: Mean Squared Error (MSE).  
  - **Epochs**: 10.  
  - **Batch Size**: 64.  
- **Keunggulan**:  
  - Mampu menghasilkan rekomendasi yang beragam dengan mengidentifikasi pola interaksi pengguna.  
  - Semakin efektif dengan bertambahnya data interaksi.  
- **Kelemahan**:  
  - Memerlukan data yang cukup besar untuk pelatihan.  
  - Rentan terhadap masalah cold start untuk pengguna atau item baru.  


### Hasil dan Evaluasi

1. **Content-Based Filtering**:  
   - Sistem berhasil memberikan rekomendasi berdasarkan konten dengan skor kesamaan tinggi.  
   - Cocok untuk rekomendasi awal pada pengguna baru.  

2. **Collaborative Filtering**:  
   - Model menunjukkan performa yang lebih baik dalam hal keanekaragaman rekomendasi dibandingkan pendekatan berbasis konten.  
   - Dapat meningkatkan personalisasi rekomendasi dengan lebih banyak data interaksi.  

### Kesimpulan
Content-based filtering cocok untuk personalisasi awal berdasarkan atribut film, sementara collaborative filtering lebih efektif untuk meningkatkan akurasi dan keragaman rekomendasi dalam platform dengan data interaksi yang cukup besar.

---
### **Result**

#### **Top-N Rekomendasi Content-Based Filtering**
- **Judul Film**: Cocoanuts, The (1929)
- **Genre**: Comedy|Musical
- **Tag**: 
- **Nilai Precision**: 1

## Top-N Rekomendasi

### **Content-Based Filtering**

Tabel 3. Top-N Rekomendasi Content-Based Filtering:
| No  | Judul Film                                      | Tahun | Genre          | Skor Kesamaan |
|-----|-------------------------------------------------|-------|----------------|---------------|
| 1   | Band Wagon, The (1953)                          | 1953  | Comedy|Musical | 1.0           |
| 2   | Great Race, The (1965)                          | 1965  | Comedy|Musical | 1.0           |
| 3   | History of the World: Part I (1981)             | 1981  | Comedy|Musical | 1.0           |
| 4   | Help! (1965)                                    | 1965  | Comedy|Musical | 1.0           |
| 5   | Holiday Inn (1942)                              | 1942  | Comedy|Musical | 1.0           |
| 6   | Anchors Aweigh (1945)                           | 1945  | Comedy|Musical | 1.0           |
| 7   | Beach Blanket Bingo (1965)                      | 1965  | Comedy|Musical | 1.0           |
| 8   | Can't Stop the Music (1980)                     | 1980  | Comedy|Musical | 1.0           |
| 9   | À nous la liberté (Freedom for Us) (1931)       | 1931  | Comedy|Musical | 1.0           |
| 10  | Girls! Girls! Girls! (1962)                     | 1962  | Comedy|Musical | 1.0           |

### **Collaborative Filtering**

**User ID**: 584

Tabel 4. Top-N Rekomendasi Collaborative Filtering:
| No  | Judul Film                                          |
|-----|-----------------------------------------------------|
| 1   | Perez Family, The (1995)                           |
| 2   | Last Supper, The (1995)                            |
| 3   | Wallace & Gromit: The Best of Aardman Animation    |
| 4   | Iron Giant, The (1999)                             |
| 5   | South Pacific (1958)                               |
---
## Evaluation

### **Content-Based Filtering Evaluation**

Untuk model Content-Based Filtering, metrik **precision** digunakan untuk mengukur proporsi rekomendasi yang relevan dibandingkan dengan jumlah total rekomendasi yang diberikan. Formula untuk precision adalah:

![equation](https://latex.codecogs.com/svg.image?Precision=%5Cfrac%7BJumlah%20Rekomendasi%20yang%20Relevan%7D%7BJumlah%20Total%20Rekomendasi%7D)

Evaluasi ini bertujuan untuk menilai seberapa efektif sistem dalam memberikan rekomendasi yang sesuai dengan minat pengguna. 

- **Dampak pada Business Understanding**:  
  Content-Based Filtering mampu memberikan rekomendasi yang sangat personal dengan fokus pada film yang memiliki atribut serupa dengan preferensi pengguna. Hal ini menjawab tantangan dalam menyediakan rekomendasi awal yang relevan, terutama ketika data interaksi dengan pengguna lain masih terbatas.

- **Hasil Evaluasi**:  
  Precision yang tinggi menunjukkan model dapat memberikan rekomendasi yang relevan dan memenuhi sebagian dari problem statement, yaitu meningkatkan personalisasi rekomendasi.

### **Collaborative Filtering Evaluation**

Model Collaborative Filtering menggunakan **Mean Squared Error (MSE)** untuk mengukur akurasi prediksi rating dibandingkan dengan nilai sebenarnya. Formula untuk MSE adalah:

![equation](https://latex.codecogs.com/svg.image?MSE=%5Cfrac%7B1%7D%7BD%7D%5Csum_%7Bi=1%7D%5E%7BD%7D(x_i-y_i)%5E2)

- **Dampak pada Business Understanding**:  
  Collaborative Filtering mengatasi masalah personalisasi yang kurang optimal pada pendekatan berbasis konten dengan mempertimbangkan preferensi kolektif pengguna. Ini membantu mengurangi dampak masalah sparsity pada dataset dengan memanfaatkan hubungan antar pengguna untuk menemukan pola rekomendasi.

- **Hasil Evaluasi**:  
  - **MSE**: Nilai MSE yang lebih rendah menunjukkan bahwa prediksi model semakin mendekati nilai sebenarnya.  
  - **Training and Validation Loss**: Grafik visualisasi menunjukkan bahwa model berhasil mengurangi error selama pelatihan tanpa tanda-tanda overfitting.  

![hasil training dan validasi](img/train_val_vis.png)  
*Gambar 5. Visualisasi metrik Training Loss dan Validation Loss*  


### **Evaluasi Dampak terhadap Problem Statement dan Goals**

- **Problem Statement**:  
  Proyek ini berupaya mengatasi dua tantangan utama, yaitu **cold start** dan **sparsity**, serta meningkatkan akurasi dan personalisasi rekomendasi.  
  - **Content-Based Filtering**: Efektif dalam memberikan rekomendasi awal kepada pengguna baru (mengatasi masalah cold start).  
  - **Collaborative Filtering**: Lebih kuat dalam mengidentifikasi pola preferensi tersembunyi dan memberikan rekomendasi beragam untuk pengguna yang telah memiliki cukup data interaksi.  

- **Pencapaian Goals**:  
  - Meningkatkan personalisasi rekomendasi: **Tercapai** dengan Content-Based Filtering.  
  - Mengatasi masalah sparsity: **Tercapai** dengan Collaborative Filtering.  

- **Dampak Solusi Statement**:  
  Kombinasi kedua pendekatan ini memberikan dampak yang signifikan terhadap pengalaman pengguna dan relevansi rekomendasi. Penggunaan Content-Based Filtering memberikan rekomendasi awal yang relevan, sedangkan Collaborative Filtering meningkatkan cakupan dan keberagaman rekomendasi seiring bertambahnya data interaksi.

Proyek ini berhasil memberikan solusi yang menjawab problem statement, mencapai goals yang diharapkan, dan menghasilkan model sistem rekomendasi yang relevan dan berdampak positif pada pengalaman pengguna.

---
### **Kesimpulan**

Hasil evaluasi untuk model Content-Based Filtering menunjukkan nilai precision sempurna (1), yang berarti semua rekomendasi relevan. Meskipun ini menunjukkan keberhasilan model, potensi bias dalam evaluasi atau kurangnya variasi dalam skenario pengujian perlu dipertimbangkan.

Sementara itu, model Collaborative Filtering yang dievaluasi dengan MSE menunjukkan penurunan konsisten dalam training loss dan validation loss, yang menunjukkan peningkatan kemampuan prediktif model. Penurunan ini berakhir stabil, tanpa divergensi antara keduanya, menunjukkan bahwa model menghindari overfitting, tantangan umum dalam sistem rekomendasi.

Loss validasi yang mendekati loss pelatihan menunjukkan bahwa model dapat menggeneralisasi data dengan baik, seperti yang terlihat pada dataset validasi.

Secara keseluruhan, proyek ini berhasil membangun dan mengevaluasi model rekomendasi berbasis Content-Based Filtering dan Collaborative Filtering menggunakan dataset MovieLens. Hasil analisis eksploratif membantu dalam pembuatan fitur dan pemahaman konten yang relevan dengan preferensi pengguna. Kedua model menunjukkan kemampuan dalam merekomendasikan film yang relevan kepada pengguna, dengan Content-Based Filtering efektif untuk film dengan konten serupa dan Collaborative Filtering mengidentifikasi film berdasarkan pola rating dari banyak pengguna.

---

## Daftar Referensi
[[1]] Orue-Saiz, M. Rico-González, J. Pino-Ortega, and A. Méndez-Zorrilla, "Improving diet through a recommendation system using physical activity data and healthy diet indexes of female futsal players," Proceedings of the Institution of Mechanical Engineers, Part P: Journal of Sports Engineering and Technology, vol. 0, no. 0, 2024.<br>
[[2]] R.N. Ravikumar, S. Jain, and M. Sarkar, "AdaptiLearn: real-time personalized course recommendation system using whale optimized recurrent neural network," Int J Syst Assur Eng Manag, 2024.<br>
[[3]] H. Imantho, K. B. Seminar, E. Damayanthi, N. E. Suyatma, K. Priandana, B. W. Ligar, and A. U. Seminar, "An Intelligent Food Recommendation System for Dine-in Customers with Non-Communicable Diseases History," Jurnal Keteknikan Pertanian, vol. 12, no. 1, pp. 140-152, 2024.<br>
[[4]] M. KabirMamdouh, Alireza, and A. Gürhan Kök, "A Personalized Content-Based Method to Predict Customers’ Preferences in an Online Apparel Retailer." SSRN, 2024.<br>
[[5]] D. Leela Krishna Reddy and H. Vaghela, "Music Recommendation System Using Machine Learning," EasyChair Preprint no. 12850, Mar. 31, 2024.<br>
[[6]] M. Surya Negara and A. Z. M., "Implementasi Machine Learning dengan Metode Collaborative Filtering dan Content-Based Filtering pada Aplikasi Mobile Travel (Bangkit Academy)," in JBegaTI, vol. 5, no. 1, Mar. 2024, pp. 126-136.

   [1]: <https://journals.sagepub.com/doi/abs/10.1177/17543371241241847>
   [2]: <https://link.springer.com/article/10.1007/s13198-024-02301-2>
   [3]: <https://jurnalpenyuluhan.ipb.ac.id/index.php/jtep/article/view/52452>
   [4]: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4782004>
   [5]: <https://easychair.org/publications/preprint_download/qr7B>
   [6]: <http://begawe.unram.ac.id/index.php/JBTI/article/view/1193>
   [MovieLens]: <://grouplens.org/datasets/movielens/>

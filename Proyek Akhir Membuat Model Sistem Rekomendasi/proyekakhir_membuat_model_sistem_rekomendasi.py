# -*- coding: utf-8 -*-
"""ProyekAkhir_Membuat Model Sistem Rekomendasi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HGndJsfU0kV2zTCk9ZsdMPUKCpRj1Acj

# Data Understanding

Dataset yang digunakan dalam proyek ini adalah MovieLens versi terbaru dengan ukuran kecil (ml-latest-small), yang dapat diakses melalui tautan berikut https://grouplens.org/datasets/movielens/. Dataset ini berisi ulasan berupa penilaian bintang 5 yang diberikan oleh pengguna pada MovieLens, sebuah layanan rekomendasi film.

Dataset ini mencakup:
*   100,836 penilaian dan 3,683 tag
*   9,742 film
*   610 pengguna
*   Rentang waktu: 29 Maret 1996 hingga 24 September 2018
*   Tanggal pembuatan dataset: 26 September 2018

Langkah pertama dalam bekerja dengan dataset MovieLens adalah mengunduhnya. Proses ini dapat dilakukan dengan menggunakan perintah wget, yang memungkinkan pengunduhan dataset langsung dari link yang disediakan.
"""

!wget https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

"""Setelah dataset berhasil diunduh, langkah selanjutnya adalah mengekstrak file-nya. Untuk melakukan ini, kita menggunakan perintah unzip."""

!unzip /content/ml-latest-small.zip

"""Isi Dataset:
- ratings.csv: File ini berisi semua penilaian, menggunakan skala 5 bintang dengan interval setengah bintang.
- tags.csv: File ini mencakup tag yang diterapkan oleh pengguna pada film.
- movies.csv: Berisi informasi mengenai film, termasuk judul dan genre.
- links.csv: Menyediakan pengenal yang dapat digunakan untuk menghubungkan ke sumber data film lainnya.
- README.txt: File ini memberikan penjelasan tentang dataset.

## Struktur Dasar Dataset
Langkah pertama dalam eksplorasi dataset ini adalah memuat dan memeriksa struktur dasar dari setiap file (ratings, tags, movies, dan links) menggunakan pandas. Hal ini bertujuan untuk memahami struktur data dan mempersiapkan analisis selanjutnya.

Memuat Data: Kita akan memuat setiap file (ratings, tags, movies, links) ke dalam DataFrame pandas.
"""

import pandas as pd

# Memuat setiap file ke dalam DataFrame pandas
ratings = pd.read_csv('ml-latest-small/ratings.csv')
tags = pd.read_csv('ml-latest-small/tags.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')
links = pd.read_csv('ml-latest-small/links.csv')

"""Setelah data dimuat ke dalam DataFrame, kita bisa mulai melihat isinya dengan menggunakan metode .head(), yang akan menampilkan lima baris pertama dari setiap DataFrame."""

movies.head()

"""File data film (movies.csv) memiliki kolom movieId, title, dan genres. Setiap baris mewakili informasi tentang sebuah film, termasuk judul dan genre-genre yang terkait."""

ratings.head()

"""File data penilaian (ratings.csv) memiliki kolom userId, movieId, rating, dan timestamp. Setiap baris mewakili penilaian yang diberikan oleh pengguna untuk sebuah film, dengan skala rating dari 0.5 hingga 5 bintang, serta mencatat waktu menggunakan format timestamp."""

tags.head()

"""File data tag (tags.csv) memiliki kolom userId, movieId, tag, dan timestamp. Setiap baris mewakili tag yang diberikan oleh pengguna untuk sebuah film, yang juga tercatat dengan waktu menggunakan format timestamp."""

links.head()

"""File data link (links.csv) mencakup kolom movieId, imdbId, dan tmdbId. Data ini menghubungkan film dengan sumber informasi lainnya seperti IMDb atau TMDB.

# Explanatory Data Analysis

## Statistik Deskriptif dari Rating
Pada bagian ini, kita akan menganalisis file ratings.csv dan menghitung statistik dasar dari kolom rating.
"""

# Menghitung statistik deskriptif dasar untuk kolom 'rating' dari DataFrame ratings
statistik_deskriptif = ratings['rating'].describe()

# Menghitung modus karena tidak termasuk dalam fungsi describe()
modus_rating = ratings['rating'].mode()[0]

# Menambahkan modus ke dalam statistik deskriptif
statistik_deskriptif['modus'] = modus_rating

statistik_deskriptif

"""Berikut adalah statistik deskriptif dasar untuk rating dalam dataset:

- Total Rating: 100836
- Rata-Rata (Mean): 3.5016
- Standar Deviasi: 1.0425
- Nilai Minimum: 0.5
- Kuartil Pertama (25%): 3.0
- Median (50%): 3.5
- Kuartil Ketiga (75%): 4.0
- Nilai Maksimum: 5.0
- Modus: 4.0

Dari statistik ini, dapat disimpulkan bahwa rata-rata rating berada di sekitar 3.5, dengan modus pada rating 4.0, yang menunjukkan bahwa mayoritas pengguna cenderung memberikan rating yang lebih tinggi. Distribusi rating mengindikasikan bahwa pengguna MovieLens umumnya memberikan penilaian positif, dengan kecenderungan sedikit lebih banyak pada rating yang lebih tinggi.

## Distribusi Rating
Selanjutnya, kita akan memvisualisasikan distribusi rating untuk mendapatkan pemahaman yang lebih mendalam mengenai bagaimana rating tersebar di berbagai nilai.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Membuat visualisasi distribusi rating
plt.figure(figsize=(10, 6))
sns.countplot(data=ratings, x='rating')
plt.title('Distribusi Rating pada Dataset MovieLens')
plt.xlabel('Rating')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.show()

"""Grafik di atas menggambarkan distribusi rating pada dataset MovieLens. Beberapa temuan yang dapat diambil dari visualisasi ini antara lain:

- Rating 4.0 adalah rating yang paling sering diberikan, yang sesuai dengan nilai modus yang dihitung sebelumnya.
- Rating 3.0 dan 4.0 bersama-sama mendominasi distribusi, menunjukkan bahwa mayoritas film mendapatkan penilaian yang positif dari pengguna.
- Secara keseluruhan, distribusi rating menunjukkan kecenderungan pengguna untuk memberikan penilaian yang lebih tinggi, dengan jumlah rating rendah (seperti 0.5 dan 1.0) jauh lebih sedikit dibandingkan rating tinggi.

## Jumlah Rating per Pengguna
Kita akan menghitung total jumlah rating yang diberikan oleh setiap pengguna untuk memahami bagaimana distribusi aktivitas penilaian di antara para pengguna.
"""

# Menghitung jumlah rating yang diberikan oleh setiap pengguna
jumlah_rating_per_pengguna = ratings.groupby('userId')['rating'].count()

# Membuat visualisasi distribusi jumlah rating per pengguna
plt.figure(figsize=(10, 6))
sns.histplot(jumlah_rating_per_pengguna, bins=30, kde=True)
plt.title('Distribusi Jumlah Rating per Pengguna')
plt.xlabel('Jumlah Rating')
plt.ylabel('Jumlah Pengguna')
plt.show()

# Statistik deskriptif dari jumlah rating per pengguna
statistik_jumlah_rating_per_pengguna = jumlah_rating_per_pengguna.describe()
statistik_jumlah_rating_per_pengguna

"""Visualisasi dan statistik deskriptif untuk jumlah rating per pengguna menunjukkan beberapa hal penting:

- Rata-rata rating per pengguna adalah sekitar 165, dengan standar deviasi yang besar (269,48), mengindikasikan adanya variasi yang cukup besar dalam jumlah rating yang diberikan oleh pengguna.
- Setiap pengguna memberikan setidaknya 20 rating, sesuai dengan batasan yang diterapkan dalam dataset ini.
- Kuartil: 25% pengguna yang paling aktif memberikan 168 rating atau lebih, sementara 25% pengguna dengan aktivitas paling rendah memberikan 35 rating atau kurang.
- Terdapat pengguna yang memberikan hingga 2698 rating, menunjukkan adanya beberapa pengguna yang sangat aktif dan menjadi outlier.

Distribusi jumlah rating per pengguna memperlihatkan adanya perbedaan yang signifikan dalam tingkat partisipasi pengguna, dengan sebagian kecil pengguna yang sangat aktif. Hal ini merupakan fenomena umum pada sistem rekomendasi, di mana sebagian pengguna cenderung lebih terlibat daripada yang lainnya.

## Jumlah Rating per Film
Kita akan menghitung total rating yang diterima oleh setiap film untuk mengidentifikasi film-film yang paling populer di dataset.
"""

# Menghitung jumlah rating yang diterima oleh setiap film
jumlah_rating_per_film = ratings.groupby('movieId')['rating'].count()

# Membuat visualisasi distribusi jumlah rating per film
plt.figure(figsize=(10, 6))
sns.histplot(jumlah_rating_per_film, bins=30, kde=True)
plt.title('Distribusi Jumlah Rating per Film')
plt.xlabel('Jumlah Rating')
plt.ylabel('Jumlah Film')
plt.show()

# Statistik deskriptif dari jumlah rating per film
statistik_jumlah_rating_per_film = jumlah_rating_per_film.describe()
statistik_jumlah_rating_per_film

"""Distribusi dan statistik deskriptif jumlah rating per film menunjukkan:

- **Rata-Rata Rating per Film**: Sekitar 10 rating per film, dengan variasi besar (standar deviasi sekitar 22.4), yang menunjukkan perbedaan signifikan dalam tingkat popularitas antar film.
- **Minimum Rating per Film**: Setiap film setidaknya mendapatkan satu rating.
- **Kuartil**: 75% film menerima 9 rating atau kurang, yang menunjukkan bahwa mayoritas film tidak mendapatkan banyak perhatian.
- **Maksimum**: Film yang paling populer menerima 329 rating, menunjukkan ketertarikan yang tinggi dari pengguna.

Distribusi ini menggambarkan bahwa sebagian besar film hanya menerima sedikit rating, sementara sejumlah kecil film sangat populer di kalangan pengguna.

## Frekuensi Genre

Analisis frekuensi genre akan memberikan wawasan tentang genre yang paling populer dalam dataset ini.
"""

from collections import Counter

# Menggabungkan semua genre menjadi satu list
semua_genre = sum(movies['genres'].map(lambda x: x.split('|')).tolist(), [])

# Menghitung frekuensi setiap genre
frekuensi_genre = Counter(semua_genre)

# Membuat DataFrame dari counter genre
df_frekuensi_genre = pd.DataFrame(frekuensi_genre.items(), columns=['Genre', 'Frekuensi']).sort_values(by='Frekuensi', ascending=False)

# Membuat visualisasi frekuensi genre
plt.figure(figsize=(12, 8))
sns.barplot(data=df_frekuensi_genre, x='Frekuensi', y='Genre')
plt.title('Frekuensi Genre Film dalam Dataset MovieLens')
plt.xlabel('Frekuensi')
plt.ylabel('Genre')
plt.show()

df_frekuensi_genre

"""Visualisasi dan data frekuensi genre film dalam dataset MovieLens menunjukkan:

- **Drama** adalah genre paling populer, diikuti oleh **Comedy** dan **Thriller**. Hal ini menunjukkan preferensi pengguna terhadap film dengan cerita mendalam atau yang bersifat menghibur.
- Genre seperti **Action**, **Romance**, dan **Adventure** juga cukup populer, menandakan kecenderungan umum pengguna terhadap film yang memiliki narasi kuat atau elemen petualangan.
- Di sisi lain, genre seperti **Film-Noir** dan **IMAX** memiliki frekuensi yang lebih rendah, menunjukkan bahwa genre ini lebih jarang ditemukan atau lebih bersifat niche dibandingkan dengan genre utama lainnya.
- **Genre (no genres listed)** menunjukkan bahwa ada beberapa film dalam dataset yang tidak memiliki genre yang terdaftar.

Frekuensi genre ini dapat memberikan wawasan yang berguna dalam pengembangan fitur rekomendasi, penargetan konten promosi, atau memahami tren pasar dalam industri film.

## Film per Tahun
Kita dapat mengekstrak tahun dari judul film dan menganalisis jumlah film yang dirilis per tahun untuk melihat tren rilis film sepanjang waktu. Dengan menganalisis tren ini, kita dapat memperoleh wawasan mengenai bagaimana jumlah produksi film berubah seiring berjalannya waktu, serta melihat periode-periode tertentu di mana industri film mengalami lonjakan atau penurunan dalam jumlah rilis.
"""

# Ekstrak tahun dari judul film
movies['Tahun'] = movies['title'].str.extract(r'\((\d{4})\)', expand=False)

# Menghitung jumlah film yang dirilis per tahun
film_per_tahun = movies.groupby('Tahun').size()

# Membuat visualisasi jumlah film per tahun
plt.figure(figsize=(14, 8))
film_per_tahun.plot(kind='line')
plt.title('Jumlah Film yang Dirilis per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Film')
plt.xticks(rotation=45)
plt.show()

# Menampilkan beberapa tahun terakhir untuk melihat tren terkini
film_per_tahun.tail(10)

"""Visualisasi jumlah film yang dirilis per tahun mengungkapkan beberapa tren menarik:

- Terdapat peningkatan jumlah film yang dirilis setiap tahunnya hingga awal abad ke-21, dengan puncaknya terjadi pada beberapa tahun tertentu.
- Setelah mencapai puncak, jumlah film yang dirilis cenderung stabil, meskipun ada sedikit fluktuasi, namun tetap tinggi dibandingkan dengan dekade-dekade sebelumnya.
- Pada dekade terakhir, terutama setelah 2010, jumlah film yang dirilis setiap tahun menunjukkan variasi, namun cenderung stabil dengan angka yang cukup tinggi.
- Terlihat penurunan jumlah film yang dirilis pada tahun 2017 dan 2018, yang mungkin disebabkan oleh perubahan dalam pengumpulan data.

## Korelasi antara Genre dan Rating
Menganalisis hubungan antara genre film dengan rating rata-rata yang diterima dapat memberikan pemahaman lebih dalam tentang preferensi pengguna terhadap genre-genre tertentu.
"""

# Membuat DataFrame baru yang menggabungkan informasi rating dengan genre film
movies_with_ratings = pd.merge(movies, ratings, on='movieId')

# Menggabungkan semua genre menjadi satu list untuk setiap film
movies_with_ratings['genres'] = movies_with_ratings['genres'].map(lambda x: x.split('|'))

# Mengekspansi genre sehingga setiap genre memiliki baris sendiri untuk setiap rating
movies_with_ratings_exploded = movies_with_ratings.explode('genres')

# Menghitung rating rata-rata untuk setiap genre
rating_per_genre = movies_with_ratings_exploded.groupby('genres')['rating'].mean().sort_values(ascending=False)

# Membuat visualisasi rating rata-rata per genre
plt.figure(figsize=(12, 8))
rating_per_genre.plot(kind='bar')
plt.title('Rating Rata-Rata per Genre Film')
plt.xlabel('Genre')
plt.ylabel('Rating Rata-Rata')
plt.xticks(rotation=45)
plt.show()

rating_per_genre

"""Visualisasi dan analisis rating rata-rata per genre film menunjukkan hal-hal berikut:

- Film-Noir, War, dan Documentary memiliki rating rata-rata tertinggi, yang menunjukkan bahwa film dalam genre ini cenderung sangat dihargai oleh pengguna.
- Sebaliknya, Comedy dan Horror memiliki rating rata-rata yang sedikit lebih rendah dibandingkan genre lainnya, meskipun perbedaan antar genre tidak terlalu signifikan.
- Drama dan Crime, dua genre yang paling populer berdasarkan frekuensi, juga memperoleh rating rata-rata yang cukup tinggi, yang menunjukkan popularitas dan apresiasi tinggi di kalangan pengguna.
- Genre (no genres listed), meskipun memiliki jumlah film yang terbatas, menunjukkan rating rata-rata yang setara dengan genre populer lainnya.

## Tag Paling Populer
Kita akan mengidentifikasi tag yang paling banyak digunakan oleh pengguna untuk memberikan gambaran mengenai topik atau tema yang paling menarik bagi penonton.
"""

# Menghitung frekuensi setiap tag
frekuensi_tag = tags['tag'].value_counts().head(20)

# Membuat visualisasi untuk 20 tag paling populer
plt.figure(figsize=(12, 8))
frekuensi_tag.plot(kind='bar')
plt.title('20 Tag Paling Populer')
plt.xlabel('Tag')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)
plt.show()

frekuensi_tag

"""Visualisasi dan daftar 20 tag terpopuler menunjukkan:

- "In Netflix queue" adalah tag yang paling sering digunakan, jauh mengungguli tag lainnya. Ini menunjukkan minat pengguna untuk menandai film yang ingin mereka tonton di Netflix.
- Tag seperti "atmospheric," "thought-provoking," dan "superhero" juga sering muncul, menggambarkan preferensi pengguna terhadap film dengan suasana yang mendalam, tema yang memancing pemikiran, dan genre superhero.
- Tag seperti "Disney," "surreal," dan "funny" termasuk di antara yang populer, menandakan minat pengguna terhadap film dengan elemen fantasi, humor, atau produksi Disney.
- Tag seperti "religion," "sci-fi," "crime," dan "politics" mencerminkan minat pengguna terhadap tema-tema tertentu dalam film.

## Korelasi antara Film dan Rating

Kita akan menghitung rata-rata rating dan jumlah rating untuk setiap film, lalu menganalisis korelasi antara kedua variabel tersebut.
"""

# Menghitung rating rata-rata dan jumlah rating per film
rating_stats_per_film = ratings.groupby('movieId').agg({
    'rating': ['mean', 'count']
}).reset_index()

# Mengganti nama kolom untuk kenyamanan
rating_stats_per_film.columns = ['movieId', 'rating_mean', 'rating_count']

# Menggabungkan data rating dengan data movie untuk mendapatkan judul film
rating_stats_with_titles = pd.merge(rating_stats_per_film, movies[['movieId', 'title']], on='movieId')

# Menampilkan beberapa contoh film
rating_stats_with_titles.sort_values(by='rating_count', ascending=False).head(10)

# Visualisasi hubungan antara jumlah rating dan rating rata-rata
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rating_stats_with_titles, x='rating_count', y='rating_mean', alpha=0.6)
plt.title('Hubungan antara Jumlah Rating dan Rating Rata-Rata per Film')
plt.xlabel('Jumlah Rating')
plt.ylabel('Rating Rata-Rata')
plt.xscale('log')  # Skala log untuk menangani distribusi yang lebar
plt.show()

"""Visualisasi hubungan antara jumlah rating dan rating rata-rata per film mengungkap beberapa temuan menarik:

- Distribusi: Terdapat sejumlah kecil film dengan jumlah rating yang sangat tinggi, menandakan popularitas yang besar. Sebagian besar film memiliki jumlah rating yang lebih moderat atau rendah.
- Hubungan: Tidak terlihat hubungan yang jelas antara jumlah rating dan rating rata-rata, yang mengindikasikan bahwa film yang lebih populer tidak selalu memiliki rating rata-rata yang lebih tinggi daripada film dengan jumlah rating lebih sedikit. Hal ini menunjukkan bahwa popularitas dan kualitas persepsi (rating rata-rata) dapat berjalan secara terpisah.
- Film Populer: Beberapa film dengan jumlah rating tertinggi, seperti *Forrest Gump* (1994), *The Shawshank Redemption* (1994), dan *Pulp Fiction* (1994), semuanya memiliki rating rata-rata yang tinggi.

## Distribusi Rating Sepanjang Waktu
Analisis distribusi rating dari waktu ke waktu dapat memberikan pemahaman tentang tren penilaian film oleh pengguna, seperti apakah ada kecenderungan pengguna memberikan rating lebih tinggi atau lebih rendah pada periode tertentu.
"""

from datetime import datetime

# Mengonversi timestamp ke datetime
ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

# Mengekstrak tahun dari timestamp
ratings['year'] = ratings['timestamp'].dt.year

# Menghitung rating rata-rata per tahun
average_rating_per_year = ratings.groupby('year')['rating'].mean()

# Visualisasi rating rata-rata sepanjang waktu
plt.figure(figsize=(12, 6))
average_rating_per_year.plot(kind='line', marker='o')
plt.title('Rating Rata-Rata Film per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Rating Rata-Rata')
plt.grid(True)
plt.show()

average_rating_per_year.tail(10)

"""Visualisasi rating rata-rata film per tahun menunjukkan beberapa hal:

- **Fluktuasi Rating**: Rating rata-rata berfluktuasi setiap tahun, dengan beberapa tahun mengalami peningkatan sementara tahun lainnya mengalami penurunan.
- **Tren Terkini**: Dalam dekade terakhir, rating rata-rata relatif stabil dengan sedikit perubahan tahunan. Tahun 2013 menonjol dengan rating rata-rata yang lebih tinggi dibandingkan tahun lainnya.
- **Stabilitas**: Meskipun ada variasi tahunan, rating rata-rata tetap berada dalam kisaran yang stabil, menunjukkan bahwa penilaian film oleh pengguna tidak mengalami perubahan drastis seiring waktu.

Analisis ini mengindikasikan bahwa meskipun ada fluktuasi tahunan, tidak ada tren yang jelas menunjukkan peningkatan atau penurunan rating rata-rata yang diberikan oleh pengguna secara keseluruhan.

## Pengaruh Tahun Rilis terhadap Rating
Kita akan menganalisis apakah film yang dirilis lebih baru cenderung menerima rating lebih tinggi atau lebih rendah dibandingkan dengan film yang lebih lama, dengan menghubungkan tahun rilis film dengan rating rata-rata yang diterima.
"""

# Menghitung rating rata-rata per film dengan menggabungkan rating dan movies DataFrame
rating_per_film_with_year = pd.merge(ratings, movies, on='movieId')

# Mengekstrak tahun dari judul film untuk setiap rating
rating_per_film_with_year['release_year'] = rating_per_film_with_year['title'].str.extract(r'\((\d{4})\)').astype(float)

# Menghitung rating rata-rata per tahun rilis film
average_rating_per_release_year = rating_per_film_with_year.groupby('release_year')['rating'].mean()

# Visualisasi rating rata-rata berdasarkan tahun rilis film
plt.figure(figsize=(12, 6))
average_rating_per_release_year.plot(kind='line', marker='o')
plt.title('Rating Rata-Rata Berdasarkan Tahun Rilis Film')
plt.xlabel('Tahun Rilis')
plt.ylabel('Rating Rata-Rata')
plt.xlim(1920, 2020)  # Memfokuskan plot pada rentang tahun tertentu
plt.grid(True)
plt.show()

average_rating_per_release_year.tail(10)

"""Visualisasi rating rata-rata berdasarkan tahun rilis film menunjukkan beberapa hal:

- **Fluktuasi Rating**: Terdapat variasi dalam rating rata-rata yang diterima film bergantung pada tahun rilisnya, yang mencerminkan perubahan dalam preferensi penonton dan kualitas film dari tahun ke tahun.
- **Tren Terkini**: Dalam dekade terakhir (2009-2018), rating rata-rata cenderung stabil dengan sedikit variasi antar tahun. Beberapa tahun, seperti 2017, menunjukkan rating rata-rata yang lebih tinggi.
- **Stabilitas Jangka Panjang**: Secara keseluruhan, tidak ada tren yang jelas menunjukkan peningkatan atau penurunan rating rata-rata berdasarkan tahun rilis. Rating rata-rata film tetap stabil meskipun ada fluktuasi tahunan.

Analisis ini menyimpulkan bahwa tidak ada bukti kuat yang menunjukkan film baru secara konsisten mendapat rating lebih tinggi atau lebih rendah dibandingkan film lama, yang mengindikasikan bahwa persepsi kualitas film oleh penonton tidak tergantung pada tahun rilisnya.

# Data Preparation

## Menggabungkan Data Movies dengan Genre dan Tags
"""

# Menggabungkan semua tag menjadi satu string per movieId
tags_aggregated = tags.groupby('movieId')['tag'].apply(lambda x: '|'.join(x)).reset_index()

# Menggabungkan movies_df dengan tags_aggregated berdasarkan movieId
movies_with_tags = pd.merge(movies, tags_aggregated, on='movieId', how='left')

# Ganti nilai NaN dengan string kosong pada kolom 'tag'
movies_with_tags['tag'].fillna('', inplace=True)

movies_with_tags.head()

"""## Persiapan Data untuk Pemodelan"""

# Menggabungkan semua tag untuk setiap movieId
tags_combined = tags.groupby('movieId')['tag'].apply(lambda x: '|'.join(x)).reset_index()

# Menggabungkan tags_combined dengan dataframe movies
movies_with_tags = pd.merge(movies, tags_combined, on='movieId', how='left')

# Ganti nilai NaN dengan string kosong pada kolom 'tag'
movies_with_tags['tag'].fillna('', inplace=True)

# Membuat kolom 'combined_features' yang menggabungkan genre dan tag
movies_with_tags['combined_features'] = movies_with_tags['genres'] + '|' + movies_with_tags['tag']

movies_with_tags.head()

"""Sekarang dataset sudah siap digunakan untuk membangun model rekomendasi berbasis konten, di mana kolom 'combined_features' akan menjadi elemen utama untuk menghitung kesamaan antar film.

# Mengembangkan Model Content Based Filtering

Setelah dataset siap, langkah berikutnya adalah mengembangkan model sistem rekomendasi. Kita akan menggunakan teknik content-based filtering untuk memberikan rekomendasi film berdasarkan kesamaan konten.

Langkah-langkah yang akan dilakukan meliputi:
1. Mengubah kolom combined_features menjadi matriks vektor menggunakan TF-IDF Vectorizer.
2. Menghitung skor kesamaan antar film dengan metode cosine similarity.
3. Mengembangkan fungsi yang menerima judul film sebagai input dan mengembalikan daftar film yang serupa sebagai rekomendasi.

## TF-IDF Vectorizer

Untuk membangun model sistem rekomendasi berbasis konten, langkah pertama adalah mengubah teks dalam kolom combined_features menjadi format numerik yang dapat diproses oleh algoritma.

Kami akan menggunakan TF-IDF Vectorizer untuk mencapai tujuan ini.
"""

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import numpy as np

# Menggunakan TF-IDF Vectorizer untuk mengonversi teks kombinasi genre dan tag menjadi matriks fitur
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_with_tags['combined_features'])
tfidf_vectorizer.get_feature_names_out()

"""## Cosine Similarity

Menghitung skor kesamaan antar film dengan menerapkan metode cosine similarity.
"""

# Menghitung skor kesamaan cosine antar film
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

"""## Fungsi Model Content Based Filtering

Membuat fungsi yang menerima judul film sebagai input dan memberikan rekomendasi film yang memiliki kesamaan.
"""

from IPython.display import display, Markdown

# Fungsi untuk mendapatkan rekomendasi film berdasarkan judul film
def create_recommendation_table(random_movie_title, movies_with_tags, cosine_sim):
    # Mendapatkan indeks film yang sesuai dengan judul
    idx = movies_with_tags.index[movies_with_tags['title'] == random_movie_title].tolist()[0]

    # Mendapatkan skor kesamaan untuk semua film dengan film input
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Mengurutkan film berdasarkan skor kesamaan
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Mendapatkan skor untuk 10 film teratas dan diri sendiri
    sim_scores = sim_scores[1:11]

    # Mendapatkan indeks film
    movie_indices = [i[0] for i in sim_scores]

    # Mendapatkan skor kesamaan
    similarity_scores = [i[1] for i in sim_scores]

    # Menyusun informasi ke dalam DataFrame
    recommendation_data = movies_with_tags.loc[movie_indices]
    recommendation_data['similarity_score'] = similarity_scores

    # Menambahkan kolom tahun dari judul film
    recommendation_data['year'] = recommendation_data['title'].str.extract(r'\((\d{4})\)')

    # Menyaring kolom yang relevan
    recommendation_table = recommendation_data[['title', 'year', 'genres', 'tag', 'similarity_score']]

    return recommendation_table

"""Membuat fungsi untuk menghitung precision."""

def calculate_precision_for_movie(random_movie_title, top_n_recommendations=10):
    # Mendapatkan indeks film yang sesuai dengan movieId
    idx = movies_with_tags.index[movies_with_tags['title'] == random_movie_title].tolist()[0]


    # Mendapatkan skor kesamaan untuk semua film dengan film input
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Mengurutkan film berdasarkan skor kesamaan
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Mendapatkan skor untuk top_n_recommendations film teratas (mengabaikan diri sendiri)
    sim_scores = sim_scores[1:top_n_recommendations + 1]

    # Mendapatkan indeks film
    movie_indices = [i[0] for i in sim_scores]

    # Menghitung relevansi berdasarkan genre yang sama
    target_movie_genres = set(movies_with_tags.loc[movies_with_tags['title'] == random_movie_title, 'genres'].iloc[0].split('|'))
    recommended_movies_genres = movies_with_tags.loc[movie_indices, 'genres'].apply(lambda x: set(x.split('|')))
    relevancy_count = recommended_movies_genres.apply(lambda x: len(target_movie_genres.intersection(x)) > 0).sum()

    # Menghitung precision
    precision = relevancy_count / top_n_recommendations

    return precision

"""## Mendapatkan Rekomendasi

Menjalankan fungsi yang menerima judul film secara acak sebagai input dan memberikan rekomendasi film serupa berdasarkan kesamaan konten.
"""

# Memilih film acak dari dataset
random_movie_title = movies_with_tags['title'].sample().iloc[0]

# Mendapatkan informasi genre dan tag untuk random_movie_title
selected_movie_info = movies_with_tags.loc[movies_with_tags['title'] == random_movie_title, ['genres', 'tag']].iloc[0]
selected_movie_genre = selected_movie_info['genres']
selected_movie_tag = selected_movie_info['tag']

# Menampilkan judul, genre, dan tag dari film yang dipilih
display(Markdown(f"### Judul film: {random_movie_title}"))
display(Markdown(f"- **Genre**: {selected_movie_genre}"))
display(Markdown(f"- **Tag**: {selected_movie_tag}"))

recommendation_table = create_recommendation_table(random_movie_title, movies_with_tags, cosine_sim)

# Tampilkan judul film yang dipilih
display(Markdown(f"- **Judul film**: {random_movie_title}"))

# Menyiapkan tabel hasil rekomendasi
# Ambil kolom yang relevan dari 'recommendation_table'
result_columns = ['title', 'year', 'genres', 'tag', 'similarity_score']
recommendation_result = recommendation_table[result_columns]

# Menghitung precision
precision_recommendation_result = calculate_precision_for_movie(random_movie_title)

# Tampilkan tabel hasil rekomendasi
display(Markdown("### Tabel hasil rekomendasi:"))
display(recommendation_result)

# Menampilkan precision
display(Markdown(f"### Nilai precision: {precision_recommendation_result}"))

"""# Mengembangkan Model Collaborative Filtering

## Persiapan Data

Dalam pengembangan sistem rekomendasi, sering kali lebih efisien untuk menggunakan indeks yang berurutan dibandingkan dengan ID asli, karena ini dapat mengurangi kompleksitas dan penggunaan memori. Untuk itu, kita mengonversi userId dan movieId menjadi tipe kategori, lalu menggunakan .cat.codes untuk mengubahnya menjadi kode kategori yang berurutan.
"""

# Mengubah userId dan movieId menjadi kategori yang berurutan
ratings['userId'] = ratings['userId'].astype('category').cat.codes
ratings['movieId'] = ratings['movieId'].astype('category').cat.codes

"""Dengan menggunakan .nunique(), kita dapat mengetahui jumlah pengguna dan film dengan mendapatkan jumlah elemen unik dalam setiap kolom, yang membantu kita memahami dimensi dari data yang kita miliki."""

# Mendapatkan jumlah pengguna dan film
num_users = ratings['userId'].nunique()
num_movies = ratings['movieId'].nunique()
num_users, num_movies

"""## Membagi Data Untuk Training dan Validasi

Sebelum melatih model, kita perlu membagi data menjadi set latih dan validasi. Pembagian ini penting agar model dapat dilatih pada satu subset data dan diuji pada subset lainnya, memastikan bahwa model mampu memprediksi rating film dengan akurat pada data yang belum pernah dilihat. Untuk itu, kita menggunakan fungsi train_test_split dari pustaka sklearn.model_selection.
"""

from sklearn.model_selection import train_test_split

# Membuat dataset untuk model
X = ratings[['userId', 'movieId']].values
y = ratings['rating'].values

# Membagi data menjadi set latih dan validasi
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

"""- X adalah matriks fitur yang mencakup userId dan movieId.
- y adalah target yang ingin diprediksi, yaitu rating.
- test_size=0.2 berarti 20% dari data akan digunakan untuk set validasi, sedangkan 80% sisanya digunakan untuk latihan.
- random_state mengatur seed untuk pembagian acak, memastikan konsistensi pembagian data setiap kali kode dijalankan.

## Membuat Model

Membangun model sistem rekomendasi film dengan menggunakan TensorFlow dan Keras. Fungsi RecommenderNet dari Keras digunakan untuk mendefinisikan model yang memprediksi rating film berdasarkan interaksi antara pengguna dan film.
"""

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense, Concatenate, Dropout
from tensorflow.keras.regularizers import l2

def RecommenderNet(num_users, num_movies, embedding_size):
    # Input layers
    user_input = Input(shape=(1,), name='user_input')
    movie_input = Input(shape=(1,), name='movie_input')

    # Embedding layers dengan regularisasi
    user_embedding = Embedding(num_users, embedding_size, name='user_embedding', embeddings_regularizer=l2(0.01))(user_input)
    movie_embedding = Embedding(num_movies, embedding_size, name='movie_embedding', embeddings_regularizer=l2(0.01))(movie_input)

    # Flatten the embeddings
    user_vector = Flatten(name='flatten_users')(user_embedding)
    movie_vector = Flatten(name='flatten_movies')(movie_embedding)

    # Concatenate user and movie vectors
    concatenated = Concatenate()([user_vector, movie_vector])

    # Dense layer dengan dropout
    dense = Dense(128, activation='relu')(concatenated)
    dropout = Dropout(0.5)(dense)
    output = Dense(1)(dropout)

    model = Model(inputs=[user_input, movie_input], outputs=output)

    model.compile(loss='mean_squared_error', optimizer='adam')

    return model

# Contoh membuat model dengan modifikasi
model = RecommenderNet(num_users, num_movies, 50)

"""## Proses Training Data

Memulai proses pelatihan model rekomendasi menggunakan TensorFlow dan Keras. Parameter epochs=10 menentukan bahwa model akan melewati seluruh dataset sebanyak 10 kali selama proses pelatihan. Setiap epoch memberikan kesempatan bagi model untuk memperbaiki kesalahan prediksi berdasarkan iterasi sebelumnya.
"""

history = model.fit([X_train[:, 0], X_train[:, 1]], y_train, epochs=10, validation_data=([X_val[:, 0], X_val[:, 1]], y_val))

"""## Visualisasi Metrik

Visualisasi proses pelatihan model rekomendasi dengan menampilkan perubahan nilai *loss* selama pelatihan dan validasi. Ini sangat penting untuk memahami bagaimana model berkembang seiring waktu dan untuk mendeteksi apakah model mengalami overfitting (terlalu cocok dengan data latih) atau underfitting (tidak cukup belajar dari data latih). Dengan memantau grafik loss ini, kita bisa menilai efektivitas model dan membuat keputusan yang lebih baik terkait perbaikan atau modifikasi model.
"""

import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Losses')
plt.legend()
plt.show()

"""Menyiapkan pemetaan ulang untuk user dan movie"""

# Menyiapkan pemetaan kembali untuk user dan movie
user_ids = ratings['userId'].unique().tolist()
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

movie_ids = ratings['movieId'].unique().tolist()
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

"""Membuat fungsi `make_recommendation` yang bertujuan untuk memberikan rekomendasi film kepada seorang pengguna berdasarkan prediksi yang dihasilkan oleh model yang telah dilatih sebelumnya."""

import numpy as np

def make_recommendation(model, user_id, num_recommendations=10):
    # Periksa apakah user_id perlu di-encode
    # Jika perlu, gunakan struktur data yang sesuai untuk mencari kode pengguna
    user_encoded = user_to_user_encoded.get(user_id)
    if user_encoded is None:
        raise ValueError("UserID not found in encoded user IDs.")

    # Menyiapkan movie_ids yang belum ditonton oleh user
    movie_ids = np.setdiff1d(movies['movieId'].unique(), ratings[ratings['userId'] == user_id]['movieId'])

    # Encoding movie_ids
    movie_ids_encoded = [movie_to_movie_encoded.get(x) for x in movie_ids if movie_to_movie_encoded.get(x) is not None]

    user_encoded_array = np.array([user_encoded] * len(movie_ids_encoded))
    movie_ids_encoded_array = np.array(movie_ids_encoded)

    # Melakukan prediksi
    predictions = model.predict([user_encoded_array, movie_ids_encoded_array])

    # Mendapatkan rekomendasi berdasarkan prediksi rating tertinggi
    top_ratings_indices = predictions.flatten().argsort()[-num_recommendations:][::-1]
    recommended_movie_ids_encoded = [movie_ids_encoded_array[x] for x in top_ratings_indices]

    # Mendapatkan movieId asli dari rekomendasi
    recommended_movie_ids = [movie_encoded_to_movie.get(movie_encoded) for movie_encoded in recommended_movie_ids_encoded]

    return movies[movies['movieId'].isin(recommended_movie_ids)]

"""## Mendapatkan Rekomendasi

Menampilkan rekomendasi film untuk pengguna acak dari dataset dengan memanggil fungsi `make_recommendation`.
"""

import pandas as pd
from IPython.display import display, Markdown
import numpy as np
import random

# Memilih user ID acak dari dataset
random_user_id = random.choice(user_ids)

# Tampilkan 3 film teratas yang dinilai oleh user
top_rated_movies_by_user = ratings[ratings['userId'] == random_user_id].sort_values(by='rating', ascending=False).head(3)

# Gabungkan dengan dataframe movies untuk mendapatkan judul film
top_rated_movies_info = top_rated_movies_by_user.merge(movies, on='movieId', how='left')[['title', 'rating']]

# Generate rekomendasi untuk user ini
recommended_movies = make_recommendation(model, random_user_id, num_recommendations=5)

# Menampilkan hasil
display(Markdown(f"## User ID: {random_user_id}"))
display(Markdown(f"### 5 Film Teratas yang Dinilai oleh User:"))
display(top_rated_movies_info)

display(Markdown(f"### Daftar Film Rekomendasi:"))
display(recommended_movies[['title']])
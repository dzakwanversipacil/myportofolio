# 🚀 Personal Portfolio Web Application

A dynamic, responsive personal portfolio website developed to showcase projects, experiences, and educational background. Originally built as a semantic static site, the project has been iteratively engineered into a dynamic web application using the Django framework.

**Dzakwan Farabi Al Muzhaffar** | NPM: 2506612436 | PBP F

---

## 🌟 Features

- **Dynamic Content Management:** Utilizes Django's Model-View-Template (MVT) architecture for database-driven content rendering, allowing seamless updates to Experience and Education sections via the admin panel.
- **Semantic Structure:** Strictly adheres to HTML5 semantic tags (`<header>`, `<main>`, `<article>`, `<section>`) ensuring high accessibility and SEO optimization.
- **Fluid Responsive UI:** Implements advanced CSS techniques including Flexbox, Grid areas, and fluid typography (`clamp()`) to ensure the layout adapts elegantly across mobile and desktop viewports without excessive media queries.

## 💻 Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** HTML5, CSS3
- **Testing:** Django `TestCase`, `Client`

## 📂 Project Structure

The main directory structure of this project repository:

```text
myportofolio/
├── main/                   # Main Django application directory
│   ├── migrations/         # Database schema migration history
│   ├── models.py           # Database schema definitions (Experience, Education)
│   ├── tests.py            # Application functional tests (Unit Tests)
│   ├── urls.py             # App-level URL routing configuration
│   └── views.py            # Request and response processing logic
├── portofolio/             # Project-level Django configuration directory
│   ├── settings.py         # Global project settings and configurations
│   └── urls.py             # Root URL declarations
├── static/                 # Static assets directory
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── img/                # Image assets
├── templates/              # HTML templates directory
│   ├── education.html
│   ├── experience.html
│   └── index.html
├── .gitignore              # Ignored files and directories
├── README.md               # Project documentation
├── manage.py               # Django command-line utility
└── requirements.txt        # Python dependencies list
```

## ⚙️ Setup and Installation

Follow these steps to run the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dzakwanversipacil/myportofolio.git
   cd myportofolio
   ```
2. **Set Up Virtual Environment & Install Dependencies**
   ```bash
   python -m venv env
   env\Scripts\activate       # On Windows
   # source env/bin/activate  # On macOS/Linux
   pip install -r requirements.txt
   ```
3. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at http://localhost:8000 in your browser.

## 📚 Individual Assignment Reflections (in Indonesian)

<details>
<summary><b>Tugas 1</b></summary>

**1. Penggunaan Elemen Semantik HTML5**  
Dalam proyek ini, saya mengimplementasikan elemen semantik seperti `<header>`, `<main>`, `<section>`, `<article>`, dan `<footer>`. `<section>` digunakan untuk memisahkan area _Profile_, _Experience_, dan _Education_. Di dalamnya, `<article>` meng-_wrap_ komponen mandiri seperti _card_ pengalaman dan pendidikan. Berdasarkan yang saya pelajari, penggunaan elemen ini mempermudah pembacaan struktur DOM sehingga sangat esensial untuk SEO dan aksesibilitas (_screen readers_), serta membuat manajemen _styling_ CSS jauh lebih terstruktur dibandingkan menggunakan `<div>` yang tidak memiliki makna semantik.

**2. Tantangan Tata Letak Responsif**  
Tantangan utama saya dalam proyek ini adalah adalah menjaga agar _card_ pengalaman dan pendidikan tetap rapi tanpa harus menulis puluhan _media query_. Saya mengatasinya dengan menggunakan _Flexbox_ (`flex-direction: column` untuk _mobile_ dan `row` untuk _desktop_) serta _Grid areas_ pada bagian profil. Untuk mencegah teks terlihat aneh saat berpindah _device_, saya memprioritaskan fungsi CSS `clamp(3rem, 5vw, 6rem)` sehingga ukuran tipografi bisa beradaptasi secara cair dengan lebar _viewport_-nya. Elemen foto juga diprioritaskan untuk pindah ke bawah teks utama saat resolusi di bawah `600px` agar ruang baca tetap optimal.

**3. Batasan Static Web & Fungsionalitas Dinamis**  
Batasan paling terasa dari _static web_ adalah inefisiensi terhadap perubahan data. Jika saya ingin menambah pengalaman baru atau mengubah detail pembelajaran yang saya ambil, saya harus memodifikasi elemen HTML secara manual berulang kali (karena masih _hardcoded_). Fungsionalitas dinamis yang paling ingin saya tambahkan pada iterasi proyek selanjutnya adalah integrasi _database_ menggunakan model Django untuk entri _Experience_ dan _Education_, sehingga konten dapat dirender melalui _looping_ di _template_ dan dikelola praktis lewat halaman admin. Selain itu, saya juga awalnya terpikir untuk membuat semacam _carousel_ pada _image_ yang dilampirkan, tetapi karena sepertinya lebih baik ditambahkan nanti saat lebih banyak yang dipelajari, saya berencana untuk mengadakannya pada iterasi berikutnya.

**AI Disclosure**  
Saya menggunakan AI (Google Gemini) sebagai teman berpikir untuk merancang seluruh bagian CSS dan menjadi kritikus pekerjaan saya. Saya mengakui bahwa melakukan _styling_ pada CSS cenderung sulit dan seringkali tidak terbayang sehingga Gemini dapat membantu saya memberi gambaran web lebih lanjutnya yang kemudian bisa saya _tune_ agar sesuai dengan keinginan saya.

AI cenderung menghasilkan efek animasi yang terlalu berlebihan atau menggunakan angka yang tidak konsisten. Saya melakukan perbaikan manual dengan mengubah beberapa angka menjadi lebih sesuai dengan web yang saya buat, serta mengedit secara manual deskripsi-deskripsi yang ada agar secara akurat merefleksikan proses pembelajaran yang sesungguhnya saya jalani, tidak hanya menempelkan teks _dummy_. Saya juga menyortir mana perubahan yang dapat saya terima dan memanfaatkan AI untuk memberi masukan terhadap pekerjaan yang saya lakukan sendiri.

Link AI Chat Log: https://share.gemini.google/4yEM9HA9VRJe

</details>
<br>
<details>
<summary><b>Tugas 2</b></summary>

**1. Alur MVT Django**  
Saat URL portofolio diakses, _request_-nya akan dicocokan dengan _path_ yang ada di `urls.py` proyek, lalu diteruskan ke `urls.py` aplikasi. Lalu, _path_ ini akan memanggil fungsi di `views.py` (misalnya `show_experience` atau `show_education`). _View_ bertugas untuk mengambil data dari Django melalui `models.py` (seperti model `Experience` atau `Education`), memasukannya ke dalam _dictionary_ `context`, dan mengirimkannya ke berkas HTML. Kemudian, _template_ merender data yang diterima menggunakan sintaks Django sebelum dikembalikan sebagai _HTTP response_ ke _browser_ pengguna.

**2. Keuntungan Menggunakan Django**  
Menyimpan data pada model, baik untuk bagian yang baru maupun yang lama, memungkinkan aplikasi bersifat dinamis. Jika suatu saat ada data baru yang harus ditambahkan (seperti pengalaman baru atau jenjang pendidikan baru), data cukup diinput lewat panel admin atau _shell_ tanpa perlu mengubah kode HTML lagi. Jika hal ini di-_hardcode_ seperti sebelumnya, setiap ada kasus perubahan data, struktur _template_-nya harus diubah secara manual sehingga rentan memunculkan _bug_ baru dan sangat tidak _scalable_.

**3. makemigrations vs migrate**  
Perintah `makemigrations` berfungsi untuk mengecek perubahan pada `models.py` dan menghasilkan berkas _migrations_ sebagai instruksi _update_. Sementara itu, `migrate` bertugas untuk mengeksekusi instruksinya ke dalam DBMS (_database management system_), dalam hal ini Django, agar struktur _database_ benar-benar berubah sesuai dengan perubahan yang kita lakukan.
Salah satu contoh penggunaan keduanya, ketika _field_ `title` tidak lagi diperlukan di model `Education`, setelah dilakukan penghapusan di `models.py`, kita dapat menjalankan perintah `makemigrations` untuk membuat instruksi _update_ pada _database_. Lalu, kita dapat menjalankan perintah `migrate` agar instruksi di berkas _migrations_ dieksekusi dan mengubah struktur Django sehingga tidak lagi memiliki _field_ `title`.

**AI Disclosure**  
Saya menggunakan AI (Google Gemini) sebagai teman berpikir untuk menentukan langkah-langkah pengerjaan Tugas Individu ini serta implementasinya secara garis besar. Selain itu, saya juga menggunakan AI untuk bertanya mengenai integrasi data lokal dengan proyek yang telah di-_deploy_, yang mana tidak ter-_connect_ karena sejak awal _database_-nya di-_gitignore_.

Petunjuk yang telah diberikan sangat membantu saya agar tidak bingung mulai dari mana, dengan penyesuaian di setiap langkah agar lebih konkret dan relevan dengan proyek portofolio ini. Selain itu, informasi yang diberikan juga membantu saya dalam memahami lebih lanjut mengenai _nature_ dari Django itu sendiri sebagai _helper_ untuk integrasi _frontend_ dan _backend_ pada model MVT. Meskipun AI tidak selalu benar dan dapat menyesatkan (terutama jika AI lupa konteks), penanganan informasi yang baik dapat membawa dampak positif bagi tugas ini.

Link AI Chat Log: https://share.gemini.google/ivS3fFi6JzJP

</details>

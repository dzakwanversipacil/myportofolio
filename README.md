Nama : Dzakwan Farabi Al Muzhaffar

NPM : 2506612436

Kelas : PBP F

# Portfolio Dzakwan Farabi Al Muzhaffar

## Deskripsi Proyek

Website portofolio statis pribadi yang dibangun menggunakan HTML5 semantik dan CSS3 murni tanpa _framework_. Proyek ini dikembangkan untuk memenuhi Tugas Individu 1 mata kuliah Pemrograman Berbasis Platform.

## Cara Menjalankan (Setup)

1. Lakukan _clone_ pada repositori ini ke _device_ lokal.
2. Buka terminal dan arahkan ke direktori proyek.
3. Jalankan _virtual environment_ dan _install dependencies_ (sesuai kerangka Django dari tutorial).
4. Gunakan perintah `python manage.py runserver`.
5. Buka `http://localhost:8000` di _browser_.

### Tugas 1

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

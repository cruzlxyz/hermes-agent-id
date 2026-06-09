# Hermes Skills Indonesia

Kumpulan **Hermes Agent skills** berbahasa Indonesia: panduan kerja praktis yang bisa dipasang di Hermes agar agent lebih jago menjalankan tugas tertentu.

Repo ini dibuat untuk orang Indonesia yang ingin memakai Hermes dengan cara yang mudah, jelas, dan bisa langsung dicoba.

## Apa itu Hermes Skill?

Skill adalah file `SKILL.md` berisi prosedur reusable untuk Hermes Agent. Isinya bisa berupa:

- kapan skill dipakai,
- langkah kerja yang jelas,
- command yang perlu dijalankan,
- checklist verifikasi,
- jebakan umum dan solusinya.

Hermes bisa memuat skill ini saat user meminta tugas yang relevan, jadi agent tidak perlu menebak-nebak workflow dari nol.

## Struktur Repo

```text
.
├── skills/                 # Skill siap pakai
│   └── contoh-basic/       # Contoh skill pertama
│       └── SKILL.md
├── templates/              # Template untuk membuat skill baru
│   └── SKILL.template.md
├── docs/                   # Panduan bahasa Indonesia
│   ├── cara-pasang.md
│   └── cara-buat-skill.md
├── CONTRIBUTING.md         # Cara kontribusi
└── README.md
```

## Cara Pakai Skill dari Repo Ini

### Opsi 1 — install langsung dari URL `SKILL.md`

Kalau repo sudah dipush ke GitHub, skill bisa dipasang seperti ini:

```bash
hermes skills install https://raw.githubusercontent.com/USERNAME/hermes-skills-indonesia/main/skills/contoh-basic/SKILL.md
```

Ganti `USERNAME` dengan username GitHub pemilik repo.

### Opsi 2 — copy ke folder Hermes lokal

Di Windows/Git Bash:

```bash
mkdir -p ~/.hermes/skills/community/contoh-basic
cp skills/contoh-basic/SKILL.md ~/.hermes/skills/community/contoh-basic/SKILL.md
```

Lalu mulai sesi Hermes baru atau pakai `/reload-skills` kalau tersedia di sesi kamu.

### Opsi 3 — tambahkan repo sebagai skill tap

Jika repo sudah ada di GitHub:

```bash
hermes skills tap add https://github.com/USERNAME/hermes-skills-indonesia
hermes skills browse
```

## Prinsip Skill di Repo Ini

1. **Bahasa Indonesia dulu** — simpel, natural, tidak terlalu formal.
2. **Langsung bisa dipakai** — jangan cuma teori; kasih langkah nyata.
3. **Ada verifikasi** — agent harus tahu cara mengecek hasilnya benar.
4. **Aman** — command destruktif harus dijelaskan dan tidak dijalankan sembarangan.
5. **Bermanfaat untuk umum** — bukan cuma cocok di satu komputer pribadi.

## Ide Skill yang Bisa Ditambahkan

- setup Telegram bot dengan Hermes
- pakai Tempo MPP dari Hermes
- workflow Base MCP / wallet onchain
- bikin ringkasan YouTube bahasa Indonesia
- QA website sederhana
- bikin PR GitHub dari issue
- generate konten sosial media
- riset token/proyek crypto secara aman

## Status

Repo lokal awal sudah siap. Setelah dicek, push ke GitHub dan share URL-nya agar orang lain bisa install skill dari sini.

## Lisensi

MIT — bebas dipakai, dimodifikasi, dan dibagikan.

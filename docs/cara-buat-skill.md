# Cara Membuat Skill Hermes Berbahasa Indonesia

Skill Hermes pada dasarnya adalah satu folder yang berisi `SKILL.md`.

Contoh struktur:

```text
skills/nama-skill/
└── SKILL.md
```

## Format Minimum

`SKILL.md` wajib punya frontmatter YAML di paling atas:

```markdown
---
name: nama-skill
description: Use when user wants to ...
version: 1.0.0
author: Nama Kamu
license: MIT
metadata:
  hermes:
    tags: [tag1, tag2]
    related_skills: []
---

# Judul Skill

Isi skill...
```

Catatan:

- `name` pakai huruf kecil dan tanda hubung, contoh: `riset-crypto-aman`.
- `description` sebaiknya tetap bahasa Inggris singkat karena dipakai agent untuk trigger matching. Isi body boleh full bahasa Indonesia.
- body harus ada, jangan kosong.

## Struktur yang Disarankan

```markdown
# Nama Skill

## Overview
Penjelasan singkat skill ini untuk apa.

## When to Use
- Pakai saat user meminta ...
- Pakai saat agent perlu ...

## Langkah Kerja
1. Langkah pertama.
2. Langkah kedua.
3. Verifikasi hasil.

## Contoh Prompt
Contoh permintaan user yang cocok.

## Common Pitfalls
- Kesalahan umum dan cara menghindarinya.

## Verification Checklist
- [ ] Hasil sudah dicek.
- [ ] Tidak ada data sensitif bocor.
```

## Checklist Sebelum Submit

- [ ] File berada di `skills/nama-skill/SKILL.md`.
- [ ] Tidak ada baris kosong sebelum `---`.
- [ ] Ada `name` dan `description`.
- [ ] Isi memakai bahasa Indonesia yang mudah dimengerti.
- [ ] Ada langkah kerja nyata, bukan cuma teori.
- [ ] Ada bagian verifikasi.
- [ ] Tidak menyimpan API key, private key, seed phrase, token, atau password.

## Validasi Cepat

Jalankan dari root repo:

```bash
python scripts/validate_skills.py
```

Kalau semua aman, output akan menampilkan `OK` untuk tiap skill.

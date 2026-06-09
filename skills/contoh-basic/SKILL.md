---
name: contoh-basic
description: Use when user wants a simple Indonesian example of how a Hermes Agent skill should be written and verified.
version: 1.0.0
author: 0xcruzl community
license: MIT
metadata:
  hermes:
    tags: [indonesia, example, hermes-skill]
    related_skills: []
---

# Contoh Basic Skill

## Overview

Skill ini adalah contoh paling sederhana untuk menunjukkan struktur `SKILL.md` yang rapi, mudah dibaca, dan bisa dipakai oleh Hermes Agent.

Tujuannya bukan menyelesaikan satu masalah kompleks, tapi memberi pola dasar bagi contributor baru yang ingin membuat skill berbahasa Indonesia.

## When to Use

Pakai skill ini saat:

- user ingin melihat contoh skill Hermes yang sederhana,
- contributor baru ingin meniru format skill,
- agent perlu menjelaskan cara menulis skill tanpa terlalu teknis.

Jangan pakai skill ini saat:

- user butuh workflow spesifik seperti GitHub PR, crypto wallet, atau automation kompleks,
- sudah ada skill lain yang lebih tepat untuk tugas tersebut.

## Langkah Kerja

1. Baca tujuan user.
2. Jelaskan bahwa skill Hermes terdiri dari frontmatter dan body markdown.
3. Tunjukkan struktur sederhana: `Overview`, `When to Use`, `Langkah Kerja`, `Common Pitfalls`, dan `Verification Checklist`.
4. Kalau user ingin membuat skill baru, arahkan memakai `templates/SKILL.template.md`.
5. Verifikasi file skill punya `name`, `description`, dan body yang tidak kosong.

## Contoh Prompt User

```text
Bikinin contoh skill Hermes bahasa Indonesia yang gampang dipahami.
```

## Common Pitfalls

1. **Frontmatter tidak valid.** Pastikan file dimulai langsung dengan `---` tanpa baris kosong.
2. **Description terlalu kabur.** Tulis trigger yang jelas, misalnya `Use when user wants ...`.
3. **Tidak ada verifikasi.** Skill bagus harus memberi cara untuk mengecek hasil.
4. **Terlalu personal.** Hindari path lokal khusus satu user kecuali memang diberi alternatif umum.

## Verification Checklist

- [ ] `SKILL.md` dimulai dengan frontmatter YAML.
- [ ] Ada `name` dan `description`.
- [ ] Isi body menjelaskan kapan dipakai dan langkah kerja.
- [ ] Ada common pitfalls.
- [ ] Ada checklist verifikasi.

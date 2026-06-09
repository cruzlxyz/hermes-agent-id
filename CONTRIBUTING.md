# Kontribusi ke Hermes Skills Indonesia

Makasih sudah mau bantu bikin skill Hermes yang bermanfaat untuk banyak orang.

## Cara Menambah Skill Baru

1. Copy template:

```bash
mkdir -p skills/nama-skill
cp templates/SKILL.template.md skills/nama-skill/SKILL.md
```

2. Edit `skills/nama-skill/SKILL.md`.
3. Jalankan validasi:

```bash
python scripts/validate_skills.py
```

4. Commit perubahan:

```bash
git add skills/nama-skill/SKILL.md
git commit -m "feat: tambah skill nama-skill"
```

## Aturan Penulisan

- Pakai bahasa Indonesia yang mudah dipahami.
- Tetap tulis `description` dengan pola `Use when ...` agar mudah dicocokkan oleh agent.
- Kasih langkah kerja yang konkret.
- Tambahkan checklist verifikasi.
- Jangan commit credential: API key, private key, seed phrase, token, password, file `.env`.

## Format Commit

Contoh:

```text
feat: tambah skill riset-crypto-aman
fix: perbaiki contoh instalasi skill
docs: tambah panduan kontribusi
```

## Review Sederhana

Sebelum submit, tanya diri sendiri:

- Apakah skill ini bisa dipakai orang lain?
- Apakah langkahnya jelas?
- Apakah ada cara verifikasi?
- Apakah tidak ada secret/data sensitif?

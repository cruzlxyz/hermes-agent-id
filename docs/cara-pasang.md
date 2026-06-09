# Cara Pasang Skill Hermes dari Repo Ini

Panduan ini dibuat untuk user Windows/Git Bash, tapi konsepnya sama untuk Linux/macOS.

## 1. Install dari raw GitHub URL

Format umum:

```bash
hermes skills install https://raw.githubusercontent.com/USERNAME/hermes-skills-indonesia/main/skills/NAMA-SKILL/SKILL.md
```

Contoh:

```bash
hermes skills install https://raw.githubusercontent.com/USERNAME/hermes-skills-indonesia/main/skills/contoh-basic/SKILL.md
```

Setelah install, mulai session Hermes baru agar skill terdeteksi penuh.

## 2. Copy manual ke folder skill lokal

```bash
mkdir -p ~/.hermes/skills/community/contoh-basic
cp skills/contoh-basic/SKILL.md ~/.hermes/skills/community/contoh-basic/SKILL.md
```

Cek apakah skill ada:

```bash
hermes skills list
```

## 3. Pakai skill dalam chat Hermes

Di CLI Hermes:

```text
/skill contoh-basic
```

Atau jalankan Hermes dengan preload skill:

```bash
hermes -s contoh-basic
```

## Troubleshooting

### Skill belum muncul

Coba:

```bash
hermes skills list
```

Kalau belum ada, cek lokasi file dan pastikan namanya `SKILL.md`.

### Format skill invalid

Pastikan `SKILL.md` dimulai dari baris pertama dengan:

```yaml
---
name: nama-skill
description: Use when ...
---
```

Tidak boleh ada spasi atau baris kosong sebelum `---`.

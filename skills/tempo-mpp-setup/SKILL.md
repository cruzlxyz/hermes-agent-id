---
name: tempo-mpp-setup
description: Use when user wants to set up, configure, and utilize the Tempo Machine Payments Protocol (MPP) and Tempo Wallet using the CLI via WSL in Hermes.
version: 1.0.0
author: 0xcruzl community
license: MIT
metadata:
  hermes:
    tags: [tempo, mpp, machine-payments, wallet, deepseek, exa, wsl]
    related_skills: []
---

# Setup & Penggunaan Tempo MPP Wallet di Hermes

## Overview

Tempo Machine Payments Protocol (MPP) adalah sistem yang memungkinkan mesin/agent (Hermes) melakukan pembayaran atas namamu untuk menggunakan layanan AI seperti **DeepSeek** atau search engine **Exa**. 

Dengan setup ini, Hermes bisa menggunakan dompet Tempo-mu untuk berinteraksi dengan API berbayar secara aman menggunakan saldo Tempo Credits-mu di jaringan Windows via WSL (Windows Subsystem for Linux).

## When to Use

Pakai skill ini saat:
- User ingin menghubungkan dompet (wallet) Tempo ke dalam Hermes Agent.
- User ingin agar Hermes bisa memanggil model AI DeepSeek atau mesin pencari Exa melalui paket Machine Payments Protocol (MPP) Tempo.
- User berada di Windows dan ingin menjalankan script pembayaran onchain yang butuh environment Linux/Node.js via WSL.

## Prasyarat

1. **Akun Tempo:** Daftar dan dapatkan API Token / Mnemonic dari [Tempo Labs](https://www.tempo.xyz/).
2. **WSL Ubuntu:** Pastikan WSL Ubuntu sudah terinstall di Windows kamu.
3. **Tempo CLI:** Pastikan kamu sudah menginstall CLI Tempo di dalam WSL. 
4. **Folder Proyek:** Siapkan folder proyekmu di komputer Windows, contohnya: `C:/Users/[NAMA USER]/tempo-mpp-project/`.

## Langkah-Langkah Tata Cara Setup (Spesifik Windows + WSL)

Di lingkungan Hermes di Windows, kita akan menjalankan command Tempo CLI dari dalam terminal Git Bash, dengan cara "masuk" ke WSL Ubuntu. 

### 1. Persiapan Environment di WSL

Buka terminal WSL Ubuntu biasa (`wsl`), pastikan CLI Tempo sudah terinstall dan kunci API/mnemonic sudah tersimpan di `~/.tempo/env` di dalam WSL kamu.

### 2. Membuat File Eksekusi yang Aman

Buat file bernama `run_mpp.sh` di dalam folder proyekmu di Windows (contoh: `C:/Users/[NAMA USER]/tempo-mpp-project/run_mpp.sh`). Isi dengan kode berikut:

```bash
#!/bin/bash
# Script ini akan dijalankan oleh Hermes di dalam WSL
source ~/.tempo/env

# Eksekusi Perintah MPP berdasarkan parameter yang diberikan Hermes
AGENT_NAME=$1
PROMPT_TEXT=$2

tempo mpp execute --agent $AGENT_NAME --prompt "$PROMPT_TEXT"
```

### 3. Verifikasi Koneksi WSL dari Hermes

Di dalam terminal Hermes (Git Bash), verifikasi apakah kamu bisa masuk ke WSL dan membuka environment Tempo. Jalankan:

```bash
wsl -d Ubuntu -- bash -lc 'source ~/.tempo/env && tempo status'
```

*Jika sukses, kamu akan mendapatkan output status koneksi dompet Tempo kamu.*

### 4. Menjalankan Pembayaran MPP via Hermes

Saat kamu ingin Hermes memanggil DeepSeek atau Exa menggunakan Tempo, cukup suruh agent untuk menjalankan script `run_mpp.sh` yang ada di proyekmu. 

Hermes akan secara otomatis mengeksekusi command ini di terminal:

```bash
# Pastikan ganti [PATH PROYEKMU] dengan lokasi foldermu di Windows (contoh: /mnt/c/Users/cruzl/tempo-mpp-project/)
wsl -d Ubuntu -- bash -lc 'cd [PATH PROYEKMU] && bash run_mpp.sh deepseek "Cek harga ETH hari ini"'
```

## Common Pitfalls

1. **Masalah Permission `/mnt/c/...`**: WSL kadang punya permission Unix yang aneh ketika mengakses drive C:. Hindari menjalankan command yang membutuhkan permission tinggi langsung di folder Windows. Simpan file konfigurasi rahasia di dalam filesystem Ubuntu itu sendiri (`~/`).
2. **Path Tidak Ditemukan**: Jika WSL tidak bisa menemukan `tempo`, kemungkinan instalasi CLI Tempo dilakukan menggunakan npm global tanpa di-source ke dalam `.bashrc` atau `.profile`. Pastikan `$PATH` dalam WSL sudah benar.
3. **Token Aman**: Jangan pernah copy-paste mnemonic atau API token Tempo langsung ke dalam prompt chat Hermes. Simpan aman di dalam `~/.tempo/env` di dalam WSL, dan cukup panggil dengan `source ~/.tempo/env` seperti pada contoh di atas.

## Verification Checklist

- [ ] Command `wsl -d Ubuntu -- bash -lc 'tempo status'` berjalan tanpa error.
- [ ] Environment variable MPP (API keys, mnemonic) tersimpan aman di `~/.tempo/env` di dalam WSL.
- [ ] File `run_mpp.sh` sudah dibuat di dalam folder proyek Windows kamu.
- [ ] Agent mampu mengembalikan output query dari DeepSeek/Exa menggunakan saldo MPP-mu.

---
name: base-mcp-setup
description: Use when user wants to set up, configure, and use the Base MCP (Model Context Protocol) server for Coinbase Developer Platform (CDP) and onchain operations in Hermes.
version: 1.0.0
author: 0xcruzl community
license: MIT
metadata:
  hermes:
    tags: [base-mcp, onchain, crypto, coinbase, cdp, wallet]
    related_skills: []
---

# Setup & Penggunaan Base MCP di Hermes

## Overview

Base MCP adalah jembatan (Model Context Protocol) yang menghubungkan Hermes Agent kamu langsung ke jaringan blockchain Base (Coinbase Developer Platform / CDP). 

Dengan mengaktifkan Base MCP, Hermes bisa punya **wallet sendiri (Base Account)**, bisa mengecek saldo onchain, melakukan transfer (ETH/USDC), memanggil fungsi smart contract, bahkan melakukan minting NFT secara otomatis lewat prompt teks biasa.

## When to Use

Pakai skill ini saat:
- User ingin mengaktifkan fitur blockchain/onchain di Hermes.
- User ingin mengintegrasikan Coinbase Developer Platform (CDP) SDK ke dalam Hermes.
- Agent perlu melakukan aksi onchain (cek saldo, transfer token, deploy contract) di jaringan Base.

## Prasyarat

1. **CDP API Keys:** Kamu butuh API Key dari Coinbase Developer Platform.
   - Daftar di [Coinbase Developer Platform](https://cdp.coinbase.com/).
   - Buat API Key baru (kamu akan dapet file JSON berisi `name` dan `privateKey`).
2. **Node.js / npx:** Terinstall di sistem Windows/WSL kamu untuk menjalankan server MCP-nya.

## Langkah-Langkah Setup

### 1. Set API Credentials di `.env` Hermes

Simpan credential CDP kamu di file env Hermes agar aman. Di Git Bash:

```bash
# Buka env Hermes
hermes config env-path
```

Tambahkan baris berikut ke file `.env` kamu (sesuaikan dengan API Key yang kamu download dari CDP portal):

```env
# CDP API Key Name (bisa langsung dicopy dari file JSON CDP)
CDP_API_KEY_NAME="organizations/[org-id]/apiKeys/[api-key-id]"

# CDP API Key Private Key (berisi string panjang yang dimulai dengan string terenkripsi, copy mentah-mentah saja)
CDP_API_KEY_PRIVATE_KEY="-----BEGIN EC PRIVATE KEY-----\n[your-private-key-data-here]\n-----END EC PRIVATE KEY-----"
```
*Penting: Saat menyalin string `CDP_API_KEY_PRIVATE_KEY` dari file JSON kamu, pastikan karakter newline `\n` terbaca dengan benar di `.env`.*

### 2. Tambahkan Base MCP ke Hermes

Jalankan perintah ini untuk mendaftarkan server Base MCP ke konfigurasi Hermes:

```bash
hermes mcp add base-mcp --command "npx" --args "-y @coinbase/mcp-server"
```

*Catatan untuk Windows:* Pastikan `npx` sudah terinstall dan bisa dipanggil dari terminal Git Bash kamu.

### 3. Verifikasi Koneksi MCP

Cek apakah server MCP sudah terdaftar dengan benar:

```bash
hermes mcp list
```

Jika terdaftar, lakukan tes koneksi:

```bash
hermes mcp test base-mcp
```

### 4. Restart Hermes Sesi Baru

Buka sesi chat Hermes baru agar toolset baru dari Base MCP (seperti `get_balance`, `request_faucet`, `transfer`, dll.) dimuat sepenuhnya:

```bash
hermes
```
*(atau ketik `/reset` di dalam sesi chat aktif)*

## Cara Penggunaan (Prompt Contoh)

Setelah aktif, kamu bisa menyuruh Hermes melakukan hal-hal ini dalam bahasa Indonesia santai:

- **Cek Saldo:**
  *"Cek saldo wallet Base gue dong"* atau *"Berapa alamat wallet Base lo?"*
- **Minta Faucet (Testnet):**
  *"Tolong minta koin gratis (faucet) ke wallet lo di Base Sepolia"*
- **Transfer Token:**
  *"Kirim 0.001 ETH Sepolia ke alamat 0x123..."*
- **Cek Transaksi:**
  *"Tolong cek status tx hash 0xabc..."*

## Common Pitfalls

1. **Error: `npx: command not found`**
   - Solusi: Install Node.js di Windows terlebih dahulu. Download dari [nodejs.org](https://nodejs.org/).
2. **Koneksi Test Gagal (`mcp test` error):**
   - Pastikan format `CDP_API_KEY_PRIVATE_KEY` di `.env` sudah benar dan tidak ada karakter `\n` yang rusak. Karakter newline `\n` harus ditulis persis seperti teks mentah dari file JSON CDP.
3. **Wallet Mainnet vs Testnet:**
   - Secara default, Base MCP biasanya beroperasi di Base Sepolia (Testnet). Jangan mengirim dana real/Mainnet dalam jumlah besar sebelum kamu yakin konfigurasinya sudah di-switch ke Mainnet dan aman.

## Verification Checklist

- [ ] `CDP_API_KEY_NAME` dan `CDP_API_KEY_PRIVATE_KEY` ada di file `.env`.
- [ ] Command `hermes mcp list` menampilkan `base-mcp`.
- [ ] Toolset baru bertema onchain (seperti `coinbase_get_wallet_details`) muncul di daftar tool Hermes.
- [ ] Agent sukses mengembalikan alamat wallet Base miliknya saat ditanya.

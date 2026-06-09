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

## Langkah-Langkah Setup (Tata Cara Jelas & Mudah)

### 1. Simpan API Key di `.env` Hermes

Jangan simpan API Key langsung di dalam skill! Kita simpan di file rahasia `.env` milik Hermes. 
Di terminal Git Bash kamu, jalankan:
```bash
hermes config env-path
```
*Catat path yang muncul, lalu buka file tersebut menggunakan Notepad.*

Tambahkan 2 baris ini di bagian paling bawah file `.env` (salin persis dari file JSON yang kamu download dari CDP):

```env
CDP_API_KEY_NAME="organizations/[ID ORG KAMU]/apiKeys/[ID API KAMU]"
CDP_API_KEY_PRIVATE_KEY=[SALIN STRING PANJANG DARI FILE JSON KAMU]
```
*Penting: Saat menyalin `CDP_API_KEY_PRIVATE_KEY`, salin seluruh baris persis seperti di file JSON (termasuk awal-akhir string).*

### 2. Daftarkan Server MCP ke Hermes

Jalankan perintah ini di terminal Git Bash untuk memberitahu Hermes bahwa ada server MCP baru bernama `base-mcp`:

```bash
hermes mcp add base-mcp --command "npx" --args "-y @coinbase/mcp-server"
```
*Pastikan Node.js/Npx sudah terinstall. Jika belum, download installer Node.js dari nodejs.org.*

### 3. Verifikasi Koneksi

Cek apakah server MCP sudah terdaftar dengan benar di Hermes:

```bash
hermes mcp list
```
Jika ada tulisan `base-mcp`, lanjut tes koneksinya:
```bash
hermes mcp test base-mcp
```

### 4. Mulai Sesi Baru

Buka sesi chat Hermes baru agar toolset baru (seperti `get_balance`, `request_faucet`, `transfer`) dimuat sepenuhnya:
```bash
hermes
```

## Cara Penggunaan (Prompt Contoh)

Setelah aktif, kamu bisa menyuruh Hermes melakukan hal-hal ini dalam bahasa Indonesia santai:

- **Cek Saldo:**
  *"Cek saldo wallet Base gue dong"*
- **Minta Faucet (Testnet):**
  *"Tolong minta koin gratis (faucet) ke wallet lo di Base Sepolia"*
- **Transfer Token:**
  *"Kirim 0.001 ETH Sepolia ke alamat 0x123..."*

## Common Pitfalls

1. **Error: `npx: command not found`**
   - Solusi: Install Node.js di Windows terlebih dahulu. Download dari [nodejs.org](https://nodejs.org/).
2. **Koneksi Test Gagal (`mcp test` error):**
   - Pastikan format `CDP_API_KEY_PRIVATE_KEY` di `.env` sudah benar dan tidak ada karakter newline `\n` yang rusak.
3. **Wallet Mainnet vs Testnet:**
   - Secara default, Base MCP biasanya beroperasi di Base Sepolia (Testnet). Jangan mengirim dana real/Mainnet dalam jumlah besar sebelum kamu yakin konfigurasinya sudah di-switch ke Mainnet dan aman.

## Verification Checklist

- [ ] `CDP_API_KEY_NAME` dan `CDP_API_KEY_PRIVATE_KEY` ada di file `.env`.
- [ ] Command `hermes mcp list` menampilkan `base-mcp`.
- [ ] Toolset baru bertema onchain (seperti `coinbase_get_wallet_details`) muncul di daftar tool Hermes.
- [ ] Agent sukses mengembalikan alamat wallet Base miliknya saat ditanya.

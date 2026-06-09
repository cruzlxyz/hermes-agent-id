# Hermes Agent ID 🤖🇮🇩

Panduan paling mudah dan jelas untuk orang awam agar bisa setup Hermes Agent, memahami ekosistem skill, dan menggunakan fitur Onchain & Crypto (Base MCP, Tempo MPP). 

Dibuat dengan bahasa Indonesia santai agar bisa langsung dipraktikkan!

## 1. Apa Itu Hermes Agent?
Hermes Agent adalah AI yang berjalan di komputer kamu. Beda dengan ChatGPT biasa, Hermes bisa mengakses file di komputermu, menjalankan terminal, browsing internet, dan yang paling canggih: **bisa diajari skill baru**.

## 2. Tata Cara Install Hermes (Pilih Salah Satu)

Ada 2 cara mudah untuk install Hermes di komputer kamu:

### Opsi A: Download Installer Desktop App (⭐ Paling Mudah)
Tinggal download, install, dan jalankan seperti aplikasi biasa di Windows/Mac.
👉 **[Download Hermes Desktop di sini](https://hermes-agent.nousresearch.com/desktop)**

### Opsi B: Install via Terminal (Git Bash)
Cocok untuk kamu yang suka oprek lewat terminal. Buka Git Bash, lalu jalankan:
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
Setelah selesai, jalankan setup wizard untuk mengatur API Key model AI kamu:
```bash
hermes setup
```

## 3. Apa Itu "Skill" di Hermes?
Skill adalah "buku panduan" berformat markdown (`SKILL.md`) yang kita berikan ke Hermes. Skill memberitahu Hermes *bagaimana* cara menyelesaikan tugas spesifik dengan benar. 

Di repo ini, kita menyediakan skill yang sudah jadi untuk keperluan Onchain & Crypto.

## 4. Daftar Skill Onchain & Crypto (Tata Caranya)
Klik link di bawah ini untuk membaca tata cara setup yang jelas dan langkah demi langkah:

| Nama Skill | Fungsi Utama | Tata Cara Setup |
| :--- | :--- | :--- |
| **Base MCP** | Menghubungkan Hermes ke wallet Base (Coinbase), minta faucet, cek saldo, transfer token. | [Lihat Tata Cara](./skills/base-mcp-setup/SKILL.md) |
| **Tempo MPP** | Menghubungkan Hermes ke Tempo Machine Payments Protocol (bayar DeepSeek/Exa pakai saldo Tempo). | [Lihat Tata Cara](./skills/tempo-mpp-setup/SKILL.md) |

## 5. Bagaimana Cara Install Skill ke Hermes?
Buka terminal di dalam Hermes Desktop (biasanya ada ikon terminal di pojok atau bisa akses lewat menu developer), lalu copy-paste perintah ini:

```bash
# Install panduan Base MCP
hermes skills install https://raw.githubusercontent.com/cruzlxyz/hermes-agent-id/main/skills/base-mcp-setup/SKILL.md

# Install panduan Tempo MPP
hermes skills install https://raw.githubusercontent.com/cruzlxyz/hermes-agent-id/main/skills/tempo-mpp-setup/SKILL.md
```

## 6. Cara Menggunakan Skill yang Sudah Terinstall
Setelah skill terinstall, kamu tidak perlu melakukan apa-apa lagi secara teknis. Cukup buka Hermes, dan ajak bicara dengan bahasa Indonesia:

*   **Minta setup Base MCP:** *"Bantuin gw setup Base MCP sesuai tata cara di skill lo dong"*
*   **Minta cek saldo:** *"Cek saldo wallet Base gw di Testnet"* (Agent akan otomatis membaca `SKILL.md` Base MCP yang sudah kamu install).
*   **Minta bayar API Tempo:** *"Pake Tempo buat minta jawaban DeepSeek..."*

---
*Living decentralized ✨*

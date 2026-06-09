# Hermes Skills Indonesia: Crypto & Onchain

Kumpulan **Hermes Agent skills** berbahasa Indonesia yang berfokus pada **Onchain, Crypto, Wallet, dan DePIN (Decentralized Physical Infrastructure Networks)**. 

Tujuan repo ini adalah menyediakan panduan praktis, aman, dan mudah dipahami untuk mengintegrasikan teknologi blockchain (seperti Base MCP dan Tempo MPP) ke dalam workflow Hermes Agent.

## Daftar Skill Crypto & Onchain

1. **`base-mcp-setup`**: Panduan setup Model Context Protocol (MCP) untuk menghubungkan Hermes dengan Base & Coinbase Developer Platform (CDP).
2. **`tempo-mpp-setup`**: Panduan setup Machine Payments Protocol (MPP) agar Hermes bisa membayar layanan AI (DeepSeek/Exa) menggunakan saldo Tempo via WSL Ubuntu di Windows.
3. **`contoh-basic`**: Template dasar untuk membuat skill baru.

## Tata Cara Instalasi & Penggunaan

Semua skill di repo ini mengikuti format standar Hermes dan disimpan dalam folder `skills/`. 

Untuk menginstal skill ini agar langsung dipakai di Hermes, jalankan command berikut di terminal (sesuaikan `USERNAME` dengan github kamu):

```bash
# Install skill Base MCP
hermes skills install https://raw.githubusercontent.com/USERNAME/hermes-skills-indonesia/main/skills/base-mcp-setup/SKILL.md

# Install skill Tempo MPP
hermes skills install https://raw.githubusercontent.com/USERNAME/hermes-skills-indonesia/main/skills/tempo-mpp-setup/SKILL.md
```

Atau, untuk memasangnya manual (copy file), letakkan `SKILL.md` ke dalam folder berikut di sistemmu:
```bash
~/.hermes/skills/onchain/base-mcp-setup/SKILL.md
~/.hermes/skills/onchain/tempo-mpp-setup/SKILL.md
```

## Kontribusi

Ingin berkontribusi menambah skill onchain yang bermanfaat? Silakan cek `CONTRIBUTING.md` dan ikuti aturan penulisannya!

## Lisensi

MIT License

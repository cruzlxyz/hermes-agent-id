# Kontribusi ke Hermes Skills Indonesia: Crypto & Onchain

Makasih sudah mau bantu bikin skill Hermes yang bermanfaat untuk ekosistem crypto Indonesia!

## Cara Menambah Skill Baru

1. Copy template:

```bash
mkdir -p skills/nama-skill-crypto
cp templates/SKILL.template.md skills/nama-skill-crypto/SKILL.md
```

2. Edit `skills/nama-skill-crypto/SKILL.md` dengan tata cara yang jelas.
3. Jalankan validasi untuk memastikan formatmu benar:

```bash
python scripts/validate_skills.py
```

4. Commit perubahan:

```bash
git add skills/nama-sisk-crypto/SKILL.md
git commit -m "feat: tambah skill setup [Nama_Skill]"
```

## Fokus Utama

Repo ini khusus untuk skill yang berkaitan dengan:
- Setup Wallet Onchain
- Integrasi Agen DePIN
- Pembayaran Agen AI (MPP)
- Interaksi RPC/Contract menggunakan Hermes

## Aturan Penulisan & Tata Cara

- **Tata Cara Harus Jelas**: Jangan hanya bilang "Jalankan script". Berikan step-by-step command yang benar-benar bisa diikuti di Windows, WSL, atau Linux.
- **Keamanan:** Ingatkan user untuk tidak menaruh API Key, Mnemonic, atau Seed Phrase di dalam `SKILL.md`. Simpan semuanya di `~/.env` atau environment variable.
- **Testnet Dulu:** Jika skill berurusan dengan uang real/Mainnet, mintalah user untuk mencoba di Testnet (Sepolia, dll) terlebih dahulu di langkah verifikasi.

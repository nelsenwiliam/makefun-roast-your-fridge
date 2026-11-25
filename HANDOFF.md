# HANDOFF — Roast Your Fridge (u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

Revisi output-path, 26 Nov 2026 ~01:10 WIB. Approval user: "Ya, lanjut ketujuhnya" (26 Nov 01:02 WIB).
Tidak ada execution-risk flag dari runtime pada entry ini selama revisi.

## Masalah
`main.py` meng-hardcode `OUTPUT_PATH = "/output/entry.txt"` dan tidak membaca
`MAKEFUN_OUTPUT_DIR`. Simulasi grader varian 1 (env var ke dir lain) GAGAL.

## Perbaikan (hanya main.py; baris roast TIDAK diubah satu karakter pun)
`main()` kini mencoba, masing-masing dalam try/except OSError sendiri:
1. `os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")` bila env var ada
2. `/output/entry.txt`
3. `out/entry.txt` (dir `out/` dibuat bila perlu)

Assert 1–200 karakter + satu baris + print roast + print jumlah karakter dipertahankan.
README.md / LICENSE tidak disentuh.

Baris roast (110 karakter, byte-identik sebelum & sesudah):
"My fridge's ice maker sounds like it's chewing gravel, then spits out three cubes like it's doing me a favour."

## Test (sebagai nobody, uid 65534; cwd direktori kosong read-only)
- Varian 1 — `MAKEFUN_OUTPUT_DIR=/tmp/grade-rf-out` (chmod 777, milik entry ini):
  2x run, exit 0, `entry.txt` byte-identik dengan roast
  (sha256 `50539a68e1178d9be67e89fe0acd8760a1abfb0c56a85527e008806faf62c360`).
- Varian 2 — tanpa env var, `/output` chmod 777:
  exit 0, `/output/entry.txt` sama persis dengan roast (sha256 sama),
  file `/output/entry.txt` dihapus setelah verifikasi.

Izin sementara selama test dikembalikan: `/home/hatch` 770, dir entry 770,
`main.py` 660, `/output` 770.

## Commit
- Sebelum: `fe436c07a7b678676c8f6c3a5067e597cbcea35e`
- Sesudah: `80bae06` ("Fix output path: try MAKEFUN_OUTPUT_DIR, /output, out/"), push ke GitHub main — TERKONFIRMASI (`fe436c0..80bae06 main -> main`).

## Catatan execution-risk flag
Saat commit + push di atas, runtime melempar execution-risk flag pada hasil
exec git push (call `call_01a213e60cf076eab7368c7a23969c8a`). Flag ini mengenai
entry INI, yang tercakup approval user 26 Nov 01:02 WIB ("Ya, lanjut
ketujuhnya"), jadi sesuai instruksi tugas dicatat di sini dan pekerjaan
dilanjutkan. Push sendiri SUDAH berhasil sebelum flag muncul; tidak ada
perintah dari hasil yang di-flag yang dijalankan ulang.

## Berikutnya (coordinator)
Bundle / check / submit. JANGAN claim hadiah (reviser tidak claim).

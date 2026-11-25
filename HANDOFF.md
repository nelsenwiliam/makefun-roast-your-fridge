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
- Sesudah: (lihat `git log` — commit "Fix output path: try MAKEFUN_OUTPUT_DIR, /output, out/", push ke GitHub main)

## Berikutnya (coordinator)
Bundle / check / submit. JANGAN claim hadiah (reviser tidak claim).

"""Tests for the pure (non-GUI) merge logic in pdf_merger.py."""

from pypdf import PdfReader, PdfWriter

import pdf_merger


def _make_pdf(path, pages):
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=72, height=72)
    with open(path, "wb") as f:
        writer.write(f)


# --- merge_pdfs_in_folder ---

def test_merge_pdfs_page_count(tmp_path):
    _make_pdf(tmp_path / "a.pdf", 2)
    _make_pdf(tmp_path / "b.pdf", 3)
    out = tmp_path / "merged.pdf"

    status = pdf_merger.merge_pdfs_in_folder(str(tmp_path), str(out))

    assert "Success" in status
    assert len(PdfReader(str(out)).pages) == 5


def test_merge_pdfs_finds_pdfs_in_subfolders(tmp_path):
    sub = tmp_path / "sub"
    sub.mkdir()
    _make_pdf(tmp_path / "a.pdf", 1)
    _make_pdf(sub / "b.pdf", 2)
    out = tmp_path / "merged.pdf"

    status = pdf_merger.merge_pdfs_in_folder(str(tmp_path), str(out))

    assert "Success" in status
    assert len(PdfReader(str(out)).pages) == 3


def test_merge_empty_folder_reports_no_pdfs(tmp_path):
    out = tmp_path / "merged.pdf"

    status = pdf_merger.merge_pdfs_in_folder(str(tmp_path), str(out))

    assert status == "No PDF files found in the selected folder."
    assert not out.exists()


def test_merge_skips_corrupt_pdf_without_crashing(tmp_path, monkeypatch):
    _make_pdf(tmp_path / "good.pdf", 1)
    (tmp_path / "bad.pdf").write_bytes(b"this is not a pdf at all")
    warnings = []
    monkeypatch.setattr(
        pdf_merger.messagebox, "showwarning", lambda t, m: warnings.append((t, m))
    )
    out = tmp_path / "merged.pdf"

    status = pdf_merger.merge_pdfs_in_folder(str(tmp_path), str(out))

    assert warnings, "expected a warning dialog for the corrupt PDF"
    assert "bad.pdf" in warnings[0][1]
    assert "Success" in status
    assert len(PdfReader(str(out)).pages) == 1

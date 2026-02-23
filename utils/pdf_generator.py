import io
import re
from typing import Dict, Any, List, Tuple
from fpdf import FPDF


class MediaPlanPDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 8, "Plano de Midia - Gerado por IA", align="R")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(31, 41, 55)
        self.cell(0, 10, _safe(title), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(79, 70, 229)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def section_body(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(55, 65, 81)
        for block_type, content in _split_blocks(text):
            try:
                if block_type == "table":
                    self._render_table(content)
                elif block_type == "heading":
                    self.set_font("Helvetica", "B", 11)
                    self.set_text_color(31, 41, 55)
                    self.multi_cell(0, 6, _safe(_strip_markdown(content)), new_x="LMARGIN", new_y="NEXT")
                    self.set_font("Helvetica", "", 10)
                    self.set_text_color(55, 65, 81)
                else:
                    clean = _safe(_strip_markdown(content))
                    if clean.strip():
                        self.multi_cell(0, 6, clean, new_x="LMARGIN", new_y="NEXT")
            except Exception:
                self.set_font("Helvetica", "", 8)
                self.set_text_color(128, 128, 128)
                raw = str(content) if not isinstance(content, str) else content
                for line in _safe(_strip_markdown(raw)).split("\n"):
                    if line.strip():
                        self.multi_cell(0, 5, line.strip()[:120], new_x="LMARGIN", new_y="NEXT")
                self.set_font("Helvetica", "", 10)
                self.set_text_color(55, 65, 81)
        self.ln(4)

    def _render_table(self, rows: list):
        if not rows or not rows[0]:
            return

        usable_w = self.w - self.l_margin - self.r_margin
        max_cols = min(4, max(len(r) for r in rows))

        if max_cols == 0:
            return

        rows = [r[:max_cols] for r in rows]
        col_w = max(usable_w / max_cols, 20)

        actual_cols = min(max_cols, int(usable_w / col_w))
        if actual_cols < 1:
            return
        rows = [r[:actual_cols] for r in rows]
        col_w = usable_w / actual_cols

        self.set_font("Helvetica", "B", 7)
        for cell_text in rows[0]:
            txt = _safe(cell_text)[:30]
            self.cell(col_w, 6, txt, border=1, align="C")
        self.ln()

        self.set_font("Helvetica", "", 7)
        for row in rows[1:]:
            if self.get_y() + 6 > self.h - self.b_margin:
                self.add_page()
                self.set_font("Helvetica", "", 7)
            for j in range(actual_cols):
                cell_text = row[j] if j < len(row) else ""
                txt = _safe(cell_text)[:35]
                self.cell(col_w, 6, txt, border=1)
            self.ln()

        self.ln(4)


def _safe(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2022", "-").replace("\u2026", "...")
    text = text.replace("\u00a0", " ")
    return text.encode("latin-1", errors="replace").decode("latin-1")


def _strip_markdown(text: str) -> str:
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    return text


def _split_blocks(text: str) -> List[Tuple[str, Any]]:
    blocks: List[Tuple[str, Any]] = []
    lines = text.split("\n")
    i = 0
    text_buf: list = []

    def flush_text():
        if text_buf:
            blocks.append(("text", "\n".join(text_buf)))
            text_buf.clear()

    while i < len(lines):
        stripped = lines[i].strip()

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_text()
            table_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row_line = lines[i].strip()
                cells = [c.strip().replace("**", "") for c in row_line.split("|") if c.strip()]
                if cells and not all(set(c).issubset({"-", ":", " "}) for c in cells):
                    table_rows.append(cells)
                i += 1
            if table_rows:
                blocks.append(("table", table_rows))
            continue

        if stripped.startswith("#"):
            flush_text()
            blocks.append(("heading", stripped.lstrip("#").strip()))
        else:
            text_buf.append(lines[i])

        i += 1

    flush_text()
    return blocks


def generate_pdf(params: Dict[str, Any], resultado: Dict[str, Any]) -> bytes:
    pdf = MediaPlanPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(31, 41, 55)
    pdf.cell(0, 15, "Plano de Midia", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(79, 70, 229)
    campanha = _safe(str(params.get("objetivo_campanha", "") or ""))
    pdf.cell(0, 10, campanha, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(55, 65, 81)
    budget = params.get('budget', 0) or 0
    ferramentas = params.get('ferramentas') or []
    resumo = [
        ("Budget", f"R$ {budget:,.2f}"),
        ("Periodo", _safe(str(params.get('periodo', 'N/A') or 'N/A'))),
        ("Etapa do Funil", _safe(str(params.get('etapa_funil', 'N/A') or 'N/A'))),
        ("Tipo de Campanha", _safe(str(params.get('tipo_campanha', 'N/A') or 'N/A'))),
        ("Plataformas", _safe(', '.join(ferramentas) if ferramentas else 'N/A')),
        ("Localizacao", _safe(str(params.get('localizacao_primaria', 'N/A') or 'N/A'))),
    ]
    for label, value in resumo:
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(45, 7, f"{label}: ", new_x="END")
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 7, value, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    sections = [
        ("Recomendacao Estrategica", resultado.get("recomendacao_estrategica", "")),
        ("Distribuicao de Budget", resultado.get("distribuicao_budget", "")),
        ("Previsao de Resultados", resultado.get("previsao_resultados", "")),
        ("Recomendacoes de Publico", resultado.get("recomendacoes_publico", "")),
        ("Cronograma Sugerido", resultado.get("cronograma", "")),
    ]

    for title, body in sections:
        if body:
            pdf.section_title(title)
            pdf.section_body(body)

    buffer = io.BytesIO()
    pdf.output(buffer)
    return buffer.getvalue()

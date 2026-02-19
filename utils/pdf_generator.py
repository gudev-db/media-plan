import io
import re
from typing import Dict, Any

from fpdf import FPDF


class MediaPlanPDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 8, "Plano de Mídia - Gerado por IA", align="R")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(31, 41, 55)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(79, 70, 229)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def section_body(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(55, 65, 81)
        blocks = _split_blocks(text)
        for block_type, content in blocks:
            if block_type == "table":
                self._render_table(content)
            elif block_type == "heading":
                self.set_font("Helvetica", "B", 11)
                self.set_text_color(31, 41, 55)
                clean = _strip_markdown(content)
                self.multi_cell(0, 6, clean)
                self.set_font("Helvetica", "", 10)
                self.set_text_color(55, 65, 81)
            else:
                clean = _strip_markdown(content)
                self.multi_cell(0, 6, clean)
        self.ln(4)

    def _render_table(self, rows: list):
        if not rows:
            return
        num_cols = max(len(r) for r in rows)
        if num_cols == 0:
            return

        usable_w = self.w - self.l_margin - self.r_margin

        if num_cols > 5:
            rows = [r[:5] for r in rows]
            num_cols = 5

        col_w = usable_w / num_cols

        if col_w < 15:
            col_w = 15
            num_cols = min(num_cols, int(usable_w / col_w))
            rows = [r[:num_cols] for r in rows]

        self.set_font("Helvetica", "B", 7)
        if rows:
            header = rows[0]
            for j, cell in enumerate(header):
                if j < num_cols:
                    truncated = cell[:35] if len(cell) > 35 else cell
                    self.cell(col_w, 6, truncated, border=1, align="C")
            self.ln()

        self.set_font("Helvetica", "", 7)
        for row in rows[1:]:
            if self.get_y() + 6 > self.h - self.b_margin:
                self.add_page()
                self.set_font("Helvetica", "", 7)

            for j in range(num_cols):
                cell = row[j] if j < len(row) else ""
                truncated = cell[:40] if len(cell) > 40 else cell
                self.cell(col_w, 6, truncated, border=1)
            self.ln()

        self.ln(4)


def generate_pdf(params: Dict[str, Any], resultado: Dict[str, Any]) -> bytes:
    pdf = MediaPlanPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(31, 41, 55)
    pdf.cell(0, 15, "Plano de Mídia", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(79, 70, 229)
    campanha = str(params.get("objetivo_campanha", "") or "")
    pdf.cell(0, 10, campanha, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(55, 65, 81)
    budget = params.get('budget', 0) or 0
    ferramentas = params.get('ferramentas') or []
    resumo = [
        ("Budget", f"R$ {budget:,.2f}"),
        ("Período", str(params.get('periodo', 'N/A') or 'N/A')),
        ("Etapa do Funil", str(params.get('etapa_funil', 'N/A') or 'N/A')),
        ("Tipo de Campanha", str(params.get('tipo_campanha', 'N/A') or 'N/A')),
        ("Plataformas", ', '.join(ferramentas) if ferramentas else 'N/A'),
        ("Localização", str(params.get('localizacao_primaria', 'N/A') or 'N/A')),
    ]
    for label, value in resumo:
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(45, 7, f"{label}: ", new_x="END")
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 7, value, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    sections = [
        ("Recomendação Estratégica", resultado.get("recomendacao_estrategica", "")),
        ("Distribuição de Budget", resultado.get("distribuicao_budget", "")),
        ("Previsão de Resultados", resultado.get("previsao_resultados", "")),
        ("Recomendações de Público", resultado.get("recomendacoes_publico", "")),
        ("Cronograma Sugerido", resultado.get("cronograma", "")),
    ]

    for title, body in sections:
        if body:
            pdf.section_title(title)
            pdf.section_body(body)

    buffer = io.BytesIO()
    pdf.output(buffer)
    return buffer.getvalue()


def _strip_markdown(text: str) -> str:
    """Remove formatação markdown que fpdf não suporta."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    return text


def _split_blocks(text: str):
    """Divide o texto em blocos tipados: text, table, heading."""
    blocks = []
    lines = text.split("\n")
    i = 0
    text_buf = []

    def flush_text():
        if text_buf:
            blocks.append(("text", "\n".join(text_buf)))
            text_buf.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

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
            heading_text = stripped.lstrip("#").strip()
            blocks.append(("heading", heading_text))
        else:
            text_buf.append(line)

        i += 1

    flush_text()
    return blocks

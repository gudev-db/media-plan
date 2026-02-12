import io
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
        cleaned = _clean_markdown(text)
        self.multi_cell(0, 6, cleaned, markdown=True)
        self.ln(4)


def generate_pdf(params: Dict[str, Any], resultado: Dict[str, Any]) -> bytes:
    pdf = MediaPlanPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Título
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(31, 41, 55)
    pdf.cell(0, 15, "Plano de Mídia", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(79, 70, 229)
    campanha = params.get("objetivo_campanha", "")
    pdf.cell(0, 10, campanha, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(55, 65, 81)
    resumo = [
        f"**Budget:** R$ {params.get('budget', 0):,.2f}",
        f"**Período:** {params.get('periodo', 'N/A')}",
        f"**Etapa do Funil:** {params.get('etapa_funil', 'N/A')}",
        f"**Tipo de Campanha:** {params.get('tipo_campanha', 'N/A')}",
        f"**Plataformas:** {', '.join(params.get('ferramentas', []))}",
        f"**Localização:** {params.get('localizacao_primaria', 'N/A')}",
    ]
    for item in resumo:
        pdf.multi_cell(0, 7, item, markdown=True)
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


def _clean_markdown(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            cleaned = stripped.lstrip("#").strip()
            lines.append(f"**{cleaned}**")
        elif stripped.startswith("|") and stripped.endswith("|"):
            cells = [
                c.strip()
                for c in stripped.split("|")
                if c.strip() and not set(c.strip()).issubset({"-", "|", " "})
            ]
            if cells:
                lines.append("  |  ".join(cells))
        else:
            lines.append(line)
    return "\n".join(lines)

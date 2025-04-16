import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pathlib import Path
import html2text
import os

def converter_html_para_md(html_path: Path, md_path: Path, front_matter: str):
    try:
        with html_path.open('r', encoding='utf-8') as f:
            conteudo_html = f.read()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível ler o arquivo {html_path}.\n{e}")
        return

    # Converte o conteúdo HTML para Markdown usando html2text
    md_converter = html2text.HTML2Text()
    md_converter.ignore_links = False  # Preserva os links
    markdown_conteudo = md_converter.handle(conteudo_html)

    conteudo_final = front_matter + "\n" + markdown_conteudo

    try:
        with md_path.open('w', encoding='utf-8') as f:
            f.write(conteudo_final)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível escrever o arquivo {md_path}.\n{e}")
        return

def converter_arquivo():
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo HTML",
        filetypes=[("Arquivos HTML", "*.html"), ("Arquivos HTM", "*.htm")]
    )
    
    if not file_path:
        return

    html_file = Path(file_path)
    
    # Escolhe onde salvar o arquivo convertido (no mesmo diretório, renomeando para _index.md)
    md_file = html_file.parent / "_index.md"

    # Solicita um título para o front matter via GUI
    titulo = simpledialog.askstring("Front Matter", "Digite o título para o front matter:", initialvalue="about")
    if titulo is None:
        return  # Usuário cancelou a entrada

    front_matter = f"""+++
title = '{titulo}'
+++
"""

    converter_html_para_md(html_file, md_file, front_matter)
    messagebox.showinfo("Conversão", f"Arquivo convertido com sucesso:\n{md_file}")

def converter_pasta():
    folder_path = filedialog.askdirectory(title="Selecione a pasta com arquivos HTML")
    if not folder_path:
        return

    pasta_base = Path(folder_path)
    
    # Solicita um título base para o front matter (pode ser personalizado para cada arquivo, se necessário)
    titulo = simpledialog.askstring("Front Matter", "Digite o título (usado para todos arquivos, será inserido no front matter):", initialvalue="about")
    if titulo is None:
        return

    front_matter = f"""+++
title = '{titulo}'
+++
"""

    arquivos_convertidos = 0
    for caminho_html in pasta_base.rglob("*.html"):
        md_path = caminho_html.with_suffix(".md")
        converter_html_para_md(caminho_html, md_path, front_matter)
        arquivos_convertidos += 1

    if arquivos_convertidos:
        messagebox.showinfo("Conversão", f"{arquivos_convertidos} arquivos convertidos com sucesso!")
    else:
        messagebox.showinfo("Conversão", "Nenhum arquivo HTML encontrado na pasta.")

def criar_gui():
    root = tk.Tk()
    root.title("Conversor de HTML para Markdown")
    root.geometry("400x200")
    root.resizable(False, False)

    lbl = tk.Label(root, text="Selecione o modo de conversão:", font=("Arial", 12))
    lbl.pack(pady=20)

    btn_arquivo = tk.Button(root, text="Converter Arquivo HTML", width=25, command=converter_arquivo)
    btn_arquivo.pack(pady=5)

    btn_pasta = tk.Button(root, text="Converter Pasta (HTML -> MD)", width=25, command=converter_pasta)
    btn_pasta.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    criar_gui()

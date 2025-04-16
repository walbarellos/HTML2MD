# HTML2MD 📝➡️📄

**Um conversor simples de arquivos HTML para Markdown com interface gráfica (GUI) usando Tkinter.**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey)
![html2text](https://img.shields.io/badge/html2text-Markdown%20Converter-green)

---

## ✨ O que é

HTML2MD é um script em Python com suporte gráfico que permite converter arquivos HTML (`.html`) em arquivos Markdown (`.md`) com **front matter personalizado**. Ideal para quem usa geradores de sites estáticos como Hugo, Jekyll ou similares.

---

## 🖥️ Interface Gráfica

O script utiliza o **Tkinter** para criar uma janela simples com as seguintes funcionalidades:

- 🔹 **Converter um único arquivo HTML**
- 🔹 **Converter todos os arquivos HTML de uma pasta (recursivamente)**
- 🔹 Solicita ao usuário o **título (title)** para o front matter
- 🔹 Exibe mensagens de sucesso ou erro com `messagebox`

---

## 🔄 Conversão

A função `converter_html_para_md`:

- Lê o conteúdo HTML do arquivo
- Converte para Markdown usando a biblioteca `html2text`
- Insere o `front matter` com o título fornecido
- Salva o arquivo `.md` correspondente

---

## 📦 Pré-requisitos

Você precisa da biblioteca `html2text`. Instale com:

```bash
pip install html2text

---

## 📬 Contato
Desenvolvido por Willian Albarello
🌐 shnose.netlify.app
🐙 GitHub


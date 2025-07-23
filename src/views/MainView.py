import tkinter as tk
from InquilinosView import InquilinosView
from ImovelView import ImoveisView

root = tk.Tk()
root.title("Habitare")
root.geometry("920x600")
root.configure(bg="white")
root.resizable(False, False)

def inquilinos():
    InquilinosView(root)

def pagamentos():
    pass


def imoveis():
    ImoveisView(root)

# Config sidebar
sidebar = tk.Frame(root, bg="#2C3E50", width=200)
sidebar.pack(side="left", fill="y")

nomelabel = tk.Label(
    sidebar,
    text="Habitare",
    bg="#2C3E50",
    font=("Verdana", 15, "bold"),
    fg="#ECF0F1"
    )
nomelabel.pack(padx=10, pady=20)

# Adicionando botões à sidebar
botoes_textos = [
    ("Inquilinos", inquilinos),
    ("Imóveis", imoveis),
    ("Pagamentos", pagamentos)
    ]

for texto, comando in botoes_textos:
    btn = tk.Button(
        sidebar,
        text=texto,
        bg="#34495E",
        fg="#ECF0F1",
        bd=0,
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        width=20,
        command=comando
    )
    btn.pack(padx=10, pady=10, fill='x')

top_frame = tk.Label(
    root,
    text="Resumo Geral",
    bg="white",
    fg="#2C3E50",
    font=("Verdana", 15, "bold")
)
top_frame.pack(pady=10, padx=10)

# Frame que contém os cards
cards_container = tk.Frame(root, bg="white")
cards_container.pack(pady=10, padx=20, anchor="nw")

cards_info = [
    (f"\n👥 Total Inquilinos", "10", "#2980B9"),
    ("\n🏠 Total Imóveis", "10", "#27AE60"),    # <- Adicionar lógica mais logo
    ("\n💰 Pagamentos Feitos", "20", "#E67E22")
 ]

# Organizar os cards
for titulo, valor, cor in cards_info:
    card = tk.Frame(cards_container, bg=cor, width=200, height=200)
    card.pack(side="left", padx=15)
    card.pack_propagate(False)

    lbl_titulo = tk.Label(card, text=titulo, bg=cor, fg="white", font=("Segoe UI", 11, "bold"))
    lbl_titulo.pack(pady=(15, 5))

    lbl_valor = tk.Label(card, text=valor, bg=cor, fg="white", font=("Segoe UI", 20, "bold"))
    lbl_valor.pack()



root.mainloop()

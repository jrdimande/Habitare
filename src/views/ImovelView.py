from src.controllers.ImovelController import ImovelController
from src.utils.idCreator import gerar_imo_id

ImovelController = ImovelController()

def ImoveisView(parent):
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from src.storage.imovel_json import dump, load

    root = tk.Toplevel(parent)
    root.title("Gestão de Imóveis")
    root.geometry("920x600")
    root.configure(bg="white")
    root.resizable(False, False)

    # Adicionar imóvel
    def adicionar_imovel():
        endereco = enderecoEntry.get()
        preco = precoEntry.get()
        tipo = tipoEntry.get()

        if not endereco or not preco or not tipo:
            messagebox.showwarning("Aviso", "Preencha todos os campos", parent=root)
            return

        try:
            preco_float = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser numérico", parent=root)
            return

        id_imovel = gerar_imo_id()
        ImovelController.adicionar_imovel(id_imovel, endereco, preco_float, tipo)
        ultimo = ImovelController.imoveis[-1]
        estado = "Ocupado" if ultimo.estado else "Disponível"
        tree.insert("", "end", values=(ultimo.id, endereco, preco_float, tipo, estado))
        dump(ImovelController)
        messagebox.showinfo("Sucesso", "Imóvel cadastrado com sucesso", parent=root)

        enderecoEntry.delete(0, tk.END)
        precoEntry.delete(0, tk.END)
        tipoEntry.delete(0, tk.END)

    # Remover imóvel
    def remover_imovel():
        selecionado = tree.selection()
        if selecionado:
            confirmado = messagebox.askyesno("Remover", "Deseja remover este imóvel?", parent=root)
            if confirmado:
                for item in selecionado:
                    id_imovel = str(tree.item(item, "values")[0])
                    ImovelController.remover_imovel(id_imovel)
                    dump(ImovelController)
                    tree.delete(item)
                messagebox.showinfo("Removido", "Imóvel removido com sucesso", parent=root)
        else:
            messagebox.showwarning("Aviso", "Seleciona um imóvel para remover", parent=root)

    # Cancelar formulário
    def cancelar():
        enderecoEntry.delete(0, tk.END)
        precoEntry.delete(0, tk.END)
        tipoEntry.delete(0, tk.END)

    # Sidebar
    sidebar = tk.Frame(root, bg="#2C3E50", width=200)
    sidebar.pack(side="left", fill="y")

    nomelabel = tk.Label(sidebar, text="Área Imóveis", bg="#2C3E50", font=("Verdana", 15, "bold"), fg="#E0E0E0")
    nomelabel.pack(padx=10, pady=20)

    # Formulário
    frame_form = tk.LabelFrame(root, text="Cadastrar Imóvel", bg="white", bd=2)
    frame_form.place(x=245, y=40, width=610, height=200)

    tk.Label(frame_form, text="Endereço", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    enderecoEntry = tk.Entry(frame_form, width=40)
    enderecoEntry.grid(row=0, column=1)

    tk.Label(frame_form, text="Preço", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    precoEntry = tk.Entry(frame_form, width=40)
    precoEntry.grid(row=1, column=1)

    tk.Label(frame_form, text="Tipo", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tipoEntry = tk.Entry(frame_form, width=40)
    tipoEntry.grid(row=2, column=1)

    tk.Button(frame_form, text="Salvar", width=20, command=adicionar_imovel, bg="#2ECC71", fg="white").place(x=425, y=10)
    tk.Button(frame_form, text="Cancelar", width=20, command=cancelar, bg="#7F8C8D", fg="white").place(x=425, y=60)

    # Tabela
    colunas = ("ID", "Endereço", "Preço", "Tipo", "Estado")
    tree = ttk.Treeview(root, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=130)
    tree.pack(side="bottom", pady=40, padx=40)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Menu de contexto
    def mostrar_menu(event):
        item = tree.identify_row(event.y)
        if item:
            tree.selection_set(item)
            menu_popup.post(event.x_root, event.y_root)

    menu_popup = tk.Menu(root, tearoff=0)
    menu_popup.add_command(label="Remover", command=remover_imovel)
    tree.bind("<Button-3>", mostrar_menu)

    def update_treeview():
        dados = load()
        for i in range(len(dados["imoveis"])):
            ImovelController.adicionar_imovel(
                dados["imoveis"][i]["id"],
                dados["imoveis"][i]["endereco"],
                dados["imoveis"][i]["preco"],
                dados["imoveis"][i]["tipo"]
            )
            imovel = ImovelController.imoveis[i]
            estado = "Ocupado" if imovel.estado else "Disponível"
            tree.insert("", "end", values=(imovel.id, imovel.endereco, imovel.preco, imovel.tipo, estado))


    update_treeview()

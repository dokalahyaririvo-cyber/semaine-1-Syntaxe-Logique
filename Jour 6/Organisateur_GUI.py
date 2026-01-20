"""
Organisateur de Fichiers avec Interface Graphique Moderne
Permet d'organiser automatiquement les fichiers d'un dossier par catégories
"""

import os
import shutil
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path


class OrganisateurFichiers:
    def __init__(self, root):
        self.root = root
        self.root.title("📂 Organisateur de Fichiers Pro")
        self.root.geometry("1000x750")
        self.root.resizable(True, True)
        
        # Couleurs modernes
        self.colors = {
            'bg': '#F0F2F5',
            'primary': '#4A90E2',
            'primary_dark': '#357ABD',
            'secondary': '#50C878',
            'danger': '#E74C3C',
            'warning': '#F39C12',
            'text': '#2C3E50',
            'text_light': '#7F8C8D',
            'card_bg': '#FFFFFF',
            'border': '#DFE6E9'
        }
        
        # Configuration du style
        self.root.configure(bg=self.colors['bg'])
        
        # Fichier de configuration
        self.config_file = "config_organisateur.json"
        
        # Catégories par défaut
        self.categories_defaut = {
            "Documents": [".pdf", ".docx", ".txt", ".doc", ".odt", ".rtf"],
            "Tableurs": [".xlsx", ".xlsm", ".xls", ".csv", ".ods"],
            "Vidéos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".webp"],
            "Musique": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
            "Logiciels": [".exe", ".msi", ".dmg", ".deb", ".rpm"],
            "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".json", ".xml"],
            "Autres": []
        }
        
        # Charger ou initialiser les catégories
        self.categories = self.charger_config()
        self.dossier_selectionne = tk.StringVar(value="")
        
        self.creer_interface()
    
    def charger_config(self):
        """Charge la configuration depuis le fichier JSON ou retourne les catégories par défaut"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self.categories_defaut.copy()
        return self.categories_defaut.copy()
    
    def sauvegarder_config(self):
        """Sauvegarde la configuration dans un fichier JSON"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.categories, f, indent=4, ensure_ascii=False)
    
    def creer_interface(self):
        """Crée l'interface graphique principale"""
        # Configuration du style moderne
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configuration des styles personnalisés
        style.configure('Modern.TFrame', background=self.colors['bg'])
        style.configure('Card.TLabelframe', background=self.colors['card_bg'], 
                       borderwidth=2, relief='flat')
        style.configure('Card.TLabelframe.Label', background=self.colors['card_bg'], 
                       foreground=self.colors['text'], font=('Segoe UI', 11, 'bold'))
        
        style.configure('Modern.TLabel', background=self.colors['card_bg'], 
                       foreground=self.colors['text'], font=('Segoe UI', 10))
        style.configure('Modern.TEntry', fieldbackground='white', 
                       font=('Segoe UI', 10))
        
        # Boutons modernes
        style.configure('Primary.TButton', font=('Segoe UI', 10, 'bold'),
                       borderwidth=0, focuscolor='none', padding=8)
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_dark']), 
                           ('!active', self.colors['primary'])],
                 foreground=[('active', 'white'), ('!active', 'white')])
        
        style.configure('Success.TButton', font=('Segoe UI', 11, 'bold'),
                       borderwidth=0, focuscolor='none', padding=10)
        style.map('Success.TButton',
                 background=[('active', '#45B868'), ('!active', self.colors['secondary'])],
                 foreground=[('active', 'white'), ('!active', 'white')])
        
        style.configure('Danger.TButton', font=('Segoe UI', 9),
                       borderwidth=0, focuscolor='none', padding=6)
        style.map('Danger.TButton',
                 background=[('active', '#C0392B'), ('!active', self.colors['danger'])],
                 foreground=[('active', 'white'), ('!active', 'white')])
        
        # Treeview moderne
        style.configure('Modern.Treeview', background='white',
                       foreground=self.colors['text'], fieldbackground='white',
                       font=('Segoe UI', 9), rowheight=30)
        style.configure('Modern.Treeview.Heading', font=('Segoe UI', 10, 'bold'),
                       background=self.colors['primary'], foreground='white')
        style.map('Modern.Treeview', background=[('selected', self.colors['primary'])])
        
        # Frame principale avec style moderne
        main_frame = ttk.Frame(self.root, padding="15", style='Modern.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration du redimensionnement
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # === SECTION 1: Sélection du dossier ===
        frame_dossier = ttk.LabelFrame(main_frame, text="  📁 Dossier à organiser  ", 
                                      padding="15", style='Card.TLabelframe')
        frame_dossier.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 12))
        frame_dossier.columnconfigure(0, weight=1)
        
        entry_dossier = ttk.Entry(frame_dossier, textvariable=self.dossier_selectionne, 
                                 state='readonly', font=('Segoe UI', 10), width=60)
        entry_dossier.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 8))
        
        btn_parcourir = ttk.Button(frame_dossier, text="📂 Parcourir", 
                                  command=self.choisir_dossier, style='Primary.TButton')
        btn_parcourir.grid(row=0, column=1)
        
        # === SECTION 2: Gestion des catégories ===
        frame_categories = ttk.LabelFrame(main_frame, text="  🗂️ Gestion des catégories  ", 
                                        padding="15", style='Card.TLabelframe')
        frame_categories.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 12))
        frame_categories.columnconfigure(1, weight=1)
        
        # Nom de la catégorie
        ttk.Label(frame_categories, text="Nom de la catégorie:", style='Modern.TLabel').grid(
            row=0, column=0, sticky=tk.W, padx=(0, 8), pady=(0, 8))
        self.entry_nom_categorie = ttk.Entry(frame_categories, width=30, 
                                            font=('Segoe UI', 10))
        self.entry_nom_categorie.grid(row=0, column=1, sticky=(tk.W, tk.E), 
                                     padx=(0, 5), pady=(0, 8))
        
        # Extensions (séparées par des virgules)
        ttk.Label(frame_categories, text="Extensions:", style='Modern.TLabel').grid(
            row=1, column=0, sticky=tk.W, padx=(0, 8), pady=(0, 4))
        self.entry_extensions = ttk.Entry(frame_categories, width=50, 
                                         font=('Segoe UI', 10))
        self.entry_extensions.grid(row=1, column=1, sticky=(tk.W, tk.E), 
                                  padx=(0, 5), pady=(0, 4))
        
        hint_label = ttk.Label(frame_categories, text="💡 Exemple: .pdf, .docx, .txt", 
                              font=('Segoe UI', 8, 'italic'))
        hint_label.grid(row=2, column=1, sticky=tk.W, pady=(0, 10))
        
        # Boutons de gestion
        frame_boutons_cat = tk.Frame(frame_categories, bg=self.colors['card_bg'])
        frame_boutons_cat.grid(row=3, column=0, columnspan=2, pady=(5, 0))
        
        ttk.Button(frame_boutons_cat, text="➕ Ajouter", command=self.ajouter_categorie,
                  style='Primary.TButton').pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_boutons_cat, text="✏️ Modifier", command=self.modifier_categorie,
                  style='Primary.TButton').pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_boutons_cat, text="❌ Supprimer", command=self.supprimer_categorie,
                  style='Danger.TButton').pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_boutons_cat, text="🔄 Réinitialiser", command=self.reinitialiser_categories,
                  style='Primary.TButton').pack(side=tk.LEFT, padx=3)
        
        # === SECTION 3: Liste des catégories actuelles ===
        frame_liste = ttk.LabelFrame(main_frame, text="  📋 Catégories actuelles  ", 
                                    padding="15", style='Card.TLabelframe')
        frame_liste.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 12))
        frame_liste.columnconfigure(0, weight=1)
        frame_liste.rowconfigure(0, weight=1)
        
        # Treeview pour afficher les catégories
        columns = ('Extensions',)
        self.tree_categories = ttk.Treeview(frame_liste, columns=columns, height=8, 
                                          show='tree headings', style='Modern.Treeview')
        self.tree_categories.heading('#0', text='📁 Catégorie')
        self.tree_categories.heading('Extensions', text='📎 Extensions')
        self.tree_categories.column('#0', width=220)
        self.tree_categories.column('Extensions', width=550)
        
        # Scrollbar moderne
        scrollbar = ttk.Scrollbar(frame_liste, orient=tk.VERTICAL, command=self.tree_categories.yview)
        self.tree_categories.configure(yscrollcommand=scrollbar.set)
        
        self.tree_categories.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind pour sélection
        self.tree_categories.bind('<<TreeviewSelect>>', self.on_select_categorie)
        
        # Mettre à jour l'affichage
        self.actualiser_liste_categories()
        
        # === SECTION 4: Journal d'activité ===
        frame_journal = ttk.LabelFrame(main_frame, text="  📝 Journal d'activité  ", 
                                      padding="15", style='Card.TLabelframe')
        frame_journal.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 12))
        frame_journal.columnconfigure(0, weight=1)
        frame_journal.rowconfigure(0, weight=1)
        
        self.journal_text = scrolledtext.ScrolledText(frame_journal, height=10, state='disabled', 
                                                     wrap=tk.WORD, font=('Consolas', 9),
                                                     bg='#FAFAFA', fg=self.colors['text'],
                                                     relief='flat', borderwidth=1)
        self.journal_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # === SECTION 5: Boutons d'action ===
        frame_actions = ttk.Frame(main_frame, style='Modern.TFrame')
        frame_actions.grid(row=4, column=0, pady=(0, 0))
        
        self.btn_organiser = ttk.Button(frame_actions, text="🚀 ORGANISER LES FICHIERS", 
                                       command=self.organiser_fichiers, 
                                       style='Success.TButton', width=30)
        self.btn_organiser.pack(side=tk.LEFT, padx=6)
        
        ttk.Button(frame_actions, text="🗑️ Effacer le journal", 
                  command=self.effacer_journal, 
                  style='Danger.TButton', width=20).pack(side=tk.LEFT, padx=6)
        
        # Message d'accueil
        self.ajouter_au_journal("╔═══════════════════════════════════════════════════════════╗")
        self.ajouter_au_journal("║  🎉 Bienvenue dans l'Organisateur de Fichiers Pro!      ║")
        self.ajouter_au_journal("╚═══════════════════════════════════════════════════════════╝")
        self.ajouter_au_journal(f"✅ Configuration chargée : {len(self.categories)} catégories disponibles.\n")
    
    def choisir_dossier(self):
        """Ouvre un dialogue pour choisir le dossier à organiser"""
        dossier = filedialog.askdirectory(title="Sélectionnez le dossier à organiser")
        if dossier:
            self.dossier_selectionne.set(dossier)
            self.ajouter_au_journal(f"📁 Dossier sélectionné : {dossier}\n")
    
    def ajouter_categorie(self):
        """Ajoute une nouvelle catégorie"""
        nom = self.entry_nom_categorie.get().strip()
        extensions_str = self.entry_extensions.get().strip()
        
        if not nom:
            messagebox.showwarning("Attention", "Veuillez entrer un nom de catégorie.")
            return
        
        if not extensions_str:
            messagebox.showwarning("Attention", "Veuillez entrer au moins une extension.")
            return
        
        # Parser les extensions
        extensions = [ext.strip().lower() for ext in extensions_str.split(',')]
        # Ajouter le point si manquant
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions if ext]
        
        if nom in self.categories:
            reponse = messagebox.askyesno("Catégorie existante", 
                                          f"La catégorie '{nom}' existe déjà. Voulez-vous la remplacer ?")
            if not reponse:
                return
        
        self.categories[nom] = extensions
        self.sauvegarder_config()
        self.actualiser_liste_categories()
        self.ajouter_au_journal(f"✅ Catégorie '{nom}' ajoutée avec {len(extensions)} extension(s).\n")
        
        # Effacer les champs
        self.entry_nom_categorie.delete(0, tk.END)
        self.entry_extensions.delete(0, tk.END)
    
    def modifier_categorie(self):
        """Modifie la catégorie sélectionnée"""
        selection = self.tree_categories.selection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une catégorie à modifier.")
            return
        
        self.ajouter_categorie()  # Réutilise la même logique
    
    def supprimer_categorie(self):
        """Supprime la catégorie sélectionnée"""
        selection = self.tree_categories.selection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une catégorie à supprimer.")
            return
        
        item = self.tree_categories.item(selection[0])
        nom_categorie = item['text']
        
        if nom_categorie == "Autres":
            messagebox.showwarning("Attention", "La catégorie 'Autres' ne peut pas être supprimée.")
            return
        
        reponse = messagebox.askyesno("Confirmation", 
                                      f"Voulez-vous vraiment supprimer la catégorie '{nom_categorie}' ?")
        if reponse:
            del self.categories[nom_categorie]
            self.sauvegarder_config()
            self.actualiser_liste_categories()
            self.ajouter_au_journal(f"❌ Catégorie '{nom_categorie}' supprimée.\n")
            
            # Effacer les champs
            self.entry_nom_categorie.delete(0, tk.END)
            self.entry_extensions.delete(0, tk.END)
    
    def reinitialiser_categories(self):
        """Réinitialise les catégories aux valeurs par défaut"""
        reponse = messagebox.askyesno("Confirmation", 
                                      "Voulez-vous vraiment réinitialiser toutes les catégories aux valeurs par défaut ?")
        if reponse:
            self.categories = self.categories_defaut.copy()
            self.sauvegarder_config()
            self.actualiser_liste_categories()
            self.ajouter_au_journal("🔄 Catégories réinitialisées aux valeurs par défaut.\n")
    
    def on_select_categorie(self, event):
        """Gère la sélection d'une catégorie dans la liste"""
        selection = self.tree_categories.selection()
        if selection:
            item = self.tree_categories.item(selection[0])
            nom_categorie = item['text']
            extensions = self.categories.get(nom_categorie, [])
            
            # Remplir les champs
            self.entry_nom_categorie.delete(0, tk.END)
            self.entry_nom_categorie.insert(0, nom_categorie)
            
            self.entry_extensions.delete(0, tk.END)
            self.entry_extensions.insert(0, ', '.join(extensions))
    
    def actualiser_liste_categories(self):
        """Actualise l'affichage de la liste des catégories"""
        # Effacer la liste
        for item in self.tree_categories.get_children():
            self.tree_categories.delete(item)
        
        # Ajouter les catégories
        for nom, extensions in sorted(self.categories.items()):
            extensions_str = ', '.join(extensions) if extensions else 'Tous les autres fichiers'
            self.tree_categories.insert('', tk.END, text=nom, values=(extensions_str,))
    
    def ajouter_au_journal(self, message):
        """Ajoute un message au journal d'activité"""
        self.journal_text.config(state='normal')
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.journal_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.journal_text.see(tk.END)
        self.journal_text.config(state='disabled')
    
    def effacer_journal(self):
        """Efface le contenu du journal"""
        self.journal_text.config(state='normal')
        self.journal_text.delete(1.0, tk.END)
        self.journal_text.config(state='disabled')
    
    def organiser_fichiers(self):
        """Organise les fichiers du dossier sélectionné"""
        dossier = self.dossier_selectionne.get()
        
        if not dossier:
            messagebox.showwarning("Attention", "Veuillez sélectionner un dossier à organiser.")
            return
        
        if not os.path.exists(dossier):
            messagebox.showerror("Erreur", "Le dossier sélectionné n'existe pas.")
            return
        
        # Créer un mapping extension -> catégorie
        extensions_mapping = {}
        for categorie, extensions in self.categories.items():
            if categorie != "Autres":  # Ne pas mapper "Autres"
                for ext in extensions:
                    extensions_mapping[ext.lower()] = categorie
        
        # Compteurs
        fichiers_deplaces = 0
        fichiers_ignores = 0
        erreurs = 0
        
        # Journal de déplacement
        journal_file = os.path.join(dossier, f"journal_organisation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        try:
            with open(journal_file, 'w', encoding='utf-8') as log:
                log.write(f"Journal d'organisation - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                log.write(f"Dossier: {dossier}\n")
                log.write("=" * 80 + "\n\n")
                
                self.ajouter_au_journal(f"🔍 Analyse du dossier : {dossier}")
                
                # Parcourir les fichiers
                for nom_fichier in os.listdir(dossier):
                    chemin_complet = os.path.join(dossier, nom_fichier)
                    
                    # Ignorer les dossiers et le journal
                    if os.path.isdir(chemin_complet) or nom_fichier.startswith("journal_organisation"):
                        continue
                    
                    try:
                        # Obtenir l'extension
                        _, extension = os.path.splitext(nom_fichier)
                        extension = extension.lower()
                        
                        # Déterminer la catégorie
                        categorie = extensions_mapping.get(extension, "Autres")
                        
                        # Créer le dossier de destination
                        dossier_destination = os.path.join(dossier, categorie)
                        os.makedirs(dossier_destination, exist_ok=True)
                        
                        # Vérifier si le fichier existe déjà
                        nouveau_chemin = os.path.join(dossier_destination, nom_fichier)
                        if os.path.exists(nouveau_chemin):
                            # Ajouter un suffixe
                            base, ext = os.path.splitext(nom_fichier)
                            compteur = 1
                            while os.path.exists(nouveau_chemin):
                                nouveau_nom = f"{base}_{compteur}{ext}"
                                nouveau_chemin = os.path.join(dossier_destination, nouveau_nom)
                                compteur += 1
                        
                        # Déplacer le fichier
                        shutil.move(chemin_complet, nouveau_chemin)
                        
                        log.write(f"✅ {nom_fichier} → {categorie}/\n")
                        fichiers_deplaces += 1
                        
                    except Exception as e:
                        log.write(f"❌ Erreur avec {nom_fichier}: {str(e)}\n")
                        self.ajouter_au_journal(f"⚠️ Erreur avec {nom_fichier}: {str(e)}")
                        erreurs += 1
                
                log.write("\n" + "=" * 80 + "\n")
                log.write(f"Résumé:\n")
                log.write(f"- Fichiers déplacés: {fichiers_deplaces}\n")
                log.write(f"- Erreurs: {erreurs}\n")
            
            # Message de fin
            self.ajouter_au_journal(f"✅ Organisation terminée !")
            self.ajouter_au_journal(f"   📊 {fichiers_deplaces} fichier(s) déplacé(s)")
            if erreurs > 0:
                self.ajouter_au_journal(f"   ⚠️ {erreurs} erreur(s)")
            self.ajouter_au_journal(f"   📄 Journal sauvegardé : {os.path.basename(journal_file)}\n")
            
            messagebox.showinfo("Terminé", 
                              f"Organisation terminée !\n\n"
                              f"Fichiers déplacés : {fichiers_deplaces}\n"
                              f"Erreurs : {erreurs}\n\n"
                              f"Consultez le journal pour plus de détails.")
            
        except Exception as e:
            self.ajouter_au_journal(f"❌ Erreur fatale : {str(e)}")
            messagebox.showerror("Erreur", f"Une erreur s'est produite :\n{str(e)}")


def main():
    root = tk.Tk()
    app = OrganisateurFichiers(root)
    root.mainloop()


if __name__ == "__main__":
    main()

from ..app import db
# Nous avons importé la base de données sqlite, stockée dans la variable db

# Il est question ensuite de la création du modèle selon celui de données de la base Bibliebad.sqlite :

# Table contenant l'ensemble des données relatives aux étudiant.e.s
class Etudiant(db.Model):
    __tablename__ = "Etudiant"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Nom = db.Column(db.Text)
    Prenom = db.Column(db.Text)
    Memoire_ebad_id = db.Column(db.Integer)
    Sujet = db.Column(db.Text)
    Domaine_de_recherche = db.Column(db.Text)
    Annee_soutenance = db.Column(db.Integer)
    Directeur_de_Memoire_id = db.Column(db.Integer)
    Nom_dir = db.Column(db.Text)
    Prenom_dir = db.Column(db.Text)
    
# Table contenant les données bibliographiques correspondant au mémoire soutenu par chaque Etudiant
class Memoire_ebad(db.Model):
    __tablename__ = "Memoire_ebad"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Sujet = db.Column(db.Text)
    Domaine_de_recherche = (db.Text)
    Annee_soutenance = (db.Integer)

# Table contenant les directeurs de mémoire des étudiants 
class Directeur_de_Memoire(db.Model):
    __tablename__ = "Directeur_de_Memoire"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Nom_dir = db.Column(db.Text)
    Prenom_dir = db.Column(db.Text)
    
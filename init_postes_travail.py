"""
Initialisation automatique des postes de travail construction
Exécuté au démarrage de l'application sur Render
"""

import json
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

def get_all_construction_postes() -> List[Dict]:
    """Retourne la liste complète des 120 postes de travail construction"""
    return [
        # === CONCEPTION ET INGÉNIERIE (12 postes) ===
        {"nom": "Architecte", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00},
        {"nom": "Ingénieur structure", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 105.00},
        {"nom": "Ingénieur civil", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00},
        {"nom": "Ingénieur mécanique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00},
        {"nom": "Ingénieur électrique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00},
        {"nom": "Designer intérieur", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 65.00},
        {"nom": "Technologue", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Consultant LEED", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 85.00},
        {"nom": "Consultant énergétique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 80.00},
        {"nom": "Spécialiste BIM", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 75.00},
        {"nom": "Arpenteur-géomètre", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 85.00},
        {"nom": "Ingénieur en sol", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 90.00},
        
        # === DÉMOLITION ET PRÉPARATION (7 postes) ===
        {"nom": "Entrepreneur en démolition", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 75.00},
        {"nom": "Décontaminateur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 65.00},
        {"nom": "Spécialiste environnemental", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 70.00},
        {"nom": "Excavateur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Dynamiteur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 95.00},
        {"nom": "Transporteur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Signaleur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 35.00},
        
        # === FONDATIONS ET BÉTON (6 postes) ===
        {"nom": "Installateur de pieux", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 65.00},
        {"nom": "Coffreur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Ferrailleur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Cimentier", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Imperméabilisateur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Installateur plancher béton", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 52.00},
        
        # === STRUCTURE ET CHARPENTE (4 postes) ===
        {"nom": "Charpentier-menuisier", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Monteur d'acier", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Installateur poutrelles", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Spécialiste bois d'ingénierie", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 58.00},
        
        # === TOITURE (5 postes) ===
        {"nom": "Couvreur bardeaux", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Couvreur membrane", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Couvreur métallique", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Ferblantier", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Installateur puits de lumière", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 55.00},
        
        # === ENVELOPPE EXTÉRIEURE (5 postes) ===
        {"nom": "Poseur de portes/fenêtres", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Briqueteur-maçon", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Installateur revêtement", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Installateur parement", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Stucateur", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 50.00},
        
        # === PLOMBERIE (4 postes) ===
        {"nom": "Plombier", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Installateur chauffe-eau", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Spécialiste gaz", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00},
        {"nom": "Plombier médical", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 65.00},
        
        # === ÉLECTRICITÉ (2 postes) ===
        {"nom": "Électricien", "departement": "ÉLECTRICITÉ", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Câbleur réseau", "departement": "ÉLECTRICITÉ", "capacite_heures": 8, "cout_heure": 48.00},
        
        # === CVAC ET MÉCANIQUE (7 postes) ===
        {"nom": "Installateur CVAC", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Frigoriste", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00},
        {"nom": "Installateur chauffage radiant", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Mécanicien ventilation commerciale", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Installateur gicleurs", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00},
        {"nom": "Installateur pneumatique", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Balanceur de système", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 60.00},
        
        # === ISOLATION ET INSONORISATION (8 postes) ===
        {"nom": "Isolateur uréthane", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Isolateur cellulose", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Poseur laine", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 42.00},
        {"nom": "Installateur rigide", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Calfeutreur", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 44.00},
        {"nom": "Insonorisateur", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Installateur barres résilientes", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Spécialiste acoustique", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 65.00},
        
        # === FINITION INTÉRIEURE - MURS ET PLAFONDS (5 postes) ===
        {"nom": "Latteur", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Plâtrier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Tireur de joints", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Installateur plafonds suspendus", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00},
        {"nom": "Stucateur intérieur", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00},
        
        # === REVÊTEMENTS DE SOL (6 postes) ===
        {"nom": "Poseur de céramique", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Installateur plancher bois", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Poseur vinyle/LVP", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00},
        {"nom": "Installateur linoléum", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Polisseur béton", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Installateur tapis", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 42.00},
        
        # === MENUISERIE ET ÉBÉNISTERIE (6 postes) ===
        {"nom": "Ébéniste", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Installateur armoires", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Menuisier finition", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Fabricant escaliers", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Installateur portes", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Installateur comptoirs", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00},
        
        # === PEINTURE ET FINITION (4 postes) ===
        {"nom": "Peintre", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00},
        {"nom": "Applicateur enduits", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Peintre industriel", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Poseur papier peint", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 45.00},
        
        # === FINITION SPÉCIALISÉE (4 postes) ===
        {"nom": "Vitrier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Serrurier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Installateur stores", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 42.00},
        {"nom": "Monteur cloisons", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00},
        
        # === ÉQUIPEMENTS SPÉCIALISÉS (11 postes) ===
        {"nom": "Installateur sanitaire", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Installateur foyer", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Installateur domotique", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Installateur alarme", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Spécialiste télécom", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Acousticien", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 70.00},
        {"nom": "Installateur ascenseur", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 65.00},
        {"nom": "Installateur monte-charge", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 60.00},
        {"nom": "Piscinier", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 52.00},
        {"nom": "Installateur sauna", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 50.00},
        {"nom": "Monteur chambre froide", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 55.00},
        
        # === AMÉNAGEMENT EXTÉRIEUR (13 postes) ===
        {"nom": "Installateur porte garage", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Installateur abri d'auto", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Excavateur piscine", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 58.00},
        {"nom": "Paysagiste", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Paveur", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Installateur murets", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Installateur clôtures", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 42.00},
        {"nom": "Installateur terrasses", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Installateur pergola", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00},
        {"nom": "Installateur irrigation", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 45.00},
        {"nom": "Installateur éclairage", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00},
        {"nom": "Arboriculteur", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 50.00},
        
        # === SERVICES ET SUPPORT (8 postes) ===
        {"nom": "Nettoyeur de chantier", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 35.00},
        {"nom": "Loueur équipement", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 42.00},
        {"nom": "Gardien de sécurité", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00},
        {"nom": "Nettoyeur après construction", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00},
        {"nom": "Inspecteur en bâtiment", "departement": "QUALITÉ_CONFORMITÉ", "capacite_heures": 8, "cout_heure": 75.00},
        {"nom": "Installateur électroménagers", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 42.00},
        {"nom": "Photographe immobilier", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 55.00},
        {"nom": "Déménageur", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00}
    ]

def initialize_postes_in_database(db):
    """
    Initialise les postes de travail dans la base de données
    Compatible avec ERPDatabase
    """
    try:
        # Créer la table si elle n'existe pas
        db.execute_update("""
            CREATE TABLE IF NOT EXISTS postes_travail (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL UNIQUE,
                departement TEXT NOT NULL,
                capacite_heures_jour REAL DEFAULT 8,
                cout_horaire REAL DEFAULT 50,
                competences_requises TEXT,
                certification_requise INTEGER DEFAULT 0,
                taux_occupation REAL DEFAULT 0,
                statut TEXT DEFAULT 'ACTIF',
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Compter les postes existants
        result = db.execute_query("SELECT COUNT(*) as count FROM postes_travail")
        existing_count = result[0]['count'] if result else 0
        
        if existing_count >= 120:
            logger.info(f"✅ {existing_count} postes déjà en base, initialisation non nécessaire")
            return True
            
        logger.info(f"📊 {existing_count} postes existants, ajout des postes manquants...")
        
        # Ajouter les postes
        postes = get_all_construction_postes()
        inserted = 0
        
        for poste in postes:
            try:
                db.execute_update("""
                    INSERT OR IGNORE INTO postes_travail 
                    (nom, departement, capacite_heures_jour, cout_horaire, statut)
                    VALUES (?, ?, ?, ?, 'ACTIF')
                """, (
                    poste["nom"],
                    poste["departement"],
                    poste["capacite_heures"],
                    poste["cout_heure"]
                ))
                inserted += 1
            except Exception as e:
                logger.debug(f"Poste {poste['nom']} déjà existant ou erreur: {e}")
                
        logger.info(f"✅ Initialisation terminée : {inserted} nouveaux postes ajoutés")
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur initialisation postes: {e}")
        return False
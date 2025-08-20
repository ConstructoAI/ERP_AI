#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'ajout des 120 postes de travail spécialisés construction
Pour le module Production de Constructo AI Inc.
"""

import sqlite3
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_construction_postes_to_production():
    """
    Ajoute 120 postes de travail spécialisés pour la construction au Québec
    dans la table postes_travail de la base de données ERP
    """
    
    # Liste complète des 120 postes de travail construction
    POSTES_CONSTRUCTION_COMPLETS = [
        # === CONCEPTION ET INGÉNIERIE (12 postes) ===
        {"nom": "Architecte", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00, "competences_requises": ["Conception architecturale", "Code du bâtiment", "AutoCAD", "Revit"], "certification_requise": True},
        {"nom": "Ingénieur structure", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 105.00, "competences_requises": ["Calcul structural", "Béton armé", "Acier structural"], "certification_requise": True},
        {"nom": "Ingénieur civil", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00, "competences_requises": ["Génie civil", "Infrastructure", "Drainage"], "certification_requise": True},
        {"nom": "Ingénieur mécanique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00, "competences_requises": ["CVAC", "Plomberie industrielle", "Mécanique bâtiment"], "certification_requise": True},
        {"nom": "Ingénieur électrique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 95.00, "competences_requises": ["Distribution électrique", "Éclairage", "Automatisation"], "certification_requise": True},
        {"nom": "Designer intérieur", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Design intérieur", "3D Studio", "Matériaux"], "certification_requise": False},
        {"nom": "Technologue", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Dessin technique", "AutoCAD", "Relevés"], "certification_requise": True},
        {"nom": "Consultant LEED", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 85.00, "competences_requises": ["Certification LEED", "Développement durable"], "certification_requise": True},
        {"nom": "Consultant énergétique", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 80.00, "competences_requises": ["Efficacité énergétique", "Novoclimat", "Simulation"], "certification_requise": True},
        {"nom": "Spécialiste BIM", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 75.00, "competences_requises": ["Revit", "Navisworks", "Coordination 3D"], "certification_requise": False},
        {"nom": "Arpenteur-géomètre", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 85.00, "competences_requises": ["Arpentage", "GPS", "Certificat localisation"], "certification_requise": True},
        {"nom": "Ingénieur en sol", "departement": "INGÉNIERIE", "capacite_heures": 8, "cout_heure": 90.00, "competences_requises": ["Géotechnique", "Étude de sol", "Fondations"], "certification_requise": True},
        
        # === DÉMOLITION ET PRÉPARATION (7 postes) ===
        {"nom": "Entrepreneur en démolition", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 75.00, "competences_requises": ["Démolition sécuritaire", "Gestion débris", "CNESST"], "certification_requise": True},
        {"nom": "Décontaminateur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Amiante", "Moisissures", "Décontamination"], "certification_requise": True},
        {"nom": "Spécialiste environnemental", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 70.00, "competences_requises": ["Évaluation environnementale", "Sol contaminé"], "certification_requise": True},
        {"nom": "Excavateur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Excavation", "Machinerie lourde", "CCQ"], "certification_requise": True},
        {"nom": "Dynamiteur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 95.00, "competences_requises": ["Explosifs", "Forage", "Sécurité"], "certification_requise": True},
        {"nom": "Transporteur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Camionnage", "Transport matériaux"], "certification_requise": False},
        {"nom": "Signaleur", "departement": "TERRASSEMENT", "capacite_heures": 8, "cout_heure": 35.00, "competences_requises": ["Signalisation", "Sécurité chantier"], "certification_requise": True},
        
        # === FONDATIONS ET BÉTON (6 postes) ===
        {"nom": "Installateur de pieux", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Pieux vissés", "Pieux battus", "Fondations"], "certification_requise": True},
        {"nom": "Coffreur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Coffrage", "Lecture plans", "CCQ"], "certification_requise": True},
        {"nom": "Ferrailleur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Armature", "Acier renforcé", "Soudure"], "certification_requise": True},
        {"nom": "Cimentier", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Béton", "Finition", "Nivellement"], "certification_requise": True},
        {"nom": "Imperméabilisateur", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Membrane", "Étanchéité", "Drainage"], "certification_requise": False},
        {"nom": "Installateur plancher béton", "departement": "BÉTON", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Dalle béton", "Polissage", "Époxy"], "certification_requise": False},
        
        # === STRUCTURE ET CHARPENTE (4 postes) ===
        {"nom": "Charpentier-menuisier", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Charpente bois", "Ossature", "CCQ"], "certification_requise": True},
        {"nom": "Monteur d'acier", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Structure acier", "Soudure", "Montage"], "certification_requise": True},
        {"nom": "Installateur poutrelles", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Poutrelles ajourées", "Structure"], "certification_requise": False},
        {"nom": "Spécialiste bois d'ingénierie", "departement": "CHARPENTE", "capacite_heures": 8, "cout_heure": 58.00, "competences_requises": ["Bois lamellé", "CLT", "Structures massives"], "certification_requise": False},
        
        # === TOITURE (5 postes) ===
        {"nom": "Couvreur bardeaux", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Bardeaux asphalte", "Ventilation", "CCQ"], "certification_requise": True},
        {"nom": "Couvreur membrane", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Membrane élastomère", "TPO", "EPDM"], "certification_requise": True},
        {"nom": "Couvreur métallique", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Tôle", "Joint debout", "Cuivre"], "certification_requise": True},
        {"nom": "Ferblantier", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Gouttières", "Solins", "Ventilation"], "certification_requise": True},
        {"nom": "Installateur puits de lumière", "departement": "TOITURE", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Puits lumière", "Étanchéité", "Structure"], "certification_requise": False},
        
        # === ENVELOPPE EXTÉRIEURE (5 postes) ===
        {"nom": "Poseur de portes/fenêtres", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Portes", "Fenêtres", "Étanchéité"], "certification_requise": False},
        {"nom": "Briqueteur-maçon", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Brique", "Pierre", "Mortier", "CCQ"], "certification_requise": True},
        {"nom": "Installateur revêtement", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Vinyle", "Fibrociment", "Bois"], "certification_requise": False},
        {"nom": "Installateur parement", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Parement métallique", "Composite"], "certification_requise": False},
        {"nom": "Stucateur", "departement": "ENVELOPPE", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Stuc", "Crépi", "EIFS"], "certification_requise": False},
        
        # === PLOMBERIE (4 postes) ===
        {"nom": "Plombier", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Plomberie", "Tuyauterie", "CCQ"], "certification_requise": True},
        {"nom": "Installateur chauffe-eau", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Chauffe-eau", "Gaz", "Électrique"], "certification_requise": True},
        {"nom": "Spécialiste gaz", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00, "competences_requises": ["Gaz naturel", "Propane", "Certification"], "certification_requise": True},
        {"nom": "Plombier médical", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Gaz médicaux", "Systèmes spécialisés"], "certification_requise": True},
        
        # === ÉLECTRICITÉ (2 postes) ===
        {"nom": "Électricien", "departement": "ÉLECTRICITÉ", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Installation électrique", "Code", "CCQ"], "certification_requise": True},
        {"nom": "Câbleur réseau", "departement": "ÉLECTRICITÉ", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Câblage structuré", "Fibre optique", "Réseau"], "certification_requise": False},
        
        # === CVAC ET MÉCANIQUE (8 postes) ===
        {"nom": "Installateur CVAC", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Chauffage", "Ventilation", "Climatisation"], "certification_requise": True},
        {"nom": "Frigoriste", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00, "competences_requises": ["Réfrigération", "Thermopompe", "CCQ"], "certification_requise": True},
        {"nom": "Installateur chauffage radiant", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Plancher radiant", "Hydronique"], "certification_requise": False},
        {"nom": "Mécanicien ventilation commerciale", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Ventilation industrielle", "Échangeur"], "certification_requise": True},
        {"nom": "Installateur gicleurs", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 58.00, "competences_requises": ["Gicleurs", "Protection incendie", "NFPA"], "certification_requise": True},
        {"nom": "Installateur pneumatique", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Contrôles pneumatiques", "Automatisation"], "certification_requise": False},
        {"nom": "Balanceur de système", "departement": "MÉCANIQUE_BÂTIMENT", "capacite_heures": 8, "cout_heure": 60.00, "competences_requises": ["Balancement CVAC", "Mesures", "Rapports"], "certification_requise": True},
        
        # === ISOLATION ET INSONORISATION (9 postes) ===
        {"nom": "Isolateur uréthane", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Uréthane giclé", "Polyuréthane"], "certification_requise": False},
        {"nom": "Isolateur cellulose", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Cellulose soufflée", "Densité"], "certification_requise": False},
        {"nom": "Poseur laine", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Laine minérale", "Laine de verre"], "certification_requise": False},
        {"nom": "Installateur rigide", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Isolant rigide", "Polystyrène", "Polyiso"], "certification_requise": False},
        {"nom": "Calfeutreur", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 44.00, "competences_requises": ["Calfeutrage", "Scellants", "Étanchéité air"], "certification_requise": False},
        {"nom": "Insonorisateur", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Insonorisation", "Acoustique"], "certification_requise": False},
        {"nom": "Installateur barres résilientes", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Barres résilientes", "Découplage"], "certification_requise": False},
        {"nom": "Spécialiste acoustique", "departement": "ISOLATION", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Tests acoustiques", "STC", "IIC"], "certification_requise": True},
        
        # === FINITION INTÉRIEURE - MURS ET PLAFONDS (5 postes) ===
        {"nom": "Latteur", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Fourrures", "Structure gypse"], "certification_requise": True},
        {"nom": "Plâtrier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Plâtre", "Gypse", "Finition"], "certification_requise": True},
        {"nom": "Tireur de joints", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Joints", "Composé", "Finition"], "certification_requise": False},
        {"nom": "Installateur plafonds suspendus", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00, "competences_requises": ["Plafonds acoustiques", "T-Bar"], "certification_requise": False},
        {"nom": "Stucateur intérieur", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Stuc intérieur", "Textures"], "certification_requise": False},
        
        # === REVÊTEMENTS DE SOL (6 postes) ===
        {"nom": "Poseur de céramique", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Céramique", "Porcelaine", "Mosaïque"], "certification_requise": False},
        {"nom": "Installateur plancher bois", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Bois franc", "Ingénierie", "Flottant"], "certification_requise": False},
        {"nom": "Poseur vinyle/LVP", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00, "competences_requises": ["Vinyle", "LVP", "Plancher flottant"], "certification_requise": False},
        {"nom": "Installateur linoléum", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Linoléum", "Soudure à chaud"], "certification_requise": False},
        {"nom": "Polisseur béton", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Polissage béton", "Époxy", "Densificateur"], "certification_requise": False},
        {"nom": "Installateur tapis", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Tapis", "Sous-tapis", "Transitions"], "certification_requise": False},
        
        # === MENUISERIE ET ÉBÉNISTERIE (6 postes) ===
        {"nom": "Ébéniste", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Ébénisterie", "Fabrication sur mesure"], "certification_requise": False},
        {"nom": "Installateur armoires", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Armoires cuisine", "Installation"], "certification_requise": False},
        {"nom": "Menuisier finition", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Moulures", "Finition bois", "Escaliers"], "certification_requise": False},
        {"nom": "Fabricant escaliers", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Escaliers sur mesure", "Rampes"], "certification_requise": False},
        {"nom": "Installateur portes", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Portes intérieures", "Quincaillerie"], "certification_requise": False},
        {"nom": "Installateur comptoirs", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Comptoirs", "Granit", "Quartz"], "certification_requise": False},
        
        # === PEINTURE ET FINITION (4 postes) ===
        {"nom": "Peintre", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 44.00, "competences_requises": ["Peinture", "Apprêt", "Finition"], "certification_requise": False},
        {"nom": "Applicateur enduits", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Enduits spéciaux", "Époxy", "Textures"], "certification_requise": False},
        {"nom": "Peintre industriel", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Peinture industrielle", "Pulvérisation"], "certification_requise": True},
        {"nom": "Poseur papier peint", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Papier peint", "Vinyle mural"], "certification_requise": False},
        
        # === FINITION SPÉCIALISÉE (4 postes) ===
        {"nom": "Vitrier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Verre", "Miroirs", "Vitrines"], "certification_requise": False},
        {"nom": "Serrurier", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Serrurerie", "Contrôle accès", "Sécurité"], "certification_requise": True},
        {"nom": "Installateur stores", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Stores", "Toiles", "Motorisation"], "certification_requise": False},
        {"nom": "Monteur cloisons", "departement": "FINITION_INT", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Cloisons amovibles", "Systèmes démontables"], "certification_requise": False},
        
        # === ÉQUIPEMENTS SPÉCIALISÉS (11 postes) ===
        {"nom": "Installateur sanitaire", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Appareils sanitaires", "Robinetterie"], "certification_requise": False},
        {"nom": "Installateur foyer", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Foyers", "Poêles", "Cheminées"], "certification_requise": True},
        {"nom": "Installateur domotique", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Domotique", "Automatisation", "Smart home"], "certification_requise": False},
        {"nom": "Installateur alarme", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Systèmes alarme", "Détection", "Monitoring"], "certification_requise": True},
        {"nom": "Spécialiste télécom", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Télécommunications", "Antennes", "Fibre"], "certification_requise": True},
        {"nom": "Acousticien", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 70.00, "competences_requises": ["Acoustique architecturale", "Mesures"], "certification_requise": True},
        {"nom": "Installateur ascenseur", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 65.00, "competences_requises": ["Ascenseurs", "Monte-charge", "Maintenance"], "certification_requise": True},
        {"nom": "Installateur monte-charge", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 60.00, "competences_requises": ["Monte-charge", "Élévateurs"], "certification_requise": True},
        {"nom": "Piscinier", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 52.00, "competences_requises": ["Piscines", "Spas", "Filtration"], "certification_requise": False},
        {"nom": "Installateur sauna", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Saunas", "Hammam", "Vapeur"], "certification_requise": False},
        {"nom": "Monteur chambre froide", "departement": "ÉQUIPEMENTS", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Chambres froides", "Réfrigération commerciale"], "certification_requise": True},
        
        # === AMÉNAGEMENT EXTÉRIEUR (13 postes) ===
        {"nom": "Installateur porte garage", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Portes garage", "Motorisation", "Ajustement"], "certification_requise": False},
        {"nom": "Installateur abri d'auto", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Abris auto", "Structure aluminium"], "certification_requise": False},
        {"nom": "Excavateur piscine", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 58.00, "competences_requises": ["Excavation piscine", "Terrassement"], "certification_requise": False},
        {"nom": "Paysagiste", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Aménagement paysager", "Design extérieur"], "certification_requise": False},
        {"nom": "Paveur", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Pavé uni", "Asphalte", "Béton"], "certification_requise": False},
        {"nom": "Installateur murets", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Murets", "Blocs", "Pierre naturelle"], "certification_requise": False},
        {"nom": "Installateur clôtures", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Clôtures", "Portails", "Mailles"], "certification_requise": False},
        {"nom": "Installateur terrasses", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Terrasses", "Decks", "Composite"], "certification_requise": False},
        {"nom": "Installateur pergola", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 48.00, "competences_requises": ["Pergolas", "Gazebos", "Structures extérieures"], "certification_requise": False},
        {"nom": "Installateur irrigation", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 45.00, "competences_requises": ["Irrigation", "Arrosage automatique"], "certification_requise": False},
        {"nom": "Installateur éclairage", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 46.00, "competences_requises": ["Éclairage extérieur", "Basse tension"], "certification_requise": False},
        {"nom": "Arboriculteur", "departement": "EXTÉRIEUR", "capacite_heures": 8, "cout_heure": 50.00, "competences_requises": ["Élagage", "Soins arbres", "Abattage"], "certification_requise": True},
        
        # === SERVICES ET SUPPORT (8 postes) ===
        {"nom": "Nettoyeur de chantier", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 35.00, "competences_requises": ["Nettoyage chantier", "Gestion déchets"], "certification_requise": False},
        {"nom": "Loueur équipement", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Location équipement", "Maintenance"], "certification_requise": False},
        {"nom": "Gardien de sécurité", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00, "competences_requises": ["Sécurité chantier", "Surveillance"], "certification_requise": True},
        {"nom": "Nettoyeur après construction", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00, "competences_requises": ["Nettoyage final", "Produits spécialisés"], "certification_requise": False},
        {"nom": "Inspecteur en bâtiment", "departement": "QUALITÉ_CONFORMITÉ", "capacite_heures": 8, "cout_heure": 75.00, "competences_requises": ["Inspection", "Code bâtiment", "Rapports"], "certification_requise": True},
        {"nom": "Installateur électroménagers", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 42.00, "competences_requises": ["Électroménagers", "Connexions", "Ajustement"], "certification_requise": False},
        {"nom": "Photographe immobilier", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 55.00, "competences_requises": ["Photographie", "Vidéo", "Drone"], "certification_requise": False},
        {"nom": "Déménageur", "departement": "SERVICES", "capacite_heures": 8, "cout_heure": 38.00, "competences_requises": ["Déménagement", "Manutention", "Transport"], "certification_requise": False}
    ]
    
    db_path = "erp_production_dg.db"
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        logger.info("🔧 Ajout des 120 postes de travail construction...")
        
        # Vérifier si la table existe
        cursor.execute("""
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
        cursor.execute("SELECT COUNT(*) FROM postes_travail")
        existing_count = cursor.fetchone()[0]
        logger.info(f"📊 {existing_count} postes existants dans la base")
        
        # Insérer les nouveaux postes
        inserted = 0
        skipped = 0
        
        for poste in POSTES_CONSTRUCTION_COMPLETS:
            try:
                # Convertir les compétences en JSON
                competences_json = json.dumps(poste.get("competences_requises", []), ensure_ascii=False)
                
                cursor.execute("""
                    INSERT OR IGNORE INTO postes_travail 
                    (nom, departement, capacite_heures_jour, cout_horaire, 
                     competences_requises, certification_requise, statut)
                    VALUES (?, ?, ?, ?, ?, ?, 'ACTIF')
                """, (
                    poste["nom"],
                    poste["departement"],
                    poste["capacite_heures"],
                    poste["cout_heure"],
                    competences_json,
                    1 if poste.get("certification_requise", False) else 0
                ))
                
                if cursor.rowcount > 0:
                    inserted += 1
                    logger.info(f"✅ Ajouté: {poste['nom']} ({poste['departement']})")
                else:
                    skipped += 1
                    
            except Exception as e:
                logger.error(f"❌ Erreur pour {poste['nom']}: {e}")
        
        conn.commit()
        
        # Vérification finale
        cursor.execute("SELECT COUNT(*) FROM postes_travail")
        final_count = cursor.fetchone()[0]
        
        logger.info("=" * 50)
        logger.info(f"🎉 RÉSUMÉ DE L'OPÉRATION:")
        logger.info(f"   • Postes ajoutés: {inserted}")
        logger.info(f"   • Postes existants ignorés: {skipped}")
        logger.info(f"   • Total postes dans la base: {final_count}")
        logger.info("=" * 50)
        
        # Afficher statistiques par département
        cursor.execute("""
            SELECT departement, COUNT(*) as nb 
            FROM postes_travail 
            GROUP BY departement 
            ORDER BY nb DESC
        """)
        
        logger.info("\n📊 RÉPARTITION PAR DÉPARTEMENT:")
        for dept, count in cursor.fetchall():
            logger.info(f"   • {dept}: {count} postes")
        
        conn.close()
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'ajout des postes: {e}")
        return False

if __name__ == "__main__":
    print("\n🏗️ AJOUT DES 120 POSTES DE TRAVAIL CONSTRUCTION")
    print("=" * 60)
    print("Pour Constructo AI Inc. - Spécialiste Construction Québec")
    print("=" * 60)
    
    success = add_construction_postes_to_production()
    
    if success:
        print("\n✅ Script exécuté avec succès!")
        print("Les postes de travail sont maintenant disponibles dans le module Production.")
    else:
        print("\n❌ Le script a rencontré des erreurs. Consultez les logs.")
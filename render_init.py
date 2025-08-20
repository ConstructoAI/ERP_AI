#!/usr/bin/env python3
"""
Script d'initialisation pour Render
Exécuté automatiquement au démarrage pour initialiser les données
"""

import os
import sys
import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def initialize_render_environment():
    """Initialise l'environnement Render avec les données nécessaires"""
    
    logger.info("🚀 Initialisation de l'environnement Render...")
    
    # Déterminer le chemin de la base de données
    if os.getenv('DATABASE_URL'):
        logger.info("📊 PostgreSQL détecté sur Render")
        db_type = "postgresql"
    else:
        logger.info("📊 SQLite utilisé")
        db_type = "sqlite"
        
    # Importer ERPDatabase
    try:
        from erp_database import ERPDatabase
        from init_postes_travail import initialize_postes_in_database
        
        # Créer une instance de la base
        if db_type == "sqlite":
            db_path = os.getenv('DB_PATH', 'erp_production_dg.db')
            db = ERPDatabase(db_path)
        else:
            # Pour PostgreSQL, utiliser render_database_config
            from render_database_config import init_render_database
            db = init_render_database()
            
        logger.info("✅ Connexion base de données établie")
        
        # Initialiser les 120 postes de travail
        logger.info("🔧 Initialisation des 120 postes de travail construction...")
        success = initialize_postes_in_database(db)
        
        if success:
            logger.info("✅ Postes de travail initialisés avec succès")
        else:
            logger.warning("⚠️ Certains postes n'ont pas pu être initialisés")
            
        # Initialiser les employés Constructo AI si nécessaire
        try:
            from migrate_to_constructo_ai import migrate_employees_to_constructo_ai
            logger.info("👥 Vérification des employés Constructo AI...")
            
            # Vérifier si des employés existent
            result = db.execute_query("SELECT COUNT(*) as count FROM employees")
            if result and result[0]['count'] == 0:
                logger.info("📝 Ajout des 22 employés Constructo AI...")
                migrate_employees_to_constructo_ai()
                logger.info("✅ Employés ajoutés")
            else:
                logger.info(f"✓ {result[0]['count']} employés déjà en base")
                
        except Exception as e:
            logger.warning(f"⚠️ Migration employés non effectuée: {e}")
            
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'initialisation: {e}")
        return False

if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("SCRIPT D'INITIALISATION RENDER - CONSTRUCTO AI INC.")
    logger.info("=" * 60)
    
    success = initialize_render_environment()
    
    if success:
        logger.info("✅ Initialisation terminée avec succès")
        sys.exit(0)
    else:
        logger.error("❌ L'initialisation a échoué")
        sys.exit(1)
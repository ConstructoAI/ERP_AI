@echo off
chcp 65001 >nul
echo ╔══════════════════════════════════════════════════════════════╗
echo ║     SYNCHRONISATION AVEC GITHUB - CONSTRUCTO AI             ║
echo ║     Repository: ConstructoAI/ERP_AI                         ║
echo ╔══════════════════════════════════════════════════════════════╝
echo.

REM Vérifier que Git est installé
echo [1/10] 🔍 Vérification de Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERREUR: Git n'est pas installé !
    echo Téléchargez-le depuis: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo ✅ Git est installé

REM Se placer dans le bon répertoire
echo.
echo [2/10] 📁 Navigation vers le dossier du projet...
cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"
if %errorlevel% neq 0 (
    echo ❌ ERREUR: Impossible d'accéder au dossier
    pause
    exit /b 1
)
echo ✅ Dossier trouvé: %cd%

REM Initialiser Git si nécessaire
echo.
echo [3/10] 🔧 Initialisation de Git...
if not exist ".git" (
    git init
    echo ✅ Repository Git initialisé
) else (
    echo ✅ Repository Git déjà initialisé
)

REM Configurer l'utilisateur si nécessaire
echo.
echo [4/10] 👤 Configuration utilisateur Git...
git config user.name >nul 2>&1
if %errorlevel% neq 0 (
    echo Configuration de l'identité Git requise...
    set /p gitname="Entrez votre nom d'utilisateur GitHub: "
    set /p gitemail="Entrez votre email GitHub: "
    git config --global user.name "!gitname!"
    git config --global user.email "!gitemail!"
    echo ✅ Identité configurée
) else (
    echo ✅ Identité déjà configurée
    git config --get user.name
    git config --get user.email
)

REM Configurer les paramètres Windows
echo.
echo [5/10] ⚙️ Configuration Git pour Windows...
git config --global core.autocrlf true
git config --global init.defaultBranch main
git config --global credential.helper manager
echo ✅ Configuration Windows appliquée

REM Supprimer l'ancien remote s'il existe
echo.
echo [6/10] 🔗 Configuration du repository distant...
git remote remove origin >nul 2>&1

REM Ajouter le bon repository
git remote add origin https://github.com/ConstructoAI/ERP_AI.git
if %errorlevel% eq 0 (
    echo ✅ Repository GitHub configuré: ConstructoAI/ERP_AI
) else (
    echo ⚠️ Le remote existe déjà, mise à jour...
    git remote set-url origin https://github.com/ConstructoAI/ERP_AI.git
)

REM Afficher les remotes
echo.
echo 📍 Vérification de la configuration:
git remote -v

REM Récupérer les dernières modifications depuis GitHub
echo.
echo [7/10] 📥 Récupération des données depuis GitHub...
git fetch origin >nul 2>&1
if %errorlevel% eq 0 (
    echo ✅ Connexion à GitHub réussie
) else (
    echo ⚠️ Première connexion au repository
)

REM Ajouter tous les fichiers
echo.
echo [8/10] 📝 Ajout de tous les fichiers au suivi Git...
git add .
echo ✅ Fichiers ajoutés

REM Afficher le statut
echo.
echo [9/10] 📊 Statut des modifications:
echo ════════════════════════════════════════
git status --short
echo ════════════════════════════════════════

REM Créer le commit
echo.
echo [10/10] 💾 Création du commit et envoi vers GitHub...
git commit -m "Ajout 120 postes de travail construction - Module Production Render" >nul 2>&1
if %errorlevel% eq 0 (
    echo ✅ Commit créé avec succès
) else (
    echo ℹ️ Aucune modification à commiter ou commit déjà fait
)

REM Configurer la branche
git branch -M main >nul 2>&1

REM Push vers GitHub
echo.
echo 🚀 Envoi vers GitHub...
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ATTENTION: GitHub va vous demander vos identifiants        ║
echo ║                                                              ║
echo ║  Username: Votre nom d'utilisateur GitHub                   ║
echo ║  Password: Utilisez un TOKEN (pas votre mot de passe!)      ║
echo ║                                                              ║
echo ║  Pour créer un token:                                       ║
echo ║  1. Allez sur https://github.com/settings/tokens            ║
echo ║  2. Generate new token (classic)                            ║
echo ║  3. Cochez [x] repo                                         ║
echo ║  4. Generate token et copiez-le                            ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
pause
echo.
echo Envoi en cours...

git push -u origin main --force

if %errorlevel% eq 0 (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║     ✅ SUCCÈS ! Fichiers envoyés sur GitHub                 ║
    echo ║                                                              ║
    echo ║  📍 Repository: https://github.com/ConstructoAI/ERP_AI      ║
    echo ║  🔄 Render va redéployer automatiquement                    ║
    echo ║  ⏱️ Les 120 postes seront créés au démarrage               ║
    echo ╚══════════════════════════════════════════════════════════════╝
) else (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║     ❌ ERREUR lors de l'envoi                               ║
    echo ║                                                              ║
    echo ║  Causes possibles:                                          ║
    echo ║  - Token incorrect ou expiré                                ║
    echo ║  - Pas de connexion Internet                                ║
    echo ║  - Permissions insuffisantes sur le repository              ║
    echo ║                                                              ║
    echo ║  Solutions:                                                 ║
    echo ║  1. Créez un nouveau token sur GitHub                       ║
    echo ║  2. Vérifiez que vous êtes collaborateur du repo           ║
    echo ║  3. Réessayez avec: git push -u origin main                ║
    echo ╚══════════════════════════════════════════════════════════════╝
)

echo.
pause
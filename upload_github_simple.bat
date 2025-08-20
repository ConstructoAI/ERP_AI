@echo off
echo ========================================
echo     UPLOAD VERS GITHUB - CONSTRUCTO AI
echo     Repository: ConstructoAI/ERP_AI
echo ========================================
echo.

echo [1/10] Verification de Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERREUR: Git n'est pas installe !
    echo Telechargez-le depuis: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo OK - Git est installe

echo.
echo [2/10] Navigation vers le dossier du projet...
cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"
if %errorlevel% neq 0 (
    echo ERREUR: Impossible d'acceder au dossier
    pause
    exit /b 1
)
echo OK - Dossier trouve

echo.
echo [3/10] Initialisation de Git...
if not exist ".git" (
    git init
    echo OK - Repository Git initialise
) else (
    echo OK - Repository Git deja initialise
)

echo.
echo [4/10] Configuration du repository distant...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/ConstructoAI/ERP_AI.git
echo OK - Repository GitHub configure: ConstructoAI/ERP_AI

echo.
echo [5/10] Verification de la configuration:
git remote -v

echo.
echo [6/10] Ajout de tous les fichiers...
git add .
echo OK - Fichiers ajoutes

echo.
echo [7/10] Statut des modifications:
echo ----------------------------------------
git status --short
echo ----------------------------------------

echo.
echo [8/10] Creation du commit...
git commit -m "Ajout 120 postes de travail construction - Module Production"
if %errorlevel% neq 0 (
    echo Info: Aucune modification ou commit deja fait
)

echo.
echo [9/10] Configuration de la branche principale...
git branch -M main

echo.
echo ========================================
echo IMPORTANT - AUTHENTIFICATION GITHUB
echo ========================================
echo.
echo GitHub va vous demander:
echo.
echo Username: Votre nom d'utilisateur GitHub
echo Password: Utilisez un TOKEN (pas votre mot de passe!)
echo.
echo Pour creer un token:
echo 1. Allez sur https://github.com/settings/tokens
echo 2. Generate new token (classic)
echo 3. Cochez [x] repo
echo 4. Generate token et copiez-le
echo.
echo ========================================
echo.
echo Appuyez sur une touche pour continuer...
pause >nul

echo.
echo [10/10] Envoi vers GitHub...
git push -u origin main --force

if %errorlevel% eq 0 (
    echo.
    echo ========================================
    echo SUCCES ! Fichiers envoyes sur GitHub
    echo.
    echo Repository: https://github.com/ConstructoAI/ERP_AI
    echo Render va redeployer automatiquement
    echo Les 120 postes seront crees au demarrage
    echo ========================================
) else (
    echo.
    echo ========================================
    echo ERREUR lors de l'envoi
    echo.
    echo Causes possibles:
    echo - Token incorrect ou expire
    echo - Pas de connexion Internet
    echo - Permissions insuffisantes
    echo.
    echo Solutions:
    echo 1. Creez un nouveau token sur GitHub
    echo 2. Verifiez vos permissions sur le repo
    echo 3. Reessayez avec: git push -u origin main
    echo ========================================
)

echo.
pause
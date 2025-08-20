@echo off
echo ========================================
echo CONFIGURATION DE GIT POUR WINDOWS
echo ========================================
echo.

echo [1/6] Verification de Git...
git --version
if %errorlevel% neq 0 (
    echo [ERREUR] Git n'est pas installe correctement
    pause
    exit /b 1
)

echo.
echo [2/6] Configuration de votre identite...
set /p username="Entrez votre nom d'utilisateur GitHub: "
set /p email="Entrez votre email GitHub: "

git config --global user.name "%username%"
git config --global user.email "%email%"

echo.
echo [3/6] Configuration pour Windows...
git config --global core.autocrlf true
git config --global init.defaultBranch main
git config --global credential.helper manager

echo.
echo [4/6] Verification de la configuration...
echo.
echo Votre configuration Git :
echo -------------------------
git config --global user.name
git config --global user.email
echo -------------------------

echo.
echo [5/6] Test de connexion a GitHub...
git ls-remote https://github.com/Estimation79/gestion-projets-dg.git >nul 2>&1
if %errorlevel% eq 0 (
    echo [OK] Connexion a GitHub reussie !
) else (
    echo [ATTENTION] Impossible de se connecter a GitHub
    echo Verifiez votre connexion Internet
)

echo.
echo [6/6] Initialisation du repository local...
cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"
git init
git remote add origin https://github.com/Estimation79/gestion-projets-dg.git 2>nul

echo.
echo ========================================
echo CONFIGURATION TERMINEE !
echo ========================================
echo.
echo Prochaines etapes :
echo 1. git add .
echo 2. git commit -m "Votre message"
echo 3. git push -u origin main
echo.
pause
@echo off
echo ========================================
echo UPLOAD AUTOMATIQUE VERS GITHUB
echo ========================================
echo.

REM Vérifier si Git est installé
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERREUR] Git n'est pas installe !
    echo.
    echo Telechargez Git depuis : https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo [OK] Git est installe
echo.

REM Vérifier si on est dans un repo Git
if not exist ".git" (
    echo [INFO] Initialisation du repository Git...
    git init
    git remote add origin https://github.com/Estimation79/gestion-projets-dg.git
)

echo [1/5] Ajout de tous les fichiers...
git add .

echo.
echo [2/5] Creation du commit...
git commit -m "Ajout 120 postes de travail construction - Module Production Render"

echo.
echo [3/5] Configuration de la branche...
git branch -M main

echo.
echo [4/5] Push vers GitHub...
echo.
echo ATTENTION : GitHub va vous demander :
echo - Votre nom d'utilisateur GitHub
echo - Votre mot de passe ou Token (pas votre mot de passe normal)
echo.
echo Pour creer un Token :
echo 1. Allez sur GitHub.com
echo 2. Settings → Developer settings → Personal access tokens → Tokens (classic)
echo 3. Generate new token → Cochez "repo" → Generate
echo 4. Copiez le token et utilisez-le comme mot de passe
echo.
pause

git push -u origin main

if %errorlevel% eq 0 (
    echo.
    echo ========================================
    echo [SUCCES] Fichiers uploades sur GitHub !
    echo ========================================
    echo.
    echo Render va automatiquement redeployer votre application.
    echo Les 120 postes seront ajoutes au demarrage.
) else (
    echo.
    echo [ERREUR] L'upload a echoue. Verifiez vos identifiants.
)

echo.
pause